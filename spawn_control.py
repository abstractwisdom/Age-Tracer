# Setting up spawn file
#
#   
#


import  csv

p = range(1,50) #number of particles
l = -6.536887   #latitude 
#numpy.arange(-5, -6, 0.0005) code use later
la = 59.244806  #Longitude
#numpy.arange(58, 59, 0.0005) code use later
d = 00.0000     #Depth
da = 2015/10/01 #Date
list_of_lists = [[p[0],l,la,d,da]]

with open("spawntest.csv","w") as f:     
     wr = csv.writer(f,delimiter=" ")     
     wr.writerows(list_of_lists)
     wr.writerows('\n')

counter = 0
while counter <= 50:
     p[0] = p[0] + 1
     while d <= 50:
          d = d + 1 
          with open("spawntest.csv","w") as f:   
               wr = csv.writer(f,delimiter=" ")     
               wr.writerows(list_of_lists)
               wr.writerows('\n')
          counter = counter + 1
