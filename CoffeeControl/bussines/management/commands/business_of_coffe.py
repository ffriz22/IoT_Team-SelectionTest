from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from bussines.models import Department, Worker
from logistics.models import CoffeeType

class Command(BaseCommand):
    help = 'Adding departments, workers and coffeTypes'
    def handle(self, *args, **kwargs):

        print("Departaments added")
        #Departments
        try:
            d1 = Department.objects.get(name='P&G')
        except Department.DoesNotExist:
            d1 = Department(name='P&G')
            d1.save()
        try:
            d2 = Department.objects.get(name='VR')
        except Department.DoesNotExist:
            d2 = Department(name='VR')
            d2.save()
        try:
            d3 = Department.objects.get(name='IOT')
        except Department.DoesNotExist:
            d3 = Department(name='IOT')
            d3.save()
        try:
            d4 = Department.objects.get(name='AR')
        except Department.DoesNotExist:
            d4 = Department(name='AR')
            d4.save()

        print("Users added")
        #Users
        try:
            u1 = User.objects.get(username='bob1')
        except User.DoesNotExist:
            u1 = User.objects.create_user('bob1','bob1@bob.com','bob1pssword')
            u1.save()

        try:
            u2 = User.objects.get(username='bob2')
        except User.DoesNotExist:
            u2 = User.objects.create_user('bob2','bob2@bob.com','bob2pssword')
            u2.save()

        try:
            u3 = User.objects.get(username='bob3')
        except User.DoesNotExist:
            u3 = User.objects.create_user('bob3','bob3@bob.com','bob3pssword')
            u3.save()

        try:
            u4 = User.objects.get(username='bob4')
        except User.DoesNotExist:
            u4 = User.objects.create_user('bob4','bob4@bob.com','bob4pssword')
            u4.save()

        print("Workers added")
        #Workers
        try:
            w1 = Worker.objects.get(user=u1, department = d1)
        except Worker.DoesNotExist:
            w1 = Worker(user=u1, department = d1)
            w1.save()
        try:
            w2 = Worker.objects.get(user=u2, department = d2)
        except Worker.DoesNotExist:
            w2 = Worker(user=u2, department = d2)
            w2.save()
        try:
            w3 = Worker.objects.get(user=u3, department = d3)
        except Worker.DoesNotExist:
            w3 = Worker(user=u3, department = d3)
            w3.save()
        try:
            w4 = Worker.objects.get(user=u4, department = d4)
        except Worker.DoesNotExist:
            w4 = Worker(user=u4, department = d4)
            w4.save()

        print("CoffeTypes added")
        #CoffeTypes
        try:
            c1 = CoffeeType.objects.get(name='Verdadero', current_price=5.0)
        except CoffeeType.DoesNotExist:
            c1 = CoffeeType(name='Verdadero', current_price=5.0)
            c1.save()
        try:
            c2 = CoffeeType.objects.get(name='Con leche', current_price=6.0)
        except CoffeeType.DoesNotExist:
            c2 = CoffeeType(name='Con leche', current_price=6.0)
            c2.save()