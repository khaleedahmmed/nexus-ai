from .app_settings import AppSettings
from .ai_settings import AISettings


class Settings:
    def __init__(self):
        self.app = AppSettings()
        self.ai = AISettings()
        
settings = Settings()