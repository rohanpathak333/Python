import datetime

class Player:
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    
    def get_age(self): 
        now = datetime.datetime.now()
        return now.year - self.birth_year

class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year):
        super().__init__(fname, lname, birth_year)
        self.aces = []

    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)
    
class CricketPlayer(Player):
    def __init__(self, fname, lname, team, birth_year):
        super().__init__(fname, lname, birth_year)
        self.team = team
        self.scores = []
        
    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)

roger = TennisPlayer("roger", "federer", 1988)
print(roger.first_name)
