from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST" :
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send an email
        send_mail(
            'Message from ' + message_name, # subject
            message, # message
            message_email, # from email
            ['cachouline@gmail.com'], # to email
        )

        return render(request, 'contact.html', {'message_name' : message_name})

    else :
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})

def appointment(request):
    if request.method == "POST" :
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']


        # Send an email
        appointment = "Hello " + your_name + ", vous avez pris RDV au labo à " + your_scheldule
        send_mail(
            'Appointment request ', # subject
            appointment, # message
            your_email, # from email
            ['cachouline@gmail.com'], # to email
        )

        return render(request, 'appointment.html', {
            'your_name' : your_name,
            'your_phone' : your_phone,
            'your_email' : your_email,
            'your_address' : your_address,
            'your_scheldule' : your_scheldule,
            'your_time' : your_time,
            'your_message' : your_message
            })
        # We created a dictionary

    else :
        return render(request, 'home.html', {})

def prendrerdv(request):
    if request.method == "POST" :
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        laboratoire = request.POST['laboratoire']
        jour = request.POST['jour']
        heure = request.POST['heure']
        motif = request.POST['motif']


        # Send an email
        contenu = prenom + " " + nom + " désire prendre rendez-vous au laboratoire " + laboratoire + " " + jour +\
                  " à " + heure + " pour une prestation '" + motif + "'. Merci d'envoyer un mail de confirmation."
        send_mail(
            'Demande de rendez-vous ' + prenom + " " + nom, # subject
            contenu, # message
            email, # from email
            ['cachouline@gmail.com'], # to email
        )

        return render(request, 'prendrerdv.html', {
            'nom' : nom,
            'prenom' : prenom,
            'email' : email,
            'telephone' : telephone,
            'laboratoire' : laboratoire,
            'jour' : jour,
            'heure' : heure,
            'motif' : motif
            })
        # We created a dictionary

    else :
        return render(request, 'prendrerdv.html', {})