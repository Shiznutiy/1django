from django.db import models

class Review(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    email = models.EmailField("Email")
    text = models.TextField("Текст отзыва")
    checked = models.BooleanField("Проверено", default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} — {self.email}"