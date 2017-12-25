from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Team, Player
from .forms import TeamForm

def create(request, **kwargs):
    form = TeamForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            team = form.save()
            return redirect(team)
    elif request.method == 'GET':
        """"""

    else:
        return HttpResponseBadRequest("This operation is only defined for GET and POST")

    return render(request, 'golf/teams/create.html',
                {
                    'form': form,
                }
           )


def detail(request, pk, **kwargs):
    team = get_object_or_404(Team, pk=pk)
    players = team.player_set.all().order_by('handicap')

    return render(request, 'golf/teams/detail.html',
            {
                'team': team,
                'players': players,

            }
        )

def list(request, **kwargs):
    teams = Team.objects.all()
    return render(request, 'golf/teams/list.html',
                {
                    'teams': teams,
                }
            )

def delete(request, pk, **kwargs):
    team = get_object_or_404(Team, pk=pk)
    team.delete()
    return redirect('golf:teams:list')
