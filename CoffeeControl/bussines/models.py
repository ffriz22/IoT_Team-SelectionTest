from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40)

    #Custom SAVE to filter only one coffeStock per department and CoffeType
    #By default CoffeeStock currents_units = 0
    def save(self, *args, **kwargs):
        from logistics.models import CoffeeType, CoffeeStock
        super(Department, self).save(*args, **kwargs)
        for coffee_type in CoffeeType.objects.all():
            try:
                CoffeeStock(department=self, coffee_Type=coffee_type).save()
            except AssertionError:
                print('There can only be one CoffeStock for Department -> CoffeType')
    
    def __str__(self):
        return 'Department: {}'.format(self.name)

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return 'Worker: {} working on {}'.format(self.user, self.department)