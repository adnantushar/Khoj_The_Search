from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import json
# Create your models here.


class ValuesStored(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    inputValues = models.CharField(max_length=200)
    timeStamp = models.DateTimeField(default=datetime.now)

    def set_inputValues(self, x):
        self.inputValues = json.dumps(x)

    def get_inputValues(self):
        return json.loads(self.inputValues)

    def __str__(self):
        return '{0} - {1}'.format(self.user.email, self.timeStamp)