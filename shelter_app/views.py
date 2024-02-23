from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import testimonial, contact, shelteragents, shelterproperties, bookedproperty
from django.db.models import Q
from shelter_app.forms import ShelterPropertiesForm
import razorpay
import string
import random

# Create your views here.
def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']

        if firstname == "" or lastname == "" or email == "" or email == "" or username == "" or upass == "" or ucpass == "":
            context = {}
            context['errmsg'] = "Please Enter All Details !!!"
            return render(request, 'register.html', context)
        elif upass != ucpass:
            context = {}
            context['errmsg'] = "Password did not match!!!"
            return render(request, 'register.html', context)
        else:
            try:
                u = User.objects.create(first_name = firstname, last_name = lastname, email = email, username = username, password = ucpass)
                u.set_password(ucpass)
                u.save()

                context = {}
                context['success'] = "Account created Successfully! Sign In Now"
                return render(request, 'register.html', context)
            except:
                context = {}
                context['errmsg'] = "Username already exists!!!"
                return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']

        if username == "" or upass == "" or ucpass == "":
            context = {}
            context['errmsg'] = "Please enter all details!!!"
            return render(request, 'login.html', context)
        elif upass != ucpass:
            context = {}
            context['errmsg'] = "Password did not match!!!"
            return render(request, 'login.html', context)
        else:
            u = authenticate(username = username, password = ucpass)
            if u is not None:
                login(request, u)
                return redirect('/home')
            else:
                context = {}
                context['errmsg'] = "Invalid Username/Password !!!"
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('/home')

def home(request):
    s = shelterproperties.objects.all()
    context = {}
    context['properties'] = s
    return render(request, 'home.html', context)

def about(request):
    show = testimonial.objects.all()
    context = {}
    context['testimonies'] = show
    return render(request, 'about.html', context)

def contactus(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        pmiddlename = request.POST['pmiddlename']
        psurname = request.POST['psurname']
        pmail = request.POST['pmail']
        pmob1 = request.POST['pmob1']
        pmob2 = request.POST['pmob2']
        paddress = request.POST['paddress']
        pmsg = request.POST['pmsg']

        if pname == "" or pmiddlename == "" or psurname == "" or pmail == "" or pmob1 == "" or paddress == "" or pmsg == "":
            context = {}
            context['errmsg'] = "Please enter all details!!!"
            return render(request, "contact.html", context)
        else:
            pmob2 = 0
            c = contact.objects.create(firstname = pname, middlename = pmiddlename, lastname = psurname, email = pmail, mob1 = pmob1, mob2 = pmob2, address = paddress, msg = pmsg)
            c.save()

            context = {}
            context['pname'] = pname + " " + psurname + " : )"
            context['success'] = "Thank you for Contacting Us "
            return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')

def agents(request):
    context = {}
    a = shelteragents.objects.all()
    context['agents'] = a
    return render(request, 'agents.html', context)

def shelterproperty(request):
    s = shelterproperties.objects.all()
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def buyproperty(request):
    s = shelterproperties.objects.filter(ptype2 = 1)
    print(s)
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def rentproperty(request):
    r = shelterproperties.objects.filter(ptype2 = 2)
    context = {}
    context['property'] = r
    return render(request, 'shelterproperty.html', context)

def shelterpropertytype(request, type):
    propertytype = int(type)
    s = shelterproperties.objects.filter(ptype1 = propertytype)
    # print(s)
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def sortbeds(request, bed):
    noofbed = int(bed)
    s = shelterproperties.objects.filter(beds = noofbed)
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def sortarea(request, alimit):
    alimitupper = int(alimit)
    alimitlower = int(alimitupper / 2)
    # print(alimitupper, alimitlower)
    q1 = Q(area__lte = alimitupper)
    q2 = Q(area__gte = alimitlower)
    s = shelterproperties.objects.filter(q1 and q2)
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def sortareabelow(request, alimit):
    alimitupper = int(alimit)
    q1 = Q(area__lte = 2000)
    s = shelterproperties.objects.filter(q1)
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def sortareaabove(request, alimit):
    alimitlower = int(alimit)
    q1 = Q(area__gte = alimitlower)
    s = shelterproperties.objects.filter(q1)
    context = {}
    context['property'] = s
    return render(request, 'shelterproperty.html', context)

def plimitbelow(request, pl):
    plimit = int(pl)
    # print(plimit, type(plimit))
    q1 = Q(area__lt = plimit)
    s = shelterproperties.objects.filter(q1)
    return render(request, 'shelterproperty.html', {'property': s})

def booked(request):
    userid = request.user.id
    u = User.objects.filter(id = userid)

    b = bookedproperty.objects.filter(uid = u[0])
    context = {}
    context['bproperty'] = b
    return render(request, 'booking.html', context)

def booking(request, pid):
    userid = request.user.id
    u = User.objects.filter(id = userid)
    print(u[0])
    s = shelterproperties.objects.filter(id = pid)
    print(s[0])

    b = string.ascii_letters + string.digits
    l = len(b)

    bid = ""
    for i in range(0, 10, 1):
        index = random.randrange(0, l)
        bid += b[index]

    print(bid)

    b = bookedproperty.objects.create(bookingid = bid, uid = u[0], pid = s[0])
    b.save()

    b = bookedproperty.objects.filter(uid = u[0])
    context = {}
    context['bproperty'] = b
    return render(request, 'booking.html', context)

def removebooking(request, bid):
    b = bookedproperty.objects.filter(id = bid)
    b.delete()
    return redirect('/booked')

def submitproperty(request):
    if request.method == 'POST':
        form = ShelterPropertiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            context = {}
            context['success'] = "Thank you for submiting your Property : )"
            return render(request, 'shelterproperty.html', context)
        else:
            form = ShelterPropertiesForm()
        # firstname = request.POST['sname']
        # middlename = request.POST['smiddlename']
        # lastname = request.POST['slastname']
        # email = request.POST['smail']
        # mob1 = request.POST['smob1']
        # mob2 = request.POST['smob2']
        # address = request.POST['saddress']
        # city = request.POST['scity']
        # propertyname = request.POST['spname']
        # ptype1 = request.POST['spropertytype']
        # ptype2 = request.POST['ssaleorrent']
        # beds = request.POST['noofbeds']
        # area = request.POST['sarea']
        # spdescription = request.POST['spropertydescription']
        # simage = request.POST['simage']
        # print(firstname,middlename,lastname,email,mob1,mob2, address,city, propertyname,ptype1, ptype2, beds,area,spdescription, simage, sep="\n")

        # p = shelterproperties.objects.create(firstname = firstname, middlename = middlename, lastname = lastname, email = email, mob1 = mob1, mob2 = mob2, address = address, city = city, propertyname = propertyname, ptype1 = ptype1, ptype2 = ptype2, beds = beds, area = area, description = spdescription, pimage = simage)
        # p.save()
        context = {}
        context['form'] = form
        return render(request, 'submitproperty.html', context)
    else:
        form = ShelterPropertiesForm()
        context = {}
        context['form'] = form
        return render(request, 'submitproperty.html', context)
    

def paynow(request):

    b = bookedproperty.objects.filter(uid = request.user.id)
    bid = b.bookingid
    client = razorpay.Client(auth=("rzp_test_9TH7HLFyaq2ysI", "0ESpk0Atz5iu8kPVRe6QJNWL"))

    amt = 800

    DATA = {
        "amount":amt * 100,
        "currency": "INR",
        "receipt": "bid",
        "notes": {
            "key1": "value3",
            "key2": "value2"
        }
    }
    payment = client.order.create(data=DATA)
    print(payment)
    context = {}
    context['data'] = payment
    client.order.create(data = DATA)
    return render(request, 'booked.html', context)