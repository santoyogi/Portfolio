from django.db import models


# Create your models here.
class Hobbies(models.Model):
    def __str__(self):
        return self.hobby_name+ "-" + self.hobby_description + " "

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)

class Portfolio(models.Model):
    def __str__(self):
        return self.portfolio_item_name + "-" + \
            self.portfolio_item_description + " "
    portfolio_item_name = models.CharField(max_length=200)
    portfolio_item_description = models.CharField(max_length=200)

