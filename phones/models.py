from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, null=False)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs) - models



