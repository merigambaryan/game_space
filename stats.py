class Stats():
    """остлеживание статистики"""

    def __init__(self):
        """инициаизирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())
    def reset_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.guns_left = 3
        self.score = 0
