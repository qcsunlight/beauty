from aip import AipFace


# 定义常量
APP_ID = '10894783'
API_KEY = 'IkuNpLsPkGtaFwT3WIF3Quro'
SECRET_KEY = 'KDftL1loA5WgGlxbcteDFslinSdPtiUW'


#初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()

#定义参数变量
options = {
	'face_fields': "age,beauty",
}

def get_age_beauty(filename):
	result = aipFace.detect(get_file_content(filename), options)
	result = (result['result'])[0]
	obj = {
	'age': result['age'],
	'beauty': round(result['beauty'], 2),
	}
	return obj
'''
print('age:', result['age'])
print('beauty:', round(result['beauty'], 2))
'''