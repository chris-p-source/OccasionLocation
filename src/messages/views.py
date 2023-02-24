from django.shortcuts import render
from .models import Message
from .forms import MessageForm, NewMessageForm

from django.http import HttpResponseRedirect

from accounts.models import User
# Create your views here.



def your_messages(request):
	
	messages_list = Message.objects.all()
	

	new_messages = messages_list.filter(reciever=request.user, replied_to=False)
	inbox_messages = messages_list.filter(reciever=request.user, replied_to=True)
	outbox_messages = messages_list.filter(sender=request.user)



	return render(request, 'your_messages.html', {'new_list' : new_messages, 'inbox_list': inbox_messages, 'outbox_list': outbox_messages})




def show_message(request, message_id):
	
	submitted = False
	message = Message.objects.get(pk=message_id)
	if request.method == "POST":

		form = MessageForm(request.POST)

		
		sender = User.objects.get(email=request.user)
		reciever = message.sender

		if form.is_valid():



			obj = form.save(commit=False)
			obj.sender = sender
			obj.reciever = reciever

			
			
			obj.save()
			
			return HttpResponseRedirect('/show_message/' + message_id + '?submitted=True')
	else:
		form = MessageForm
		if 'submitted' in request.GET:
			submitted = True

			form_update = MessageForm(request.POST or None, instance=message)

			obj2 = form_update.save(commit=False)
			obj2.replied_to = True
			obj2.save()


	return render(request, 'show_message.html', {'form':form, 'message': message, 'submitted':submitted})


	
def new_message(request):
	
	submitted = False
	
	if request.method == "POST":

		form = NewMessageForm(request.POST)

		if form.is_valid():



			obj = form.save(commit=False)
			obj.sender = request.user
			
			obj.save()
			
			return HttpResponseRedirect('message_submitted')
	else:

		form = NewMessageForm
		if 'submitted' in request.GET:
			submitted = True



	return render(request, 'new_message.html', {'form':form, 'submitted':submitted})


def message_submitted(request):

	context = {}

	return render(request, 'message_submitted.html', context)


