import sys
from java.util import Vector
from services.spawn import DynamicSpawnGroup
from services.spawn import MobileTemplate

def addDynamicGroup(core):
	dynamicGroup = DynamicSpawnGroup()
	mobileTemplates = Vector()
	mobileTemplates.add('outbreak_afflicted_lvl_10')
	mobileTemplates.add('outbreak_deathtrooper_lvl_10')
	dynamicGroup.setMobiles(mobileTemplates)
	dynamicGroup.setGroupMembersNumber(-5)
	dynamicGroup.setName('dathomir_quarantine_lvl_10')
	dynamicGroup.setMaxSpawns(-1)
	dynamicGroup.setMinSpawnDistance(10)
	core.spawnService.addDynamicGroup('dathomir_quarantine_lvl_10', dynamicGroup)
	return
