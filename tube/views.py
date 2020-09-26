from django.shortcuts import render
from pytube import YouTube
import os

url=''
# Create your views here.
def index(request):
   return render(request, 'tube/index.html')

def process(request):
   global url
   url = request.GET.get('url')
   try:
      yt=YouTube(url)
      streams_all=yt.streams.filter(progressive=True,file_extension='mp4').all()
      resolutions=[]
      for i in streams_all:
          resolutions.append(i.resolution)

      resolutions=list(dict.fromkeys(resolutions))
    #  embed_link=url.replace("watch?v=","embed/")
     # path='D:\\'
      return render(request,'tube/process.html',{'rsl':resolutions ,'url':url})
   except:
       return render(request,'tube/error.html')



def result(request,res):
   global url
   homedir=os.path.expanduser("~")
   dirs=homedir+'/Downloads'
   if request.method=='POST':
      YouTube(url).streams.get_by_resolution(res).download(dirs)
      return render(request,'tube/result.html')

   else:
      return render(request,'tube/error.html')


def about(request):
   return render(request,'tube/about.html')

def help(request):
   return render(request,'tube/help.html')







