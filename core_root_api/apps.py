from django.apps import AppConfig


class CoreRootApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_root_api"

    def ready(self):
        import core_root_api.recievers  # Ensure th
