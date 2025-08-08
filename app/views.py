from django.shortcuts import render
from .forms import AppForm


def app_view(request):
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            print(f"Name: {name}, Email: {email}, Message: {message}")
            return render(request, "Form.html", {"name": name, "form": form})
    else:
        form = AppForm()

    return render(request, "Form.html", {"form": form})
