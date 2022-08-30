from email import message
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseNotFound


from django.conf import settings

# Create your views here.
def Home(request):
    return render(request,'core/home.html')
def CV(request):
    fs = FileSystemStorage()
    filename = 'G:\mywork\media\Shivam.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
            response['Content-Disposition'] = 'inline; filename="G:\mywork\media\Shivam.pdf"' #user will be prompted display the PDF in the browser
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        msg = request.POST['msg']
        send_mail(
            'Subject',
            'msg',
            'settings.EMAIL_HOST_USER ',
            ['email'],
            fail_silently=False,                     
        )
    return render(request,'core/contact.html')