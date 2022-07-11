from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from login.forms import civilianProfileForm
from fir.models import jurisdictionModel, reportModel
from login.models import civilianModel
from users.models import userHistoryModel
from project_fir.methods import create_response, validate_civilian, validate_officer

# Create your views here.
def change_pwd_method(request):
    if validate_civilian(request):
        if request.method  ==  'POST':
            try:
                id = request.session['user_id']
                object = get_object_or_404(civilianModel, pk = id)
                if (check_password(request.POST['password'], object.password) and request.POST['newpassword']  ==  request.POST['repassword']):
                    object.password = make_password(request.POST['newpassword'])
                    object.save()
                    params = create_response('Password Changed Successfully', 2, 'civilian', 'primary', 'check_circle')
                    return render(request, 'respond.html', params)
                params = create_response('Password mismatched.', 0, 'signup_o', 'secondary', 'warning')
                return render(request, 'respond.html', params)
            except:
                params = create_response('Something went wrong:(', 0, 'login_c', 'danger', 'warning')
                return render(request, 'respond.html', params)
        else:
            return render(request, 'change_pwd.html')
    params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
    return render(request, 'respond.html', params)

def civilian_method(request):
    if validate_civilian(request):
        civilian_object = get_object_or_404(civilianModel, pk = request.session['user_id'])
        draft_object = reportModel.objects.filter(civilian = civilian_object.pk, status = 0)
        report_object = reportModel.objects.filter(civilian = civilian_object.pk).exclude(status = 0)
        history_object = userHistoryModel.objects.filter(civilian = civilian_object.pk).order_by('-id')
        to_date = datetime.today()
        params = {'draft_object': draft_object, 'report_object': report_object, 'history_object': history_object, 'to_date': to_date}
        if civilian_object.aadhar:
            params.update({'civilian_object': civilian_object})
        else:
            usermail = civilian_object.email.rsplit('@', 1)
            params.update({'civilian_object': civilian_object, 'usermail': usermail[0]})
        return render(request, 'civilian.html', params)
    params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
    return render(request, 'respond.html', params)

def edit_c_method(request):
    if validate_civilian(request):
        if request.method  ==  'POST':
            civilian_object = get_object_or_404(civilianModel, pk = request.session['user_id'])
            civilian_form = civilianProfileForm(request.POST or None, instance = civilian_object)
            if civilian_form.is_valid():
                try:
                    civilian_form.save()
                    params = create_response('Profile Updated Successfully', 2, 'civilian', 'primary', 'check_circle')
                    return render(request, 'respond.html', params)
                except:
                    params = create_response('Something went wrong:(', 0, 'login_c', 'danger', 'warning')
                    return render(request, 'respond.html', params)
            else:
                params = create_response('Something went wrong:(', 0, 'login_c', 'danger', 'warning')
                return render(request, 'respond.html', params)
        else:
            id = request.session['user_id']
            object = get_object_or_404(civilianModel, pk = id)
            division = jurisdictionModel.objects.all().order_by('division')
            params = {'division': division, 'civilian': object}
            try:
                fir = request.GET['fir']
                params.update({'fir': fir})
            except:
                pass
            return render(request, 'civilian_edit.html', params)
    params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
    return render(request, 'respond.html', params)

def officer_method(request):
    if validate_officer(request):
        return render(request, 'officer.html')
    params = create_response('Access Denied', 3, 'login_o', 'danger', 'warning')
    return render(request, 'respond.html', params)

def test_c_method(request):
    if validate_civilian(request):
        id = request.session['user_id']
        object = get_object_or_404(civilianModel, pk = id)
        params = {'object': object}
        return render(request, 'civilian.html', params)
    params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
    return render(request, 'respond.html', params)
