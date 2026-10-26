from django.shortcuts import render
from .serializer import EventSerializer
from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class RetriveUpdate(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,pk):
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)    


    def post(self,request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        

    def put(self,request,pk):
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
    def delete(self,request,pk):
        event = Event.objects.get(id=pk)
        event.delete()
        return Response({"message": "Event deleted successfully"})



class EventListCreate(GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self,request):
        events = self.get_queryset()
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data)



    def post(self,request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class EventListCreateMixin(
    ListModelMixin,
    CreateModelMixin,
    GenericAPIView
):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        return self.list(request)


    def post(self,request):
        return self.create(request)


class EventDetailMixin(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView
):

    queryset = Event.objects.all()
    serializer_class = EventSerializer




    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get(self,request,pk):
        return self.retrieve(request,pk=pk)



    def put(self,request,pk):
           return self.update(request,pk=pk)
    
    def patch(self,request,pk):
           return self.partial_update(request,pk=pk)
    
    def delete(self,request,pk):
           return self.destroy(request,pk=pk)

    

class EventListUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Create(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
  




class EventJWT(
    ListModelMixin,
    CreateModelMixin,
    GenericAPIView
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



class PrivateView(APIView):
    event = Event.objects.all()
    authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        return Response("First login")