#!/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
import argparse
from mpl_toolkits.basemap import Basemap
import datetime
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--dataset', required=True, help='NETCDF Datafile')
parser.add_argument('-s', '--subsample', required=False, help='Subsample dataset')

args = parser.parse_args()

netdata = args.dataset
sub = args.subsample


particle_data = Dataset(netdata, 'r')

nps = particle_data.dimensions['nps']            #
print ("Number of particles:", len(nps))          #
time = particle_data.variables['time'][:]      #'
print(time.shape)
ipos = particle_data.variables['ipos'][:]    #'
print ("x location of particles loaded!", len(ipos))     #'
jpos = particle_data.variables['jpos'][:]      #'
wfact = particle_data.variables['wfact'][:]      #'
print(wfact)
print ("y location of particles loaded!")       #'
print ("Length of X/Y dimensions:", len (ipos), len(jpos))
print ("Everything loaded! Now time to plot....")
# The length of the x and y positions of the particles - 1 to make it plot onto a map
#ipossy = len(ipos) - 1 
ipossy = len(ipos) / 2
#jpossy = len(jpos) - 1
jpossy = len(jpos) / 2

# Save file name
date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")
named = str(len(ipos) / 2 )

fig = plt.figure(figsize=(180,120))

#ax = fig.add_subplot(111)
m = Basemap(projection='lcc',resolution='i',lat_0=44, lon_0=0, llcrnrlon= -18, urcrnrlon=15, urcrnrlat=64, llcrnrlat=44)
#m.etopo()
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawparallels(np.arange(-90.,120.,2.), labels=[False,True,True,False])
m.drawmeridians(np.arange(0.,420.,2.), labels=[True,False,False,True])

x, y = m(ipos[ipossy,:], jpos[jpossy,:])

# Sets the size of the hexagons 
gridsize = 200

cus_colour = 0


if cus_colour == 1:
    cdict = {'red':  ( (0.0,  1.0,  1.0),
                       (1.0,  0.9,  1.0) ),
             'green':( (0.0,  1.0,  1.0),
                       (1.0,  0.03, 0.0) ),
             'blue': ( (0.0,  1.0,  1.0),
                       (1.0,  0.16, 0.0) ) }
    custom_map = LinearSegmentedColormap('custom_map', cdict)
    plt.register_cmap(cmap=custom_map)

    plt.hexbin(x,y, gridsize=gridsize, mincnt=1, vmax=50, cmap='custom_map')

# mincnt allows us to only plot where there are one or more values in a cell! 
if cus_colour == 0:
    plt.hexbin(x,y, gridsize=gridsize, mincnt=1, vmax=12, alpha=0.8)
        #m.plot(ipos[ipossy, x], jpos[ipossy, x], 'bo', alpha=0.5, latlon=True)

for x in range(0,len(nps), 6001):
    m.plot(ipos[0, x], jpos[0, x],'pink',  latlon=True, marker = "*", markersize=20)


#red_patch = mpatches.Patch(label='Number of particles: ' + len(nps))
#plt.legend(label='Number of particles: ' + str(len(nps)))
#red_patch = mpatches.Patch(color='white', label='Total number of particles: ' + str(len(nps)))
#plt.legend(handles=[red_patch])

blue_line = mlines.Line2D([], [], color='Pink', marker='*',
                          markersize=15, label='Particle Spawn Locations \n Number of particles: ' + str(len(nps)))
plt.legend(handles=[blue_line])

cb = plt.colorbar()
cb.set_label('Number of Particles')
#plt.clf()
#plt.imshow(heatmap)
#plt.imshow(heatmap, extent=extent)
#plt.savefig(date_string + '_' + named)

plt.show()


