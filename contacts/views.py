from django.shortcuts import render
from  .models import Contacts

# Create your views here.
def home(request):
    return render(request,"phone.html")
    
def addcontact(request):
    try:
     NAME=request.POST["Name"]
     MOBILENO=int(request.POST["Mobileno"])
     explist=Contacts.objects.filter(name=NAME)
     numberlist=Contacts.objects.filter(mobileno=MOBILENO)
     if numberlist.exists():
        return render(request,"phone.html",{'msg':"Number already registered."})

     elif explist.exists():
          return render(request,"phone.html",{'msg':"Contact already exists."})
    
     else:
        emplist=Contacts(name=NAME,mobileno=MOBILENO)
        emplist.save()
        return render(request,"phone.html",{'msg':"Contact added."})

    except Exception as e:
        print(e)
        return render(request,"phone.html",{'msg':"Contact could not be added."})

def displaycontact(request):
    contactlists=Contacts.objects.all()
    return render(request,"phone.html",{"contact":contactlists})

def deletecontact(request):
    try:
      NAME=request.POST["Name"]
      explist=Contacts.objects.filter(name=NAME)
      if explist.exists():
       explist.delete()
       return render(request,"phone.html",{'msg2':"Contact deleted."})
      else:
           return render(request,"phone.html",{'msg2':"Contact not found."})


    except Exception as e:
         print(e)
         return render(request,"phone.html",{'msg2':"Contact could not be deleted due to issues."})

def updatecontact(request):
    BTN=request.POST["btn"]
    if BTN=="Update name":
     try:
       Oldname=request.POST["oldname"]
       Newname=request.POST["newname"]
       contactlist=Contacts.objects.filter(name=Oldname)
       if contactlist.exists():
           contactlist.update(name=Newname)
           return render(request,"phone.html",{'msg3':"Contact name updated."})

       else:
             return render(request,"phone.html",{'msg3':"Contact name not found."})

     except Exception as e:
          print(e)
          return render(request,"phone.html",{'msg3':"Contact name could not be updated."})
    
    elif BTN=="Update number":
        try:
         Oldnumber=request.POST["oldnumber"]
         Newnumber=request.POST["newnumber"]
         contactlist=Contacts.objects.filter(mobileno=Oldnumber)
         if contactlist.exists():
            contactlist.update(mobileno=Newnumber)
            return render(request,"phone.html",{'msg3':"Contact number updated."})

         else:
            return render(request,"phone.html",{'msg3':"Contact number not found."})

        except Exception as e:
            print(e)
            return render(request,"phone.html",{'msg3':"Contact number could not be updated."})
       