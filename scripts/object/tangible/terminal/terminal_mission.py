import sys
from resources.datatables import TerminalType
def setup(core, object):
	core.mapService.addLocation(object.getPlanet(), '@map_loc_cat_n:terminal_mission', object.getPosition().x, object.getPosition().z, 41, 44, 0)
	object.setAttachment("terminalType", TerminalType.GENERIC)
	return
	