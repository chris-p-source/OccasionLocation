from django import forms
from django.forms import ModelForm
from .models import Message






class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        exclude = ["sender", "reciever", "replied_to"]
        fields = ('sender', 'reciever', 'msg_content', 'replied_to')


class NewMessageForm(ModelForm):
    
    class Meta:
        model = Message
        exclude = ["sender", "replied_to"]
        fields = ('sender', 'reciever', 'msg_content', 'replied_to')