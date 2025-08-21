from TempMem import *
from Calculator import *
from Adversaries import *

def main():
    memory = MemoryBank(input("What Tier is your party? (Pg 24): "), input("How many characters are in your party?: "), input("Is this Combat Scene Easy, Medium, or Hard?: "))
    memory.ValidityCheck()
    
    if memory.EncounterDifficulty == "easy":
        memory.UpdateThreat(EasyThreat(memory.PartyNumber))
    if memory.EncounterDifficulty == "medium":
        memory.UpdateThreat(MediumThreat(memory.PartyNumber))
    if memory.EncounterDifficulty == "hard":
        memory.UpdateThreat(HardThreat(memory.PartyNumber))
        
    memory.Responses.append("Your options are:")

    memory.Responses.append("TIER 1")

    memory.MinionCount = MinionCalculation(1, memory.Threat, memory.PartyTier)
    memory.MaxBosses =  BossCalculation(1, memory.Threat, memory.PartyTier)

    for e in range(memory.MaxBosses):
        if memory.TieredRivalCount < 4:
            for i in range(abs(-memory.MinionCount // 2)):
                memory.RivalCount += 1
                memory.TieredRivalCount += 1
                response = (f"- {memory.MinionCount - (2 * i)} Tier 1 Minions, {i} Tier 1 Rivals, and {memory.BossCount} Tier 1 Bosses")
                if response not in memory.Responses:
                    memory.Responses.append(response)
                memory.TieredMinionCount = memory.MinionCount - (2 * i)
        if memory.RivalCount >= 4:
            for i in range(abs(-memory.RivalCount // 4)):
                if memory.RivalCount >= 4:
                    response = (f"- {memory.TieredMinionCount} Tier 1 Minions, {memory.RivalCount - (4 * (i + 1))} Tier 1 Rivals, and {i + 1} Tier 1 Bosses")
                    if response not in memory.Responses:
                        memory.Responses.append(response)
                    memory.TieredRivalCount -= 4
                else:
                    pass
            memory.RivalCount = 0

    memory.Responses.append("")
    memory.Responses.append("TIER 2")

    memory.MinionCount = MinionCalculation(2, memory.Threat, memory.PartyTier)
    memory.RivalCount = 0
    memory.BossCount = 0
    memory.MaxBosses =  BossCalculation(2, memory.Threat, memory.PartyTier)
    memory.TieredMinionCount = 0
    memory.TieredRivalCount = 0

    for e in range(memory.MaxBosses):
        if memory.TieredRivalCount < 4:
            for i in range(abs(-memory.MinionCount // 2)):
                memory.RivalCount += 1
                memory.TieredRivalCount += 1
                response = (f"- {memory.MinionCount - (2 * i)} Tier 2 Minions, {i} Tier 2 Rivals, and {memory.BossCount} Tier 2 Bosses")
                if response not in memory.Responses:
                    memory.Responses.append(response)
                memory.TieredMinionCount = memory.MinionCount - (2 * i)
        else:
            for i in range(abs(-memory.RivalCount // 4)):
                if memory.TieredRivalCount >= 4:
                    response = (f"- {memory.TieredMinionCount} Tier 2 Minions, {memory.RivalCount - (4 * (i + 1))} Tier 2 Rivals, and {i + 1} Tier 2 Bosses")
                    if response not in memory.Responses:
                        memory.Responses.append(response)
                    memory.TieredRivalCount -= 4
                    memory.BossCount += 1
                else:
                    pass

    memory.Responses.append("")
    memory.Responses.append("TIER 3")

    memory.MinionCount = MinionCalculation(3, memory.Threat, memory.PartyTier)
    memory.RivalCount = 0
    memory.BossCount = 0
    memory.MaxBosses =  BossCalculation(3, memory.Threat, memory.PartyTier)
    memory.TieredMinionCount = 0
    memory.TieredRivalCount = 0

    for e in range(memory.MaxBosses):
        if memory.TieredRivalCount < 4:
            for i in range(abs(-memory.MinionCount // 2)):
                memory.RivalCount += 1
                memory.TieredRivalCount += 1
                response = (f"- {memory.MinionCount - (2 * i)} Tier 3 Minions, {i} Tier 3 Rivals, and {memory.BossCount} Tier 3 Bosses")
                if response not in memory.Responses:
                    memory.Responses.append(response)
                memory.TieredMinionCount = memory.MinionCount - (2 * i)
        if memory.RivalCount >= 4:
            for i in range(abs(-memory.RivalCount // 4)):
                if memory.TieredRivalCount >= 4:
                    response = (f"- {memory.TieredMinionCount} Tier 3 Minions, {memory.RivalCount - (4 * (i + 1))} Tier 3 Rivals, and {i + 1} Tier 3 Bosses")
                    if response not in memory.Responses:
                        memory.Responses.append(response)
                    memory.TieredRivalCount -= 4
                else:
                    pass

    memory.Responses.append("")
    memory.Responses.append("TIER 4")

    memory.MinionCount = MinionCalculation(4, memory.Threat, memory.PartyTier)
    memory.RivalCount = 0
    memory.BossCount = 0
    memory.MaxBosses =  BossCalculation(4, memory.Threat, memory.PartyTier)
    memory.TieredMinionCount = 0
    memory.TieredRivalCount = 0

    for e in range(memory.MaxBosses):
        if memory.TieredRivalCount < 4:
            for i in range(abs(-memory.MinionCount // 2)):
                memory.RivalCount += 1
                memory.TieredRivalCount += 1
                response = (f"- {memory.MinionCount - (2 * i)} Tier 4 Minions, {i} Tier 4 Rivals, and {memory.BossCount} Tier 4 Bosses")
                if response not in memory.Responses:
                    memory.Responses.append(response)
                memory.TieredMinionCount = memory.MinionCount - (2 * i)
        if memory.RivalCount >= 4:
            for i in range(abs(-memory.RivalCount // 4)):
                if memory.TieredRivalCount >= 4:
                    response = (f"- {memory.TieredMinionCount} Tier 4 Minions, {memory.RivalCount - (4 * (i + 1))} Tier 4 Rivals, and {i + 1} Tier 4 Bosses")
                    if response not in memory.Responses:
                        memory.Responses.append(response)
                    memory.TieredRivalCount -= 4
                else:
                    pass

    for response in memory.Responses:
        print(response)


if __name__ == "__main__":
    main()
