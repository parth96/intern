from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext


def index(request):
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
