from django.db import models


class Transaction(models.Model):
    amount = models.DecimalField(default=.0, decimal_places=2, max_digits=9, blank=False)
    description = models.TextField(verbose_name='description')
    payment_dt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    payment_success = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'

    def __str__(self):
        return str(self.id)

