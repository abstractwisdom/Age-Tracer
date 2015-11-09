#!/bin/env python

                                 #- - - - - - - - - - - - - - -#
                                #         Commander V0.1        #
                                 # - - - - - - - - - - - - - - #

import os

        # [[ OPENS CONTROL FILES  ]] #
       # {{  ONLY EDIT IF NEED TO  }} #
# ((  CONTROL FILES SHOULD*NOT*BE EDITED  )) #
   # << PLACE IN THE SAME DIRECTORY >> # 
with open('particle_spawn_v0.1.py', 'r') as file :
    filedata = file.read()
with open('lag_setup', 'r') as set_up :
    set_up_lagfile = set_up.read()
#  < < < < < < < < < > > > > > > > > > > > > > > > #


                                        # ~ ~ ~ ~ ~ ~ ~ #
                                       #  User editable  #
                                        # * * * * * * * #

model_input_file = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/north_west_european_shelf.3d.nc'
input_directory  = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/'
output_directory = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/outputfiles/'


interpolation_mode = 1  #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                      #<>  Interpolation mode hydrodynamics                          <>#
                      #<>  1: interpolate whole field                                <>#
                      #<>  2: interpolate block around particles if more efficient   <>#
                      #<>  3: as 2, but dynamically                                  <>#
                        #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                       
#------------------------------------------------#

date_time_model_start  = ('2001/01/01 00:59:60')
date_time_model_finish = ('2001/02/01 00:00:00')
model_time_step = '10.0,'# Resolution of the microtime step forcings within the model in seconds. The lower the number, the higher the resolution and higher computational time. 
model_timefmt = '2,' # Defines how the model interprets start/stop time. Use '2' for when specifying both start and stop above (see lag_getm.inp for more info)
run_time = '18640,' ### How long the model runs for? 

#------------------------------------------------#

particles_per_box = 100


particle_spawn_depth = 200      # (m)
particle_spawn_depth_range = 50 # (m)
# depth_range spawns particles either side of the depth. 

model_grid_spacing_lat = 0.05
model_grid_spacing_lon = 0.08

#------------------------------------------------#


# # # # # # # Don't touch # # # # # # # # # # # # # # # #
 # # # # ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !  # # #
with open('spawn_setup', 'w') as spawnsetup: # ! ! ! ! ! ! !  # # # # # # # ## 
    filedata = filedata.replace('p_in', str(particles_per_box))              #
    filedata = filedata.replace('mod_in', str(model_input_file))            #
    filedata = filedata.replace('date_time', str(date_time_model_start))   #
    filedata = filedata.replace('bottom_spawn', str(particle_spawn_depth)) ###
    filedata = filedata.replace('part_tol', str(particle_spawn_depth_range)) #
    filedata = filedata.replace('lat_space', str(model_grid_spacing_lat))  ##
    filedata = filedata.replace('lon_space', str(model_grid_spacing_lon)) ##
    spawnsetup.write(filedata)                                              # # #
with open('lag_setup', 'w') as setup:                                        # # # #
    set_up_lagfile = set_up_lagfile.replace('outputdir', str(output_directory)) #
    set_up_lagfile = set_up_lagfile.replace('dir_input', str(input_directory) )    #
    set_up_lagfile = set_up_lagfile.replace('intwerp',str(interpolation_mode))    #
    set_up_lagfile = set_up_lagfile.replace('input_data',str(model_input_file))  #
    set_up_lagfile = set_up_lagfile.replace('step_time',str(model_time_step))   #
    set_up_lagfile = set_up_lagfile.replace('fmt_time',str(model_timefmt))       ####
    set_up_lagfile = set_up_lagfile.replace('last_n',str(run_time))                  #
    set_up_lagfile = set_up_lagfile.replace('time_start',str(date_time_model_start))  #
    set_up_lagfile = set_up_lagfile.replace('time_stop',str(date_time_model_finish)) #
    setup.write(set_up_lagfile)          # # # # # # # # # # # # # # # # # # # # # ## 
# # # # # # # # # # # # # # # # # # # # # 


                               #  ............................... #
                              # #   ENTER LONGITUDE AND LATITUDE # #
                               #        BOX LOCATIONS BELOW       #       
                                # .............................. #

               # 0 #        # 1 #       # 2 #       # 3 #      # 4 #
latitude =   '48, 49',    '50,51',    '55,56',    '57,58',    '61,62'
longitude =  '-10, -8',   '-11,-10',  '-10,-8',   '-10,-8',   '-2,2' 

model_name_0 = 'celtic_south'      # 0 #
model_name_1 = 'celtic_north'      # 1 # 
model_name_2 = 'IRL_north'         # 2 # 
model_name_3 = 'SCOT_west'         # 3 #
model_name_4 = 'Scot_north_east'   # 4 #
#model_name_x = 'celtic_10_particles_3_fmt'

 
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
# These scripts need to be made excutable
# with os.fdopen(os.open('/path/to/file', os.O_WRONLY | os.O_CREAT, 0700), 'w') as handle:
#  handle.write(...)    


#with os.fdopen(os.open('spawn_setup', os.O_WRONLY | os.O_CREAT,777), 'w') as fileid: 
#    fileid = fileid.replace('spawn_file', str(box_spawn_0))
#    fileid = fileid.replace('lat_box', str(latitude[0]))
#    fileid = fileid.replace('lon_box', str(longitude[0]))    
#with os.fdopen(os.open('spawn_setup_0', os.O_WRONLY | os.O_CREAT,777), 'w') as fileid: 

 
################
# LOCATION [0] #
################
with open('setup_spawn', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_0))
    write0 = read0.replace('lon_box', str(longitude[0]))
    write0 = write0.replace('lat_box', str(latitude[0]))
with open ('setup_spawn_' + str(model_name_0), 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    with open('lag_' + str(model_name_0), 'w') as spa:
        read0 = laggy.read()
        write0 = read0.replace('traj_id', str(model_name_0))
        spa.write(write0)
        write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_0))
        spa.write(write0)

with open('run_' + str(model_name_0), 'w') as spa:
    spa.write('/gpfs/home/zgv09gsu/particle/version1.8x/bin/lagrange' ' ' 'lag_' + str(model_name_0) + ' ' '>/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/Particle_Tracking_Working/Errors/err_lagrange.msg')

# <> <> <> <> <> #
#   LOCATION 2   #
# <> <> <> <> <> #

with open('setup_spawn', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_2))
    write0 = read0.replace('lon_box', str(longitude[2]))
    write0 = write0.replace('lat_box', str(latitude[2]))
with open ('setup_spawn_' + str(model_name_2), 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    with open('lag_' + str(model_name_2), 'w') as spa:
        read0 = laggy.read()
        write0 = read0.replace('traj_id', str(model_name_2))
        spa.write(write0)
        write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_2))
        spa.write(write0)

with open('run_' + str(model_name_2), 'w') as spa:
    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_2) + ' ' '> err_lagrange.msg')

# <> <> <> <> <> #
#   LOCATION 3   #
# <> <> <> <> <> #

with open('setup_spawn', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_3))
    write0 = read0.replace('lon_box', str(longitude[3]))
    write0 = write0.replace('lat_box', str(latitude[3]))
with open ('setup_spawn_' + str(model_name_3), 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    with open('lag_' + str(model_name_3), 'w') as spa:
        read0 = laggy.read()
        write0 = read0.replace('traj_id', str(model_name_3))
        spa.write(write0)
        write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_3))
        spa.write(write0)

with open('run_' + str(model_name_3), 'w') as spa:
    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_3) + ' ' '> err_lagrange.msg')

# <> <> <> <> <> #
#   LOCATION 4   #
# <> <> <> <> <> #

with open('setup_spawn', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_4))
    write0 = read0.replace('lon_box', str(longitude[4]))
    write0 = write0.replace('lat_box', str(latitude[4]))
with open ('setup_spawn_' + str(model_name_4), 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    with open('lag_' + str(model_name_4), 'w') as spa:
        read0 = laggy.read()
        write0 = read0.replace('traj_id', str(model_name_4))
        spa.write(write0)
        write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_4))
        spa.write(write0)

with open('run_' + str(model_name_4), 'w') as spa:
    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_4) + ' ' '> err_lagrange.msg')

# <> <> <> <> <> #
#   LOCATION 5   #
# <> <> <> <> <> #

#with open('setup_spawn', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_5))
#    write0 = read0.replace('lon_box', str(longitude[5]))
#    write0 = write0.replace('lat_box', str(latitude[5]))
#with open ('setup_spawn_' + str(model_name_5), 'w') as spa:
#    spa.write(write0)

#with open('lag_setup', 'r') as laggy:
#    with open('lag_' + str(model_name_5), 'w') as spa:
#        read0 = laggy.read()
#        write0 = read0.replace('traj_id', str(model_name_5))
#        spa.write(write0)
#        write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_5))
#        spa.write(write0)

#with open('run_' + str(model_name_5), 'w') as spa:
#    spa.write('../../../../bin/lagrange' ' ' 'lag_' + str(model_name_5) + ' ' '> err_lagrange.msg')


################
# LOCATION [X] #
################

#with open('spawn_setup', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_X))  #Replace X with box_spawn_number 
#    write0 = write0.replace('lat_box', str(latitude[X]))    #Replace X with box_spawn_number 
#    write0 = write0.replace('lon_box', str(longitude[X])    #Replace X with box_spawn_number 
#with open ('setup_spawn_' + str(model_name_x), 'w') as spa:
#    spa.write(write0)

#with open('lag_setup', 'r') as laggy:
#    read0 = laggy.read()
#    write0 = read0.replace('spawn_file', 'spawn_' + str(model_name_X))   #Replace X with box_spawn_number 
#    write0 = read0.replace('run_name', str(model_name_x))
#    write0 = read0.replace('traj_id', str(model_name_x))
#with open('lag_' + str(model_name_X), 'w') as spa:
#    spa.write(write0)

#with open('run_' + str(model_name_X), 'w') as spa:
#    spa.write('../../../../bin/lagrange' 'lag_' ' ' + str(model_name_X) + ' ' '> err_lagrange.msg')







