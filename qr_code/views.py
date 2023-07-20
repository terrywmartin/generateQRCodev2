from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

from django.http import HttpResponse

from .utils import generate_qr_code


# Create your views here.

class GenerateQRCodeWIFI(View):
    def post(self, request):
       
        ssid = request.POST.get('ssid', '')
        password = request.POST.get('password', '')
        security_method = request.POST.get('security_method', '')
    
        if ssid == '':
            return render(request, 'partials/failure.html', { 'msg': 'Please enter an SSID.'})
        
        stream = generate_qr_code('wifi', ssid=ssid, password=password, security_method=security_method)
        
        context = { 
            'qrcode': stream.getvalue().decode(),
            'ssid': ssid,
            'password': password,
            'security_method': security_method,
            'type': 'wifi'
         }
        return render(request, 'qr_code/partials/view_qrcode.html', context)
    
class GenerateQRCodeVcard(View):
    def post(self, request):
        
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email_address = request.POST.get('email_address', '')
        phone = request.POST.get('phone', '')

        if first_name == '' or last_name == '':
            return render(request, 'partials/failure.html', { 'msg': 'Please enter first and last name.'})
        
        if phone == '' and email_address == '':
            return render(request, 'partials/failure.html', { 'msg': 'Please enter a phone number or email address.'})
        
        stream = generate_qr_code('vcard', first_name=first_name, last_name=last_name, email_address=email_address, phone=phone)
        
        context = { 
            'qrcode': stream.getvalue().decode(),
            'first_name': first_name,
            'last_name': last_name,
            'email_address': email_address,
            'phone': phone,
            'type': 'vcard'       
         }
        return render(request, 'qr_code/partials/view_qrcode.html', context)

class GenerateQRCode(View):
    def post(self, request):
        url = request.POST.get('url')
       
        if url == '':
            return render(request, 'partials/failure.html', { 'msg': 'Please enter a URL.'})

        
        stream = generate_qr_code('url', url=url)
        context = { 'qrcode': stream.getvalue().decode(),
            'url': url,
            'type': 'url'
         }
        return render(request, 'qr_code/partials/view_qrcode.html', context)

class DownloadQRCode(View):
    def get(self, request):
        type = request.GET.get('type', None)

        if type == None:
            return render(request, 'partials/failure.html', { 'msg': 'Error downloading QR Code.'})
        
        if type == 'url':
            url = request.GET.get('url')
            
            if url == '':
                return render(request, 'partials/failure.html', 'Please enter a URL.')

            stream = generate_qr_code('url', url=url)

            
        elif type == 'wifi':
            ssid = request.GET.get('ssid', '')
            password = request.GET.get('password', '')
            security_method = request.GET.get('security_method', '')
            stream = generate_qr_code('wifi', ssid=ssid, password=password, security_method=security_method)
        elif type == 'vcard':
            first_name = request.GET.get('first_name', '')
            last_name = request.GET.get('last_name', '')
            email_address = request.GET.get('email_address', '')
            phone = request.GET.get('phone', '')
            stream = generate_qr_code('vcard', first_name=first_name, last_name=last_name, email_address=email_address, phone=phone)
        #response = FileResponse(stream.getvalue().decode(), as_attachment=True,filename='qrcode.svg')

        headers = {
                'Content-Type': 'image/svg+xml',
                'Content-Disposition': 'inline; filename="qrcode.svg"'
            }
            
        return HttpResponse(stream.getvalue().decode(), headers=headers)
        #return response