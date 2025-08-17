from TempMem import *
from Adversaries import *

def EasyThreat(PartyNumber):
    return PartyNumber * 0.5

def MediumThreat(PartyNumber):
    return PartyNumber

def HardThreat(PartyNumber):
    return PartyNumber * 1.5

def Calculation(tier, threat, partytier):
    clock = threat
    count = 0

    while clock > 0:
        minion = Minion(tier, partytier)
        count += tier
        clock -= minion.RelativeThreat
    return count
