
from clickFuUtils import cfAction

class gnExtended(cfAction):
    def __init__(self,iface):
        cfAction.__init__(self,self.name(),iface)
        return None
    def name(self):
        return "GN Extended"
    def desc(self):
        return "Geoname extendedFindNearby XML search"
    def createURL(self,lat,long):
        url = "http://ws.geonames.org/extendedFindNearby?lat=%s&lng=%s" % (lat,long)
        return url
