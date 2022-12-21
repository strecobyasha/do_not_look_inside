from random import randrange


class OddsGenerator:

    def __init__(self):
        self.margin = 5

    def match(self) -> tuple:
        home_win_prob, draw_prob, away_win_prob = self.probs(randrange(20, 80))
        home_win_odd, draw_odd, away_win_odd = self.odds(home_win_prob, draw_prob, away_win_prob)
        result = self.result(home_win_prob, draw_prob)

        return home_win_odd, draw_odd, away_win_odd, result

    def probs(self, home_win_prob: int) -> tuple:
        if home_win_prob > 50:
            draw_prob = (100-home_win_prob) * home_win_prob/100
            away_prob = 100-home_win_prob-draw_prob
        else:
            away_prob = (100-home_win_prob) * (100-home_win_prob)/100
            draw_prob = 100-home_win_prob-away_prob

        return home_win_prob, draw_prob, away_prob

    def odds(self, home_win_prob: float, draw_prob: float, away_win_prob: float) -> tuple:
        home_win_odd = round((100/home_win_prob)/(1+self.margin/100), 2)
        draw_odd = round((100 / draw_prob) / (1 + self.margin / 100), 2)
        away_win_odd = round((100/away_win_prob)/(1+self.margin/100), 2)

        return home_win_odd, draw_odd, away_win_odd

    def result(self, home_win_prob: float, draw_prob: float) -> int:
        random_result = randrange(0, 101)
        if random_result < home_win_prob:
            return 0
        if random_result < home_win_prob + draw_prob:
            return 1

        return 2

    def generator(self, games_num: int) -> list:
        return [self.match() for _ in range(games_num)]
