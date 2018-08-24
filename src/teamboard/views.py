from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from teamboard.models import Profile, Team


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    first_name = forms.CharField(
        label=_("First name"),
        widget=forms.TextInput,
        strip=True
    )
    last_name = forms.CharField(
        label=_("Last name"),
        widget=forms.TextInput,
        strip=True
    )
    email = forms.EmailField(
        label=_("E-Mail"),
        widget=forms.EmailInput
    )
    invite = forms.CharField(
        label=_("Invite code"),
        widget=forms.TextInput,
        strip=True,
        help_text='Optional. You can use invite code to join team automatically.',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('User with email already exists')
        return email

    def clean_invite(self):
        invite = self.cleaned_data['invite']
        if invite and not Team.objects.filter(invite=invite).exists():
            raise ValidationError('Invite code not valid.')
        return invite


class Register(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        username = form['username'].data
        invite = form['invite'].data

        form.save()
        user = User.objects.filter(username=username)[0]

        if invite:
            team = Team.objects.filter(invite=invite)[0]
            profile = Profile(user=user, team=team)
        else:
            profile = Profile(user=user)
        profile.save()
        return super().form_valid(form)


def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    profile = request.user.profile

    has_team = bool(profile.team)
    team_name = profile.team.name if has_team else ''

    message = ''
    status = 'fail'
    box = 'invite'

    if request.method == "POST":
        box = 'invite'

        invite = request.POST.get('invite')
        team_name = request.POST.get('team')

        if team_name:
            box = 'team'
            if Team.objects.filter(name=team_name).exists():
                message = 'Team with this name already exists. Please choose another name.'
            elif Team.objects.filter(invite=invite).exists():
                message = 'Invite code already exists. Please choose another invite code.'
            else:
                Team(name=team_name, invite=invite).save()
                profile.team = Team.objects.get(name=team_name)
                profile.save()

                message = f'You created team {team_name}.'
                status = 'ok'
        elif invite and not Team.objects.filter(invite=invite).exists():
            message = 'Invite code not valid.'

        else:
            team = Team.objects.get(invite=invite)
            profile.team = team
            profile.save()

            message = f'You joined team {team.name}.'
            status = 'ok'

    return render(request, 'profile.html',
                  context={'has_team': has_team, 'team_name': team_name, 'message': message, 'status': status,
                           'box': box})


@login_required
def scoreboard(request):
    return render(request, 'scoreboard.html', context={'teams': Team.objects.order_by('-score')})
