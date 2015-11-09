#!/bin/env python

                                 #- - - - - - - - - - - - - - -#
                                #         Commander V0.1        #
                                 # - - - - - - - - - - - - - - #


        # [[ OPENS CONTROL FILES  ]] #
       # {{  ONLY EDIT IF NEED TO  }} #
# ((  CONTROL FILES SHOULD*NOT*BE EDITED  )) #
   # << PLACE IN THE SAME DIRECTORY >> # 
with open('particle_spawn_v0.1.py', 'r') as file :
    filedata = file.read()
with open('lag_getm.inp', 'r') as set_up :
    set_up_lagfile = set_up.read()


                                        # ~ ~ ~ ~ ~ ~ ~ #
                                       #  User editable  #
                                        # * * * * * * * #

model_name = 'MODEL RUN 1'
model_id = 'particle_runs'
model_input_file = 'north_west_european_shelf.3d.200110.3h.nc'
input_directory  = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/inputfiles/'
output_directory = '/gpfs/home/zgv09gsu/particle/version1.8x/modelsetups/matt_setup/outputfiles/'


interpolation_mode = 1  #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
                      #<>  Interpolation mode hydrodynamics                          <>#
                      #<>  1: interpolate whole field                                <>#
                      #<>  2: interpolate block around particles if more efficient   <>#
                      #<>  3: as 2, but dynamically                                  <>#
                        #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

#------------------------------------------------#

date_time_model_start  = ('2001/10/01 01:00:00')
date_time_model_finish = ('2001-10-01 03:00:00')
model_time_step = '10.0,'
model_timefmt = '2,' ### Not sure?
run_time = '18640,' ### How long the model runs for? 

#------------------------------------------------#

particles_per_box = 4


particle_spawn_depth = 200      # (m)
particle_spawn_depth_range = 50 # (m)
# depth_range spawns particles either side of the depth. 

model_grid_spacing_lat = 0.05
model_grid_spacing_lon = 0.08

#------------------------------------------------#


    #  Number of boxes | creation of spawn file #
     #   If more boxes are required, add here  #
      #  and copypaste Location[X] code below #
box_spawn_0            =       'spawn0.inp'
#box_spawn_1            =       'spawn1.inp'
#box_spawn_2            =       'spawn2.inp'
#box_spawn_3            =       'spawn3.inp'
#box_spawn_4            =       'spawn4.inp'
#box_spawn_X            =       'spawnX.inp'


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
    set_up_lagfile = set_up_lagfile.replace('run_name', str(model_name))         ##
    set_up_lagfile = set_up_lagfile.replace('input_dir',str(input_directory) )    #
    set_up_lagfile = set_up_lagfile.replace('traj_id', str(model_id))            ##
    set_up_lagfile = set_up_lagfile.replace('intwerp',str(interpolation_mode))    #
    set_up_lagfile = set_up_lagfile.replace('input_data',str(model_input_file))  #
    set_up_lagfile = set_up_lagfile.replace('step_time',str(model_time_step))   #
    set_up_lagfile = set_up_lagfile.replace('fmt_time',str(model_timefmt))       ####
    set_up_lagfile = set_up_lagfile.replace('last_n',str(run_time))                  #
    set_up_lagfile = set_up_lagfile.replace('time_start',str(date_time_model_start))  #
    set_up_lagfile = set_up_lagfile.replace('time_stop',str(date_time_model_finish)) #
    setup.write(set_up_lagfile)          # # # # # # # # # # # # # # # # # # # # # ## 
# # # # # # # # # # # # # # # # # # # # # 


     # . . . . . . . . . . . . . . . . . . . . #
    #  Number of boxes | creation of spawn file #
     #   If more boxes are required, add here  #
      #  and copypaste Location[X] code below #
       # . . . . . . . . . . . . . . . . . . #

box_spawn_0            =       'spawn0.inp'
box_spawn_1            =       'spawn1.inp'
box_spawn_2            =       'spawn2.inp'
box_spawn_3            =       'spawn3.inp'
box_spawn_4            =       'spawn4.inp'
#box_spawn_X            =       'spawnX.in



                               #  ............................... #
                              # #   ENTER LONGITUDE AND LATITUDE # #
                               #        BOX LOCATIONS BELOW       #       
                                # .............................. #

latitude = '54.5, 55',  '55,55.5', '55.5,56', '56.5,57', '57.5,58'
longitude = '-8, -7.5', '-7.5,-7', '-7,-6.5', '-6.5,-6', '-6,-5.5'

# ! ! ! ! ! ! ! 
#     Note    ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 
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
################
# LOCATION [0] #
################
with open('spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', str(box_spawn_0))
    write0 = write0.replace('lat_box', str(latitude[0]))
    write0 = write0.replace('lon_box', str(longitude[0]))
with open('spawn_setup_0', 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    read0 = laggy.read()
    write0 = read0.replace('spawn.inp', str(box_spawn_0))
with open('lag_setup_0', 'w') as spa:
    spa.write(write0)

################
# LOCATION [1] #
################
with open('spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', str(box_spawn_1))
    write0 = write0.replace('lat_box', str(latitude[1]))
    write0 = write0.replace('lon_box', str(longitude[1]))
with open('spawn_setup_1', 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    read0 = laggy.read()
    write0 = read0.replace('spawn.inp', str(box_spawn_1))
with open('lag_setup_1', 'w') as spa:
    spa.write(write0)

################
# LOCATION [2] #
################
with open('spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', str(box_spawn_2))
    write0 = write0.replace('lat_box', str(latitude[2]))
    write0 = write0.replace('lon_box', str(longitude[2]))
with open('spawn_setup_2', 'w') as spa:
    spa.write(write0)
    
with open('lag_setup', 'r') as laggy:
    read0 = laggy.read()
    write0 = read0.replace('spawn.inp', str(box_spawn_2))
with open('lag_setup_2', 'w') as spa:
    spa.write(write0)

################
# LOCATION [3] #
################
with open('spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', str(box_spawn_3))
    write0 = write0.replace('lat_box', str(latitude[3]))
    write0 = write0.replace('lon_box', str(longitude[3]))
with open('spawn_setup_3', 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    read0 = laggy.read()
    write0 = read0.replace('spawn.inp', str(box_spawn_3))
with open('lag_setup_3', 'w') as spa:
    spa.write(write0)

################
# LOCATION [4] #
################
with open('spawn_setup', 'r') as spawny:
    read0 = spawny.read()
    write0 = read0.replace('spawn_file', str(box_spawn_4))
    write0 = write0.replace('lat_box', str(latitude[4]))
    write0 = write0.replace('lon_box', str(longitude[4]))
with open('spawn_setup_4', 'w') as spa:
    spa.write(write0)

with open('lag_setup', 'r') as laggy:
    read0 = laggy.read()
    write0 = read0.replace('spawn.inp', str(box_spawn_4))
with open('lag_setup_4', 'w') as spa:
    spa.write(write0)

################
# LOCATION [X] #
################
#with open('spawn_setup', 'r') as spawny:
#    read0 = spawny.read()
#    write0 = read0.replace('spawn_file', str(box_spawn_X))  #Replace X with box_spawn_number 
#    write0 = write0.replace('lat_box', str(latitude[X]))    #Replace X with box_spawn_number 
#    write0 = write0.replace('lon_box', str(longitude[X])    #Replace X with box_spawn_number 
#with open('spawn_setup_X', 'w') as spa:                     #Replace X with box_spawn_number 
#    spa.write(write0)

#with open('lag_setup', 'r') as laggy:
#    read0 = laggy.read()
#    write0 = read0.replace('spawn.inp', str(box_spawn_X))   #Replace X with box_spawn_number 
#with open('lag_setup_X', 'w') as spa:                       #Replace X with box_spawn_number
#    spa.write(write0)




