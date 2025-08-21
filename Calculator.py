from TempMem import *
from Adversaries import *

def EasyThreat(PartyNumber):
    return PartyNumber * 0.5

def AverageThreat(PartyNumber):
    return PartyNumber

def HardThreat(PartyNumber):
    return PartyNumber * 1.5

def MinionCalculation(tier, threat, partytier):
    clock = threat
    count = 0

    while clock > 0:
        minion = Minion(tier, partytier)
        count += 1
        clock -= minion.RelativeThreat
    return count

def BossCalculation(tier, threat, partytier):
    clock = threat
    count = 0

    while clock > 3:
        boss = Boss(tier, partytier)
        count += 1
        clock -= boss.RelativeThreat
    return count
