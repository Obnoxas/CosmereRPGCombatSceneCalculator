from TempMem import *
from Calculator import *

def main():
    memory = MemoryBank(input("What Tier is your party? (Pg 24): "), input("How many characters are in your party?: "), input("Is this Combat Scene Easy, Medium, or Hard?: "))
    memory.ValidityCheck()
    
    if memory.EncounterDifficulty == "easy":
        memory.UpdateThreat(EasyThreat(memory.PartyNumber))
    if memory.EncounterDifficulty == "medium":
        memory.UpdateThreat(MediumThreat(memory.PartyNumber))
    if memory.EncounterDifficulty == "hard":
        memory.UpdateThreat(HardThreat(memory.PartyNumber))
    
    memory.log()


if __name__ == "__main__":
    main()
