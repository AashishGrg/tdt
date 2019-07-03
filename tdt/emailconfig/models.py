from django.db import models
from authentication.models import User


class FetchParentRequest(models.Model):
    parent_email = models.EmailField()
    approved = models.BooleanField(default=False)
    your_email = models.EmailField()
    
    def __str__(self):
    	return 'Request Email-{}'.format(self.your_email)
