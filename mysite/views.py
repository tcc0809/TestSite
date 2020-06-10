from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

	return render(request,"index.html",locals())

def page(request,pno):
	authors = [
	'王小明',
	'林小華',
	'陳小華',
	'曾小花',
	'張花花'
	]
	if pno>=0 and pno<len(authors):
		author = authors[pno]
	else:
		author = "未知成員"
	return HttpResponse("成員簡介:{}".format(author))

def db(request,sno):
	stories = models.Story.objects.filter(sno=sno)
	if len(authors)>=1:
		sno = stories[0]
	else:
		story="找不到!"
	return HttpResponse(story)