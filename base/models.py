from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def save(self,*args,**kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        self.created_at = timezone.now()

        super(BaseModel,self).save(*args,**kwargs)