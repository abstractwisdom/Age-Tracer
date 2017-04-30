#!/usr/bin/env python3

## This scripts automates the processes of calling the Reborn script for each model run and generates the new spawnfiles accordingly. 

import os
import argparse
import numpy as np

#parser = argparse.ArgumentParser()
#parser.add_argument('-n', '--file number', required=True, help='How many files')
#parser.add_argument('-y', '--new year', required=True, help='How many files')

n=55
y=5
x = 1




filelist = "./reborn_v1.0.py -i "

#### Thi is requires if you are using split.py - nested loop
#for x in range(n):
#    complete = filelist + "Part_" + str(x) + "_" + particles  + ".nc -o Part_" + str(x) + "_" + str(y) + "year -s /gpfs/home/zgv09gsu/Final_Year/PAR-SPA_output_files/Python_Scripts/spawn_particles_Part_"+str(x) + " 1996-01-01 01:00:00"


for i in range(1,53):
    complete = filelist + "Part_" + str(i)  + ".nc -o spawn_particles_Part_" + str(i)  + " -s /gpfs/home/zgv09gsu/Model_data/HPC_Admin_troubleshoot/new/Commander/PAR-SPA_run_files/spawn_particles_Part_1" + " 1996-01-01 01:00:00"
    #print(x, i)        
    os.system(complete)
    os.system("rm -f spawn_particles_Part_" + str(i))


#os.system("cp spawn_particles_Part_* /gpfs/home/zgv09gsu/Model_data/HPC_Admin_troubleshoot/new/Commander/PAR-SPA_run_files/")
os.system("mkdir Spawn_Dir")
os.system("mv spawn_particles_Part_* Spawn_Dir/")
print("\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/")
print("Copied new spawn file to run directory and moved origional to Spawn_Dir/")
print("Moved NetCDF data to: combined_nc/")
os.system("mkdir All_nc_Data")
os.system("mkdir All_nc_Data/Log_Files")
os.system("mv Part_*.log All_nc_Data/Log_Files")
os.system("mv Part_* All_nc_Data/")
