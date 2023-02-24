"""finalyearproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from pages.views import home_view, about_view, faq_view, addevent_view, results_view

from events.views import (
    search_events,
    list_events,
    show_event,
    add_event,
    your_events,
    update_event,
    delete_event,
    message_host,
    
    )

from accounts.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,


    )

from messages.views import (

    your_messages,
    show_message,
    new_message,
    message_submitted,
    
    )

urlpatterns = [
    
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('about/', about_view, name='about'),
    path('faq/', faq_view, name='faq'),
    
    path('addevent/', addevent_view, name='addevent'),
    path('results/', results_view, name='results'),
    path('signup/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name='login'),
    path('settings/', account_view, name='settings'),

    #search 
    path('search_events', search_events, name='search-events'),
    #list all events on all events page
    path('list_events', list_events, name='list-events'),
    #show details of events on both search page and all events page
    path('show_event/<event_id>', show_event, name= 'show-event'),
    #add event
    path('add_event', add_event, name='add-event'),
    #show what events user is hosting/attending
    path('your_events', your_events, name='your-events'),
    #update event
    path('update_event/<event_id>', update_event, name= 'update-event'),
    #Delete event
    path('delete_event/<event_id>', delete_event, name= 'delete-event'),

    
    #private chat system
    path('your_messages', your_messages, name='your-messages'),
    #show details of messages between users
    path('show_message/<message_id>', show_message, name= 'show-message'),
    #new message
    path('new_message', new_message, name='new-message'),
    #succesful submission of new message page
    path('message_submitted', message_submitted, name='message-submitted'),

    #messaging host from event page
    path('show_event/<event_id>/message_host', message_host, name= 'message-host'),

    

    
    #Password reset
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

]
