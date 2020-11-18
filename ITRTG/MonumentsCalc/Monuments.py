import Creations

#Assumption: One of everything except black hole built
# 1 * Mighty Statue:            1 + 1 Physical
# 1 * Mystic Garden:            1 + 6 Mystic
# 1 * Tomb of Gods:             1 + 30 Battle
# 1 * Everlasting Lighthouse:   1 + 150 Creation
# 1 * Godly Statue:             1 + 200 All
# 1 * Pyramids of Power:        1 + 600 All
# 1 * Temple of God:            1 + 1500 All
# Totals:                       P: 2301
#                               M: 2306
#                               B: 2330
#                               C: 2450

class Monument():
    def __init__(self,name, builtCount, multIncrease, buildCost):
        self.name = name
        self.bc = builtCount
        self.mult = multIncrease
        self.build = buildCost * (builtCount + 1)
        self.cpp = self.build/self.mult

def buildMonument(monToBuild):
    monToBuild.bc += 1
    monToBuild.build *= monToBuild.bc + 1
    monToBuild.cpp = monToBuild.build/monToBuild.mult


monMightyStatue = Monument('Mighty Statue',0,1, 10000*Creations.crStone.div)
monMysticGarden = Monument('Mystic Garden',0,6,(1250*Creations.crWater.div + 500*Creations.crPlant.div))
monTombOfGods = Monument('Tomb of Gods',0,30,(5000*Creations.crStone.div + 5*Creations.crHuman.div))
monEverlasting = Monument('Everlasting Lighthouse', 0,150,(1250000*Creations.crLight.div + 250000*Creations.crStone.div))
monGodlyStatue = Monument('Godly Statue', 0,800,(5*Creations.crMountain.div + 500000*Creations.crStone.div + 125000*Creations.crWater.div))
monPyramids = Monument('Pyramids of Power', 0,2400,(250000*Creations.crWater.div + 2500000*Creations.crStone.div + 1000000*Creations.crLight.div))
monTemple = Monument('Temple of God', 0,6000,(1000000*Creations.crStone.div + 100000*Creations.crLight.div + 2000*Creations.crPlant.div + 1000*Creations.crTree.div + 60000*Creations.crWater.div + 1000*Creations.crFish.div))

monumentsList = [monMightyStatue,monMysticGarden,monTombOfGods,monEverlasting,monGodlyStatue,monPyramids,monTemple]

   
for i in range(1001):
    monumentsList.sort(key=lambda monuments: monuments.cpp)
    buildMonument(monumentsList[0])

for monuments in monumentsList:
    print(monuments.name + ': ' + str(monuments.bc + 1))
