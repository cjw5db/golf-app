from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Team, Player, Trip
from .forms import CreateForm, TeamAddForm

def create(request, **kwargs):

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            trip = form.save()
            return redirect('golf:trip:generate', pk=trip.pk)
    else:
        form = CreateForm()

    return render(request, 'golf/trip/create.html', {'form': form} )


def generate(request, pk, **kwargs):
    trip = get_object_or_404(Trip, pk=pk)
    size = trip.team_size
    pk_list = []
    for team in Team.objects.all():
        if team.player_set.count() == size:
            pk_list.append(team.pk)
    queryset = Team.objects.filter(pk__in=pk_list)

    form = TeamAddForm(request.POST or None, queryset=queryset)

    if request.method == 'POST':
        if form.is_valid():
            l = request.POST.getlist('teams')
            for pk in l:
                u = Team.objects.get(pk=pk)
                trip.teams.add(u)
            return redirect(trip)

    return render(request, 'golf/trip/generate.html',
                {
                    'form': form,
                }
            )

def detail(request, pk, **kwargs):
    trip = get_object_or_404(Trip, pk=pk)
    round_list = range(trip.rounds)
    return render(request, 'golf/trip/detail.html',
            {'trip':trip, 'round_list':round_list}
        )

def list(request, **kwargs):
    trips = Trip.objects.all()
    return render (request, 'golf/trip/list.html', {'trips':trips})

def delete(request, pk, **kwargs):
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    return redirect('golf:trip:list')
