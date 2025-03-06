from django.shortcuts import render
from Web_Side.models import RegisterDB,ComplaintdB,ContactdB
from django.http import JsonResponse

# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def display_user(request):
    data = RegisterDB.objects.all()
    return render(request,"Display_User.html",{'data':data})

def display_complaint(request):
    data = ComplaintdB.objects.all()
    return render(request,"Display_Complaint.html",{'data':data})

def display_contact(request):
    data = ContactdB.objects.all()
    return render(request,"Contact.html",{'data':data})


def warned_users_page(request, count):
    users_got_warning = RegisterDB.objects.filter(warning_count=count)

    # Get the list of users who will be deleted before deletion
    warned_users = list(RegisterDB.objects.filter(warning_count__gte=5).values('id', 'username', 'email', 'warning_count'))

    # Delete users with warning_count >= 5
    RegisterDB.objects.filter(warning_count__gte=5).delete()

    if warned_users:
        return JsonResponse({'message': 'Users deleted due to repeated cyberbullying offenses', 'deleted_users': warned_users}, status=403)

    return render(request, "Warned_Users.html", {'warned_users': warned_users, 'users_got_warning': users_got_warning})

