from django.db import models

# Create your models here.

class Equipment(models.Model):
    
    Name = models.CharField(max_length=100)
    Number = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Prodate = models.CharField(max_length=100)
    Buydate = models.CharField(max_length=100)

    def __unicode__(self):

        return self.Name
        
class User(models.Model):
    
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Leixing = models.CharField(max_length=30)
    
class LendEquipment(models.Model):
    
    LName = models.CharField(max_length=100)
    LNumber = models.CharField(max_length=100)
    LModel = models.CharField(max_length=100)
    LPrice = models.CharField(max_length=100)
    LProdate = models.CharField(max_length=100)
    LBuydate = models.CharField(max_length=100)
    LendDate=models.CharField(max_length=100)
    Lender=models.CharField(max_length=100)

class LendingEquipment(models.Model):
    
    LingName = models.CharField(max_length=100)
    LingNumber = models.CharField(max_length=100)
    LingModel = models.CharField(max_length=100)
    LingPrice = models.CharField(max_length=100)
    LingProdate = models.CharField(max_length=100)
    LingBuydate = models.CharField(max_length=100)
    LendingDate=models.CharField(max_length=100)
    Lendinger=models.CharField(max_length=100)
    
class GiveEquipment(models.Model):
    
    GName = models.CharField(max_length=100)
    GNumber = models.CharField(max_length=100)
    GModel = models.CharField(max_length=100)
    GPrice = models.CharField(max_length=100)
    GProdate = models.CharField(max_length=100)
    GBuydate = models.CharField(max_length=100)
    GivePlace=models.CharField(max_length=100)
    Giver=models.CharField(max_length=100)
    
class DeleteEquipment(models.Model):
    
    DName = models.CharField(max_length=100)
    DNumber = models.CharField(max_length=100)
    DModel = models.CharField(max_length=100)
    DPrice = models.CharField(max_length=100)
    DProdate = models.CharField(max_length=100)
    DBuydate = models.CharField(max_length=100)
    DeleteReason=models.CharField(max_length=200)
    Deleter=models.CharField(max_length=100)
  
