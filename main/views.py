
from django.shortcuts import render,redirect

#For Authentication
from django.contrib.auth import authenticate,login ,logout

#For pop up Messages
from django.contrib import messages

#To register  the new user  we import
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required,user_passes_test


from .models import Profile,Trip,Upcoming,Review,Price,Itenerary

import os

from django.conf import settings

import random

#For sending Emails
import smtplib

#Email and password for the server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart






#make sure u delete your password before uploading to the github
passwordName ='roue egvy bumj wkez'
company_email="joshhearns37@gmail.com"




@login_required(login_url='/login/')
def index(request):


    trips=Trip.objects.filter(user=request.user)[:3]
    upcoming =Upcoming.objects.all()[:3]
    reviews =Review.objects.all()
    profile =Profile.objects.get(user=request.user)


    if request.method == "POST":

        if 'review' in request.POST:
                

            name =request.POST.get('name')
            
            topic =request.POST.get('topic')
            
            message  =request.POST.get('message')

    # Option A: Select a random image from static files
            #We use the [0] because the staticfilesdirs is a list and we cant pass a string ti a list
            random_images_path = os.path.join(settings.STATICFILES_DIRS[0], 'random_images')
            random_image = random.choice(os.listdir(random_images_path))
            

            


            review = Review.objects.create(
                name =name,
                topic = topic,
                message = message,
                image=f'random_images/{random_image}',                   

            )

            review.save()


        if 'mails' in request.POST:
            
            email_input =request.POST.get('email')

            try:
                  # Create a MIMEText object
                Message = MIMEMultipart()
                Message['From'] = f"{company_email} <{email_input}>"
                Message['To'] = email_input
                Message['Reply-To'] = f"<{company_email}>"

                Message['Subject'] ="Expense Voyages"
                

                body =f"Hello{request.user}\n\n\n You've Subscribed for our Travel and Tour  Platform "

                
                # Attach the email body to the message
                Message.attach(MIMEText(body, 'plain'))

                            

                                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(company_email, passwordName)

                    # Send the email
                server.sendmail(company_email, email_input, Message.as_string())

                
                server.quit()

                messages.success(request, 'Yo"ve Subscribed Successfully ......')

              
        
            except Exception as e:

                messages.error(request,('There is an error trying to subscribe pls try again......'))
                    
                    
        
        return redirect('/')
            

    return render(request,'index.html',{
        'trips':trips,
        'upcomings':upcoming,
        'reviews':reviews,
        'profile':profile,
        

    })



#Login the user
def Login(request):

    
    if request.method =="POST":
        username =request.POST.get("user")
        password =request.POST.get("password")

        user =authenticate(request,username =username , password =password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in Successfully!!!!!!')

            return redirect('profile')
            
        else:
            messages.error(request,'There was an error when logging in,Please Login in again!!!!!')
            
            return redirect('login')
        


    return render(request,'login.html',{

    })


def sign_up(request):
        
        

    if request.method =="POST":

        firstname =request.POST.get('fname')

        lastname =request.POST.get('lname')
        
        username =request.POST.get('username')

        number  =request.POST.get('number')

        email =request.POST.get('email')

        password1 =request.POST.get('password')

        password2=request.POST.get('cpassword')


          
        
        if firstname =='' or lastname =='' or username=='' or number =='' or number =='' or  email =='' or password1 =='' or password2 =='':
             
            messages.error(request,("All Entry must be filled......"))
            return redirect('register')

        else:
         


                if User.objects.filter(username =username).exists():

                    messages.error(request,("Sorry!!,there was a problem registering. Username already taken. Please try again...."))

                    return redirect('register')

                elif password1 != password2:
                    messages.error(request,("Sorry!!,Make sure your password matches...."))

                    return redirect('register')

                    

        
                else :
                    try:
                                                
                        user=  User.objects.create_user(username=username,
                                                            
                                                            first_name=firstname, 

                                                            last_name =lastname,

                                                            password=password1,

                                                            email=email
                                                            
                                                            )
                        
                        user_model =User.objects.get(username=username)

                        
                        new_profile =Profile.objects.create(user =user_model,
                                                            
                                                            fname =user_model.first_name,

                                                            lname =user_model.last_name,

                                                            email =user_model.email,

                                                            number = number,




                                                            
                                                            )

                
                        new_profile.save()
                
                        
                            

                        messages.success(request,("You Have Regsitered Successfully......."))
                

                        return redirect('login')

                    except Exception as e:
                            messages.error(request, f"An error occurred: {str(e)}. Please try again.")
                            return redirect('register')

    


    


    return render(request,'sign_up.html',{
        
    })





#Login out process and redirecting to the welcome Page
def logout_user(request):

    logout(request)

    messages.success(request,'Logged out sucessfully.....')


    return redirect('login')






@login_required(login_url='/login/')
def trip(request):

    trips=Trip.objects.filter(user=request.user)



    
    if request.method == "POST":

        if request.FILES.get('image') == None:
            pass

        else:
            
            image =request.FILES.get('image')
            
        
        name=request.POST.get('name')
        country =request.POST.get('country')
        country_city =request.POST.get('city')
        date_booked=request.POST.get('booked')
        
        
        
        
        

        new_trip =Trip.objects.create(
            user =request.user,
            name=name,
            country =country,
            country_city =country_city,
            date_booked =date_booked,
            profile_img =image
        )
        

        new_trip.save()



    return render(request,'trip.html',{
                'trips':trips


    })




     
@login_required(login_url='/login/')
def trip_details(request,trip_id):

    profile =Profile.objects.get(user=request.user)

    trip =Trip.objects.get(id=trip_id,user=request.user)

    itenary =Itenerary.objects.filter(trip=trip,user=profile)

    if request.method=="POST":

        select =request.POST.get('select')

        name =request.POST.get('name')

        details =request.POST.get('details')


        real_itenary =Itenerary.objects.create(
            user =profile,
            trip =trip,
            transportation =select,
            lodging =name,
            activities =details

        )

        real_itenary.save()



          
    return render(request,'trip_details.html',{
        'itenary':itenary
    })



     
@login_required(login_url='/login/')
def trip_delete(request,item):

    trip =Trip.objects.get(id=item)

    trip.delete()

    

    return redirect('trip')

          




@login_required(login_url='/login/')
def profile(request):


    user_profile =Profile.objects.get(user=request.user)

    


    if request.method == "POST":

        if request.FILES.get('image') == None:
            image =user_profile.profile_img

        else:
            
            image =request.FILES.get('image')
            
        
        dob =request.POST.get('dob')
        number =request.POST.get('number')
        print(dob)
        
        
        
        address =request.POST.get('address')

        email =request.POST.get('email')
        

        user_profile.profile_img =image

        
        user_profile.Dob =dob
        user_profile.number= number
        user_profile.address =address

        user_profile.email =email

        

        # user_profile.location =location


        user_profile.save()


    
        return redirect('profile')


     



     
    return render(request,'profile.html',{
        'profile':user_profile,

    })

     



@user_passes_test(lambda u: u.is_superuser,login_url='/login/')
def manager(request):

    trips =Trip.objects.all()
     
     
    return render(request,'manager.html',{
        'trips':trips

    })


@user_passes_test(lambda u: u.is_superuser,login_url='/login/')
def manager_search(request):

    if request.method =="POST":
        searched =request.POST.get('search')

        if searched == 'all':
            trips=Trip.objects.all()

        else:

            trips =Trip.objects.filter(country__icontains=searched)

            
              
        
    return render(request,'manager_searched.html',{
            'trips':trips,
            'searched':searched

        })

    


@login_required(login_url='/login/')
def upcoming(request):
    upcomings =Upcoming.objects.all()
    




    return render(request,'upcoming.html',{
        'upcomings':upcomings

    })
     





@login_required(login_url='/login/')
def reviews(request):

    reviews =Review.objects.all()


    return render(request,'reviews.html',{
        'reviews':reviews

    })



@login_required(login_url='/login/')
def places(request):

    prices =Price.objects.all()


    return render(request,'places.html',{
        'prices':prices

    })



@login_required(login_url='/login/')
def place_searched(request):

    if request.method =="POST":
        searched =request.POST.get('search')

        if searched == 'all':
            prices=Price.objects.all()

        else:

            prices =Price.objects.filter(country_name__icontains=searched)



    return render(request,'places.html',{
        'prices':prices

    })





@login_required(login_url='/login/')
def contact(request):

                
    
        




    


    return render(request,'contact.html',{
        

    })




'''

lawal
1234
lawalhussein775@gmail.com

Taiwo
1234


Kenny
1234



'''