from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from .models import Student
from datetime import date,time


def home(request):
    # stu = Student.objects.get(pk=1) # use column which are  unique otherwise it wiil raise exceptins
    # stu=Student.object.first()
    # stu=Student.object.order_by('name').first()

    # stu = Student.objects.last()
    # stu=Student.objects.order_by('name').last()

    # stu = Student.objects.latest('pass_date')
    # stu = Student.objects.earliest('pass_date')

    # stu = Student.objects.all()
    # print('hey',stu.exists())

    # stu = Student.objects.all()
    # one_data = Student.objects.get(pk=1)
    # print(stu.filter(pk=one_data.pk).exists())

    # stu=Student.objects.create(name="girish",roll=20,city='allahbaad',marks=87,pass_date='2020-3-4') # create save and get in one method
    # stu, created = Student.objects.get_or_create(
    #     name="girish", roll=20, city='allahbaad', marks=87, pass_date='2020-3-4')
    # print('createdd or not', created)
    # print('return', stu)

    # stu = Student.objects.filter(marks=100).update(city='pune')
    # stu, created = Student.objects.update_or_create(
    #     id=11, name='girish', defaults={'name': 'Kohli'})
    # print(created)

    # stu = Student.objects.all()
    # print('count is', stu.count())

    # stu = Student.objects.filter(name__startswith='a')
    # stu = Student.objects.filter(city__iexact='New delhi')
    # stu = Student.objects.filter(marks__lte='70')
    # stu = Student.objects.filter(id__in=[1,4,7,99])
    # stu = Student.objects.filter(marks__range=(90, 100))
    # stu = Student.objects.filter(Q(marks__range=(90, 100)) & Q(name__istartswith='r'))
    stu = Student.objects.filter(pass_date__time__gte=time(6,00))

    return render(request, 'school/home.html', {'stu': stu})
