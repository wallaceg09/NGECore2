# Spawn Area file created with PSWG Planetary Spawn Tool
import sys
from java.util import Vector

def addSpawnArea(core):
	dynamicGroups = Vector()
	dynamicGroups.add('voritors_east_group_1')
	core.spawnService.addDynamicSpawnArea(dynamicGroups, 3717, 544, 4894, 'dantooine')
	return
