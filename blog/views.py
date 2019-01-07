from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
	post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#The line above puts the query into the variable into post
	#The line below turns the variable post into post in the html template
	return render(request, 'blog/post_list.html',{'posts':post})