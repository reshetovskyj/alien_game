class Settings:
    """Клас для збереження налаштувань"""

    def __init__(self):
        """Ініціалізувати постійні налаштування гри"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Налаштування кулі
        self.bullet_width = 1500
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_alowed = 10

        # Налаштування корабля

        self.ship_limit = 3

        # Налаштування прибульця
        self.fleet_drop_speed = 10

        # Як швидко гра має прискорюватися
        self.speedup_scale = 1.1

        # Як швидко збільшується вартість прибульців
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізація змінних налаштувань"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

        # Отримання балів
        self.alien_points = 50

    def increase_speed(self):
        """Збільшення налаштувань швидкості"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
