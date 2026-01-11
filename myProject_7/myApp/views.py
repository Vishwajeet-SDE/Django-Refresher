from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact_form(request):
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == "POST":
        try:
            contact = Contact(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                subject=request.POST.get("subject"),
                message=request.POST.get("message"),
                ip_address=request.META.get("REMOTE_ADDR"),
            )

            # 🔑 This triggers unique constraint check
            contact.full_clean()
            contact.save()

            messages.success(request, "Message sent successfully ✅")
            return redirect("submit_contact")

        except ValidationError as e:
            # 🔥 Display field-wise errors
            for field, errors in e.message_dict.items():
                for error in errors:
                    messages.error(request, f"{field} : {error}")

            return redirect("submit_contact")

    return render(request, "contact_error.html")