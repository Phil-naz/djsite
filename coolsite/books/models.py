from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

from django.conf import settings
User = settings.AUTH_USER_MODEL


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name | Название")  # 'verbose_name' for view in the admin panel
    slug = AutoSlugField(populate_from='name', unique_with='author')
    author = models.CharField(max_length=255, verbose_name="Author(s) | Автор(ы)")
    author_description = models.TextField(verbose_name="Author's description | Описание автора")
    photo = models.ImageField(upload_to="books_photos", verbose_name="Photo | Фотография")
    publishing_house = models.ForeignKey('Publishing_house', on_delete=models.PROTECT, verbose_name="Publishing house | Издательство", null=True)

    def __str__(self):  # function for showing field 'name' in SQL query (in CMD)
        return self.name  # SQL: Books.objects.all()

    def get_absolute_url(self):  # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('book', kwargs={'slug': self.slug})  # функция reverse составляет url, ‘book’ - URL name from file ‘URL.PY’

    class Meta:
        verbose_name = 'Книги'  # название в админ панели
        verbose_name_plural = 'Книги'  # множ. число в админ панели
        ordering = ['-id']  # сортировка, "-" - обр.порядок. Ordering for view at site


class Publishing_house(models.Model):
    publishing_house = models.TextField(verbose_name="Издательство")

    def __str__(self):  # function for showing field 'quote' in SQL query
        return self.publishing_house  # SQL: Quotes.objects.all()

    class Meta:
        verbose_name = 'Издательство'  # название в админ панели
        verbose_name_plural = 'Издательства'  # множ. число в админ панели