#!/bin/env python

                                 #- - - - - - - - - - - - - - -#
                                #         Commander V0.25       #
                                 # - - - - - - - - - - - - - - #
                                        # 11 / 01 / 2016 #
                                         ## # # ## # # ##
 
#  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 
#						     #
#                   In Working Order                   #
# > File organisation                                #
# > User input fields                                  #
# > Generates Spawn and Lag set up files             #
# > Generates Spawn and Lag model files                #
# > Automatically runs Spawn file                    #
# 
#                   Requires Testing                 #
#                                                      #
#                                                    #
#                                                      #
#				                     #
#                     Requires Work 		       #
# 					             #
# > Self genereation of specdef.txt file               #
# > Continous spawning (in the works!)	             #
# > Put locations into a function                      #



import os
import csv
        # [[ OPENS CONTROL FILES  ]] #
       # {{  ONLY EDIT IF NEED TO  }} #
# ((  CONTROL FILES SHOULD*NOT*BE EDITED  )) #
   # << PLACE IN THE SAME DIRECTORY >> #
os.makedirs("PAR-SPA_run_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_output_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_input_files", 0o700, exist_ok=True)
with open('PAR-SPA_template_spawn', 'r') as file :
    filedata = file.read()
with open('PAR-SPA_template_lag', 'r') as set_up :
    set_up_lagfile = set_up.read()

os.chdir("PAR-SPA_input_files")
os.makedirs("PAR-SPA_spawn_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_lag_files", 0o700, exist_ok=True)
#  < < < < < < < < < > > > > > > > > > > > > > > > #


                                        # ~ ~ ~ ~ ~ ~ ~ #
                                       #  User editable  #
                                        # * * * * * * * #


# Specify name for the run and setup configurations which will match the output data
config_name = 'matt_test'
# Specify NETCDF file name
model_input_file = 'nwes-3d-2001001.nc'
# Specify NETCDF dir
input_directory  = '/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/Create_links'
# Specify Output dir for particle data - this folder is created automatically above, so no need to change unless absolutely necessesary
output_directory = '/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/PAR-SPA_output_files'
# Specify spawn_file dir if different
spawn_file_dir = '/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/PAR-SPA_input_files/PAR-SPA_spawn_files/'

interpolation_mode = 1  #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                      #<>  Interpolation mode hydrodynamics                          <>#
                      #<>  1: interpolate whole field                                <>#
                      #<>  2: interpolate block around particles if more efficient   <>#
                      #<>  3: as 2, but dynamically                                  <>#
                        #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                       
#---------------------------------------------------------------------------------------------------------#
#------------------------('YEAR' 'MONTH'  'DAY'  'HOURS''MINUTES''SECONDS'--------------------------------#
date_time_model_start  = '2001/01/01 00:59:60'
date_time_model_finish = '2001/04/01 00:00:00'


model_time_step = '10.0,'# Resolution of the microtime step forcings within the model in seconds. The lower the number, the higher the resolution and higher computational time. 
model_timefmt = '2,' # Defines how the model interprets start/stop time. Use '2' for when specifying both start and stop above (see lag_getm.inp for more info)
run_time = '18640,' ### How long the model runs for? 

#------------------------------------------------#


continous_spawning_of_particles = 1   # [0 = off] [1 = on] #
spawn_interval = 2 # Enter time period (days) between particle spawning. A month is currently considered 29days for simplicity 

particles_per_box = 2 # How many particles do you want to spawn per model grid box?

particle_spawn_depth = 200      # (m)
particle_spawn_depth_range = 5 # (m)
# depth_range spawns particles either side of the depth. 

model_grid_spacing_lat = 0.05
model_grid_spacing_lon = 0.08

#------------------------------------------------#

print ("Number of particles per box:", particles_per_box)
print ("Spawn depth:", particle_spawn_depth,'(m)', "(+-)",particle_spawn_depth_range,'m')

# # # # # # # Don't touch # # # # # # # # # # # # # # # #
 # # # # ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !  # # # # # # # #
filedata = filedata.replace('p_in', str(particles_per_box))              # # # # # # # # #
filedata = filedata.replace('mod_in', str(input_directory) + '/' + str(model_input_file)) #     
filedata = filedata.replace('date_time', str(date_time_model_start))   # # # # # # # # # #
filedata = filedata.replace('bottom_spawn', str(particle_spawn_depth)) ###
filedata = filedata.replace('part_tol', str(particle_spawn_depth_range)) #
filedata = filedata.replace('lat_space', str(model_grid_spacing_lat))  ##
filedata = filedata.replace('lon_space', str(model_grid_spacing_lon)) ##
os.chdir("PAR-SPA_spawn_files")                                      ##
with open(config_name + '_spawn_setup', 'w') as spawnsetup:          ## # # #
    spawnsetup.write(filedata)                                              # # #
os.chdir("../../")                                                         #
set_up_lagfile = set_up_lagfile.replace('outputdir', str(output_directory)) # #
set_up_lagfile = set_up_lagfile.replace('dir_input', str(input_directory) )    #
set_up_lagfile = set_up_lagfile.replace('intwerp',str(interpolation_mode))    #
set_up_lagfile = set_up_lagfile.replace('input_data',str(model_input_file))  #
set_up_lagfile = set_up_lagfile.replace('step_time',str(model_time_step))   #
set_up_lagfile = set_up_lagfile.replace('fmt_time',str(model_timefmt))       ####
set_up_lagfile = set_up_lagfile.replace('last_n',str(run_time))                  #
set_up_lagfile = set_up_lagfile.replace('time_start',str(date_time_model_start))  #
set_up_lagfile = set_up_lagfile.replace('time_stop',str(date_time_model_finish)) #
os.chdir("PAR-SPA_input_files//PAR-SPA_lag_files/")                             #
with open(config_name + '_lag_setup', 'w') as lagfile:                         # 
    lagfile.write(set_up_lagfile)           # # # # # # # # # # # # # # # # # #   
# # # # # # # # # # # # # # # # # # # # # #


                               #  ............................... #
                              # #   ENTER LATITUDE AND LONGITUDE # #
                               #        BOX LOCATIONS BELOW       #       
                                # .............................. #

               # 0 #        # 1 #       # 2 #       # 3 #      # 4 #      # 5 #       # 6 #
latitude =   '48, 49',    '50,51',    '55,56',    '57,58',    '61,62',   '48, 62',  '53.5, 56'
longitude =  '-10, -8',   '-11,-10',  '-10,-8',   '-10,-8',   '-2,2',   '-12, 0',   '-12, -7'

model_name_0 = 'celtic_south'      # 0 #
model_name_1 = 'celtic_north'      # 1 # 
model_name_2 = 'IRL_north'         # 2 # 
model_name_3 = 'SCOT_west'         # 3 #
model_name_4 = 'Scot_north_east'   # 4 #
model_name_5 = 'whole_shelf'       # 5 #
model_name_6 = 'ire_north_west'    # 6 #

print ("Latitude:", latitude [0])
print ( "Longitude:", longitude [0])

 
# The amount of rectiangular box spawn locations must equal #
# the amount of LOCATIONS[X] below.                         #
# If more/less required, copy/delete LOCATION[X] code below #
# ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 

                                              #
                                            #   #
                                          #       #
                                        #           #
                                      #               #
                                    #                   #
                                  #    Copy and paste     #
                                #  location code below if   #
                              #   more spawn locations are    #
                               #          required.          #
                                 #  & spawn[?].inp need to #   
                                  #     to be changed     #
                                  #     according to    #
                                    #      box value    #
                                        #><><><><><>#         

################
# LOCATION [0] #
################
os.chdir("../PAR-SPA_spawn_files")
with open(config_name + '_spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_0))
    writeA = write0.replace('lon_box', str(longitude[0]))
    writeB = writeA.replace('lat_box', str(latitude[0]))
with os.fdopen(os.open(config_name + '_spawn_setup_' + model_name_0, os.O_WRONLY | os.O_CREAT, 0o744), 'w') as spa:
    spa.write(writeB)
print ("Writing spawn setup file")
spawn_run_name = config_name + '_spawn_setup_' + model_name_0
spawn_run_name_file = config_name + model_name_0 + 'spawn_locations_file'
print ("Depth of particles:")
os.system("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/Test2/PAR-SPA_input_files/PAR-SPA_spawn_files/" + spawn_run_name)
print ("Spawn file generated")

 # ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' #
#  Continous spawning of particles  #
 # ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' #
os.chdir("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/Test2/PAR-SPA_input_files/PAR-SPA_spawn_files")

length_of_particles = len(latitude) 
print ("length of particles:", length_of_particles)
spawn_run_name = config_name + '_spawn_' + model_name_0
spawn_run_name_file = config_name + "_"  +  model_name_0 + "_" + 'spawn_file'
print ("Particle file name:", spawn_run_name)

#load in 2001 dates
 
os.chdir("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/Test2")
with open('spawn_2001.csv', 'r') as all_dates:
    dates = all_dates.read().splitlines()

spawn_dates = dates[spawn_interval::spawn_interval]

os.chdir("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/Test2/PAR-SPA_input_files/PAR-SPA_spawn_files")

if continous_spawning_of_particles == 1:
    with open('spawn_' + model_name_0, 'r') as spawn_continuously:
        spawn_continuously_file = spawn_continuously.read()
    get_number_of_particles = str(spawn_continuously_file.splitlines()[0])
    spawn_template_text = str(spawn_continuously_file)[len(get_number_of_particles)+1:]
    print (spawn_template_text)    
#for every date in spawn_dates reproduce first_spawn time and append to end of file
    for spawn_date in spawn_dates:
       ## changed spawn_date to spawn_dates
        newtext = spawn_template_text.replace(str(date_time_model_start[0:10]),str(spawn_dates))
        with open('spawn_' + model_name_0, 'a') as spawn_continuously:
            spawn_continuously.write(newtext)

    with open('spawn_' + model_name_0, 'r+') as spawn_all_times:
        spawn_continuously_file = spawn_all_times.read()
    nrows = len(spawn_continuously_file)    
    print (nrows)
    with open('spawn_' + model_name_0 + 'hacked', 'w') as spawn_out_csv:
            rdr = csv.reader(spawn_continuously_file)
            rowcount=0
            for row in rdr:
                if rowcount==0:
                    print (row[0])
                    int(row[0])
                    print (row[1])
                    row[0]= nrows
                    rowcount=rowcount+1
                else:
                    row[0]=rowcount
                    rowcount=rowcount+1
                wtr=csv.writer(spawn_out_csv)
                wtr.writerow(row)
               
os.chdir("../PAR-SPA_lag_files")
with open(config_name + '_lag_setup', 'r') as laggy:
    read0 = laggy.read()
    with os.fdopen(os.open(config_name + '_lag_' + str(model_name_0), os.O_WRONLY | os.O_CREAT, 0o744), 'w') as laggy2:
        write0 = read0.replace('traj_id', str(model_name_0))
        write1 = write0.replace('spawn_file', str(spawn_file_dir) + 'spawn_' + str(model_name_0))
        laggy2.write(write1)


os.chdir("../../PAR-SPA_run_files")
with os.fdopen(os.open('run_' + str(model_name_0) + '_' + config_name, os.O_WRONLY | os.O_CREAT, 0o744), 'w') as runningmod:
    runningmod.write('../../../../bin/lagrange'' ' + config_name + '_lag_setup') 

