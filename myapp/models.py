from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    
class Child(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent)
    

class Publication(models.Model):
    title = models.CharField(max_length=30)
    
class Author(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)


class Person(models.Model):
    name = models.CharField(max_length=128)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    remarks = models.CharField(max_length=50, default='')
