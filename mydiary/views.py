from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template  import RequestContext
from django.http 	  import HttpResponse
from mydiary.models   import Diary
from mydiary.forms 	  import DiaryForm, LoginForm
from django.utils 	  import timezone
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

'''
	Auth views
'''
def login(request):
	message=None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user 	 = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					message="Te has identificado"
				else:
					message="No estás activado"
			else:
				message="Credenciales inválidas"
	else:
		form = LoginForm()
	return render_to_response("auth/login.html", {"message": message, "form": form}, context_instance=RequestContext(request))


def logout(request):
	auth_logout(request)
	return redirect('login')



'''
	Diaries views
'''
def index(request):
	diaries = Diary.objects.all()
	return render_to_response("diary/index.html", {"diaries": diaries}, context_instance=RequestContext(request))


def show(request, diary_id):
	diary = get_object_or_404(Diary, pk=diary_id)
	return render_to_response("diary/show.html", {"d": diary})


@login_required
def create(request):
	if request.method == 'POST':
		a 		= User.objects.get(pk=1)
		diary 	= Diary(author=a)
		form 	= DiaryForm(request.POST, instance=diary)
		if form.is_valid():
			form.save()
			return redirect('diaries')
	else:
		form = DiaryForm()

	return render_to_response("diary/create.html", {"form": form}, context_instance=RequestContext(request))


@login_required
def destroy(request, diary_id):
	d = get_object_or_404(Diary, pk=diary_id, author=request.user)
	if d is not None:
		d.delete()
	return redirect("diaries")