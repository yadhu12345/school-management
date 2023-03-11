from django.shortcuts import render
from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import login, logout
from smsapp.models import *
from smsapp.forms import *
from .forms import *

def user_login(request):
	msg=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		school=request.POST['school']
		userlogin=login.objects.filter(username=username,password=password,school=school,role=1).count()
		if userlogin > 0:
			userlogin=login.objects.filter(username=username,password=password,school=school,role=1).first()
			request.session['userid']=userlogin.id
			return redirect('homeu')
		else:
			print("ERROR: Invalid username or password")
			msg='Invalid!!'
            
	form=LoginForm
	return render(request, 'user/login.html',{'forms':form,'msg':msg})

def user_logout(request):
    logout(request)
    return redirect('loginu')

def admin_logout(request):
    logout(request)
    return redirect('login')

def user_registration(request):

	if request.method == 'POST':  
		form = userregForm(request.POST, request.FILES)
		print
		if form.is_valid():
			obj=form.save(commit=False)
			uid=0
			obj.role=uid
			obj.save()
			form = userregForm()
			designation = schools.objects.all()
			context = {'forms': form,}
			return render(request, 'user/registration.html',context)
	else:
		form=userregForm()
	context = {'forms': form}
	return render(request, 'user/registration.html', context)

def home(request):
	if 'userid' not in request.session:
		return redirect('loginu')
	else:
		useri = request.session.get('userid')
		name=login.objects.filter(id=useri)[0]
		school=schools.objects.all()
		stuiid=student.objects.filter(user=useri)
		designation = results.objects.filter(student_id=stuiid[0])
		context = {'st': designation,'school':school,'uname':name}
		return render(request,'user/home.html',context)

def info(request):
	if 'userid' not in request.session:
		return redirect('loginu')
	else:
		useri = request.session.get('userid')
		designation = student.objects.filter(user=useri)
		context = {'st': designation}
		return render(request,'user/info/info.html',context)
def getresult(request):
	if 'userid' not in request.session:
		return redirect('loginu')
	else:
		useri = request.session.get('userid')
		stuiid=student.objects.filter(user=useri)
		designation = results.objects.filter(student_id=stuiid[0])
		context = {'st': designation}
		return render(request,'user/result/result.html',context)