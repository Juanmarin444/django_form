from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    return render(request, 'survey/index.html')

def create(request):
    if request.method == "POST":
        if 'count' not in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] += 1
        request.session['fname'] = request.POST['fname']
        request.session['lname'] = request.POST['lname']
        request.session['motorcycle'] = request.POST['motorcycle']
        request.session['displacement'] = request.POST['displacement']
        return redirect('/show')
    else:
        return redirect('/')

def show(request):
    return render(request, 'survey/results.html')
