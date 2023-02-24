from django.db import models

from accounts.models import User
# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replied_to = models.BooleanField(default=False)

    

    def __str__(self):
        return "%s - %s" % (self.sender, self.reciever)