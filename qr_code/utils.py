from django.core.paginator import Paginator, EmptyPage

import qrcode
import qrcode.image.svg

from io import BytesIO


def generate_qr_code(type, **kwargs):
    factory = qrcode.image.svg.SvgImage
    qr = qrcode.QRCode(
             version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
            image_factory=factory
        )
    
    if type == 'url':
        url = kwargs['url']
        data = url
        
    elif type == 'vcard':
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        email_address = kwargs['email_address']
        phone = kwargs['phone']
        data = f'BEGIN:VCARDVERSION:3.0\r\nN:{last_name};{first_name}\r\nFN:{first_name} {last_name}\r\nEMAIL:{email_address}\r\nTEL:{phone}\r\nEND:VCARD'

    elif type == 'wifi':
        ssid = kwargs['ssid']
        password = kwargs['password']
        security_method = kwargs['security_method']
        data = f'WIFI:S:{ssid};T:{security_method};P:{password};;'

    qr.add_data(data)
    img = qr.make_image()
    stream = BytesIO()
    img.save(stream) 
    return stream

def paginate_qrcodes(request, qrcodes, results):
    page = request.GET.get('page', 1)
    paginator = Paginator(qrcodes, results)
    try:
            qrcodes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        qrcodes = paginator.page(page)

    left_index = (int(page) - 2)
    if left_index < paginator.num_pages:
        left_index = 1

    right_index = (int(page) + 3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
        
    custom_range = range(left_index, right_index)

    return custom_range, qrcodes