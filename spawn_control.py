# Spawn file setup for tracer release in two positions
#
#   
#this looks really handy http://www.unidata.ucar.edu/blogs/developer/en/entry/accessing_netcdf_data_by_coordinates


import  csv
from netCDF4 import Dataset
import numpy as np

# define + open netcdf physical model output
model_output = "north_west_european_shelf.3d.200110.3h.nc"

dataset = Dataset(model_output,'r')

p_box = 50 #number of particles per box

date = "testdate"

locations=[[59,-6],[56,2]]


def brute_force_location_index(latvar,lonvar,lat0,lon0):
    latvals = latvar[:]
    lonvals = lonvar[:]
    ny,nx = latvals.shape[0], lonvals.shape[0]
    dist_sq_min = 1.0e30
    for iy in range(ny):
        for ix in range(nx):
            latval = latvals[iy]
            lonval = lonvals[ix]
            dist_sq = (latval - lat0)**2 + (lonval - lon0)**2
            if dist_sq < dist_sq_min:
                iy_min, ix_min, dist_sq_min = iy, ix, dist_sq
    return iy_min,ix_min




#iy,ix = brute_force_location_index(latvar, lonvar, 59, -6)
#print('Closest lat lon:', latvar[iy,ix], lonvar[iy,ix])


def createspawnlist_singlelocation(nparticles, latitude, longitude, date, model_output):
    
    #distance from bottom of deepest particle realease
    bottom_scrape = 0.1


    p = list(range(nparticles)) #number of particles



    latvar = model_output.variables['latc']
    lonvar = model_output.variables['lonc']
    
    # Get netcdf x and y indexes for lon lat position
    iy, ix = brute_force_location_index(latvar, lonvar, latitude, longitude)
    
    depth=dataset.variables['bathymetry'][iy,ix]
    print depth
    
    depthinterval = (depth - bottom_scrape)/(nparticles-1)


    #create list of lists to write out file - first particle is particle number, second is depth (needs improving)
    list_of_lists = [[particle+1,latitude,longitude,(particle)*depthinterval,date] for particle in p]
    return list_of_lists


lists = [createspawnlist_singlelocation(p_box,location[0],location[1],date,dataset) for location in locations]

list_of_lists=lists[0]+lists[1]

with open("spawntest.csv","w") as f:
    wr = csv.writer(f,delimiter=' ')
    wr.writerows(list_of_lists)

    f.close()


