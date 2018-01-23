from django.shortcuts import render,redirect
from main.models import BuyUser
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def shoppingcar(request):
    '''
    Render the shoppingcar page
    '''
    ur=BuyUser.objects.filter(user=request.user)
    print(ur)
    
    total=0
    for i in ur:
        total=total+i.count
    
    BuyList = {
            'BuyList': ur,
            'total':total
    }
    return render(request, 'shoppingcar/shoppingcar.html',BuyList)
    
