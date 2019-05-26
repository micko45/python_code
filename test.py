#!/usr/bin/env python
l = ['exiv2-devel', 'mingw-libs', 'tcltk-demos', 'fcgi', 'netcdf', 
    'pdcurses-devel',     'msvcrt', 'gdal-grass', 'iconv', 'qgis-devel', 
    'qgis1.1', 'php_mapscript']

if len(l) % 2 != 0:
    l.append(" ")

split = len(l)/2
l1 = l[0:split]
l2 = l[split:]
for key, value in zip(l1,l2):
    print '%-20s %s' % (key, value)         #python <2.6
#    print "{0:<20s} {1}".format(key, value) #python 2.6+
