from django.shortcuts import render

def store(request):
    	
	return render(request, 'store/store.html')

def cart(request):
	
	return render(request, 'store/cart.html')

def checkout(request):
	
	return render(request, 'store/checkout.html')

def prod_det_1(request):
    	
	return render(request, 'store/prod_det_1.html')

def prod_det_2(request):
    	
	return render(request, 'store/prod_det_2.html')
	
def prod_det_3(request):
    	
	return render(request, 'store/prod_det_3.html')