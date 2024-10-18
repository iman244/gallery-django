from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class WorksPage(SingletonModel):
    title = models.CharField(_("title"), max_length=1000)

    def __str__(self) -> str:
        return "works page"


class Work(models.Model):
    caption = models.CharField(_('caption'), max_length=255)
    image = models.ImageField(_("image"))

    def __str__(self) -> str:
        return self.image
