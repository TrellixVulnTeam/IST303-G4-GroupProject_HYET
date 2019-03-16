from django.db import models

class Product(models.Model):
    SKU = models.CharField(max_length=200)
    stock_status = models.BinaryField()
    url = models.URLField()
    picture_url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def getSKU(self):
        return self.SKU

    def getImage(self):
        return self.picture_url
