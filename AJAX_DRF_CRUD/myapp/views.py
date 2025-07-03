from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.views import APIView
from myapp.models import Task
from myapp.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views import View



class TaskView(APIView):
    def get(self,request):
        task = Task.objects.all()
        serialzer = TaskSerializer(task,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class TaskDetailView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Task,id=pk)
    
    def get(self,rquest,pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        print(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,requst,pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task,data=requst.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
        else:
            print(serializer.errors)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_200_OK)
    

class Index(View):
    def get(self,request):
        return render(request,'index.html')
    
    # def post(self,request):
    #     title = request.POST['title']
    #     Task.objects.create(title=title)
    #     return redirect('index')
        
    

