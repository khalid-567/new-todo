from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,CustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer
# Create your views here.


@login_required(login_url='login')
def index(request):
	form=CustomerForm()
	customers=Customer.objects.filter(added_by = request.user)
	
	if request.method=='POST':

		new_customer = Customer(
			first_name = request.POST['first_name'], 
			last_name = request.POST['last_name'],
			email = request.POST['email'],
			added_by = request.user
		)
		
		new_customer.save()
		return redirect('home page')
		
			
	return render(request,'task/index.html',{'form':form,'customers':customers})


def delete_items(request, pk):
	data = Customer.objects.get(id=pk)
	if request.method == 'POST':
		data.delete()
		# messages.success(request,'successfully deleted')
		return redirect('home page')
	return render(request, 'task/task_confirm_delete.html')




    


def register(request):


	form=UserRegistrationForm()

	if request.method=='POST':

		form=UserRegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created, Login now')

			return redirect('login')
		
			
	return render(request,'task/register.html',{'form':form})   