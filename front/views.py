from django.shortcuts import redirect, render
from .models import Tipoff
# Create your views here.

IMAGE_FILE_TYPES = ['pdf']

def FrontPage(request):
    return render(request, "manthan/index.html")

def addTipOff(request):
    if request.method == "POST":
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        t = Tipoff(
            Nature_of_Incidence= request.POST.get('incidence'),
            Death_or_Loss_in_Family=request.POST.get('death-or-loss'),
            Family_Member_is_not_healthy=request.POST.get('family-history'),
            Disruption_of_Intimate_Relationships=request.POST.get('disruption-relation'),
            Faced_any_Violence=request.POST.get('faced-violence'),
            Disruption_in_Studies=request.POST.get('study-disruption'),
            Provided_information_to_Police_or_Justice_System=request.POST.get('information-to-police'),
            Listed_Cases=request.POST.get('case-id'),
            Existing_or_Other=request.POST.get('type'),
            State=request.POST.get('state'),
            District=request.POST.get('district'),
            Gender=request.POST.get('gender'),
            Age=request.POST.get('age'),
            Mother_Tongue=request.POST.get('mother-tongue'),
            Educational_Qualification=request.POST.get('qualification'),
            Got_Information_About_Case=request.POST.get('about-case'),
            Relation_to_Suspect_or_Victim=request.POST.get('relation'),
            Pincode=request.POST.get('pincode'),
            Message=request.POST.get('message'),
            File_Uploaded=request.POST.get('myfile'),
            ip = ip)
        t.save()
        return redirect("/")

