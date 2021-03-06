from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Work
from bs4 import BeautifulSoup
import requests
from django.contrib import messages

# Create your views here.
def home(request):
  if request.method =='POST':
      url=request.POST['url']
      if Work.objects.filter(url=url).exists():
       ans=Work.objects.filter(url=url)
       url=ans[0].url
       word=ans[0].word
       return HttpResponse("<h2 style='color:#ea5252;'>Hey,This url somebody already present in our databse...!!!</h2><h2>Processed url: </h2>"+url+"<h2>Most Renderd Text :</h2>"+word+"<br><br><br><br><a href='/' style=' text-decoration: none; border-radius: 1px;border:1px solid black; background:#3aa1d8;'>Search another site</a>")
      res=requests.get(url)
      soup=BeautifulSoup(res.text,"html.parser")
      tex=soup.find('body')
      mapa=tex.text.split(" ")
      
      common=['the',"","The",'are','.','-','at','there','some','my','of','be' ,'use','her','than','and','this','an','would','first','a','have','each','make','water','to','from','which','like','been','in','or','she','him','call','is','one','do','into','who','you','had','how','time','oil','that','by','their','has','its','it','word','if','look','now','he','but','will','two','find','was','not','up','more','long','for','what','other','write','down','on','all','about','day']
      dic={}
      for k in mapa:
       if k in common:
         continue
       dic.setdefault(k,0)
       dic[k]=dic[k]+1
      ans={}
      que=list(dic.values())
      que.sort()
      for j in que[::-1][:10]:
        for key in dic.keys():
         if dic[key]==j:
           ans[key]=j

      form=Work.objects.create(url=url,word=ans)
      form.save()
      return redirect("/result")
  return render(request,"1.html")

def result(request):
  res=Work.objects.order_by("-id")[0]
  return render(request,"result.html",{'res':res})


'''def countword(query):
  res=requests.get(query)
  lab=res.text
  sap=lab.text
  mapa=sap.split(" ")
  dic={}
  for k in mapa:
   dic.setdefault(k,0)
   dic[k]=dic[k]+1
  
  return dic'''
