from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_page'

    verbose_name = _("home page")