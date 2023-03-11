from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

def admin_login(request):
	msg=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		school=request.POST['school']
		userlogin=login.objects.filter(username=username,password=password,school=school,role=0).count()
		if userlogin > 0:
			userlogin=login.objects.filter(username=username,password=password,school=school,role=0).first()
			request.session['username']=userlogin.id
			return redirect('home')
		else:
			msg='Invalid!!'
            
	form=AdminLoginForm
	return render(request, 'administration/login.html',{'forms':form,'msg':msg})

def admin_logout(request):
    logout(request)
    return redirect('login')


def admin_registration(request):

	if request.method == 'POST':  
		form = AdminregForm(request.POST, request.FILES)
		print
		if form.is_valid():
			obj=form.save(commit=False)
			uid=0
			obj.role=uid
			obj.save()
			form = AdminregForm()
			designation = schools.objects.all()
			context = {'forms': form,}
			return render(request, 'administration/registration.html',context)
	else:
		form=AdminregForm()
	context = {'forms': form}
	return render(request, 'administration/registration.html', context)

def home(request):
	if 'username' not in request.session:
		return redirect('login')
	else:
		useri = request.session.get('username')
		name=login.objects.filter(id=useri)[0]
		designation = student.objects.all().count()
		context = {'st': designation,'uname':name}
		return render(request,'home.html',context)

def subjectView(request):
	if 'username' not in request.session:
		return redirect('login')
	else:
		if request.method == 'POST':  
			useri = request.session.get('username')
			form = subjectForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				form = subjectForm()
				designation = subject.objects.all()
				context = {'forms': form,'st':designation}
				return render(request, 'subject/subject.html',context)
		else:
			form=subjectForm()
		designation = subject.objects.all()
		context = {'forms': form,'st':designation}
		return render(request, 'subject/subject.html',context)

def staffinfoView(request):
	if 'username' not in request.session:
		return redirect('login')
	else:
		if request.method == 'POST':  
			form = staffinfoForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				form = staffinfoForm()
				designation = staff.objects.all()
				context = {'forms': form,'st':designation}
				return render(request,'staff/staff.html',context)
		else:
			form=staffinfoForm()
		designation = staff.objects.all()
		context = {'forms': form,'st':designation}
		return render(request,'staff/staff.html',context)

def studentloginView(request):
	if 'username' not in request.session:
		return redirect('login')
	else:
		if request.method == 'POST':  
			form = StudentLoginForm(request.POST, request.FILES)
			print
			if form.is_valid():
				obj=form.save(commit=False)
				uid=1
				obj.role=uid
				obj.save()
				form = StudentLoginForm()
				designation = login.objects.filter(role=1)
				context = {'forms': form,'st':designation}
				return render(request, 'stlogin/stlogin.html',context)
		else:
			form=StudentLoginForm()
		designation = login.objects.filter(role=1)
		context = {'forms': form,'st':designation}
		return render(request, 'stlogin/stlogin.html',context)
@csrf_exempt
def delete_data_studentl(request):
    if request.method == 'POST':
        id = request.POST.get('bid')
        d = login.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def studentinfoView(request):
	if 'username' not in request.session:
		return redirect('login')
	else:
		if request.method == 'POST':  
			form = studentinfoForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				form = studentinfoForm()
				designation = student.objects.all()
				context = {'forms': form,'st':designation}
				return render(request,'student/student.html',context)
		else:
			form=studentinfoForm()
		designation = student.objects.all()
		context = {'forms': form,'st':designation}
		return render(request,'student/student.html',context)

@csrf_exempt
def delete_data_student(request):
    if request.method == 'POST':
        id = request.POST.get('bid')
        d = student.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def addresultView(request):
	if 'username' not in request.session:
		return redirect('login')
	else:
		if request.method == 'POST':  
			form = resultForm(request.POST, request.FILES)
			total_score=request.POST['total_score']
			obtained_score=request.POST['obtained_score']
			print(total_score)
			if form.is_valid():
				obj=form.save(commit=False)
				uid=(int(obtained_score)/int(total_score))*100
				obj.grade=uid
				obj.save()
				form = resultForm()
				designation = results.objects.all()
				context = {'forms': form,'st':designation}
				return render(request,'result/result.html',context)
		else:
			form=resultForm()
		designation = results.objects.all()
		context = {'forms': form,'st':designation}
		return render(request,'result/result.html',context)
