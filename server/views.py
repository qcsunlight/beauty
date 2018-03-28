from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import os, hashlib
from server import utils
# Create your views here.


def index_view(request):

	return render(request, 'index.html')

def upload_view(request):
		if request.method == 'POST':
			_file = request.FILES.get('file')
		if not _file:
			return HttpResponseRedirect('/')
		path = 'imgs'
		if not os.path.exists(path):
			os.mkdir(path)
		hash_md5 = hashlib.md5(_file.read()).hexdigest()
		file_name = os.path.join(path, hash_md5) + '.jpg'
		des = open(file_name, 'wb+')
		for chunk in _file.chunks():
			des.write(chunk)
		des.close()
		#获取颜值
		obj = utils.get_age_beauty(filename=file_name)
		print(obj)
		return JsonResponse(obj)