from django.db import models


# Create your models here.
class Hobbies(models.Model):
    def __str__(self):
        return self.hobby_name+ "-" + self.hobby_description + " "

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://sarkissian.pro/wp-content/uploads/2021/01/Jewelry-Inventory-1-256x256.png")


class Portfolio(models.Model):
    def __str__(self):
        return self.portfolio_item_name + "-" + \
            self.portfolio_item_description + " "
    portfolio_item_name = models.CharField(max_length=200)
    portfolio_item_description = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500, default="https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/3162705/portfolio-clipart-md.png")
