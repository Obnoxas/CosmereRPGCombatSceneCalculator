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
        minion.log() # DEBUG TEST, PLEASE DELETE
        count += 1
        clock -= minion.RelativeThreat
    return count
