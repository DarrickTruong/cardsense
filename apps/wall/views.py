from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import RedirectView
from django.contrib import messages
from .models import Lead, User, Loyalty, Message, Review, Event, Comment
from time import strftime

def index(request):
    return redirect('/login')

# user/dashboard routes
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'user' : user,
        'leads' : user.my_lead.all(),
        'my_messages' : user.written_message.all(),
        'reviews' : user.my_review.all(),
        'loyalty' : user.loyal_client.all(),
        'events' :user.my_event.all(),
    }
    return render(request, 'wall/dashboard.html', context)

def thewall(request, user_id):
    user = User.objects.get(id=user_id)
    # print("user messages", user.written_message.all())
    # print("user pinned messages", user.written_message.filter(pinned=True))
    context = {
        'user' : user,
        'id' : user.id,
        'reviews' : user.my_review.all(),
        'events' : user.my_event.all(),
        'session_id' : request.session,
        'profile_pic' : user.profile_pic.url,
        'user_messages' : user.written_message.filter(pinned=True)
    }
    return render(request, 'wall/thewall.html', context)

def edit_contact(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'date' : User.objects.get(id=request.session['user_id']).birthday.strftime("%Y-%m-%d"),
    }
    return render(request, 'wall/edit_contact.html', context)

def process_edit_contact(request):
    errors = User.objects.edit_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/edit_contact')
    
    user = User.objects.get(id=request.session['user_id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.phone = request.POST['phone']
    user.birthday = request.POST['birthday']
    user.website = request.POST['website']
    user.linkedin= request.POST['linkedin']
    user.facebook = request.POST['facebook']
    user.instagram = request.POST['instagram']
    user.save()
    return redirect('/dashboard')

def update_profile_pic(request):
    user = User.objects.get(id=request.session['user_id'])
    # print('profile pic', request.FILES['profile_pic'])
    user.profile_pic = request.FILES['profile_pic']
    user.save()
    return redirect('/dashboard')






# Message/Lead/Comment routes
def write_message(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, "wall/write_message.html", context)

def process_message(request, user_id):

    # print('in process message', user_id)
    errors = Lead.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/write_message')
    all_leads =Lead.objects.all()
    if len(all_leads.filter(email=request.POST['email'])) > 0:
        Message.objects.create(message=request.POST['message'], user_message=User.objects.get(id=user_id), author=Lead.objects.get(email=request.POST['email']))
        return('/wall/' + str(user_id))
    else:
        lead = Lead.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], phone= request.POST['phone'], owner=User.objects.get(id=user_id))
        Message.objects.create(message=request.POST['message'], user_messaged=User.objects.get(id=user_id), author=lead)
    return redirect('/wall/' + str(user_id))

def comment(request, message_id):
    Comment.objects.create(comment=request.POST['comment'], author=User.objects.get(id=request.session['user_id']), message=Message.objects.get(id=message_id))
    return redirect('/dashboard')

def pin_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.pinned = True
    message.save()
    return redirect('/dashboard')

def unpin_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.pinned = False
    message.save()
    # print('message pinned True', message.pinned)
    return redirect('/dashboard')
    

def convert_lead(request):
    lead = Lead.objects.get(id=request.POST['lead_id'])
    # print('this is lead first_name', lead.first_name)
    first_name = lead.first_name
    last_name = lead.last_name
    email = lead.email
    phone = lead.phone
    Loyalty.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, owner= User.objects.get(id=request.session['user_id']))
    lead.delete()
    return redirect('/dashboard')




# Review routes
def write_review(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, "wall/write_review.html", context)

def process_review(request, user_id):
    errors = Loyalty.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/write_review')

    all_loyalty =Loyalty.objects.all()
    if len(all_loyalty.filter(email=request.POST['email'])) > 0:
        Review.objects.create(review=request.POST['review'], author=Loyalty.objects.get(email=request.POST['email']), user_reviewed=User.objects.get(id=user_id))
        return redirect('/wall/' + str(user_id))
    else:
        loyalty = Loyalty.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], phone=request.POST['phone'], owner=User.objects.get(id=user_id))
        Review.objects.create(review=request.POST['review'], author=loyalty, user_reviewed=User.objects.get(id=user_id))
    return redirect('/wall/' + str(user_id))

def destroy_review(request):
    review = Review.objects.get(id=request.POST['review_id'])
    # print('review_id object', review)
    review.delete()
    return redirect('/dashboard')





# Event routes
def process_event(request):
    errors = Event.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/dashboard')
    else:
        Event.objects.create(what=request.POST['what'], where=request.POST['where'], when=request.POST['when'], why=request.POST['why'], owner=User.objects.get(id=request.POST['owner_id']), event_pic=request.FILES['event_pic'])
        return redirect('/dashboard')

def edit_event(request, event_id):
    context = {
        'event' : Event.objects.get(id=event_id),
        'when' : Event.objects.get(id=event_id).when.strftime("%Y-%m-%d"),
    }
    return render(request, 'wall/edit_event.html', context)

def process_edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.what = request.POST['what']
    event.when = request.POST['when']
    event.where = request.POST['where']
    event.why = request.POST['why']
    event.save()
    return redirect('/dashboard')

def update_event_pic(request, event_id):
    event = Event.objects.get(id=event_id)
    event.event_pic = request.FILES['event_pic']
    event.save()
    return redirect('/dashboard')

def destroy_event(request, event_id):
    event = Event.objects.get(id=event_id)
    # print('event_id object', event)
    event.delete()
    return redirect('/dashboard')