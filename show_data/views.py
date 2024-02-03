from django.shortcuts import render
from show_data.models import Student



# Create your views here.
def StudentDetail(request):
    # stu= Student.objects.all()
    # when we want the specific data fromteh database then wee will use 
    stu = Student.objects.get(pk=5455)
    return render(request,'show_data/studetail.html',{'stud':stu})
