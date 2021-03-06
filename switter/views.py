import profile
from django.shortcuts import redirect, render

from switter.forms import SweetForm
from .models import Profile,Sweet
# Create your views here.


def dashboard(request):
    return render(request, 'base.html')


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "switter/profile_list.html", {
        "profiles": profiles
    })


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "switter/profile.html", {
        "profile": profile,
    })

def dashboard(request):
    if request.method == "POST":
        form = SweetForm(request.POST)
        if form.is_valid():
            sweet = form.save(commit=False)
            sweet.user = request.user
            sweet.save()
            return redirect("dashboard")
    form = SweetForm()
    return render(request,"switter/dashboard.html",{
        "form":form
    })
    

