from django.apps import AppConfig


class ScrapperappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrapperApp'

    def ready(self):
        from jobs import updater
        updater.start()
