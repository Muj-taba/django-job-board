from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

JOB_TYPE = (
    ('Full time','Full time'),
    ('Part time','Part time')
)


def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


class Job(models.Model):

    owner        = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title        = models.CharField(max_length=500)
    slug         = models.SlugField(blank=True)
    #location
    job_type     = models.CharField(max_length=20 ,choices= JOB_TYPE)
    describtion  = models.TextField(max_length=500, blank=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy      = models.IntegerField(default=1)
    salary       = models.IntegerField(default=1)
    experience   = models.IntegerField(default=1)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    image        = models.ImageField(upload_to=image_upload)




    def save(self, *args ,**kwargs):
        self.slug = slugify(self.title)
        #+"-"+str(self.id)
        super(Job,self).save(*args, **kwargs)
    

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25, )
    
    class Meta:
        verbose_name=('Category')
        verbose_name_plural=("Categories")

    def __str__(self):
        return self.name




class Apply(models.Model):
    job         = models.ForeignKey(Job,related_name='Apply_job' , on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    email       = models.EmailField(max_length=100)
    website     = models.URLField()
    cv          = models.FileField(upload_to='apply/')
    coverletter = models.TextField(max_length=500)
    created_at  = models.DateTimeField(auto_now=True)

        
    class Meta:
        verbose_name=('Applicant')
        verbose_name_plural=("Applicants")


    def __str__(self):
        return self.name


