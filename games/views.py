from django.shortcuts import render,redirect
from .models import Game,Contact
from .forms import ContactMe
# Create your views here.
def all_game(request):
    all_games = Game.objects.all()
    if request.method == "POST":
        form = ContactMe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_games')
    else:
        form = ContactMe()
    
    context = {
        'games':all_games,
        'form':form,
    }
    return render(request,'all_game.html',context)

def game(request,id):
    game = Game.objects.get(id=id)
    if request.method == "POST":
        form = ContactMe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_games')
    else:
        form = ContactMe()
    
    context = {
        'game':game,
        'form':form,
    }
    return render(request,'game.html',context)