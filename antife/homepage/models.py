from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

class Product(models.Model):
    name = models.CharField(max_length=255)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    fiber = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    phenylalanine = models.DecimalField(max_digits=5, decimal_places=3)
    def __str__(self):
        return self.name

class Naudotojai(AbstractUser):
    # Add additional fields here if needed
    telefonas = models.CharField(max_length=255)
    el_pastas = models.EmailField(max_length=255, unique=True)
    gimimo_data = models.DateField()

    # Define the USERNAME_FIELD
    USERNAME_FIELD = 'username'  # or 'email' if you want to use email as the username

    # Define additional required fields
    REQUIRED_FIELDS = ['telefonas', 'el_pastas', 'gimimo_data', 'level']

class Receptai(models.Model):
    kalorijos = models.FloatField(default=0.0)
    pavadinimas = models.CharField(max_length=255)
    fenilalaninas = models.FloatField(default=0.0)
    aprasas = models.CharField(max_length=255)

class Forumai(models.Model):
    pavadinimas = models.CharField(max_length=255)

class Irasai(models.Model):
    tekstas = models.CharField(max_length=255)
    data = models.DateField()
    fk_Forumasid_Forumas = models.ForeignKey(Forumai, on_delete=models.CASCADE)
    fk_Naudotojasid_Naudotojas = models.ForeignKey(Naudotojai, on_delete=models.CASCADE)

class Kraujo_tyrimai(models.Model):
    data = models.DateField()
    fenilalaninas = models.IntegerField()
    fk_Naudotojasid_Naudotojas = models.ForeignKey(Naudotojai, on_delete=models.CASCADE)

class Recepto_produktai(models.Model):
    fk_Receptasid_Receptas = models.ForeignKey(Receptai, on_delete=models.CASCADE)
    fk_Produktasid_Produktas = models.ForeignKey(Product, on_delete=models.CASCADE)

class Naudotojo_receptai(models.Model):
    fk_Receptasid_Receptas = models.ForeignKey(Receptai, on_delete=models.CASCADE)
    fk_Naudotojasid_Naudotojas = models.ForeignKey(Naudotojai, on_delete=models.CASCADE)

class Valgiarasciai(models.Model):
    diena = models.IntegerField()
    bendras_fenilalaninas = models.IntegerField()
    data = models.DateField()
    fk_Naudotojasid_Naudotojas = models.ForeignKey(Naudotojai, on_delete=models.CASCADE)

class Komentarai(models.Model):
    tekstas = models.CharField(max_length=255)
    data = models.DateField()
    fk_Irasasid_Irasas = models.ForeignKey(Irasai, on_delete=models.CASCADE)
    fk_Naudotojasid_Naudotojas = models.ForeignKey(Naudotojai, on_delete=models.CASCADE)

class Valgymai(models.Model):
    tipas = models.CharField(max_length=255)
    fk_Valgiarastisid_Valgiarastis = models.ForeignKey(Valgiarasciai, on_delete=models.CASCADE)

class Valgomas_produktas(models.Model):
    fk_Valgymasid_Valgymas = models.ForeignKey(Valgymai, on_delete=models.CASCADE)
    fk_Produktasid_Produktas = models.ForeignKey(Product, on_delete=models.CASCADE)

class Valgymo_receptas(models.Model):
    fk_Receptasid_Receptas = models.ForeignKey(Receptai, on_delete=models.CASCADE)
    fk_Valgymasid_Valgymas = models.ForeignKey(Valgymai, on_delete=models.CASCADE)
