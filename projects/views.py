
from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

allprojects=Project.objects.all()

def projects(request):
    context= {'projects' :allprojects }
    return render(request,'projects/projects.html',context)
def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context={'project':project, 'tags':tags}
    return render(request,'projects/single_project.html', context)  

def createproject(request):

    projectform=ProjectForm()
    context={'projectform':projectform}
    if request.method=="POST":
        projectform=ProjectForm(request.POST)
        if projectform.is_valid():
            projectform.save()
            return redirect('projects')

    return render(request,'projects/createproject.html',context)

def updateproject(request,pk):
    project=Project.objects.get(id=pk)
    updateform=ProjectForm(instance=project)

    context={'updateform':updateform}
    if request.method=="POST":
        projectform=ProjectForm(request.POST,instance=project)
        if projectform.is_valid():
            projectform.save()
            return redirect('projects')
    return render(request,'projects/createproject.html',context)

def deleteproject(request,pk):
    project=Project.objects.get(id=pk)
    context={'object':project}
    if request.method=="POST":
        project.delete()
        return redirect('projects')
    return render(request,'projects/deleteproject.html',context)