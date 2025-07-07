from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientsForm
from django.contrib import messages
import smtplib
import ssl



def index(request):
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form_data = serialize_form_data(form)
            messages.success(request, f"Thank You {form_data['name']}, Message successfully sent!")
            print(form_data)
            send_email(form_data)
            return redirect('index')
        else:
            print("Form Errors:", form.errors)  # Print validation errors
            messages.error(request, "Invalid Email. Please check your Email/Cell.")
    else:
        form = ClientsForm()

    return render(request, "mvulane/mvulane_index.html", {'form': form})


def contact(request):
    form = ClientsForm()
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            pass

        else:
                form.save()
                messages.success(request, 'New staff added')
                return redirect("index")

    # context = {'form': form}
    return render(request, "mvulane/contact.html", {
        'form': form
    })

def espanini(request):
    return render(request,"mvulane/espanini.html", )

def webdev(request):
    return render(request,"mvulane/webdev.html", )


def serialize_form_data(form):
    """
    Serialize Django form data into JSON format.
    """
    serialized_data = {}
    for field_name, field_value in form.cleaned_data.items():
        serialized_data[field_name] = field_value
    return serialized_data


def send_email(form_data):
    my_email = "mothalindokuhle168@gmail.com"
    my_password = "ebjmkthbnjphixwk"  # Use your App Password

    friend_email = "civilmotha@gmail.com"
    name = form_data['name']
    email = form_data['email']
    message = form_data['message']
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friend_email,
            msg=f"Subject: New Message\n\n"
                f"From: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}"
        )
    print("Email sent successfully!")


def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form_data = serialize_form_data(form)
            messages.success(request, f"Thank You {form_data['Name']}, Message successfully sent")
            print(form_data)
            send_email(form_data)
            return redirect('index')
        else:
            print("Form Errors:", form.errors)  # Print form validation errors
            messages.error(request, "Invalid Email or Cell. Please check your Email/Cell.")

    else:
        form = QuoteForm(initial={'created_date': datetime.now()})

    return render(request, "cusp/quote.html", {'form': form})