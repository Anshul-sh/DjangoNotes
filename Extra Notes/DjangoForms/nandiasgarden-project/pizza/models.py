from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    #if one thing is deleted we are going to delete the corresponidng object too. That's what on_delete = models.CASCADE means.
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
