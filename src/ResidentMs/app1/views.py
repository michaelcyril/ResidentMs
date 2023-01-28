from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


# Create your views here.

@api_view(["GET"])
@permission_classes([AllowAny])
def getWilaya(request):
    data = Wilaya.objects.values('id', 'name').all()
    response = {"data": data}
    return Response(response)


@api_view(["POST"])
@permission_classes([AllowAny])
def getKata(request):
    wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
    data = Kata.objects.values('id', 'name').filter(id=wilaya)
    response = {"data": data}
    return Response(response)


# {
#     "wilaya_id": 1
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def getMtaa(request):
    kata = Kata.objects.get(id=request.data['kata_id'])
    data = Mtaa.objects.values('id', 'name').filter(id=kata)
    response = {"data": data}
    return Response(response)


# {
#     "kata_id": 1
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def createCitizen(request):
    kata = Kata.objects.get(id=request.data['kata'])
    mtaa = Mtaa.objects.get(id=request.data['mtaa'])
    wilaya = Kata.objects.get(id=request.data['wilaya'])
    citizen = Citizen.objects.create(nida=request.data['nida'], firstname=request.data['firstname'],
                                     lastname=request.data['lastname'], kata=kata, mtaa=mtaa, wilaya=wilaya)
    citizen.save()
    response = {"data": "successful save"}
    return Response(response)


# {
#     "nida": "2020020200202022",
#     "firstname": "mike",
#     "lastname": "cyril",
#     "mtaa": 1,
#     "kata": 1,
#     "wilaya": 1
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def getWilayaInfo(request):
    wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
    citizen = Citizen.objects.values('id', 'nida', 'firstname',
                                     'lastname', 'mtaa', 'kata',
                                     'wilaya').filter(wilaya=wilaya)
    a = [entry for entry in citizen]
    b = []
    for c in a:
        data = {
            'nida': c['nida'],
            'firstname': c['firstname'],
            'lastname': c['lastname'],
            'mtaa': Mtaa.objects.values('name').get(id=c['mtaa'])['name'],
            'kata': Kata.objects('name').get(id=c['name'])['name'],
            'wilaya': Wilaya.objects('name').get(id=c['name'])['name']
        }
        b.append(data)

    response = {
        "number_of_citizens": len(a),
        "citizen_list": b
    }
    return Response(response)


# {
#     "wilaya_id": 1
# }

@api_view(["POST"])
@permission_classes([AllowAny])
def getKataInfo(request):
    kata = Kata.objects.get(id=request.data['kata_id'])
    citizen = Citizen.objects.values('id', 'nida', 'firstname',
                                     'lastname', 'mtaa', 'kata',
                                     'wilaya').filter(kata=kata)
    a = [entry for entry in citizen]
    b = []
    for c in a:
        data = {
            'nida': c['nida'],
            'firstname': c['firstname'],
            'lastname': c['lastname'],
            'mtaa': Mtaa.objects.values('name').get(id=c['mtaa'])['name'],
            'kata': Kata.objects('name').get(id=c['name'])['name'],
            'wilaya': Wilaya.objects('name').get(id=c['name'])['name']
        }
        b.append(data)

    response = {
        "number_of_citizens": len(a),
        "citizen_list": b
    }
    return Response(response)


# {
#     "kata_id": 1
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def getMtaaInfo(request):
    mtaa = Mtaa.objects.get(id=request.data['mtaa_id'])
    citizen = Citizen.objects.values('id', 'nida', 'firstname',
                                     'lastname', 'mtaa', 'kata',
                                     'wilaya').filter(mtaa=mtaa)
    a = [entry for entry in citizen]
    b = []
    for c in a:
        data = {
            'nida': c['nida'],
            'firstname': c['firstname'],
            'lastname': c['lastname'],
            'mtaa': Mtaa.objects.values('name').get(id=c['mtaa'])['name'],
            'kata': Kata.objects('name').get(id=c['name'])['name'],
            'wilaya': Wilaya.objects('name').get(id=c['name'])['name']
        }
        b.append(data)

    response = {
        "number_of_citizens": len(a),
        "citizen_list": b
    }
    return Response(response)

# {
#     "mtaa_id": 1
# }
