class Adversary():
    def __init__(self, threat, tier, partytier):
        self.Tier = tier
        self.RelativeTier = tier - partytier
        if self.RelativeTier > 0:
            self.RelativeThreat = (threat * 2) * self.RelativeTier
        if self.RelativeTier < 0:
            self.RelativeThreat = (threat * 0.5) * abs(self.RelativeTier)
        if self.RelativeTier == 0:
            self.RelativeThreat = threat

def log(self):
    print(f"My Realative Threat is {self.RelativeThreat}, my Tier is {self.Tier}, and the difference between the Party's Tier and my Tier is {self.RelativeTier}")

class Minion(Adversary):
    def __init__(self, tier, partytier):
        super().__init__(0.5, tier, partytier)

class Rival(Adversary):
    def __init__(self, tier, partytier):
        super().__init__(1, tier, partytier)

class Boss(Adversary):
    def __init__(self, tier, partytier):
        super().__init__(4, tier, partytier)