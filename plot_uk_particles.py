import matplotlib.pyplot as plt   
from mpl_toolkits.basemap import Basemap
import numpy as np    
from netCDF4 import Dataset

particle_data = Dataset("out_celtic_south_60days_tmstp_360.nc",'r')

xax = particle_data.dimensions['xax']
yax = particle_data.dimensions['yax']
nps = particle_data.dimensions['nps']
print (nps)
dy = particle_data.variables['dy'][:]
dx = particle_data.variables['dx'][:]
print('time')
time = particle_data.variables['time'][:]
xax = particle_data.variables['xax'][:]
yax = particle_data.variables['yax'][:]
zax = particle_data.variables['zax'][:]
h = particle_data.variables['h'][:]
ipos = particle_data.variables['ipos'][:]
jpos = particle_data.variables['jpos'][:]
kpos = particle_data.variables['kpos'][:]
wfact = particle_data.variables['wfact'][:]
print('ok')
status = particle_data.variables['status'][:]
temp = particle_data.variables['temp'][:]
salt = particle_data.variables['salt'][:]
u = particle_data.variables['u'][:]
v = particle_data.variables['v'][:]
w = particle_data.variables['w'][:]
size = particle_data.variables['size'][:]

print ('working')
fig = plt.figure(figsize=(500,500))

m = Basemap(projection='ortho',lon_0=5,lat_0=35,resolution='l')
m.etopo()
m.drawcoastlines()
m.drawparallels(np.arange(-90.,120.,15.))
m.drawmeridians(np.arange(0.,420.,30.))

# your extent in lat/lon (dec degrees)
ulx = -18
uly = 64
lrx = 8
lry = 46

# transform coordinates to map projection
xmin, ymin = m(ulx, lry)
xmax, ymax = m(lrx, uly)

# set the axes limits
ax = plt.gca()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)


for i in range(1,200):
    m.plot(ipos[:,i], jpos[:,i], label=str(i),latlon=True)
plt.show()


