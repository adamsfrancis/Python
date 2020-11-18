castList = []
spellPool = []

class Spell:
    def __init__(self,cooldownTime,cooldownRemaining,hotKey):
        self.cdt = cooldownTime
        self.cdr = cooldownRemaining
        self.hk = hotKey

def nextAction():
    for spells in spellPool:
        if spells.cdr > 0:
            spells.cdr -= 500

def hitKey(Spell):
    castList.append(Spell.hk)
    Spell.cdr = Spell.cdt
    nextAction()


def buildSpellPool():
    mysticMode = Spell(45000,0,'H')
    offenseAura = Spell(40000,0,'V')
    earthArmor = Spell(30000,0,'Z')
    elementalM = Spell(25000,0,'T')
    misDirection = Spell(20000,0,'F')
    focusedBreath = Spell(16000,0,'A')
    clairVoyance = Spell(15000,0,'I')
    defAura = Spell(15000,0,'D')
    iceWall = Spell(12000,0,'U')
    auraBall = Spell(9500,0,'G')
    ragingFist = Spell(7500,0,'S')
    dodgeSpell = Spell(7000,0,'E')
    dragonFist = Spell(4000,0,'C')
    invisHand = Spell(3000,0,'X')
    whirlFoot = Spell(3000,0,'Y')
    shadowFist = Spell(2500,0,'R')
    highKick = Spell(1000,0,'W')
    otPunch = Spell(1000,0,'Q')
    global spellPool
    spellPool = [mysticMode,offenseAura,earthArmor,elementalM,misDirection,focusedBreath,clairVoyance,defAura,iceWall,auraBall,ragingFist,dodgeSpell,dragonFist,invisHand,
    whirlFoot,shadowFist,highKick,otPunch]

def buildCastOrder():
    while len(castList) < 180:
        for spells in spellPool:
            if spells.cdr <= 0:
                hitKey(spells)
            else:
                continue


buildSpellPool()
buildCastOrder()
for keys in castList:
    currentKey = keys.strip("'")
    print(currentKey)


    



