from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# This function created for rendering Home
def home(request):
    return render(request, 'home/home.html')

# This function created for rendering about page
def about(request):
    return render(request, 'home/about.html')

# This function created for Contact Form Activation
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        
    return render(request, "home/contact.html")


# This functioons is created for search funtionality
def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsTimeStamp = Post.objects.filter(timeStamp__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent).union(allPostsTimeStamp).union(allPostsAuthor)

    # If query is not match with content.
    if allPosts.count() == 0:
        messages.warning(request, "No search results are found. Please type correctly.")
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html', params)

# This Funtion for Handling SignUp Data
def handlingSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


    # Check for errornuos problems
        # Username is must in 15
        if len(username) > 15:
            messages.error(request, "Username is must in 15 Characters")
            return redirect('home')
        # Username contains only alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should be contain letter & number")
            return redirect('home')
        # Confirm Password was same
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')
        # password is must in 17
        if len(pass1) > 17:
            messages.error(request, "Password is must in 17 characters")
            return redirect('home')
        # Create the User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your CodingColon's Account are Successfully Created")
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")
    


# Create Login & Log Out Functionility

# 1. Create Login Functionility
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        # User  Authentication
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

# 2. Create Log Out Functionilty    
def handeLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')           
    
    return HttpResponse("404-not found")