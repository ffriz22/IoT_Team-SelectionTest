from bussines.models import Department
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class CoffeeType(models.Model):
    name = models.CharField(max_length=40)
    current_price = models.FloatField(validators=[MinValueValidator(0)])

    #Custom SAVE to filter only one coffeStock per department and CoffeType
    #By default CoffeeStock currents_units = 0
    def save(self, *args, **kwargs):
        from bussines.models import Department
        super(CoffeeType, self).save(*args, **kwargs)
        for d in Department.objects.all():
            try:
                CoffeeStock(department=d, coffee_Type=self).save()
            except AssertionError:
                print('There can only be one CoffeStock per department and CoffeeType')
    
    def __str__(self):
        return 'CoffeeType: {}'.format(self.name)

class CoffeeStock(models.Model):
    currents_units = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    coffee_Type = models.ForeignKey(CoffeeType, on_delete=models.CASCADE)
    department = models.ForeignKey('bussines.Department', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        #Is new model Object
        if self.pk is None: 
            assert CoffeeStock.objects.filter(
                department=self.department, 
                coffee_Type=self.coffee_Type).count() == 0, 'There is a CoffeeStock for this department and CoffeType'
        super(CoffeeStock, self).save(*args, **kwargs)
        
        #If there are 0 units, a coffeeOrder record will be created by default
        if self.currents_units == 0:
            coffe_order = CoffeeOrder(coffee_stock=self, 
            units=100, unit_price=self.coffee_Type.current_price)
            coffe_order.save()
    
    def __str__(self):
        return 'CoffeeStock current units: {} of {} on {}'.format(
            self.currents_units, 
            self.coffee_Type, 
            self.department)
            
class CoffeeOrder(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    STATUS_CHOICES = (
        (PENDING, ('Pending status')),
        (ACCEPTED, ('Accepted status')),
    )
    unit_price = models.FloatField(validators=[MinValueValidator(0)])
    units = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=PENDING)
    coffee_stock = models.ForeignKey(CoffeeStock, on_delete=models.CASCADE)

    def __str__(self):
        return 'CoffeeOrder state: {}, units {} of {} on {}'.format(
            self.status, 
            self.units, 
            self.coffee_stock.coffee_Type, 
            self.coffee_stock.department)