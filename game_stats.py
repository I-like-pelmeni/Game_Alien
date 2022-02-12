class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра запускается в неактивной состоянии
        self.game_active = False

    def reset_stats(self):
        """Сбрасывает статистику"""
        self.ships_left = self.settings.ship_limit