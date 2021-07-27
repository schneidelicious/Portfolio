from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    return render(request, "home.html")


def creations(request):
    return render(request, "creations.html")


def resume(request):
    return render(request, "resume.html")


def about_me(request):
    return render(request, "aboutme.html")


def sendEmail(request):

    if request.method == "POST":

        email = request.POST.get("email")
        name = request.POST.get("name")
        message = request.POST.get("message")

        data = {"email": email, "name": name, "message": message}
        message = """
       {}

        EMAIL: {}
        """.format(
            data["message"], data["email"]
        )
        send_mail(data["name"], message, "", ["imschneidelicious@gmail.com"])

    return render(request, "emailsent.html")
