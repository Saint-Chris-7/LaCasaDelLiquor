from django.apps import AppConfig


class LacasadelliqourConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LaCasaDelLiqour'

    def ready(self):
        import LaCasaDelLiqour.signals
