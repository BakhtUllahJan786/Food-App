from django.db import models


class Item(models.Model):
    #user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=400)
    item_desc=models.CharField(max_length=400)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=2000,default='https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png')

    def __str__(self):
        return self.item_name
