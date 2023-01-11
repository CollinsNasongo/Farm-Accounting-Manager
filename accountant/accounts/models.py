from django.db import models


class Batch(models.Model):
    batch_number = models.AutoField(primary_key=True)
    number_of_birds = models.IntegerField()
    initial_age_in_days = models.IntegerField()
    start_date = models.DateField()

class Mortality(models.Model):
    mortality_id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    number_of_dead = models.IntegerField()
    batch_number = models.ForeignKey(Batch, on_delete=models.CASCADE)

class Egg_production(models.Model):
    egg_production_id = models.BigAutoField(primary_key=True)
    egg_production_date =  models.DateField()
    number_of_eggs = models.IntegerField()
    batch_number = models.ForeignKey(Batch, on_delete=models.CASCADE)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)

class Sale(models.Model):
    sale_id = models.BigAutoField(primary_key=True)
    date_of_sale = models.DateField()
    number_sold = models.IntegerField()
    price = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.ForeignKey(Batch, on_delete=models.CASCADE)

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=50)

class Specific_spending(models.Model):
    spec_spend_id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    amount = models.IntegerField()
    expense_id = models.ForeignKey(Expense, on_delete=models.CASCADE)
    batch_number = models.ForeignKey(Batch, on_delete=models.CASCADE)

class General_spending(models.Model):
    gen_spend_id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    amount = models.IntegerField()
    expense_id = models.ForeignKey(Expense, on_delete=models.CASCADE)
