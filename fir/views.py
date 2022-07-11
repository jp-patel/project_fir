from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .forms import reportForm
from .models import jurisdictionModel, reportModel
from login.models import civilianModel
from users.models import userHistoryModel
from project_fir.methods import create_response, validate_civilian

def create_draft_method(request):
    if validate_civilian(request):
        draft_form = reportForm(request.POST or None)
        history_obj = userHistoryModel(title = 'You have created a draft "' + request.POST['subject'] +'"', civilian = request.POST['civilian'], datetime = request.POST['date'])
        if draft_form.is_valid():
            draft_form.save()
            history_obj.save()
            return redirect('civilian')
        else:
            params = create_response('Something went wrong:(', 0, 'report', 'danger', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
        return render(request, 'respond.html', params)

def create_report_method(request):
    pass

def delete_draft_method(request):
    pass

def delete_report_method(request):
    pass

def read_draft_method(request):
    pass

def read_report_method(request):
    pass

def update_draft_method(request, id = 0):
    if validate_civilian(request):
        report_object = get_object_or_404(reportModel, pk = id)
        civilian_object = get_object_or_404(civilianModel, pk = request.session['user_id'])
        if str(report_object.civilian) == str(civilian_object.email):
            if report_object.day is not None:report_object.day = report_object.day.strftime("%Y-%m-%d")
            if report_object.time is not None:report_object.time = report_object.time.strftime("%H:%M")
            division = jurisdictionModel.objects.all().order_by('division')
            draft_form = reportForm(request.POST or None, instance = report_object)
            if draft_form.is_valid():
                draft_form.save()
                time = datetime.now()
                history_obj = userHistoryModel(title = 'You have updated a draft "' + request.POST['subject'] +'"', civilian = civilian_object, datetime = time, issue = 1)
                history_obj.save()
                return redirect('civilian')
            else:
                params = {'report_object': report_object, 'civilian_object': civilian_object, 'division': division, 'update': True}
                return render(request, 'report.html', params)
        else:
            params = create_response('Access Denied', 0, 'civilian', 'danger', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
        return render(request, 'respond.html', params)

def update_draft_label_method(request, id = 0):
    if validate_civilian(request):
        report_object = get_object_or_404(reportModel, pk = id)
        civilian_object = get_object_or_404(civilianModel, pk = request.session['user_id'])
        if str(report_object.civilian) == str(civilian_object.email):
            report_object.label = request.POST['label']
            print(request.POST['label'])
            report_object.save()
            return redirect('civilian')
        else:
            params = create_response('Access Denied', 0, 'civilian', 'danger', 'warning')
            return render(request, 'respond.html', params)
    else:
        params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
        return render(request, 'respond.html', params)

def home_method(request):
    return render(request, 'home.html')

def report_method(request, id = 0):
    if validate_civilian(request):
        params = {}
        if request.method  ==  'POST':
            pass
        else:
            try:
                report_object = reportModel.objects.get(pk = id)
                report_object.day = report_object.day.strftime("%Y-%m-%d")
                report_object.time = report_object.time.strftime("%H:%M")
                params.update({'report_object': report_object})
            except:
                id = request.session['user_id']
                civilian_object = get_object_or_404(civilianModel, pk = id)
            value = datetime.today()
            division = jurisdictionModel.objects.all().order_by('division')
            params.update({'civilian_object': civilian_object, 'division': division, 'date': value.strftime("%Y-%m-%d"), 'id': id, 'create': True})
            return render(request, 'report.html', params)
    params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
    return render(request, 'respond.html', params)

def draft_method(request):
    if validate_civilian(request):
        if request.method  ==  'POST':
            draft_obj = reportModel.objects.get(pk = request.POST['id'])
            draft_form_obj = reportForm(request.POST or None, instance = draft_obj)
            reportModel.objects.filter(pk = request.POST['id']).update(draft_form_obj)
            # for i in draft_obj:
            #     print(i)
            # for key, value in request.POST.items():
            #     print('Key:%s' % (key) )
            #     print('Value:%s' % (value) )
            # if draft_obj.is_valid():
            try:
                # draft_obj.save()
                params = create_response('Success', 2, 'civilian', 'primary', 'check_circle')
                return render(request, 'respond.html', params)
            # else:
            except:
                params = create_response('Something went wrong:(', 0, 'report', 'danger', 'warning')
                return render(request, 'respond.html', params)
    params = create_response('Access Denied', 3, 'login_c', 'danger', 'warning')
    return render(request, 'respond.html', params)
