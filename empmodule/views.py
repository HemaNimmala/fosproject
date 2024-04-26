from django.shortcuts import render, redirect
from .models import*
# Create your views here.
def jobpost(request):
    return render(request,'empmodule/jobpost.html')
def add_jobdetails(request):
    if request.method == 'POST':
        work_title = request.POST.get('workTitle')
        salary_offered = request.POST.get('salary')
        job_type = request.POST.get('jobType')
        age = request.POST.get('age')
        education = request.POST.get('education')
        skills = request.POST.get('requiredskills')


        job_details =Jobdetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            age=age,
            skills=skills,
            education=education,



        )
        job_details.save()
        #return redirect('emphomepage'),
        return render(request,'empmodule/datainserted.html')
    return render(request,'emphomepage.html')
def view_jobdetails(request):
    job_details_list=Jobdetails.objects.all()
    return render(request,'empmodule/view_job_details.html',{'job_details_list':job_details_list})

def feedback(request):
    return render(request,'empmodule/feedback.html')