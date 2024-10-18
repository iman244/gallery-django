from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AboutpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_page'

    verbose_name = _("about page")