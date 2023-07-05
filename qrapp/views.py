from typing import Any
from django.shortcuts import render
from django.views import View
from .models import QRCodeData
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

class homeView(TemplateView):
    template_name='home.html'

@login_required(login_url='login_url')
def searchView(request):
    item_list=QRCodeData.objects.all()
    username=request.user.username
    context={
        'item_list':item_list,
        'username':username,
    }
    return render(request, 'search.html', context)

@login_required(login_url='login_url')
def searchcheckoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        assgined_track=request.POST.get
        user_authority=request.user
        print(scan_track)
        #remove input 4 digit space
        scan_track=scan_track.replace(" ","")
        print(scan_track)
        #check code_data exist
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            admin_check_last=entry.admin_check
            user_check_last=entry.receiver_check
            # superuser
            if user_authority.is_superuser:
                if admin_check_last==True:
                    context={
                        "error":"Admin already checkout!"
                    }
                    return render(request,'msg_fail.html', context=context)
                else:
                    entry.admin_check=True
                    entry.admin_at=timezone.now()
                    entry.save()
                    context={
                        "message":"Admin checkout successfully!",
                    }
                    return render(request,'msg_success.html', context=context)
            # staffuser
            else:
                if user_check_last==True:
                    context={
                        "error":"Receiver already checkout!"
                    }
                    return render(request,'msg_fail.html', context=context)
                else:
                    entry.receiver_check=True
                    entry.receiver_at=timezone.now()
                    entry.save()
                    context={
                        "message":"Receiver checkout successfully!"
                    }
                    return render(request,'msg_success.html', context=context)
        except QRCodeData.DoesNotExist:
            context={
                "error":"Tracking number not exists!"
            }
            return render(request,'msg_fail.html', context=context)
    return render(request,'checkout.html')


@login_required(login_url='login_url')
def checkoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        user_authority=request.user
        user_name=request.user.username

        #remove input 4 digit space
        scan_track=scan_track.replace(" ","")

        #check code_data exist
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            admin_check_last=entry.admin_check
            user_check_last=entry.receiver_check
            # superuser
            if user_authority.is_superuser:
                if admin_check_last==True:
                    context={
                        "error":"Admin already checkout!"
                    }
                    return render(request,'msg_fail.html', context=context)
                else:
                    entry.admin_check=True
                    entry.admin_at=timezone.now()
                    entry.save()
                    context={
                        "message":"Admin checkout successfully!",
                    }
                    return render(request,'msg_success.html', context=context)
            # staffuser
            else:
                if user_check_last==True:
                    context={
                        "error":"Receiver already checkout!"
                    }
                    return render(request,'msg_fail.html', context=context)
                else:
                    #check receiver and username matching
                    if user_name==entry.receiver:
                        entry.receiver_check=True
                        entry.receiver_at=timezone.now()
                        entry.save()
                        context={
                            "message":"Receiver checkout successfully!"
                        }
                        return render(request,'msg_success.html', context=context)
                    else:
                        context={
                            "error":"This is not your package!"
                        }
                        return render(request,'msg_fail.html', context=context)
        except QRCodeData.DoesNotExist:
            context={
                "error":"Tracking number not exists!"
            }
            return render(request,'msg_fail.html', context=context)
    return render(request,'checkout.html')

@login_required(login_url='login_url')
def addView(request):
    return render(request,'add.html')

@login_required(login_url='login_url')
def addscanView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        scan_receiver=request.POST.get('receiver')

        #if each colum empty
        if not scan_track:
            context={
                "error":"Tracking number is empty!"
            }
            return render(request,'msg_fail.html', context=context)
        elif not scan_receiver:
            context={
                "error":"Receiever is empty!"
            }
            return render(request,'msg_fail.html', context=context)
        #compare existed query
        else:
            entry_exists=QRCodeData.objects.filter(code_data=scan_track).exists()
            if entry_exists:
                context={
                    "error":"Tracking number already exists!"
                }
                return render(request,'msg_fail.html', context=context)
            else:
                qr_code_scan=QRCodeData(receiver=scan_receiver, code_data=scan_track)
                qr_code_scan.save()
                context={
                    "message":"Data save successfully!"
                }
                return render(request,'msg_success.html', context=context)
    return render(request,'add_scan.html')

@login_required(login_url='login_url')
def addgenView(request):
    return render(request,'add_generate.html')

@login_required(login_url='login_url')
def msgSuccessView(request):
    context={"message":"This is default message"}
    return render(request,'msg_success.html', context=context)

@login_required(login_url='login_url')
def msgFailView(request):
    context={"error":"This is default message"}
    return render(request,'msg_fail.html', context=context)