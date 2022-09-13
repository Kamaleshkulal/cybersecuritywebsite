from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,Oneninetynine,Video,Twoninetynine,Threeninetynine,Forms

# Create your views here.
def Home(request):
    return render(request, "index.html")
   
def signup(request):
    
    if request.method=="POST":
        user=request.POST.get('username')
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")

def handlehome(request):
    return render(request, "handlehome.html")

def handlogout(request):
    logout(request)
    messages.success(request,"Logout Success")  
    return render(request,"index.html")

def buynow(request):
    if request.method=="POST":
        cardnumber=request.POST.get('card')
        month=request.POST.get('date')
        cvv=request.POST.get('cvv')
        username=request.POST.get('name')
        number=request.POST.get('phone')
        if len(cardnumber)>16 or len(cardnumber)<16:
            messages.info(request,"Card Number Must be 16 Digits")
            return redirect('/buy')  
        
        if len(cvv)>3 or len(cvv)<3:
               messages.info(request,"CVV/CVC Number Must be 3 Digits")
               return redirect('/buy')  

        if len(number)>10 or len(number)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/buy')

        else: 
             myquery=Oneninetynine(cardnumber=cardnumber,date=month,cvv=cvv,username=username,number=number)
             myquery.save()       
             messages.info(request,"payment Rs 199 Sucessfull")
             return redirect('/payment')

    return render(request, "buynow.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")



def handleservices(request):
    return render(request, "handleservices.html")

def handleabout(request):
    return render(request, "handleabout.html")    

def buylater(request):
    if request.method=="POST":
        cardnumber=request.POST.get('card')
        month=request.POST.get('date')
        cvv=request.POST.get('cvv')
        username=request.POST.get('name')
        number=request.POST.get('phone')
        if len(cardnumber)>16 or len(cardnumber)<16:
            messages.info(request,"Card Number Must be 16 Digits")
            return redirect('/buylater')  
        
        if len(cvv)>3 or len(cvv)<3:
               messages.info(request,"CVV/CVC Number Must be 3 Digits")
               return redirect('/buylater')  

        if len(number)>10 or len(number)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/buylater')

        else: 
             myquery=Twoninetynine(cardnumber=cardnumber,date=month,cvv=cvv,username=username,number=number)
             myquery.save()       
             messages.info(request,"payment Rs 299 Sucessfull")
             return redirect('/payment')

    return render(request, "buylater.html")

def buyimmediate(request):
    if request.method=="POST":
        cardnumber=request.POST.get('card')
        month=request.POST.get('date')
        cvv=request.POST.get('cvv')
        username=request.POST.get('name')
        number=request.POST.get('phone')
        if len(cardnumber)>16 or len(cardnumber)<16:
            messages.info(request,"Card Number Must be 16 Digits")
            return redirect('/buyimmediate')  
        
        if len(cvv)>3 or len(cvv)<3:
               messages.info(request,"CVV/CVC Number Must be 3 Digits")
               return redirect('/buyimmediate')  

        if len(number)>10 or len(number)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/buyimmediate')

        else: 
             myquery=Threeninetynine(cardnumber=cardnumber,date=month,cvv=cvv,username=username,number=number)
             myquery.save()       
             messages.info(request,"payment Rs 399 Sucessfull")
             return redirect('/payment')

    return render(request, "buyimmediate.html")


def payment(request):
    return render(request, "payment.html")

def sessions(request):
    videos = Video.objects.all()
    return render(request, "sessions.html",context={'videos':videos})

def awards(request):
    return render(request, "awards.html")

def project(request):
    return render(request,"project.html")

def internship(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        Gender=request.POST.get('Gender')
        SSLC_board=request.POST.get('SSLC_board')
        PUC_board=request.POST.get('PUC_board')
        interns=request.POST.get('interns')
        SSLC_percent=request.POST.get('SSLC_percent')
        PUC_percent=request.POST.get('PUC_percent')
        USN=request.POST.get('USN')
        cgpa=request.POST.get('cgpa')
        Branch=request.POST.get('Branch')
        College=request.POST.get('College')
        files=request.POST.get('files')
        if len(USN)>10 or len(USN)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/internship')

        if len(phonenumber)>10 or len(phonenumber)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/internship')

        else: 
             myquery=Forms(name=name,email=email,phonenumber=phonenumber,Gender=Gender,SSLC_board=SSLC_board,PUC_board=PUC_board,interns=interns,SSLC_percent=SSLC_percent,PUC_percent=PUC_percent,USN=USN,cgpa=cgpa,Branch=Branch,College=College,files=files)
             myquery.save()       
             messages.info(request,"Forms submitted successfully")
             return redirect('/internship')       


    return render(request,"internship.html")


def handlecontact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/handlecontact')
    return render(request,"handlecontact.html")