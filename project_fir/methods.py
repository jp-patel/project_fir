def create_response(title, body_type, href, alert, icon):
    params = {
        'title': title, 
        'body_type': body_type, 
        'href': href, 
        'alert': alert, 
        'icon': icon
    }
    return params

def validate_civilian(request):
    if 'user_id' in request.session and 'user_role' in request.session:
        if request.session['user_role']  ==  "civilian":
            return True
    return False

def validate_officer(request):
    if 'user_id' in request.session and 'user_role' in request.session:
        if request.session['user_role']  ==  "officer":
            return True
    return False