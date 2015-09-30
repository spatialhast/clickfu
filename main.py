# -*- coding: utf-8 -*-

#******************************************************************************
#
# Click-fu
# ---------------------------------------------------------
# Send click coordinates to various geoservices.
#
# Copyright (C) 2008-2010 Barry Rownligson (barry.rowlingson@gmail.com)
#               2014 NextGIS (info@nextgis.org)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
#******************************************************************************

import os
import sys
import tempfile
import gettext

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# import resources

from googlemaps import googleMap
#from geonames import gnExtended
from osm import osmViewMap,osmEditMap,osmEditMapJOSM 
from flickrMap import flickrPics
from geoHack import geoHack

import doAbout

class MainPlugin(object):
  def __init__(self, iface):
    # Save a reference to the QGIS iface
    self.iface = iface

  def initGui(self):
    # Create action
    self.menu=QMenu("Click-fu")

    self.googleMaps = googleMap(self.iface)
    #self.gnExtended = gnExtended(self.iface)
    self.osmViewMap = osmViewMap(self.iface)
    self.osmEditMap = osmEditMap(self.iface)
    self.osmEditMapJOSM = osmEditMapJOSM(self.iface)
    self.flickr = flickrPics(self.iface)
    self.geoHack = geoHack(self.iface)
    
    self.about = QAction("About Click-fu",self.iface.mainWindow())
    QObject.connect(self.about,SIGNAL("triggered()"),self.clickAbout)

    self.menu.addActions([self.googleMaps, self.osmViewMap, self.osmEditMap, self.osmEditMapJOSM, self.flickr, self.geoHack])
    self.menu.addSeparator()
    self.menu.addAction(self.about)
    
    menuBar = self.iface.mainWindow().menuBar()
    menuBar.addMenu(self.menu)

  def clickAbout(self):
    d = doAbout.Dialog()
    d.exec_()

  def unload(self):
    # Remove the plugin
    pass


