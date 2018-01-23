from django.shortcuts import render, redirect
from django.forms.forms import Form
from main.models import Product,BuyUser
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse


@login_required
def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    if request.method == 'GET':
        
        item=Product.objects.all()
    
        itemsList = {
            'itemList': item
        }
        return render(request, 'main/main.html',itemsList)

    # POST
    if not request.user.is_superuser:
        item=request.POST['item']
        count=request.POST['count']
        print(item)
        itemsList = []
        if request.user.is_authenticated:
            usr=request.user
    
            buyUser = BuyUser()
            buyUser.user = usr
            buyUser.item = item
            buyUser.count=count
            itemsList.append(buyUser)
            itemsList = BuyUser.objects.bulk_create(itemsList)
    
            print('done')

            return redirect('main/main.html')
    it=request.POST['item']
    money=request.POST['money']
    if request.user.is_authenticated:
        ur=Product.objects.filter(item=it)
        ur.money=money
        print(ur)
        return redirect('main/main.html')
    

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth


