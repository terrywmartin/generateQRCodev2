
from django.urls import path, include

from . import views

app_name = 'qr_code'

urlpatterns = [
    path("qrcode/generate", views.GenerateQRCode.as_view(), name='generate_qrcode'),
    path("qrcode/download", views.DownloadQRCode.as_view(), name='download_qrcode'),
    path("qrcode/generate_vcard", views.GenerateQRCodeVcard.as_view(), name='generate_qrcode_vcard'),
    path("qrcode/generate_wifi", views.GenerateQRCodeWIFI.as_view(), name='generate_qrcode_wifi'),
]
