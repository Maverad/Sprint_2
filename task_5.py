class Results:
    def __init__(self, victories:int=0, draws:int=0, losses:int=0):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def __init__(self, victories:int=0, draws:int=0, losses:int=0):
        super().__init__(victories, draws, losses)

    def number_of_wins(self) -> str:
        return f'Футбольных побед: {self.victories}'

    def number_of_draws(self) -> str:
        return f'Футбольных ничьих: {self.draws}'

    def number_of_losses(self) -> str:
        return f'Футбольных поражений: {self.losses}'

    def total_points(self) -> str:
        total_points = 3 * (self.victories + self.draws)
        return f'Общее количество очков: {total_points}'

class Hockey(Results):
    def __init__(self, victories:int=0, draws:int=0, losses:int=0):
        super().__init__(victories, draws, losses)

    def number_of_wins(self) -> str:
        return f'Хоккейных побед: {self.victories}'

    def number_of_draws(self) -> str:
        return f'Хоккейных ничьих: {self.draws}'

    def number_of_losses(self) -> str:
        return f'Хоккейных поражений: {self.losses}'
    
    def total_points(self) -> str:
        total_points = 2 * (self.victories + self.draws)
        return f'Общее количество очков: {total_points}'

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for i in (football_team, hockey_team):
    for j in dir(i):
        if j.startswith('__'):
            continue
        else:
            method = getattr(i, j)
            if callable(method):
                print(method())
