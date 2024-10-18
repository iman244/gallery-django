from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class HomePage(SingletonModel):
    cover = models.ImageField(_("cover"))
    title = models.CharField(_("title"), max_length=1000)
    description = models.TextField(_("description"), max_length=2000)
    second_description = models.TextField(
        _("second description"), max_length=2000)
    some_works_button_text = models.CharField(
        _("some works button text"), max_length=1000)
    about_button_text = models.CharField(
        _("about works button text"), max_length=1000)

    def __str__(self) -> str:
        return "home page"


class SocialMedia(models.Model):
    name = models.CharField(_("name"), max_length=255)
    image = models.ImageField(_("image"))
    link = models.URLField(_("your social media link"))
    page = models.ForeignKey(HomePage, on_delete=models.PROTECT, default=1)

    def __str__(self) -> str:
        return self.name
