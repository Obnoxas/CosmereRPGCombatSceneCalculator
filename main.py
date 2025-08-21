from TempMem import *
from Calculator import *
from Adversaries import *

def main():
    memory = MemoryBank(input("What Tier is your party? (Pg 24): "), input("How many characters are in your party?: "), input("Is this Combat Scene Easy, Average, or Hard?: "))
    memory.ValidityCheck()
    
    if memory.EncounterDifficulty == "easy":
        memory.UpdateThreat(EasyThreat(memory.PartyNumber))
    if memory.EncounterDifficulty == "average":
        memory.UpdateThreat(AverageThreat(memory.PartyNumber))
    if memory.EncounterDifficulty == "hard":
        memory.UpdateThreat(HardThreat(memory.PartyNumber))

    print("Your options are:")

    for t in range(4):
        print(f"TIER {t + 1}")
        memory.MaxBosses = BossCalculation(t + 1, memory.Threat, memory.PartyTier)
        for e in range(memory.MaxBosses + 1):
            print("")
            memory.MinionCount = MinionCalculation(t + 1, (memory.Threat - (e * 4)), memory.PartyTier)
            for i in range(abs(-memory.MinionCount // 2)):
                if i == 0:
                    print(f"- {memory.MinionCount - (2 * i)} Tier {t + 1} Minions, {i} Tier {t + 1} Rivals, and {e} Tier {t + 1} Bosses")
                    memory.TieredMinionCount = (memory.MinionCount - (2 * i)) - 2
                    memory.TieredRivalCount = i + 1
                if e - 4 >= 0:
                    print(f"- {memory.MinionCount - (2 * i)} Tier {t + 1} Minions, {i - (e - 4)} Tier {t + 1} Rivals, and {e} Tier {t + 1} Bosses")
                    memory.TieredMinionCount = memory.MinionCount - (2 * i)
                    memory.TieredRivalCount = i - (e - 4)
                else:
                    print(f"- {(memory.MinionCount - (2 * i)) - 2} Tier {t + 1} Minions, {i + 1} Tier {t + 1} Rivals, and {e} Tier {t + 1} Bosses")
                    memory.TieredMinionCount = (memory.MinionCount - (2 * i)) - 2
                    memory.TieredRivalCount = i + 1
        if memory.Threat % 4 == 0:
            print(f"- {memory.TieredMinionCount} Tier {t + 1} Minions, {memory.TieredRivalCount - 4} Tier {t + 1} Rivals, and {memory.MaxBosses} Tier {t + 1} Bosses")
        print("")
        print("")

if __name__ == "__main__":
    main()
