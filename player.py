import random

class Player:
    def __init__(self):
        self.score = 0
    
    def roll(self):
        outcome = random.randint(1,6)
        print(f"Player rolled {outcome}")
        self.score += outcome
        print(f"Player score is now {self.score}")

    
