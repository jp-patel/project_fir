from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render, get_object_or_404
from .forms import civilianForm, officerForm
from .models import civilianModel, officerModel
from fir.models import jurisdictionModel, reportModel
from project_fir.methods import create_response

# Create your views here.
def forgot_method(request):
    return render(request, 'forgot.html')

def login_method_c(request):
    if request.method !=  'POST':
        return render(request, 'login_c.html')

    login_obj = civilianForm(request.POST)
    if login_obj.is_valid():
        try:
            object = get_object_or_404(civilianModel, email = request.POST['email'])
            if check_password(request.POST['password'], object.password):
                request.session['user_role'] = "civilian"
                request.session['user_id'] = object.pk
                return redirect('civilian')
            else:
                params = create_response('Password mismatched.', 1, 'login_c', 'secondary', 'warning')
                return render(request, 'respond.html', params)
        except:
            params = create_response('User does not exists.', 1, 'login_c', 'secondary', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Something went wrong:(', 0, 'login_c', 'danger', 'warning')
        return render(request, 'respond.html', params)

def login_method_o(request):
    if request.method !=  'POST':
        return render(request, 'login_o.html')

    login_obj = officerForm(request.POST)
    if login_obj.is_valid():
        try:
            object = get_object_or_404(officerModel, email = request.POST['email'])
            if check_password(request.POST['password'], object.password):
                request.session['user_role'] = "officer"
                request.session['user_id'] = object.pk
                params = {'object': object}
                return render(request, 'officer.html', params)
            else:
                params = create_response('Password mismatched.', 1, 'login_o', 'secondary', 'warning')
                return render(request, 'respond.html', params)
        except:
            params = create_response('User does not exists.', 1, 'login_o', 'secondary', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Something went wrong:(', 0, 'login_o', 'danger', 'warning')
        return render(request, 'respond.html', params)

def logout_method(request):
    try:
        del request.session['user_role']
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'logout.html')

def otp_method(request):
    return render(request, 'otp.html')

#######
                                    #######
def respond_method(request):
    return render(request, 'respond.html')
                                    #######
#######

def signup_method_c(request):
    if request.method !=  'POST':
        return render(request, 'signup_c.html')
    
    signup_obj = civilianForm(request.POST)
    if signup_obj.is_valid():
        try:
            get_object_or_404(civilianModel, email = request.POST['email'])
            params = create_response('User already exists.', 0, 'signup_c', 'secondary', 'warning')
            return render(request, 'respond.html', params)
        except:
            if(request.POST['password']  ==  request.POST['repassword']):
                hashed_pwd = make_password(request.POST['password'])
                create_civilian = civilianModel(email = request.POST['email'], password = hashed_pwd)
                create_civilian.save()
                params = create_response('You\'ve signed up successfully', 1, 'login_c', 'primary', 'check_circle')
                return render(request, 'respond.html', params)
            params = create_response('Password mismatched.', 0, 'signup_c', 'secondary', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Something went wrong:(', 0, 'signup_c', 'danger', 'warning')
        return render(request, 'respond.html', params)

def signup_method_o(request):
    if request.method !=  'POST':
        division = jurisdictionModel.objects.all().order_by('division')
        params = {'division': division}
        return render(request, 'signup_o.html', params)
    
    signup_obj = officerForm(request.POST)
    if signup_obj.is_valid():
        try:
            get_object_or_404(officerModel, email = request.POST['email'])
            params = create_response('User already exists.', 0, 'signup_o', 'secondary', 'warning')
            return render(request, 'respond.html', params)
        except:
            if(request.POST['password']  ==  request.POST['repassword']):
                hashed_pwd = make_password(request.POST['password'])
                officer_division = jurisdictionModel.objects.get(division = request.POST['division'])
                create_officer = officerModel(email = request.POST['email'], password = hashed_pwd, division = officer_division)
                create_officer.save()
                params = create_response('You\'ve signed up successfully', 1, 'login_o', 'primary', 'check_circle')
                return render(request, 'respond.html', params)
            params = create_response('Password mismatched.', 0, 'signup_o', 'secondary', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Something went wrong:(', 0, 'signup_o', 'danger', 'warning')
        return render(request, 'respond.html', params)        
