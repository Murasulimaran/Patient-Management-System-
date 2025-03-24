from django.shortcuts import render,redirect,get_object_or_404
from home.models import Records

# Create your views here.

def records_save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        problem = request.POST.get('problem')
        status = request.POST.get('status')
        report = request.POST.get('report')
        next_meet = request.POST.get('next_meet')

        record = Records(name=name,age=age,phone_number=phone_number,email=email,
                         address=address,problem=problem,status=status,
                         report=report,next_meet=next_meet)
        record.save()
        return redirect('/')

    return render(request,'records.html')


def index_view(request):
    details = Records.objects.all().order_by('id')
    context = {'collection':details}
    return render(request,'index.html',context)


def update(request, record_id):
    record = get_object_or_404(Records, id=record_id)

    if request.method == 'POST':
        record.name = request.POST.get('name', record.name)
        record.age = request.POST.get('age', record.age)
        record.phone_number = request.POST.get('phone_number', record.phone_number)
        record.email = request.POST.get('email', record.email)
        record.address = request.POST.get('address', record.address)
        record.problem = request.POST.get('problem', record.problem)
        record.status = request.POST.get('status', record.status)
        record.report = request.POST.get('report', record.report)
        record.next_meet = request.POST.get('next_meet', record.next_meet)

        record.save()

        return redirect('/')

    return render(request, 'update.html', {'record': record})


def delete_view(request, record_id):
    if request.method =="POST":
        records=get_object_or_404(Records, id=record_id)
        records.delete()
        return redirect('/')
    return redirect('/')