#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
restart_particles - create a spawning file for particle tracking based on the
                    end position on a particle tracking run
                    
    restart_particles -i Input_file -o Output_file  Date Time
 
    Input_file  - name of the netcdf file
    Output_file - name of the output csv file
    Date_string - String containing the Date and time of spawning
    
    example:
    restart_particles -i tn.nc -o Output_file -s spawnfile 1996-01-01 01:00:00

Context: Particle tracking over multiple years or to repeat years
         Written for Matthew Bone's PhD on Winter Nitrate NERC-SSB

Created on Tue May 10 16:44:56 2016
Editded on Tue July 26 14:09 2016

@author: TAMS00
@coauthor: ABSDOM
"""


from netCDF4 import Dataset
import numpy as np
import argparse
import sys
import os

def line_prepender(filename, numfile):
    with open(filename, 'r') as f:
        content = f.read()
    with open(filename, 'w') as f:
        f.write(numfile + '\n' + content)


#******************************************************************
def read_nc(VarName,FName):
    #print ('VarName, FName',VarName, FName)
    try:
        grp = Dataset(FName)
    except:
        print("ERROR reading file "+FName)
        sys.exit()

    Var = grp.variables[VarName][:]

    #print ("read var "+VarName+" from "+FName)

    grp.close()

    return Var
#####################################################

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

#*****************************************************************
def sum_append_particle_file(FName):
      # Removes first line of code from a spawnfile using unix and creates new file 
    os.system('tail -n +2 ' + FName + ' > ' + FName + "_2")
      # Removes numbering up to first comma 
    os.system("sed -i 's/^[^,]*,/,/' " + FName + "_2")
      # Renumbers all particles 
    os.system("nl " + FName + "_2" + ' > ' + FName + "_3" )
      # Removes un-needed file
    os.system("rm -f " + FName + "_2")
      # Determines how many particles there are 
    numfile = str(file_len(FName + "_3"))
    print(FName + "          Particles left: [[[ " + numfile + " ]]]")
      # Addes number of particles to new spawn file
    line_prepender(FName + "_3", numfile)


#******************************************************************
def write_csv(FName,rows):
    import csv

    with open(FName,'a') as csvfile_1:
        csvfile = csv.writer(csvfile_1, delimiter=',')
        for row in rows:
        #    print(rows)
            csvfile.writerow(row)
#******************************************************************
# main() to take an optional 'argv' argument, which allows us to call it 
# from the interactive Python prompt: 
#******************************************
def main(argv=None):
#******************************************

    if argv is None:
        argv = sys.argv

    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help='date for spawing')
    parser.add_argument('time', help='time for spawing')
    parser.add_argument('-i', '--infile', required=True, help='path of data input file')
    parser.add_argument('-o', '--outfile', required=True, help='path of data output file')
    parser.add_argument('-s', '--spawnfile', required=True, help='path of spawn file')
#    parser.add_argument('-x', '--interval', required=True, help='spawning interval value (hours)')
    args = parser.parse_args()

    strDateTime = args.date+" "+args.time
#    strDateTime = str("'" + DateTime + "'")
#    print(strDateTime)
#    print (strDateTime)
    InFName = args.infile
    OutFName = args.outfile
    SpawnFName = args.spawnfile
    SpawnName = SpawnFName
#    SpawnInterval = args.interval
#    print (SpawnInterval)
    link=InFName

    # Extract ipos
    try:
        ipos = read_nc('ipos',link)
    except:
    #    print("ERROR Cannot find variable ipos")
        sys.exit()

    # Extract jpos
    try:
        jpos = read_nc('jpos',link)
    except:
    #    print("ERROR Cannot find variable jpos")
        sys.exit()

    # Extract vertical position. Negative is down.            
    try:
        kpos = read_nc('kpos',link)
    except:
    #    print("ERROR Cannot find variable kpos")
        sys.exit()
    # Extract health of superparticle
    try:
        wfact = read_nc('wfact',link)
    except:
    #    print("ERROR Cannot find variable wfact")
        sys.exit()

    # Use final position
    [Ntime,Npart]=ipos.shape
    ipos = ipos[Ntime-1,:]
    jpos = jpos[Ntime-1,:]
    kpos = kpos[Ntime-1,:]
    wfact = wfact[Ntime-1,:]

    rows=[]
    # Header has number of particles
    rows.append([Npart])
    # Create a row for every particle
    removed = 0
    for ipart in range(Npart):
        lon=ipos[ipart]
        lat=jpos[ipart]
        depth=kpos[ipart]
        health=wfact[ipart]
        row=[ipart,lon,lat,depth, "'" + strDateTime + "'",health]
        #row=[ipart,lon,lat,depth,strDateTime,health]
# trying to remove  dead particles
        if depth < 0:
            if lon > -12:
                rows.append(row)
            else:
#                print(row, "Lon removed")
                removed = removed + 1
#                print (removed)
        else:
            #print(row, "Particle flying")
            removed = removed + 1
 #           print (removed)

    write_csv(OutFName,rows)

    sum_append_particle_file(OutFName)

#    os.system("cp *_5 ../../PAR-SPA_run_files/")

if __name__ == "__main__":
    main()
