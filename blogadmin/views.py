from django.shortcuts import render_to_response

# Create your views here.
def back(request):
	return render_to_response('backEnd.html')
