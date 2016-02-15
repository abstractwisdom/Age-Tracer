#!/bin/env python

                                 #- - - - - - - - - - - - - - -#
                                #         Commander V0.31       #
                                 # - - - - - - - - - - - - - - #
                                        # 15 / 02 / 2016 #
                                         ## # # ## # # ##

# ====== Designed for use with Cefas GETM/GOTM particle tracking module developed by Johan van der Molen (Cefas) and debugged by Tiago Silva (Cefas) 

# +++ Author: Matthew Bone
 # +++ Affiliation: Environmental Sciences
  # +++             University of East Anglia,  
   # +++            Norwich,  
    # +++           Norfolk,
     # +++          NR4 7HJ,
      # +++         United Kindom. 
     # +++
    # +++ Contact: m.bone@uea.ac.uk
   # +++ Website: www.matthewbone.org
  # +++ Gihub: github.com/abstractwisdom

 
#  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 
#						     #
#                   In Working Order                   #
# > File organisation                                #
# > User input fields
#   - Start/stop                              #
#   - Model name
#   - Lat/lon                              #
#   - Number of particles spawned                             #
#   - Spawning depth interval                              #
#   - Lat/lon                              #
# > Generates Spawn and Lag set up files             #
# > Generates Spawn and Lag model files                #
# > Automatically runs Spawn file                    #
# > Continous spawning 	             #
# 
#                   Requires Testing                 #
#                                                      #
#                                                    #
#                                                      #
#				                     #
#                     Requires Work 		       #
# 					             #
# > Self genereation of specdef.txt file               #
# > Locations - breaks if only 1loction                #
# > Analysis - doesn't load file                     #


import os
#import csv
import shutil
        # [[ OPENS CONTROL FILES  ]] #
       # {{  ONLY EDIT IF NEED TO  }} #
# ((  CONTROL FILES SHOULD*NOT*BE EDITED  )) #
   # << PLACE IN THE SAME DIRECTORY >> #
os.makedirs("PAR-SPA_output_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_run_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_input_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_analysis", 0o700, exist_ok=True)
os.chdir("PAR-SPA_Templates")
with open('PAR-SPA_template_spawn', 'r') as file :
    filedata = file.read()
with open('PAR-SPA_template_lag', 'r') as set_up :
    set_up_lagfile = set_up.read()
os.chdir("../PAR-SPA_input_files")
os.makedirs("PAR-SPA_spawn_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_lag_files", 0o700, exist_ok=True)
#shutil.copy2('../PAR-SPA_Templates/PAR-SPA_template_data', '../PAR-SPA_input_files/PAR-SPA_spawn_files/')
#shutil.copy2('../PAR-SPA_Templates/PAR-SPA_template_specdef', '../PAR-SPA_run_files')
#  < < < < < < < < < > > > > > > > > > > > > > > > #


                                        # ~ ~ ~ ~ ~ ~ ~ #
                                       #  User editable  #
                                        # * * * * * * * #

                               #  ............................... #
                              # #  ENTER LATITUDE AND LONGITUDE  # #
                               # ................................ #

                                                     # 0 #        # 1 #       # 2 #       # 3 #      # 4 #      # 5 #       # 6 #
latitude =  '59, 59.1',  '58, 60', '58.8, 59', '58, 59', '58, 58.1'
longitude = '-2, 0',  '-6, -5.9', '-6, -5',   '-2, -1.5 ', '-1.5, -1 '

# Enter model names below (using the same format!) 
### !!! CURRENTLY REQUIRES AT LEAST TWO LOCTIONS OTHERWISE IT BREAKS ....!!!
model_name = str('rescue_N_con'), str('rescue2_N_con'), str('rescue3_con'), str('rescue_N_con'), str('rescue_N_con'),



#[0] str('celtic_south') '48, 49' '-10, -8'
#[1] str('celtic_north') '50,51' '-11,-10'
#[2]'IRL_north' '55,56' '-10,-8',
#[3]'SCOT_west' '57,58' '-10,-8',
#[4]'Scot_north_east' '61,62', '-2,2',
#[5]'whole_shelf'  '48, 62', '-12, 0',
#[6]'ire_north_west' '53.5, 56' '-12, -7'



#---------------------------------------------------------------------------------------------------------#

# Specify name for the run and setup configurations which will match the output data
config_name = 'swimming'

# Specify NETCDF file name
model_input_file = 'nwes-3d-2001001.nc'

# Specify NETCDF dir
input_directory  = '/gpfs/home/zgv09gsu/particle/Create_links/'

# Specify Output dir for particle data - this folder is created automatically above, so no need to change unless absolutely necessesary
output_directory = '/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/PAR-SPA/PAR-SPA_output_files'

# Specify spawn_file dir if different
spawn_file_dir = '../PAR-SPA_input_files/PAR-SPA_spawn_files/'

# Model template data for GETM/GOTM
model_temp = 'PAR-SPA_template_data' 

interpolation_mode = 3  #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                      #<>  Interpolation mode hydrodynamics                          <>#
                      #<>  1: interpolate whole field                                <>#
                      #<>  2: interpolate block around particles if more efficient   <>#
                      #<>  3: as 2, but dynamically                                  <>#
                        #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                       
#------------------------('YEAR' 'MONTH'  'DAY'  'HOURS''MINUTES''SECONDS'--------------------------------#
date_time_model_start  = '2001/01/01 01:00:00','2001/02/01 01:00:00', '2001/03/01 01:00:00', '2001/04/01 01:00:00', '2001/05/01 01:00:00', '2001/06/01 01:00:00', '2001/07/01 01:00:00', '2001/08/01 01:00:00', '2001/09/01 01:00:00', '2001/10/01 01:00:00', '2001/11/01 01:00:00', '2001/12/01 01:00:00'
date_time_model_finish = '2001/12/30 00:01:00'

date_time_model_start_1 = date_time_model_start[0]


model_time_step = '700.0,'# Resolution of the microtime step forcings within the model in seconds. The lower the number, the higher the resolution and higher computational time. 
model_timefmt = '2,' # Defines how the model interprets start/stop time. Use '2' for when specifying both start and stop above (see lag_getm.inp for more info)
run_time = '18640,' ### How long the model runs for? 

#------------------------------------------------#

## Currently does not work
#continous_spawning_of_particles = 1   # [0 = off] [1 = on] #
#spawn_interval = 2 # Enter time period (days) between particle spawning. 

particles_per_box = 30 # How many particles do you want to spawn per model grid box?

particle_spawn_depth = 180      # (m)
particle_spawn_depth_range = 179 # (m)
# depth_range spawns particles either side of the depth. 

model_grid_spacing_lat = 0.05
model_grid_spacing_lon = 0.08

#------------------------------------------------#


print ("|| / &  ||     &                            < || || || =    || || ||   ---------    || || || || || || || || || ||")
print ("|| --|=: ||  ~-|--               / || \     ||\ : |: /=     || || ||  / 0010110 \   || || || || || || || | || || || ||")
print ("||   |  || ||  |                || || ||    ||/ : |: \=     || || ||  \ 011001011\  || || || || || || ||  ||")
print ("||  / \ || || / \             /|| || || \   < || || || =    || || ||   \ 10010010/  || || || || || || || || || || || || ||")

#------------------------------------------------#
print ("Model names: ", model_name)
print ("Number of particles per box:", particles_per_box)
print ("Spawn depth:", particle_spawn_depth,'(m)', "(+-)",particle_spawn_depth_range,'m')
#------------------------------------------------#

print ("|| / &  ||      &                           = || || || >    || || ||   ---------    || || || || || || || || || || || ||")
print ("|| --|=: +|| #-/--               / || \     ||\ :| : /=     || || ||  / 0001011 \   || || || || || || || || || || || || || ")
print ("||   |  || ||  |                || * ||     ||/ :| : \=      || || |  \ 001011000\  || || || || || || || || || || || ||")
print ("||  / -- || ||/ \             /|| || || \   = || || || >    || || ||   \ 10100101/  || || || || || || || || || || ||")



#------------------------------------------------#

# # # # # # # Don't touch # # # # # # # # # # # # # # # #
 # # # # ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !  # # # # # # # #
filedata = filedata.replace('p_in', str(particles_per_box))              # # # # # # # # #
filedata = filedata.replace('date_time', str(date_time_model_start))   # # # # # # # # # #
filedata = filedata.replace('bottom_spawn', str(particle_spawn_depth)) ###
filedata = filedata.replace('part_tol', str(particle_spawn_depth_range)) #
filedata = filedata.replace('lat_space', str(model_grid_spacing_lat))  ##
filedata = filedata.replace('lon_space', str(model_grid_spacing_lon)) ##
os.chdir("PAR-SPA_spawn_files")                                      ##
with open('Master_' + config_name + '_spawn_setup', 'w') as spawnsetup:          ## # # #
    spawnsetup.write(filedata)                                              # # #
os.chdir("../../")                                                         #
set_up_lagfile = set_up_lagfile.replace('outputdir', str(output_directory)) # #
set_up_lagfile = set_up_lagfile.replace('dir_input', str(input_directory) )    #
set_up_lagfile = set_up_lagfile.replace('intwerp',str(interpolation_mode))    #
set_up_lagfile = set_up_lagfile.replace('input_data',str(model_input_file))  #
set_up_lagfile = set_up_lagfile.replace('step_time',str(model_time_step))   #
set_up_lagfile = set_up_lagfile.replace('fmt_time',str(model_timefmt))       ####
set_up_lagfile = set_up_lagfile.replace('last_n',str(run_time))                  #
set_up_lagfile = set_up_lagfile.replace('time_start',str(date_time_model_start_1))  #
set_up_lagfile = set_up_lagfile.replace('time_stop',str(date_time_model_finish)) #
os.chdir("PAR-SPA_input_files/PAR-SPA_lag_files/")                             #
with open(config_name + '_lag_setup', 'w') as lagfile:                         # 
    lagfile.write(set_up_lagfile)           # # # # # # # # # # # # # # # # # #   
# # # # # # # # # # # # # # # # # # # # # #

#########################################
# CREATE SPAWN LOCATION LOCATION FILES  #
#########################################

print ("--------------------------------------------------")
print ("<<<<<<<<<<<<<<<<<<<<WORKING>>>>>>>>>>>>>>>>>>>>>")
print ("--------------------------------------------------")
os.chdir("../PAR-SPA_spawn_files")
latitude_numbering = 0    
longitude_numbering = 0
for all_module_names in model_name:
    with open('Master_' + config_name + '_spawn_setup', 'r') as spawny:
        read0 = spawny.read()
        write0 = read0.replace('spawn_file', 'spawn_particles_' + all_module_names)
        writeA = write0.replace('lon_box', longitude[longitude_numbering])
        print ("Longitude:", longitude[longitude_numbering] )
        writeB = writeA.replace('lat_box', latitude[latitude_numbering])
        print ("Latitude:", latitude[latitude_numbering] )
    with os.fdopen(os.open(config_name + '_spawn_setup_' + all_module_names, os.O_WRONLY | os.O_CREAT, 0o700), 'w') as spa:
        spa.write(writeB)
        print ("Writing spawn setup file")
        spawn_run_name = config_name + '_spawn_setup_' + all_module_names
       #spawn_run_name_file = config_name + all_module_names + 'spawn_locations_file'
        print ("Depth of particles:")
        print(spawn_run_name)
    with os.fdopen(os.open('Configuration_' + all_module_names, os.O_WRONLY | os.O_CREAT, 0o700), 'w') as configgy:
        configgy.write('Model name:' + str(all_module_names) + '\n'  + 'Latitude:'+ str(latitude[latitude_numbering]) + '\n' + 'Longitude:' + str(longitude[longitude_numbering] + '\n' + 'Configuration name:' + str(config_name) + '\n' + 'Input file:' + str(model_input_file) + '\n' + 'Model start time:' + str(date_time_model_start) + '\n' + 'Model finish time:' + str(date_time_model_finish) + '\n' + 'Model time step:' + str(model_time_step) + '\n' + 'Model time format:' + str(model_timefmt) + '\n' + 'Run time:' + str(run_time) + '\n' + 'Particles spawned per box:' + str(particles_per_box) + '\n ' + 'Particle spawn depth:' + str(particle_spawn_depth) + '(m)' + '\n' + 'Particle spawn depth range:' + '(+-)' + str(particle_spawn_depth_range) + '(m)')) 
    os.system("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/PAR-SPA/PAR-SPA_input_files/PAR-SPA_spawn_files/" + spawn_run_name)
    os.remove("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/PAR-SPA/PAR-SPA_input_files/PAR-SPA_spawn_files/" + spawn_run_name)    
    longitude_numbering = longitude_numbering + 1
    latitude_numbering = latitude_numbering + 1
    print ("Spawn file generated")
    shutil.copy2('spawn_particles_' + all_module_names, '../../PAR-SPA_run_files')
    print ("New spawn file:")
    print ("---------------------------------------------------------------------------")
    print ("^^^^^^^^^^^^^^^^",spawn_run_name,"^^^^^^^^^^^^^^^^^^^^")
    print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^","Generated","^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print ("---------------------------------------------------------------------------")




#os.remove("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/PAR-SPA/PAR-SPA_input_files/PAR-SPA_spawn_files/" + 'Master_' + config_name + '_spawn_setup')    


       # # # - - - - - - - # # #
 # # Creates unique lag setup file # # 
       # # # - - - - - - - # # #

os.chdir("../PAR-SPA_lag_files")
with open(config_name + '_lag_setup', 'r') as laggy:
    read0 = laggy.read()
for all_module_names in model_name:
        with os.fdopen(os.open(config_name + '_lag_' + all_module_names, os.O_WRONLY | os.O_CREAT, 0o700), 'w') as laggy2:
            write0 = read0.replace('traj_id', all_module_names)
            write1 = write0.replace('spawn_file', 'spawn_particles_' + all_module_names)
            laggy2.write(write1)
            print ('Spawn file Created: run_',all_module_names,'_',config_name)

       # # # - - - - - - - # # #
 # # Creates unique run setup file # # 
       # # # - - - - - - - # # #

os.chdir("../../PAR-SPA_run_files")
for all_module_names in model_name:
    with os.fdopen(os.open('run_' + all_module_names + '_' + config_name, os.O_WRONLY | os.O_CREAT, 0o700), 'w') as runningmod:
        runningmod.write('../../../bin/lagrange'' ' + '../PAR-SPA_input_files/PAR-SPA_lag_files/' + config_name + '_lag_'  + all_module_names)
        print ('Run file Created: run_',all_module_names,'_',config_name)
 
         #......#
        #        #
       #          #
      #            #
     #   ANALYSIS   #
      #            #
       #          #
        #        #
         #......#

#import time

#while True:
#    try:
#        analyse = str(input("Are you ready for some analysis?"))
#    except ValueError:
#        continue
#

#    else:
#        print ("3")
#        time.sleep(0.8)
#        print ("2")
#        time.sleep(0.8)
#        print ("1")
#        time.sleep(0.8)
#        print ("Here we go!")
#        break


#sampling_rate = 1
#plot_x_particles = "len(nps)"    # To plot all use: len(nps) otherwise use any number.

## PRODUCES A TRAJECTORY PLOT OF PARTICLES ON UK MAP ##
#os.chdir("../PAR-SPA_Templates")
#with open('PAR-SPA_analysis_plot_template', 'r') as file:
#    plot_analysis = file.read()
#os.chdir("PAR-SPA_analysis")
#for all_module_names in model_name:
#        write0 = plot_analysis.replace('LOAD_DATA', all_module_names)
#        write1 = write0.replace('SAMPLE_ME', str(sampling_rate))
#        write2 = write1.replace('PLOT_ME', str(plot_x_particles))
#        print(write2)
#        with os.fdopen(os.open(config_name + 'analysis' + all_module_names, os.O_WRONLY | os.O_CREAT, 0o700), 'w') as laggy2:
#            laggy2.write(write2)

#for all_module_names in model_name:
#    os.system("/gpfs/home/zgv09gsu/particle/version1_8x/modelsetups/matt_setup/PAR-SPA/Test2/PAR-SPA_input_files/PAR-SPA_spawn_files/" + config_name + 'analysis' + all_module_names)


#os.chdir("../../")
#with open('PAR-SPA_analysis_start_finish_template', 'r') as file :
#    plot_analysis = file.read()
#os.chdir("PAR-SPA_analysis")
#    for all_module_names in model_name:
#        with os.fdopen(os.open(config_name + 'analysis' + all_module_names, os.O_WRONLY | os.O_CREAT, 0o700), 'w') as laggy2:
#            write0 = read0.replace('LOAD_DATA', all_module_names)
#            write1 = write0.replace('SAMPLE_ME', sampling_ rate)
#            write2 = write1.replace('PLOT_ME', plot_x_particles)
#            laggy2.write(write2)

#    start_analysis = file.read()
















#### # # # # # # # # # ####
# Create specdef.txt file #
#### # # # # # # # # # ####



#egg_diam                0.35
#l_hatch                 0.35
#cond_settle_stage       2
#l_settle_min            0
#l_settle_max            0
#n_settle_cond           0
#settle_cond_file        "/home/jv02/PARTICLE_SOURCES/support_data/ns_mpa_settledata.nc"
#settle_var              "bathy"
#settle_crit             "<"
#settle_condition        0
#settle_logic            "AND"
#p_settle_true           1
#p_settle_false          0
#n_foods                 0
#food_var                "fooda" "foodb"
#n_egg_stages            1
#n_larvae_stages         1
#n_behav                 1
#dev_timestep            3600
#particle stage          1       2
#bio_type                1       2
#stage_start_crit        0       99999
#dev_type                1       0
#a_dev                   10.     0
#b_dev                   0       0
#mort_type               0       3
#a_mort                  0       0
#b_mort                  0       0
#repro_type              0       1
#food_type               0       0
#behaviour_type          0       0
#w_migr_mode             1       1
#constmode               0       0
#diurnalmode             0       0
#tidemode                0       0
#andmode                 0       0
#wp_up1                  0       0
#wp_up2                  0       0
#wp_down1                0       0
#wp_down2                0       0
#part_dens_up            0       0
#part_dens_down          0       0
#diurnal_tdepth_top      0       0
#diurnal_tdepth_bottom   0       0
#tidal_tdepth_top        0       0
#tidal_tdepth_bottom     0       0
#hor_swim_mode           0       0
#uvp                     0       0
#



