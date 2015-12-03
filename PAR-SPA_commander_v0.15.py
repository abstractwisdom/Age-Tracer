#!/bin/env python

                                 #- - - - - - - - - - - - - - -#
                                #         Commander V0.14       #
                                 # - - - - - - - - - - - - - - #

#  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 
#                     Requires Testing                 #
#                                                      #
# > Changing the interval period                       #






import os

        # [[ OPENS CONTROL FILES  ]] #
       # {{  ONLY EDIT IF NEED TO  }} #
# ((  CONTROL FILES SHOULD*NOT*BE EDITED  )) #
   # << PLACE IN THE SAME DIRECTORY >> # 
os.makedirs("PAR-SPA_spawn_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_lag_files", 0o700, exist_ok=True)
os.makedirs("PAR-SPA_run_files", 0o700, exist_ok=True)
with open('PAR-SPA_template_spawn', 'r') as file :
    filedata = file.read()
with open('PAR-SPA_template_lag', 'r') as set_up :
    set_up_lagfile = set_up.read()
#  < < < < < < < < < > > > > > > > > > > > > > > > #


                                        # ~ ~ ~ ~ ~ ~ ~ #
                                       #  User editable  #
                                        # * * * * * * * #


# Specify name for the run and setup configurations which will match the output data
config_name = '3day'

model_input_file = 'north_west_european_shelf.3d.nc'
input_directory  = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/'
output_directory = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/outputfiles/'


interpolation_mode = 1  #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                      #<>  Interpolation mode hydrodynamics                          <>#
                      #<>  1: interpolate whole field                                <>#
                      #<>  2: interpolate block around particles if more efficient   <>#
                      #<>  3: as 2, but dynamically                                  <>#
                        #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                       
#---------------------------------------------------------------------------------------------------------#
#------------------------('YEAR' 'MONTH'  'DAY'  'HOURS''MINUTES''SECONDS'--------------------------------#
date_time_model_start  = ('2001''/''01''/''01' ' ' '00'':''59'':''60')
date_time_model_finish = ('2001''/''04''/''01' ' ' '00'':''00'':''00')
#print (date_time_model_start)
#print (date_time_model_start[0:4])
#spawn_particles_per_day = (':')  # If you want to spawn particles continously throughout the model place ':' within brackets. Alternatively specify a time frame in days   
#release burst of particles every 3hours, for a period of 12hours (covering tidal cycle) for a period of a week.  
#particle_spawn_every_x_days = 3 # Time between release of particles (days). A release of particles  every three days is default: this is to conencide with the Moons orbit (tidal cycle) and increase the probability to capture mesoscale weather events.which would impact upon water movenment onto the shelf. A higher value will increase computational time, a value of five or seven may be suggested, however this has not been tested. 
#particle_release_period = '00:00:00' # How long the particles will be released for (hours). A 1hour period of release every (0, 3, 6, 9, 12 recommended to accomodate a complete tidal cycle) 
# number of releases over release period  
#for continous_spawning in 


#date_time_model_start_spawn_days  = int(date_time_model_start[8:10]) 
#change_spawn_day = date_time_model_start_spawn_days + particle_spawn_every_x_days
#date_time_model_start[8:10].replace(str(date_time_model_start[8:10]), str(change_spawn_day) )



model_time_step = '10.0,'# Resolution of the microtime step forcings within the model in seconds. The lower the number, the higher the resolution and higher computational time. 
model_timefmt = '2,' # Defines how the model interprets start/stop time. Use '2' for when specifying both start and stop above (see lag_getm.inp for more info)
run_time = '18640,' ### How long the model runs for? 

#------------------------------------------------#

particles_per_box = 3


particle_spawn_depth = 200      # (m)
particle_spawn_depth_range = 50 # (m)
# depth_range spawns particles either side of the depth. 

model_grid_spacing_lat = 0.05
model_grid_spacing_lon = 0.08

#------------------------------------------------#


# # # # # # # Don't touch # # # # # # # # # # # # # # # #
 # # # # ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !  # # #
filedata = filedata.replace('p_in', str(particles_per_box))              #
filedata = filedata.replace('mod_in', str(model_input_file))            #
filedata = filedata.replace('date_time', str(date_time_model_start))   #
filedata = filedata.replace('bottom_spawn', str(particle_spawn_depth)) ###
filedata = filedata.replace('part_tol', str(particle_spawn_depth_range)) #
filedata = filedata.replace('lat_space', str(model_grid_spacing_lat))  ##
filedata = filedata.replace('lon_space', str(model_grid_spacing_lon)) ##
#subdir = "PAR-SPA_spawn_files"
#os.makedirs("PAR-SPA_spawn_files", 0o700, exist_ok=True)
os.chdir("/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/testing/PAR-SPA_spawn_files") 
with open(config_name + '_spawn_setup', 'w') as spawnsetup:
    spawnsetup.write(filedata)                                              # # #
os.chdir("/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/testing/") 
#with open('PAR-SPA_template_lag', 'r') as setup:                                        # # # #
set_up_lagfile = set_up_lagfile.replace('outputdir', str(output_directory)) #
set_up_lagfile = set_up_lagfile.replace('dir_input', str(input_directory) )    #
set_up_lagfile = set_up_lagfile.replace('intwerp',str(interpolation_mode))    #
set_up_lagfile = set_up_lagfile.replace('input_data',str(model_input_file))  #
set_up_lagfile = set_up_lagfile.replace('step_time',str(model_time_step))   #
set_up_lagfile = set_up_lagfile.replace('fmt_time',str(model_timefmt))       ####
set_up_lagfile = set_up_lagfile.replace('last_n',str(run_time))                  #
set_up_lagfile = set_up_lagfile.replace('time_start',str(date_time_model_start))  #
set_up_lagfile = set_up_lagfile.replace('time_stop',str(date_time_model_finish)) #
#os.makedirs(PAR-SPA_lag_files, 0o700, exist_ok=True)
os.chdir("/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/testing/PAR-SPA_lag_files")
with open(config_name + '_lag_setup', 'w') as lagfile: 
    lagfile.write(set_up_lagfile)          # # # # # # # # # # # # # # # # # # # # # ## 


#date_time_model_start  = int(date_time_model_start[8:10])
#date_time_model_start.replace(date_time_model_start[8:10], str(particle_spawn_every_x_days))




#from os.path import join as pjoin
#a = raw_input("File Name: ")
#filepath = "C:\Documents and Settings\User\My Documents\'a'"
#fout = open(filepath, "w")
#path_to_file = pjoin("C:\Documents and Settings User\My Documents\Dropbox",'a')
#FILE = open(path_to_file, "w")


#from os.path import expanduser, join

#path_to_file1 = join(expanduser('~/Dropbox/'), 'a')
#path_to_file2 = join(expanduser('~'), 'a')
#fout = open(path_to_file2, "w")
#FILE = open(path_to_file1, "w")




# # # # # # # # # # # # # # # # # # # # # 


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
os.chdir("/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/testing/PAR-SPA_spawn_files")
with open(config_name + '_spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_0))
    writeA = write0.replace('lon_box', str(longitude[0]))
    writeB = writeA.replace('lat_box', str(latitude[0]))
with os.fdopen(os.open(config_name + '_spawn_' + str(model_name_0), os.O_WRONLY | os.O_CREAT, 0o744), 'w') as spa:
    spa.write(writeB)

os.chdir("/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/testing/PAR-SPA_lag_files")
with open(config_name + '_lag_setup', 'r') as laggy:
    read0 = laggy.read()
    with os.fdopen(os.open(config_name + '_lag_' + str(model_name_0), os.O_WRONLY | os.O_CREAT, 0o744), 'w') as laggy2:
        write0 = read0.replace('traj_id', str(model_name_0))
        write1 = write0.replace('spawn_file', 'spawn_' + str(model_name_0))
        laggy2.write(write1)


os.chdir("/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/testing/PAR-SPA_run_files")
with os.fdopen(os.open('run_' + str(model_name_0) + '_' + config_name, os.O_WRONLY | os.O_CREAT, 0o744), 'w') as runningmod:
    runningmod.write('../../../ ../../bin/lagrange'' ' + config_name + '_lag_setup') 
#with open('run_' + str(model_name_0), 'w') as spa:
#    spa.write('/gpfs/home/zgv09gsu/particle/version1.8x/bin/lagrange' ' ' 'lag_' + str(model_name_0) + ' ' '>/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/Errors/err_lagrange.msg')
#
# <> <> <> <> <> #
#   LOCATION 2   #
# <> <> <> <> <> #

#with open('setup_spawn', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_2))
#    writeA = write0.replace('lon_box', str(longitude[2]))
#    writeB = writeA.replace('lat_box', str(latitude[2]))
#with open ('setup_spawn_' + str(model_name_2), 'w') as spa:
#    spa.write(writeB)

#with open('lag_setup', 'r') as laggy:
#    with open('lag_' + str(model_name_2), 'w') as spa:
#        read0 = laggy.read()
#        write0 = read0.replace('traj_id', str(model_name_2))
#        write1 = write0.replace('spawn_file', 'spawn_' + str(model_name_2))
#        spa.write(write1)

#with open('run_' + str(model_name_2), 'w') as spa:
#    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_2) + ' ' '> err_lagrange.msg')

# <> <> <> <> <> #
#   LOCATION 3   #
# <> <> <> <> <> #

#with open('setup_spawn', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_3))
#    writeA = write0.replace('lon_box', str(longitude[3]))
#    writeB = writeA.replace('lat_box', str(latitude[3]))
#with open ('setup_spawn_' + str(model_name_3), 'w') as spa:
#    spa.write(writeB)
#
#with open('lag_setup', 'r') as laggy:
#    with open('lag_' + str(model_name_3), 'w') as spa:
#        read0 = laggy.read()
#        write0 = read0.replace('traj_id', str(model_name_3))
#        write1 = write0.replace('spawn_file', 'spawn_' + str(model_name_3))
#        spa.write(write1)
#
#with open('run_' + str(model_name_3), 'w') as spa:
#    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_3) + ' ' '> err_lagrange.msg')
#
## <> <> <> <> <> #
##   LOCATION 4   #
## <> <> <> <> <> #
#
#with open('setup_spawn', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_4))
#    writeA = write0.replace('lon_box', str(longitude[4]))
#    writeB = writeA.replace('lat_box', str(latitude[4]))
#with open ('setup_spawn_' + str(model_name_4), 'w') as spa:
#    spa.write(writeB)
#
#with open('lag_setup', 'r') as laggy:
#    with open('lag_' + str(model_name_4), 'w') as spa:
#        read0 = laggy.read()
#        write0 = read0.replace('traj_id', str(model_name_4))
#        write1 = write0.replace('spawn_file', 'spawn_' + str(model_name_4))
#        spa.write(write1)

#with open('run_' + str(model_name_4), 'w') as spa:
#    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_4) + ' ' '> err_lagrange.msg')

# <> <> <> <> <> #
#   LOCATION 5   #
# <> <> <> <> <> #

#with open('setup_spawn', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_5))
#    writeA = write0.replace('lon_box', str(longitude[5]))
#    writeB = writeA.replace('lat_box', str(latitude[5]))
#with open ('setup_spawn_' + str(model_name_5), 'w') as spa:
#    spa.write(writeB)

#with open('lag_setup', 'r') as laggy:
#    with open('lag_' + str(model_name_5), 'w') as spa:
#        read0 = laggy.read()
#        write0 = read0.replace('traj_id', str(model_name_5))
#        write1 = write0.replace('spawn_file', 'spawn_' + str(model_name_5))
#        spa.write(write1)
#
#with open('run_' + str(model_name_5), 'w') as spa:
#    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_5) + ' ' '> err_lagrange.msg')







#print(longitude[6])

#with open('setup_spawn', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_6))
#    writeA = write0.replace('lon_box', str(longitude[6]))
#    writeB = writeA.replace('lat_box', str(latitude[6]))
#with open ('setup_spawn_' + str(model_name_6), 'w') as spa:
#    spa.write(writeB)
#
#with open('lag_setup', 'r') as laggy:
#    with open('lag_' + str(model_name_6), 'w') as spa:
#        read0 = laggy.read()
#        write0 = read0.replace('traj_id', str(model_name_6))
#        write1 = write0.replace('spawn_file', 'spawn_' + str(model_name_6))
#        spa.write(write1)
#
#with open('run_' + str(model_name_6), 'w') as spa:
#    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_6) + ' ' '> err_lagrange.msg')




################
# LOCATION [6] #
################

#ith open('spawn_setup', 'r') as spawny:
#   read0 = spawny.read()
#   write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_6))  #Replace 6 with box_spawn_number 
#    writeA = write0.replace('lat_box', str(latitude[6]))    #Replace X with box_spawn_number 
#    writeB = writeA.replace('lon_box', str(longitude[6])    #Replace X with box_spawn_number 
#with open ('setup_spawn_' + str(model_name_6), 'w') as spa:
#    spa.write(writeB)

#with open('lag_setup', 'r') as laggy:
#    read0 = laggy.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_6))   #Replace X with box_spawn_number 
#    write0 = read0.replace('run_name', str(model_name_6))
#    write1 = write0.replace('traj_id', str(model_name_6))
#with open ('lag_' + str(model_name_6), 'w') as spa:
#    spa.write(write1)

#with open('run_' + str(model_name_6), 'w') as spa:
#    spa.write('../../../../bin/lagrange' 'lag_' ' ' + str(model_name_X) + ' ' '> err_lagrange.msg')







