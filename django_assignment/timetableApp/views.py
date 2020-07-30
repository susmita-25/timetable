from django.shortcuts import render
from django.contrib import messages
import json
from .models import TimeTable
from django.http import HttpResponseRedirect
# Create your views here.

def transformData(username):
    data = TimeTable.objects.filter(username=username)
    key = ""
    val = []
    timetable={}
    prev_key = ""
    for d in data:
        # print(d.time)
        if prev_key != d.day:
            val.append(d.time)
            timetable[d.day] = val
        else:
            timetable.get(d.day).append(d.time)
        prev_key = d.day
        val = []
    print(timetable)
    return timetable
def timetable_view(request):
    # timetableForm = TimetableForm(request.POST or None)
    # print(request)
    # data = JSONParser().parse(request)
    # request_getdata = request.POST.get('timetable') 
    # print(timetableForm)
    timetable={
            
            'Time':["","","","","",""],
            'MONDAY':["","","","","",""],
            'TUESDAY':["","","","","",""],
            'WEDSNDAY':["","","","","",""],
            'THUSDAY':["","","","","",""],
            'FRIDAY':["","","","","",""],
            'SATURDAY':["","","","","",""],
        }
    # TimeTable.objects.all().delete()
    username=request.session['username']
    if request.method =="POST":
        
        data = json.loads(request.body)
        print(data)
        
        TimeTable.objects.filter(username=username).delete()
        for i,j in data:
            print(i)  
            print(j) 
            for k in j:
                table=TimeTable(day=i,time=k,subject=k,username=username)
                table.save()
        timetable = transformData(username)
        print("data saved successfully")
        messages.success(request, 'Data saved successfully') 
        return HttpResponseRedirect(request.path_info)
        # return render(request,"timetable.html",{'timetable':timetable,'error':'Data saved successfully'})
    else:
        data = TimeTable.objects.filter(username=username)
        print(len(data))
        if data.exists():
            print("not none")
            key = ""
            val = []
            timetable={}
            prev_key = ""
            for d in data:
                print(d.time)
                if prev_key != d.day:
                    val.append(d.time)
                    timetable[d.day] = val
                else:
                    timetable.get(d.day).append(d.time)
                prev_key = d.day
                val = []
            print(timetable)


        # context={
        #     # 'timetableform':TimetableForm(),
        #     'timetable':timetable,
        # }
    return render(request,"timetable.html",{'timetable':timetable})
