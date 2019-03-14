# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mohsen Yousefzadeh
#
# Created:     09/01/2019
# Copyright:   (c) mohsen yousefzadeh 2019
# Licence:     ArcGIS 10.2.2
# -------------------------------------------------------------------------------
myName = "Patrick"
yourName = 'holly'
print 'My name is '+ myName + ' and your name is ' + yourName + '.'
streetName = 'Candy Lane'
addressNumber = 313
percentOccupied = 32.34
ownerName = 'brown, Charles'
print 'The owner of ' + str(addressNumber)[0:1] + ' ' + streetName + 'is' + ownerName + '.'
print 'The occupied area is ' + str(100 - percentOccupied) + '.'
print 'The street number is ' + streetName[0:5] + '.'
print 'The street number is ' + streetName[-4:] + '.'
listNames = ['David', 'Cindy', 'Mohsen', 'Patrick', 'Ali']
print listNames[2]
print listNames[4]
print listNames[1:5]