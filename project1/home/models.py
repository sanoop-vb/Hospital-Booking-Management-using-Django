from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_speciality=models.CharField(max_length=100)
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image= models.ImageField(upload_to='Doctors')

    def __str__(self):
        return 'Dr'+ self.doctor_name + '-(' + self.doctor_speciality + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

