from django.shortcuts import render 
from django.contrib.auth.decorators import login_required 
from .models import Deposit, SupportRequest

@login_required
def deposit_view(request):

    btc_address = "bc1pwhk884ngmn6mx7uw2m9lnw0j968m800k3pdhn3wc850d6d4x0c5secdjj7"
    eth_address = "0x1ded46a9a7e96a967fb1d686f0d13b14aeca0d3e"
    bnb_address = "0x1ded46a9a7e96a967fb1d686f0d13b14aeca0d3e"
    sol_address = "XKO1ded46a9a7e96a967fb1d686f0d13b14aeca0d3e"

    if request.method == 'POST':

        amount = request.POST.get('amount')
        coin = request.POST.get('coin')

        if not amount:
            return render(request, 'deposit.html', {'error': 'Amount is required'})

        try:
            amount = float(amount)
        except:
            return render(request, 'deposit.html', {'error': 'Invalid amount'})

        if coin == "BTC":
            address = btc_address
        elif coin == "ETH":
            address = eth_address
        elif coin == "BNB":
            address = bnb_address
        else:
            address = sol_address

        Deposit.objects.create(
            user=request.user,
            amount=amount,
            coin=coin,
            crypto_address=address
        )

        return render(request, 'deposit.html', {
            'success': 'Deposit request submitted',
            'btc_address': btc_address,
            'eth_address': eth_address,
            'bnb_address': bnb_address,
            'sol_address': sol_address,
        })

    return render(request, 'deposit.html', {
        'btc_address': btc_address,
        'eth_address': eth_address,
        'bnb_address': bnb_address,
        'sol_address': sol_address,
    })
    
@login_required
def contact_view(request):

    if request.method == 'POST':

        tx_hash = request.POST.get('tx_hash')
        message = request.POST.get('message')
        screenshot = request.FILES.get('screenshot')

        if not tx_hash:
            return render(request, 'contact.html', {
                'error': 'Transaction hash is required'
            })

        SupportRequest.objects.create(
            user=request.user,
            tx_hash=tx_hash,
            message=message,
            screenshot=screenshot
        )

        return render(request, 'contact.html', {
            'success': 'Support request submitted successfully'
        })

    return render(request, 'contact.html')
