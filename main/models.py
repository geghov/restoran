from django.db import models

# Create your models here.


class HomePage(models.Model):

    name1 = models.CharField('HomePage name1', max_length=100)
    name2 = models.CharField('HomePage name2', max_length=100)
    about = models.TextField('HomePage about')
    img = models.ImageField('HomePage image', upload_to='home_images')

    def __str__(self):
        return self.name1


class AboutPageInfo(models.Model):

    img1 = models.ImageField('About info image1', upload_to='about_images')
    img2 = models.ImageField('About info image2', upload_to='about_images')
    img3 = models.ImageField('About info image3', upload_to='about_images')
    img4 = models.ImageField('About info image4', upload_to='about_images')
    name1 = models.CharField('About info name1', max_length=100)
    name2 = models.CharField('About info name2', max_length=100)
    about1 = models.TextField('About info about1')
    about2 = models.TextField('About info about2')
    num1 = models.PositiveIntegerField('About info num1')
    num2 = models.PositiveIntegerField('About info num2')

    def __str__(self):
        return self.name1

class AboutChef(models.Model):

    img = models.ImageField('Chefs image', upload_to='about_images')
    name = models.CharField('About Chef', max_length=100)
    prof = models.CharField('Chef prof', max_length=60)
    link1 = models.URLField('Chef link1')
    link2 = models.URLField('Chef link2')
    link3 = models.URLField('Chef link3')
    
    def __str__(self):
        return self.name


class MenuCategory(models.Model):

    img = models.ImageField('MenuCategory image', upload_to='menu_images')
    name = models.CharField('MenuCategory name', max_length=60)
    
    def __str__(self):
        return self.name

class Menu(models.Model):

    menucategory = models.ManyToManyField(MenuCategory, related_name='menu_categ')
    img = models.ImageField('Menu image', upload_to='menu_images')
    name = models.CharField('Menu name', max_length=60)
    about = models.TextField('Menu about')
    price = models.PositiveIntegerField('Menu price')

    def __str__(self):
        return self.name


class Book(models.Model):

    name = models.CharField('Book name', max_length=60)
    email = models.EmailField('Book email')
    data = models.CharField('Book date', max_length=30)
    people_count = models.PositiveIntegerField('People count')
    subject = models.TextField('Subject')

    def __str__(self):
        return self.email