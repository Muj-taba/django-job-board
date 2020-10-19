from .serializer import JobSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Job
from rest_framework.decorators import api_view


@api_view(['GET'])
def job_list_api(request):
    joblist = Job.objects.all()
    serializer = JobSerializer(joblist, many=True).data
    return Response({'serializer':serializer})

@api_view(['GET'])
def job_detail_api(request,id):
    jobdetail = Job.objects.get(id=id)
    serializer = JobSerializer(jobdetail)
    return Response(serializer.data)


@api_view(['POST'])
def job_add_api(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def job_update_api(request, id):
    jobdetail = Job.objects.get(id=id)
    serializer = JobSerializer(instance=jobdetail,data=request.data)
    if serializer.is_valid():
        serializer.save(commit=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def job_delete_api(request, id):
    jobdetail = Job.objects.get(id=id)
    jobdetail.delete()
    return Response("Deleted Successfully")


class JobListV2(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobUpdateV2(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field ='id'

class JobDeleteV2(generics.RetrieveDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field ='id'



