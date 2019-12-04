from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		return render(request, 'app01/index.html',{'name': name})
	else:
		return render(request,'app01/index.html')

def login(request):
	return render(request, 'app01/login.html')