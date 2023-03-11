from django.db import models

class schools(models.Model):
    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=100)
    address  = models.CharField(max_length=500)
    
    #adding school name and address is through the django admin panel
    #to access the admin panel create a new super user

    class Meta:
        db_table = 'schools'
    def __str__(self):
        return str(self.name)

#login is possible only after adding the school name and address through admin panel
class login(models.Model):
    id       = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    school   = models.ForeignKey(schools,on_delete=models.CASCADE,default="1")
    role     = models.IntegerField(null=True)

    class Meta:
        db_table = 'login'
    def __str__(self):
        return str(self.username)

class student(models.Model):
    id           = models.AutoField(primary_key=True)
    user         = models.ForeignKey(login, on_delete=models.CASCADE,default="")
    name         = models.CharField(max_length=50)
    class_name   = models.CharField(max_length=5)
    section      = models.CharField(max_length=2)
    admissionid  = models.CharField(max_length=10)
    age          = models.IntegerField()
    gender_choice= (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender       = models.CharField(choices=gender_choice, max_length=10)
    guardian_name= models.CharField(max_length=100)

    class Meta:
        db_table ='student'
    def __str__(self):
        return str(self.name)

class subject(models.Model):
    id           = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50,default="")
    description  = models.CharField(max_length=2000,default="")

    class Meta:
        db_table='subject'
    def __str__(self):
        return str(self.subject_name)

    
class staff(models.Model):
    id           = models.AutoField(primary_key=True)
    user         = models.ForeignKey(login, on_delete=models.CASCADE,default="")
    name         = models.CharField(max_length=50)
    staff_id     = models.CharField(max_length=20)
    age          = models.IntegerField()
    joined_date  = models.DateField()
    gender_choice= (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender       = models.CharField(choices=gender_choice, max_length=10)

    class Meta:
        db_table ='staff'

class results(models.Model):
    id           = models.AutoField(primary_key=True)
    student_id   = models.ForeignKey(student,on_delete=models.CASCADE)
    subject      = models.ForeignKey(subject, on_delete=models.CASCADE)
    total_score  = models.IntegerField()
    obtained_score = models.IntegerField()
    grade        = models.CharField(max_length=5,default="")

    class Meta:
        db_table ='results'