class MemoryBank():
    def __init__(self, tier, number, difficulty):
        self.PartyTier = int(tier)
        self.PartyNumber = int(number)
        self.EncounterDifficulty = difficulty.lower()

    def ValidityCheck(self):
        if 0 >= self.PartyTier or 5 <= self.PartyTier:
            print("Invalid Tier!")
            exit()
        if 0 >= self.PartyNumber:
            print("Invalid party size!")
            exit()
        if self.EncounterDifficulty not in ("easy", "medium", "hard"):
            print("Invalid dificulty!")
            exit()


    def log(self):
        print(f" The party is Tier {self.PartyTier}, there are {self.PartyNumber} people in the party, and the Combat Scene's difficulty is {self.EncounterDifficulty}!")
