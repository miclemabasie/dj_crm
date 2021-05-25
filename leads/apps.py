from django.apps import AppConfig


class LeadsConfig(AppConfig):
    name = 'leads'

    def ready(self):
        import leads.signals
