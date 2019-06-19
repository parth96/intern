from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from applicationform.models import applicationform
# from django.db import IntegrityError
# Create your views here.
from django.template import RequestContext


def index(request):
    if request.method == "POST":
         instance = applicationform.objects.create(name = request.POST['name'],cate = request.POST['cate'],brname = request.POST['brname'],email = request.POST['email'],phone = request.POST['phone'],fname = request.POST['fname'],foccu = request.POST['foccu'],bday = request.POST['bday'],gender = request.POST['gender'],desig = request.POST['desig'],cpf = request.POST['cpf'],section = request.POST['section'],city = request.POST['city'],phno = request.POST['phno'],mono = request.POST['mono'],insname = request.POST['insname'],sem = request.POST['sem'],semmarks = request.POST['semmarks'],address = request.POST['address'],menname = request.POST['menname'],des1 = request.POST['des1'],site = request.POST['site'],loc = request.POST['loc'])
         instance.save()
                                                  # email=request.POST.get('email'),
                                                  # fname=request.POST.get('fname'),
                                                  # foccu=request.POST.get('foccu'),
                                                  # phone=request.POST.get('phone'),
                                                  # # bday=request.POST.get('bday'),
                                                  # gender=request.POST.get('gender'),
                                                  # desig=request.POST.get('desig'),
                                                  # cpf=request.POST.get('cpf'),
                                                  # section=request.POST.get('section'),
                                                  # city=request.POST.get('city'),
                                                  # phno=request.POST.get('phno'),
                                                  # # mono=request.POST.get('mono'),
                                                  # insname=request.POST.get('insname'),
                                                  # brname=request.POST.get('brname'),
                                                  # sem=request.POST.get('sem'),
                                                  # semmarks=request.POST.get('semmarks'),
                                                  # address=request.POST.get('address'),
                                                  # menname=request.POST.get('menname'),
                                                  # des1=request.POST.get('des1'),
                                                  # site=request.POST.get('site'),
                                                  # loc=request.POST.get('loc'))


    # if request.method == "POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     fname = request.POST['fname']
    #     foccu = request.POST['foccu']
    #     bday = request.POST['bday']
    #     gender = request.POST['gender']
    #     desig = request.POST['desig']
    #     cpf = request.POST['cpf']
    #     section = request.POST['section']
    #     city = request.POST['city']
    #     phno = request.POST['phno']
    #     mono = request.POST['mono']
    #     insname = request.POST['insname']
    #     brname = request.POST['brname']
    #     sem = request.POST['sem']
    #     semmarks = request.POST['semmarks']
    #     address = request.POST['address']
    #     menname = request.POST['menname']
    #     des1 = request.POST['des1']
    #     site = request.POST['site']
    #     loc = request.POST['loc']
    #
    #     print(name)
    #     print(email)
    #     print(phone)
    #     print(fname)
    #     print(foccu)
    #     print(bday)
    #     print(gender)
    #     print(desig)
    #     print(cpf)
    #     print(section)
    #     print(city)
    #     print(phno)
    #     print(mono)
    #     print(insname)
    #     print(brname)
    #     print(sem)
    #     print(semmarks)
    #     print(address)
    #     print(menname)
    #     print(des1)
    #     print(site)
    #     print(loc)

    branch = {'MBA(HR)': 1, 'MBA(Finance)': 2, 'Geology': 3, 'Geophysics': 4, 'MSc. - Chemistry': 5,
              'Mech.Engineering': 6,
              'Petroleum Engineering': 7, 'Electrical Engineering': 8, 'Chem.Engineering': 9, 'Civil Engineering': 10,
              'BE / BTech - Computer Science': 11, 'BE / BTech - IT': 12,
              'BE / BTech Electronics. & Telecommunication': 13, 'Law': 14,
              'Environment Science': 15, 'Mass Communication': 16, 'Micro - Biology': 17, 'Logistics': 18, 'MCA': 19}
    category = {'GEN': 1, 'OBC': 2, 'SC': 3, 'ST': 4, 'Others': 5, }
    return render(request, 'buy.html', {'dictionary': branch, 'dictionary1': category})


def exam(request):
    return HttpResponse("hello world")
