from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Blogs
from .forms import BlogsForm, SignupForm




def login(request):
        '''
                login 
        '''
        url = 'blogapp/login.html'

        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = auth.authenticate(username=username, password=password)
                if user is not None:
                        auth.login(request, user)
                        return redirect('blogapp:blog')
                else:
                        return redirect('blogapp:login')
        return render(request, url)


def logout(request):
        '''
                Logout
        '''
        auth.logout(request)
        return redirect('blogapp:login')


@login_required(login_url='blogapp:login')
def index(request):
        '''
                Home Page
        '''
        url = 'blogapp/index.html'
        return render(request, url)


@login_required(login_url='blogapp:login')
def blog(request):
        '''
                Blog Page
        '''
        url = 'blogapp/blog.html'

        form = BlogsForm()

        if request.method == 'POST':
                form = BlogsForm(request.POST, request.FILES)
                if form.is_valid():
                        data = form.save(commit=False)
                        data.blog_user = User(id=request.user.id)
                        data.save()
                        
                        messages.success(request, 'Successfully new blog submitted.')
                        return redirect('blogapp:blog')
                else:
                        messages.warning(request, 'Error blog submitting..')
                        return redirect('blogapp:blog')

        return render(request, url, {'form': form})



@login_required(login_url='blogapp:login')
def blog_update(request, id):
        '''
                Blog Page
        '''
        url = 'blogapp/blog.html'

        blog = Blogs.objects.get(id=int(id))

        data = {
                'blog_title': blog.blog_title,
                'blog_description':  blog.blog_description
        }

        form = BlogsForm(initial=data)

        if request.method == 'POST':
                form = BlogsForm(request.POST, instance=blog)
                if form.is_valid:
                        form.save()
                        messages.success(request, 'Successfully updated blog details.')
                        return redirect('blogapp:blog')
                else:
                        messages.warning(request, 'Error blog submitting..')
                        return redirect('blogapp:blog')
        return render(request, url, {'form': form})



@login_required(login_url='blogapp:login')
def blog_list(request):
        url = 'blogapp/blog_list.html'
        blog = Blogs.objects.all()
        return render(request, url, {"blogs": blog })


@login_required(login_url='blogapp:login')
def blog_page(request, id):
        url = 'blogapp/blog_page.html'
        blog = Blogs.objects.get(id=int(id))
        return render(request, url, {"blog": blog })

@login_required(login_url='blogapp:login')
def blog_delete(request, id):
        blog = Blogs.objects.get(id=int(id))
        blog.delete()
        return redirect('blogapp:blog_list')


def signup(request):
        '''
                Signup Page
        '''
        url = 'blogapp/signup.html'
        form = SignupForm()

        if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid:
                        form.save()
                        return redirect('blogapp:login')
                else:
                        return redirect('blogapp:signup')
                        
        return render(request, url, {'form': form})


