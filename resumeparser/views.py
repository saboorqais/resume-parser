
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from pyresparser import ResumeParser
import shutil ,os
@api_view(["GET","POST"])
def resumeParser(request):
    if( os.path.exists(settings.MEDIA_ROOT)):
        shutil.rmtree(settings.MEDIA_ROOT)
    myfile = request.FILES['filename']
    print("here")
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    print(settings.MEDIA_ROOT+"\\"+myfile.name)
    data = ResumeParser(settings.MEDIA_ROOT+"\\"+myfile.name).get_extracted_data()
    print("not hehre")
    return  JsonResponse({"data":data})