from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComposeMessageForm
from .models import Message

# Create your views here.
@login_required(login_url='/accounts/login')
def inbox(request):
    return render(request, 'messenger/inbox.html')
    
@login_required(login_url='/accounts/login')
def sent(request):
    return render(request, 'messenger/sent_items.html')
    
@login_required(login_url='/accounts/login')
def view_message(request, id):
    message = get_object_or_404(Message, pk=id)
    message.read=True
    message.save()
    return render(request, "messenger/view_message.html", { 'message': message})
    
@login_required(login_url='/accounts/login')
def compose_message(request):
    if request.method=="POST":
        form = ComposeMessageForm(request.POST)
        message = form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect('inbox')
    else:
        form = ComposeMessageForm()
    
    return render(request, "messenger/compose_message.html", { 'form': form })