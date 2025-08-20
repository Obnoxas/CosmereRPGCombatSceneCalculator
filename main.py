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
    
    memory.log() # DEBUG TEST, PLEASE DELETE

    print("Your options are:")

    print("TIER 1")

    memory.MinionCount = Calculation(1, memory.Threat, memory.PartyTier)

    for i in range(abs(-memory.MinionCount // 2)):
        print(f"- {memory.MinionCount - (2 * i)} Tier 1 Minions, {i} Tier 1 Rivals, and ? Tier 1 Bosses")

    print("")
    print("TIER 2")

    memory.MinionCount = Calculation(2, memory.Threat, memory.PartyTier)

    for i in range(abs(-memory.MinionCount // 2)):
        print(f"- {memory.MinionCount - (2 * i)} Tier 2 Minions, {i} Tier 2 Rivals, and ? Tier 2 Bosses")

    print("")
    print("TIER 3")

    memory.MinionCount = Calculation(3, memory.Threat, memory.PartyTier)

    for i in range(abs(-memory.MinionCount // 2)):
        print(f"- {memory.MinionCount - (2 * i)} Tier 3 Minions, {i} Tier 3 Rivals, and ? Tier 3 Bosses")

    print("")
    print("TIER 4")

    memory.MinionCount = Calculation(4, memory.Threat, memory.PartyTier)

    for i in range(abs(-memory.MinionCount // 2)):
        print(f"- {memory.MinionCount - (2 * i)} Tier 4 Minions, {i} Tier 4 Rivals, and ? Tier 4 Bosses")


if __name__ == "__main__":
    main()
