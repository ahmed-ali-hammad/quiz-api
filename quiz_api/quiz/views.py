from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import *
from .serializers import *

class QuizListView(APIView):
    def get(self, request):
        query_set = Quiz.objects.all()
        serializer = QuizSerializer(query_set, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class QuizDetailView(APIView):
    def get(self, request, pk):
        query_set = get_object_or_404(Quiz, pk = pk)
        serializer= QuizSerializer(query_set)
        return Response(serializer.data) 

    def put (self, request, pk):
        query_set = Quiz.objects.get(pk= pk)
        serializer = QuizSerializer(query_set, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self,request, pk):
        query_set = Quiz.objects.get(id = pk)
        query_set.delete()
        return Response('The Quiz is deleted')



class QuestionRandomDetail(APIView):
    def get(self,request):
        query_set = Question.objects.all().order_by('?')[0]
        serializer = QuestionSerializer(query_set)
        return Response(serializer.data)


