from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from fir.models import reportModel
from login.models import civilianModel, officerModel

def about_method(request):
    return render(request, 'about.html')

def contact_method(request):
    return render(request, 'contact.html')

def docs_method(request):
    return render(request, 'docs.html')

def index_method(request):
    if 'user_id' in request.session:
        id = request.session['user_id']
        if request.session['user_role']  ==  "civilian":
            return redirect('civilian')
        else:
            object = get_object_or_404(officerModel, pk = id)
            usermail = object.email.rsplit('@', 1)
            params = {'object': object, 'usermail': usermail[0]}
            return render(request, 'officer.html', params)
    return render(request, 'index.html')

def privacy_method(request):
    return render(request, 'privacy.html')

def resources_method(request):
    return render(request, 'resources.html')

def test_method(request):
    return render(request, 'test.html')

def tac_method(request):
    return render(request, 'tac.html')
