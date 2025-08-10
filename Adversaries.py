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

class Minion(Adversary):
    def __init__(self, tier, partytier):
        super().__init__(self, 0.5, tier, partytier)

class Rival(Adversary):
    def __init__(self, tier, partytier):
        super().__init__(self, 1, tier, partytier)

class Boss(Adversary):
    def __init__(self, tier, partytier):
        super().__init__(self, 4, tier, partytier)