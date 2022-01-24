from django.db import models


class IdentificationUser(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField('Імя', max_length=50, default="")
    last_name = models.CharField('Прізвище', max_length=50, )
    full_name = models.CharField( max_length=128, default="")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def save( self, *args, **kw ):
        self.full_name = self.first_name + self.last_name
        super( IdentificationUser, self ).save( *args, **kw )
    
    
    
