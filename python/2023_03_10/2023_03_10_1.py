# ３の倍数で鳴き声が変わるきんにくん

count = 1
for i in range(10):
    if count % 3 == 0:
        print("power-!")
    else:
        print('ya-!')
    count += 1
    
# ------------------------------

# リスト内包表記練習
num_list = [i for i in range(10)]
print(num_list)

# ------------------------------

# クラス練習
class Football_Team:
    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw
        
    def culc_win_rate(self):
        win_rate = self.win / (self.win + self.lose)
        return win_rate
    
    def show_team_result(self):
        print(f"{self.name:14} W:{self.win:>3}  L:{self.lose:>3}  D:{self.draw:>3}  R:{self.culc_win_rate():.3f}")


brazil = Football_Team('Brazil', 73, 18, 18)
italy = Football_Team('Italy', 45, 21, 21)
argentina = Football_Team('Argentina', 43, 15, 15)
west_germany = Football_Team('West_Germany', 36, 14, 14)
france = Football_Team('France', 34, 13, 13)
germany = Football_Team('Germany', 31, 6, 6)
spain = Football_Team('Spain', 30, 15, 15)

teams = [brazil, italy, argentina, west_germany, france, germany, spain]
for team in teams:
    team.show_team_result()
# 後で勝率でソートして同じように表示する方法を考える。質問：DBでやれば簡単そうだけどこのプログラム内だけでやるのは面倒くさそう？
