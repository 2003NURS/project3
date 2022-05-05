from django.db import models
from datetime import datetime,date

# Create your models here.



class Posts(models.Model):
    title = models.CharField(max_length=250, verbose_name='Name_ANIME')
    is_published = models.BooleanField(default='True', verbose_name='YES?NO')
    picture = models.ImageField(default= 'default value', upload_to="")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)


    def get_absolute_urls(self):
        return reverse('post', kwargs={'post_slag':self.title})

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'AnimePosts'
        verbose_name_plural = 'AnimePosts'
        ordering =['title', 'slug']

class Categories(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank= True)
    picture = models.ImageField(default='default value')
    describe = models.TextField(default='Da taFlair Django tutorials')



    def __str__(self):
        return self.title

class Registration(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    email = models.EmailField(blank=True, unique=True)
    telnumber = models.IntegerField(max_length=11, unique=True)
    password = models.CharField(max_length=10)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Regis'
        verbose_name_plural = 'Registration'
        ordering = ['name', 'lastname']



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return str(self.name)

