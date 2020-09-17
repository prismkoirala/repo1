from django.db import models
from django.contrib.auth import get_user_model


class Train(models.Model):
    data_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    gyr_x = models.DecimalField(max_digits=10, decimal_places=8,default=0.111)
    gyr_y = models.DecimalField(max_digits=10, decimal_places=8,default=0.111)
    gyr_z = models.DecimalField(max_digits=10, decimal_places=8,default=0.111)
    acc_x = models.DecimalField(max_digits=10, decimal_places=8,default=0.111)
    acc_y = models.DecimalField(max_digits=10, decimal_places=8,default=0.111)
    acc_z = models.DecimalField(max_digits=10, decimal_places=8,default=0.111)
    user_id = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
# Create your models here.
