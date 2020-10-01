from django.shortcuts import render
from .models import SimpleForm
from .forms import SimpleFormForm
from django.shortcuts import redirect

def simple_form_list(request):
    registrations = SimpleForm.objects.all().order_by('-created_date')    
    return render(request, 'registration/simple_form_list.html', {'registrations':registrations})



def registration_new(request):
    if request.method == "POST":
        form = SimpleFormForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/success')
    else:
        form = SimpleFormForm()
    return render(request, 'registration/registration_edit.html', {'form': form})