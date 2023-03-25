from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import login, register, community, BookList
from rest_framework import generics, mixins
from rest_framework import serializers

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import serializers

from .serializer import sampleform


# Create your views here.
def Homeview(request):
    return render(request,'home.html')

def viewAuthentication(request):
    return render(request,'AuthenticationPage.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def Register(request):
    return render(request, 'RegisterPage.html')


def firstpage(request):
    return render(request, 'Loginpage.html')

def indexpage(request):
    return render(request, 'index.html')

def RegisterAuthentication(request):
    if request.method == 'POST':
        email=request.POST['email']
        Age = request.POST['age']
        Adress = request.POST['adress']
        User = request.POST['username']
        Pass = request.POST['psw']
        data = register.objects.create(Email=email, Age=Age,Adress=Adress)
        data.save()
        data1 = login.objects.create(username=User, password=Pass)
        data1.save()
        return render(request, 'Loginpage.html')

def AuthenticationEntry(request):
    if request.method == 'POST':
        u = request.POST["n1"]
        p = int(request.POST["password"])
        try:
            data3 = login.objects.get(username=u)
            if data3.password == p:
                request.session['id'] = u
                return redirect(Adminview)

            # An id is developed based on its on and carried into profile session
            # if the id is avaiable in profiles then it will automatically enter into the profile

            else:
                return HttpResponse("password incorrect:")
        except Exception:
            return HttpResponse("username is incorrect:")

    else:
        return render(request, 'loginpage.html')


# #


# #

def Adminview(request):
    return render(request, 'AdminViewPage.html')


def Memberview(request):
    return render(request, 'AdminViewPage.html')



def StayInProfile(request):
    if 'id' in request.session:
        return render(request, 'AdminViewPage.html')
    else:
        return redirect(AuthenticationEntry)


#
# # how to logout from an account and return back to login page:

def Loginview(request):
    return render(request, 'loginpage.html')

def resetdonepage(request):
    return render(request, 'resetdone.html')


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(Loginview)

class Adminfunction(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = sampleform
    queryset = community.objects.all()
    def get(self, request):
        queryset = self.get_queryset()
        serializer= sampleform(queryset, many=True)
        # return Response(serializer.data)
        # return self.list(request)
        return render(request, 'Profilepage.html',{'data':serializer.data})
    def post(self, request):
        return self.create(request)
class bookfunction(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = sampleform
    queryset = BookList.objects.all()
    def getbooklist(self, request):
        queryset = self.get_queryset()
        serializer = sampleform(queryset, many=True)
        # return Response(serializer.data)
        # return self.list(request)
        return render(request, 'bookAvaiable.html', {'data': serializer.data})

def resetpass(request):
    return render(request, 'resetpassword.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = request.POST['n1']
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = register.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "WEBSITE/template/mesege.txt"
					c = {
					"email":register.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [register.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect (resetdonepage)
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="WEBSITE/template/resetdone.html", context={"password_reset_form":password_reset_form})