from django.db import models
from  embed_video.fields  import  EmbedVideoField
# Create your models here.
# this file we creates a database tables

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=13)
    description=models.TextField()

    def __str__(self):
        return self.email


class Oneninetynine(models.Model) :
     cardnumber=models.CharField(max_length=16)
     date=models.CharField(max_length=10)
     cvv=models.CharField(max_length=3)
     username=models.CharField(max_length=25)
     number=models.CharField(max_length=10)
     def str(self):
         return self.cardnumber

class Twoninetynine(models.Model) :
     cardnumber=models.CharField(max_length=16)
     date=models.CharField(max_length=10)
     cvv=models.CharField(max_length=3)
     username=models.CharField(max_length=25)
     number=models.CharField(max_length=10)
     def str(self):
         return self.cardnumber        

class Video(models.Model):
    title=models.CharField(max_length=100)
    added=models.DateField(auto_now_add=True)
    url=EmbedVideoField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-added']


class Threeninetynine(models.Model) :
     cardnumber=models.CharField(max_length=16)
     date=models.CharField(max_length=10)
     cvv=models.CharField(max_length=3)
     username=models.CharField(max_length=25)
     number=models.CharField(max_length=10)
     def str(self):
         return self.cardnumber    

class Forms(models.Model) :
     name=models.CharField(max_length=25)
     email=models.EmailField()
     phonenumber=models.CharField(max_length=13)   
     Gender=models.CharField(max_length=6)
     SSLC_board=models.CharField(max_length=5)
     PUC_board=models.CharField(max_length=25)
     interns=models.CharField(max_length=30)
     SSLC_percent=models.CharField(max_length=5)
     PUC_percent=models.CharField(max_length=5)
     USN=models.CharField(max_length=10)
     cgpa=models.CharField(max_length=4)
     Branch=models.CharField(max_length=40)
     College=models.CharField(max_length=50)
     files=models.ImageField(null=True,blank=True,upload_to="images/")

     def str(self):
        return self.name
     