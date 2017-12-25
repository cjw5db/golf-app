from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Team, Player, Trip, Group
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

            players1=[]
            team = trip.teams.first()
            for player in team.player_set.all():
                players1.append(player)
            players2=[]
            team = trip.teams.last()
            for player in team.player_set.all():
                players2.append(player)
            groups = make_groups(trip,players1,players2)

            return redirect(trip)

    return render(request, 'golf/trip/generate.html',
                {
                    'form': form,
                }
            )

def make_groups(trip, p1, p2):
    g = []

    #Round1
    group = Group.objects.create()
    group.players.add(p1[0])
    group.players.add(p1[1])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[0])
    group.players.add(p2[1])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[2])
    group.players.add(p1[3])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[2])
    group.players.add(p2[3])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[4])
    group.players.add(p1[5])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[4])
    group.players.add(p2[5])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[6])
    group.players.add(p1[7])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[6])
    group.players.add(p2[7])
    group.trip = trip
    group.round = 1
    group.save()
    g.append(group)

    #Round2
    group = Group.objects.create()
    group.players.add(p1[0])
    group.players.add(p1[2])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[4])
    group.players.add(p2[6])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[1])
    group.players.add(p1[3])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[5])
    group.players.add(p2[7])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[4])
    group.players.add(p1[6])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[0])
    group.players.add(p2[2])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[5])
    group.players.add(p1[7])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[1])
    group.players.add(p2[3])
    group.trip = trip
    group.round = 2
    group.save()
    g.append(group)

    #Round3
    group = Group.objects.create()
    group.players.add(p1[0])
    group.players.add(p1[4])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[3])
    group.players.add(p2[7])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[1])
    group.players.add(p1[5])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[2])
    group.players.add(p2[6])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[2])
    group.players.add(p1[6])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[1])
    group.players.add(p2[5])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[3])
    group.players.add(p1[7])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[0])
    group.players.add(p2[4])
    group.trip = trip
    group.round = 3
    group.save()
    g.append(group)

    #Round4
    group = Group.objects.create()
    group.players.add(p1[0])
    group.players.add(p1[7])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[2])
    group.players.add(p2[5])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[1])
    group.players.add(p1[6])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[3])
    group.players.add(p2[4])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[2])
    group.players.add(p1[5])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[0])
    group.players.add(p2[7])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p1[3])
    group.players.add(p1[4])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    group = Group.objects.create()
    group.players.add(p2[1])
    group.players.add(p2[6])
    group.trip = trip
    group.round = 4
    group.save()
    g.append(group)

    return g

def detail(request, pk, **kwargs):
    trip = get_object_or_404(Trip, pk=pk)
    round_list = range(trip.rounds)
    group_list = []
    groups=[]

    i = 0
    while i < 32:
        t = []
        t.append(trip.group_set.all()[i])
        t.append(trip.group_set.all()[i+1])
        groups.append(t)
        i += 2

    i = 1
    while i <= trip.team_size/2:
        group_list.append(i)
        i += 1
    return render(request, 'golf/trip/detail.html',
            {
            'trip':trip,
            'round_list':round_list,
            'group_list':group_list,
            'groups':groups,
            }
        )

def list(request, **kwargs):
    trips = Trip.objects.all()
    return render (request, 'golf/trip/list.html', {'trips':trips})

def delete(request, pk, **kwargs):
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    return redirect('golf:trip:list')
