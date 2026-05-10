class Results:
    def __init__(self, victories:int=0, draws:int=0, losses:int=0):
        self.victories = victories
        self.draws = draws
        self.losses = losses

    @staticmethod
    def total_points(wins:int, draws:int) -> str:
        total_points = 3 * (wins + draws)
        return f'Общее количество очков: {total_points}'

class Football(Results):
    def __init__(self, victories:int=0, draws:int=0, losses:int=0):
        super().__init__(victories, draws, losses)

    def number_of_wins(self) -> str:
        return f'Футбольных побед: {self.victories}'

    def number_of_draws(self) -> str:
        return f'Футбольных ничьих: {self.draws}'

    def number_of_losses(self) -> str:
        return f'Футбольных поражений: {self.losses}'

class Hockey(Results):
    def __init__(self, victories:int=0, draws:int=0, losses:int=0):
        super().__init__(victories, draws, losses)

    def number_of_wins(self) -> str:
        return f'Хоккейных побед: {self.victories}'

    def number_of_draws(self) -> str:
        return f'Хоккейных ничьих: {self.draws}'

    def number_of_losses(self) -> str:
        return f'Хоккейных поражений: {self.losses}'


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)


