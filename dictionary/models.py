from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=50, help_text="Ex. Money")

    def __str__(self):
        return '{}'.format(self.name)


class Level(models.Model):
    name = models.CharField(max_length=50, help_text="Ex. B1.2")

    def __str__(self):
        return '{}'.format(self.name)


class Word(models.Model):
    english_word = models.CharField(max_length=60, help_text="Ex. Travel")
    spanish_word = models.CharField(max_length=60, help_text="Ex. Viajar")
    spanish_pronunciation = models.CharField(max_length=60,
                                             help_text="Ex. trável (puedes usar las tildes para acentuar donde se hace el énfasis en la pronunciación)",
                                             null=True, blank=True)
    phonetics = models.CharField(max_length=60,
                                 help_text="Ex. /ˈtræv(ə)l/. Get it on: https://www.wordreference.com/",
                                 null=True, blank=True)
    notes = models.TextField(max_length=settings.DEFAULT_TEXTAREA_SIZE,
                             help_text="Ex. Suele usarse como verbo, rara como sustantivo o adjetivo", null=True,
                             blank=True)
    is_important = models.BooleanField(default=False, help_text="This word has extra score for exams in the same level")
    category = models.ManyToManyField(Category)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=2)

    def get_categories(self):
        return ", ".join([l.name for l in self.category.all()])


    def __str__(self):
        return 'Word({} - {})'.format(self.english_word, self.spanish_word)
