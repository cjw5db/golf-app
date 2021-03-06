from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Team, Player
from .forms import PlayerForm
from django.contrib.auth.models import User

def create(request, **kwargs):

    print(User.objects.all())

    form = PlayerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            player = form.save()
            return redirect(player)
    elif request.method == 'GET':
        """"""

    else:
        return HttpResponseBadRequest("This operation is only defined for GET and POST")

    return render(request, 'golf/player/create.html',
                {
                    'form': form,
                }
           )


def detail(request, pk, **kwargs):
    player = get_object_or_404(Player, pk=pk)
    team = player.team

    return render(request, 'golf/player/detail.html',
            {
                'player': player,
                'team': team,

            }
        )

def list(request, **kwargs):
    players = Player.objects.order_by('handicap')
    return render(request, 'golf/player/list.html',
                {
                    'players': players,
                }
            )

def delete(request, pk, **kwargs):
    player = get_object_or_404(Player, pk=pk)
    player.delete()

    return redirect('golf:player:list')
