from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kumar(request):
    return HttpResponse('kumar is a cricketplayer')

def venky(request):
    return HttpResponse('venky is a footballplayer')

def charan(request):
    return HttpResponse('<h1>charan is a dancer</h1>')

def mahi(request):
    return HttpResponse('<h1><marquee>Mahi is a singer</marquee></h1>')

def bioData(request):
    return HttpResponse('''
                        <h1>Name is katikala</h1>
                        <i>age is 24</i>
                        <b>Gender is Male</b>
                        <img src='https://brightcove.iplt20.com/output/input/6353724999112-1718526347.jpg'</img>''')