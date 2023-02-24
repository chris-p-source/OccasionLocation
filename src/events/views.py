from django.db.models import Q

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from .models import Event, EventAttendance
from accounts.models import User
from .forms import EventForm, EventAttendanceForm
from messages.forms import MessageForm

# Create your views here.

#deleting an event
def delete_event(request, event_id):

	obj = Event.objects.get(pk=event_id)

	if request.method == "POST":
		obj.delete()
		return redirect('your-events')

	return render(request, "delete_event.html", {'object' : obj})

#updating an event
def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)

	if form.is_valid():
		form.save()
		return redirect('your-events')
	return render(request, 'update_event.html', {'event': event, 'form': form})



#Displays events user is hosting and attending
def your_events(request):
	
	event_list = Event.objects.all()
	event_attendance_list = EventAttendance.objects.all()


	hosted_events = event_list.filter(host=request.user)
	attending_list = event_attendance_list.filter(person_key=request.user)


	return render(request, 'your_events.html', {'event_list': hosted_events, 'event_list2': attending_list})







#Add event function
def add_event(request):

	submitted = False
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():

			obj = form.save(commit=False)
			obj.host= request.user

			obj.save()
			return HttpResponseRedirect('/add_event?submitted=True')
	else:
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True




	return render(request, 'add_event.html', {'form':form, 'submitted':submitted})


#Shows event details and sign up
def show_event(request, event_id):
	
	submitted = False
	event = Event.objects.get(pk=event_id)
		
	if request.user.is_authenticated:
		if request.method == "POST":

			form = EventAttendanceForm(request.POST)
		
			current_joiner = User.objects.get(email=request.user)

			if form.is_valid():

				obj = form.save(commit=False)
				obj.person_key = current_joiner
				obj.event_key = event

				obj.save()
				return HttpResponseRedirect('/show_event/' + event_id + '?submitted=True')
		else:
			form = EventAttendanceForm
			if 'submitted' in request.GET:
				submitted = True

	else:
		return redirect('register')

	return render(request, 'show_event.html', {'form':form, 'event': event, 'submitted':submitted})




#Message host
def message_host(request, event_id):
	
	submitted = False
	event = Event.objects.get(pk=event_id)
	
	if request.method == "POST":

		form = MessageForm(request.POST)
		
		sender = User.objects.get(email=request.user)
		host = event.host

		if form.is_valid():

			obj = form.save(commit=False)
			obj.sender = sender
			obj.reciever = host

			obj.save()
			return HttpResponseRedirect('/../message_submitted')
	else:
		form = MessageForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'message_host.html', {'form':form, 'event': event, 'submitted':submitted})





#Full list of all events running
def list_events(request):
	event_list = Event.objects.all()

	return render(request, 'events.html', {'event_list': event_list})


#Function to search all events
def search_events(request):
	if request.method == "POST":
		searched = request.POST['searched']
		try:
			events = Event.objects.filter(
				Q(title__contains=searched) |
				Q(town__contains=searched) |
				Q(county__contains=searched) |
				Q(postcode__contains=searched) |
				Q(address__contains=searched)


				)

		except Event.DoesNotExist:
			events = None


		return render(request, 'search_events.html', {'searched':searched, 'events':events})
	else:
		return render(request, 'search_events.html')



