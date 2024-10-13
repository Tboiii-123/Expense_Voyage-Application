from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User =get_user_model()


class Profile(models.Model):

    #Linking the fk to the use models that is imported
    user =models.ForeignKey(User, on_delete=models.CASCADE)


    fname=models.CharField(max_length=200)
    
    lname=models.CharField(max_length=200)
    

    email =models.EmailField(blank=True)

    number =models.CharField(max_length=200)

    address =models.CharField(max_length=200, blank=True)

    Dob =models.DateField(blank=True, null=True)
     
    #To add a default profile 
    #We use default attribute
    profile_img  =models.ImageField(upload_to='profile',default ='blank.png',blank=True)

    



    def __str__(self):

        return self.user.username







class Trip(models.Model):

    user =models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    
    country=models.CharField(max_length=200)

    country_city=models.CharField(max_length=200)
    
    
    
    date_booked = models.DateField()
    

    profile_img  =models.ImageField(upload_to='trip',default ='blank.png')
    
    


    def __str__(self):

        return self.name

    

#Upcoming Event


class Upcoming(models.Model):

    
    name = models.CharField(max_length=200, null=True, blank=True)
    
    country=models.CharField(max_length=200)

    country_city=models.CharField(max_length=200)
    
    
    #<p>Kuala Lumpur</p>
    #<h2 class="card-text">Malaysai</h2>
              
                  
    

    img  =models.ImageField(upload_to='trip',default ='blank.png')
    
    


    def __str__(self):

        return self.country




class Itenerary(models.Model):

     user=models.ForeignKey(Profile,on_delete=models.CASCADE)

     trip =models.ForeignKey(Trip, on_delete=models.CASCADE)

     transportation =models.CharField(max_length=300)

     lodging =models.CharField(max_length=300)

     activities =models.CharField(max_length=300)



     def __str__(self):

         return self.trip





class Review(models.Model):

    name=models.CharField(max_length=50)

    topic =models.CharField(max_length=100)

    message =models.CharField(max_length=200)


    image =models.ImageField(upload_to='random_images',default='blank.png')





    def __str__(self):

        return self.name + '  review'
    



class Price(models.Model):

    country_name=models.CharField(max_length=200)

    country_city =models.CharField(max_length=200)
    
    price_range_start =models.CharField(max_length=10)

    price_range_end =models.CharField(max_length=20)

    image =models.ImageField(upload_to='price',default='blank.png')


    def __str__(self):

        return self.country_name + '  '+ self.country_city
    
