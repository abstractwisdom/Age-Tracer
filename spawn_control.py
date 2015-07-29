import  csv
from netCDF4 import Dataset
import numpy as np

# define + open netcdf physical model output
## model_output is a string 
## north_west_european_shelf.3d.200110.3h.nc is the input file/dataset 
## The data set is held in a netCDF file format with 4Dimensions (lat, lon, depth and time)
## Various environmental parameters are stored within the dataset.  
model_output = "north_west_european_shelf.3d.200110.3h.nc"

## var dataset is created by using the function that was imported at the top of the file from module netCDF4.
## netCDF4 module has to be compiled with hdf5 and loaded independently. Significant work is required to increase the user friendlyness and time consumption with compliling and installing the netCDF4 module with python 
dataset = Dataset(model_output,'r')

## p_box is a static number that can be user edited
## Change p_box to determine how many particles will be released at each location
p_box = 100000 #number of particles per box


## Specify date and time according to the start time of inputfile: lag_getm.inp (predefined by the module)
date = "2001-10-01 01:00:00"

## This is 2 indevidual points
## This needs to be changed
## Write a function to determine location of particle release based on the depth using var dataset
locations = [[49.5, -11],[55,-10]]



## latvar,  lonvar
## latvals, lonvals
## latval,  lonval
## lat0,    lon0
## ny,      nx
## dist_sq_min
## iy,     ix
## dist_sq
## iy_min, ix_min,


## This goes through all latvar and lonvar and picks out the shortest distance from lat0 and lon0
def brute_force_location_index(latvar,lonvar,lat0,lon0):
    ## North
    latvals = latvar[:]
    ## East
    lonvals = lonvar[:]
    ## North
    ny = latvals.shape[0]
    ## East
    nx = lonvals.shape[0]
    ## dynamic value used in, if dist_sq < dist_sq_min:
    dist_sq_min = 1.0e30
    ## Itterat through all points on an x y grid
    for iy in range(ny):
        for ix in range(nx):
            latval = latvals[iy]
            lonval = lonvals[ix]
            dist_sq = (latval - lat0)**2 + (lonval - lon0)**2
            if dist_sq < dist_sq_min:
                iy_min = iy
                ix_min = ix
                dist_sq_min = dist_sq
    return iy_min, ix_min


#iy,ix = brute_force_location_index(latvar, lonvar, 59, -6)
#print('Closest lat lon:', latvar[iy,ix], lonvar[iy,ix])


def createspawnlist_singlelocation(latitude, longitude, date, model_output):
    bottom_scrape = 0.1    #distance from bottom sediment of the deepest particle realease (1mm?)
    p = list(range(p_box)) #number of particles
    latvar = model_output.variables['latc']
    lonvar = model_output.variables['lonc']
    # Get netcdf x and y indexes for lon lat position
    ## Function inside a function - aka requires the previous function (brute_force_location_index) to work! 
    iy, ix = brute_force_location_index(latvar, lonvar, latitude, longitude)
    depth=dataset.variables['bathymetry'][iy,ix]
    print depth
    depthinterval = (depth - bottom_scrape)/(p_box-1)
    #create list of lists to write out file - first particle is particle number, second is depth (needs improving)
    ## particle+particle+1 ensures that the particles are lablled 1 to p_box. Without it, the loop interupts the numbering process.
    list_of_lists = [[latitude,longitude,(particle)*depthinterval,date] for particle in p]
    #print list_of_lists
    return list_of_lists

## func createspawnlist_singlelocation, 5 paramiters
## var input is p_box fixed at int 50, within the function def its called nparticles
## 
## var input is location[0], fixed or dynamic we dont know at this point, within the function def it is called latitude
## var input is location[1], fixed or dynamic we dont know at this point, within the function def it is called longitude
## var input is date, a string defined earlier - fixed starting value, within the function is ALSO called "date"
## var input is dataset, this is a 2d matrix, UNSURE if it is static or dynamic. Within the function it is called "model_output"

## >>> def ralf(x):
## 	return x*2
## 
## >>> squares = [ralf(x) for x in range(10)]
## >>> 
## >>> squares
## [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

## for location in locations]
## location
## locations is locations=[[59,-6],[56,2]] from the top of this file

lists = [createspawnlist_singlelocation(location[0],location[1],date,dataset) for location in locations]

### Creates a list for each particle location and adds them together into one large list - Problems with numbering of particle!
list_of_lists=lists[0]+lists[1]
#print list_of_lists

### Number the particles 1 to p_box - formatting is not correct...unsure to whether this affects the model!? 
### 0 "[49.5, -11, 0.0, '2001-10-01 01:00:00']"
### should be: 0 49.5 -11 0.0 '2001-10-01 01:00:00'
n = list(enumerate(list_of_lists))


## Writes list_of_lists to file.
with open("spawntest.csv","w") as f:
    wr = csv.writer(f,delimiter=' ')
    wr.writerows(n)
    f.close()


