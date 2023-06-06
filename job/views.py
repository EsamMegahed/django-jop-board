from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import Applyform

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj}
    return render(request, "job/job_list.html", context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == "POST":
        form = Applyform(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
    else:
        form = Applyform()
    context = {"job": job_detail, "form": form}
    return render(request, "job/job_detail.html", context)
