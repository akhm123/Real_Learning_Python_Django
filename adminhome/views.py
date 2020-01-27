from django.shortcuts import render
from django.shortcuts import render_to_response,render,redirect
import pyrebase
from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore


cred = credentials.Certificate('C:/Users/harsh/AdminSite/adminhome/pythonadmin.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://learningapp-3032a.firebaseio.com/'
})
db=firestore.client();
# ref = db.reference().child('users').get();

doc = (db.collection(u'course').document())
def home(request):
	return render_to_response('home.html')

def managecourse(request):
	print("Length is")
	size1=0
	print(size1)
	return render_to_response('managecourse.html',{'size':size1})

def course(request):
	return render(request,'course.html')

def courseupload(request):
	coursename=request.POST.get('coursename','')
	text=request.POST.get('coursename','').encode()
	print(text)
	image=request.POST.get('image','')
	doc.set({
    'name':text ,
    'imageurl': request.POST.get('image',''),
    'description':request.POST.get('Description','')
	})
	print("coursename is")
	print(coursename)
	print(image)
	print("Getting data")
	user_ref = db.collection(u'course')
	for k in db.collection('course').get():
    		z=k.to_dict()
    		print(z)#.get("name").decode())
	return render(request,'login.html')

def login(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	if(username=="harsh1868" and password=="harsh1868"):
		return render(request,'managecourse.html')	
	else:
		return render(request,'login.html')	
