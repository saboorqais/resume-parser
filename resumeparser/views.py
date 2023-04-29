
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from pyresparser import ResumeParser
import shutil ,os
from urllib.parse import urlencode,quote_plus
@api_view(["GET","POST"])
def resumeParser(request):
    if( os.path.exists(settings.MEDIA_ROOT)):
        shutil.rmtree(settings.MEDIA_ROOT)
    myfile = request.FILES['filename']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    file_path ="/media/"+myfile.name
    file_url = request.build_absolute_uri(file_path)    
    data = ResumeParser(settings.MEDIA_ROOT+"\\"+myfile.name).get_extracted_data()
    return  JsonResponse({"data":data,"file_url":file_url})