from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Tutorial
from .models import Topic
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Author
from .forms import TutorialForm
import requests
import json 

def tut1(request):
	#tutorials = Tutorials.objects.all()
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    #contents = Tutorials.objects.filter(contentId__contentId=12345)
    return render(request, 'nittutorial/check.html', {'tutorials': tutorials})
def forums(request):
    #tutorials = Tutorials.objects.all()
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    #contents = Tutorials.objects.filter(contentId__contentId=12345)
    return render(request, 'nittutorial/forums.html', {'tutorials': tutorials})
def blogs(request):
    #tutorials = Tutorials.objects.all()
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    #contents = Tutorials.objects.filter(contentId__contentId=12345)
    return render(request, 'nittutorial/blogs.html', {'tutorials': tutorials})
def contributors(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/contributors.html',{'tutorials': tutorials})
def about(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/about.html',{'tutorials': tutorials})
def contact(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/contact.html',{'tutorials': tutorials})

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title','birth_date'))
    if request.method == "POST":
        formset = AuthorFormSet(request.POST, request.FILES,
                                queryset=Author.objects.filter(name__startswith='O'))
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))
    return render(request, 'nittutorial/registration.html', {'formset': formset})

def post_content(request, title, id):
    tutorial = get_object_or_404(Tutorial, pk=id)
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/post_content.html', { 'tutorials': tutorials, 'tutorial': tutorial})

def tutorial_new(request):
    if request.method == "POST":
        form = TutorialForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publishedDate = timezone.now()
            post.save()
            tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
            print(tutorials)
            return redirect('post_content', title=post.title, id=post.pk)
    else:
        form = TutorialForm()
    return render(request, 'nittutorial/post_edit.html', {'form': form})

def cf_profile(request):
    jsonList=[]
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req=requests.get('http://codeforces.com/api/user.info?handles='+username)
        jsonList.append(json.loads(req.text))
        userData = {}
        for data in jsonList:
           userData['handle'] = data["result"][0]['handle']
           userData['contribution'] = data["result"][0]['contribution']
           userData['rank'] = data["result"][0]['rank']
           userData['rating'] = data["result"][0]['rating']
           userData['maxRating'] = data["result"][0]['maxRating']
        parsedData.append(userData)
    #return HttpResponse(parsedData)
        tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
        return render(request, 'nittutorial/cf_profile.html',{'tutorials': tutorials,'data':parsedData})

def cf_form(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/cf_form.html',{'tutorials': tutorials})
def problems_find(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/problems_find.html',{'tutorials': tutorials})
def problems_display(request):
    jsonList=[]
    parsedData = []
    if request.method == 'POST':
        tag=request.POST.get('tag')
        req=requests.get('http://codeforces.com/api/problemset.problems?tags='+tag)
        jsonList.append(json.loads(req.text))
        problemName={}
        i = 0 
        while i < 10:
            problemName['problem']=jsonList[0]["result"]["problems"][i]['name']
            problemName['contestId']=jsonList[0]["result"]["problems"][i]['contestId']
            problemName['index']=jsonList[0]["result"]["problems"][i]['index']
            parsedData.append(problemName)
            i=i+1
        #return HttpResponse(parsedData)
        tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
        return render(request, 'nittutorial/problems_display.html',{'tutorials': tutorials,'data':parsedData})
        #return HttpResponse(jsonList[0]["result"]["problems"][0]['name'])
def editor(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/editor.html',{'tutorials': tutorials})
def compile(request):
    if request.method == 'POST':
        code=request.POST.get('code')
        print(code);
        Compile_URL = u'http://api.hackerearth.com/code/compile/'
        CLIENT_SECRET = 'fee4190d6e63d82853d4cb30495a2a0ecaf7e9bf'
        source = code
        data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': "PYTHON",
        'time_limit': 5,
        'memory_limit': 262144,
         }
        jsonList=[]
        req = requests.post(Compile_URL, data=data)
        jsonList.append(json.loads(req.text))
        return HttpResponse(jsonList[0]['compile_status'])
def run(request):
    if request.method == 'POST':
        code=request.POST.get('code')
        language=request.POST.get('language')
        Run_URL = u'http://api.hackerearth.com/code/run/'
        CLIENT_SECRET = 'fee4190d6e63d82853d4cb30495a2a0ecaf7e9bf'
        source = code
        data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': language,
        'time_limit': 5,
        'memory_limit': 262144,
         }
        jsonList=[]
        req = requests.post(Run_URL, data=data)
        jsonList.append(json.loads(req.text))
        parsedData = []
        userData = {}
        userData['compile_status']=jsonList[0]['compile_status']
        userData['status']=jsonList[0]['run_status']['status']
        userData['time_used']=jsonList[0]['run_status']['time_used']
        userData['memory_used']=jsonList[0]['run_status']['memory_used']
        userData['output_html']=jsonList[0]['run_status']['output_html']
        parsedData.append(userData)
        return render(request,'nittutorial/compile_editor.html',{'data':parsedData,'code':code})
def home(request):
    return render(request,'nittutorial/index.html')