from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-eno')

    def get_emp_eno(self):
        return super().get_queryset().filter(eno__in=['100','500']).order_by('-eno')

# Create your models here.
class employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=10)
    efname =models.CharField(max_length=50,null=True,blank=True)
    elname =models.CharField(max_length=50,null=True,blank=True)
    eaddr =models.CharField(max_length=50,null=True,blank=True)
    eclass =models.CharField(max_length=50,null=True,blank=True)
    emarks =models.CharField(max_length=50,null=True,blank=True)
    objects =CustomManager() 




    def __str__(self):
        return f"{self.ename} , {self.eno}"


### midddle ware
## sessions and cookies
## templates filter
## context_processors
## ORM
## Manager
## Logging
## decorators
## generators
## Serializers
## mixins 
## read all rest api topics 
## reverse once again without seeing  ## read your self and make revision 
## build an application up to login page and signup page with validations
## build an form using html form and apply validations



