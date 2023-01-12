"""
"""
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    rubric = models.ForeignKey(
        "Rubrick",
        null=True,
        on_delete=models.PROTECT,
        verbose_name="рубрика",
        )

    class Meta:
        verbose_name_plural = 'Объявления' # название модели во множественном числе;
        verbose_name = 'Объявление' # название модели в единственном числе.
        ordering = ['-published']   # последовательность полей, по которым по умолчанию будет выпол-
                                    # няться сортировка записей.

    def __str__(self):
        return f"{self.title}: {self.content}"


class Rubrick(models.Model):
    name = models.CharField(max_length=25,
                            db_index=True,
                            # unique=True,
                            verbose_name= 'Haзвaниe')
    
    class Meta:
        verbose_name = "Rubric"
        verbose_name_plural = "Rubrics"
        ordering = ["name"]

    def __str__(self):
        return f"rubrick: {self.name}"
