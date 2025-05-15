from django import template
from django.utils.timezone import localtime

register = template.Library()

#for indonesian format
hari_dict = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu',
    'Sunday': 'Minggu',
}

bulan_dict = {
    1: 'Januari',
    2: 'Februari',
    3: 'Maret',
    4: 'April',
    5: 'Mei',
    6: 'Juni',
    7: 'Juli',
    8: 'Agustus',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Desember',
}

@register.filter
def tanggal_lengkap(value):
    try:
        hari = hari_dict[value.strftime('%A')]
        tanggal = value.day
        bulan = bulan_dict[value.month]
        tahun = value.year
        return f"{hari}, {tanggal} {bulan} {tahun}"
    except:
        return ''
    
@register.filter
def hari_saja(value):
    try:
        return hari_dict[value.strftime('%A')]  
    except:
        return ''

@register.filter
def bulan_saja(value):
    try:
        return bulan_dict[value.month]
    except:
        return ''

@register.filter
def tahun_saja(value):
    try:
        return value.year
    except:
        return ''

@register.filter
def jam_menit(value):
    try:
        return localtime(value).strftime('%H:%M')
    except:
        return ''
