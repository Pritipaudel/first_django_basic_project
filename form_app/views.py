from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import RegForm  # Correct import of the model class

def reg_form(request):
    if request.method == "POST":
        data = request.POST
        Full_name = data.get("Full_name")
        Date_of_birth = data.get("Date_of_birth")
        Gender = data.get("Gender")
        mobile_number = data.get("mobile_number")
        email = data.get("email")
        address = data.get("address")

        # Save the data to the database
        RegForm.objects.create(  # Correct reference to model class
            Full_name=Full_name,
            Date_of_birth=Date_of_birth,
            Gender=Gender,
            mobile_number=mobile_number,
            email=email,
            address=address
        )

        # Create a dictionary with the data to return as a response
        response_data = {
            "Full_name": Full_name,
            "Date_of_birth": Date_of_birth,
            "Gender": Gender,
            "mobile_number": mobile_number,
            "email": email,
            "address": address
        }

        # Return a JSON response with the data
        return JsonResponse(response_data)
        
    return render(request, "form.html")
        
