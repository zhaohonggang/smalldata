from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
import api.utils as utils
from django.conf import settings
import os


''' 
def history(request):
    return render(request, 'history1.html')

def his(request):
    return render(request, 'his.html')
'''
def bag(request, foldername, filename):
    if foldername == 'house':
        foldername = 'housing'
    if utils.isBlank(filename):
        filename = 'map'

    filefullname = '.'.join([filename, 'html'])
    # PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

    filepath = os.path.abspath(os.path.join(settings.PROJECT_ROOT, 'templates', foldername, filefullname))
    # filepath = '{0}\\templates\\{1}.html'.format(settings.PROJECT_ROOT,tname)
    if not utils.isFileExists(filepath):
        tname = 'notfound'
    else:
        tname = '/'.join([foldername,filename])
    return render(request, 'bag.html', {'tname': tname})

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, 'payment.html',
                            {'form': form, 'payment': payment})