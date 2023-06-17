from django.db import models


class mstuser(models.Model):
    srno=models.AutoField(primary_key=True)
    fnm=models.CharField(max_length=40)
    mno=models.BigIntegerField()
    emailid=models.CharField(max_length=40)
    pwd=models.CharField(max_length=13)
    role=models.CharField(max_length=15)
    
class course(models.Model):
    courseid=models.AutoField(primary_key=True)
    nm=models.CharField(max_length=25)
    duration=models.IntegerField()
    fees=models.IntegerField()
    courseicon=models.CharField(max_length=60)

class batch(models.Model):
    batchid=models.AutoField(primary_key=True)
    nm=models.CharField(max_length=25)
    startdate=models.DateField()
    batchtime=models.CharField(max_length=25)
    facultyname=models.CharField(max_length=25)


    