from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

class AboutPage(SingletonModel):
    image = models.ImageField(_("image"))
    title = models.CharField(_("title"), max_length=1000)
    content = HTMLField(_("content"))
    home_page_button_text = models.CharField(_("home page button text"), max_length=1000)
    
    def __str__(self) -> str:
        return "about page"
