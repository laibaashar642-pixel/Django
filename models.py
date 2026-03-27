from django.db import models

# Create your models here.
#wo model jo hamaray database ko define krti hai
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()


def __str__(self):
    return self.name

    # frist we need to register our model in admin file
    #migrations ka mtlb wo file generate krna jo is file kai change ko store krti hai
"""     >>> from home.models import Contact
>>> Contact.objects.all()
<QuerySet [<Contact: Contact object (2)>, <Contact: Contact object (3)>, <Contact: Contact object (4)>, <Contact: Contact object (5)>]>
>>> Contact.objects.all()[0]
<Contact: Contact object (2)>
>>> Contact.objects.all()[0].name
'Harry Potter'
>>> Contact.objects.all(){1].email 
  File "<console>", line 1
    Contact.objects.all(){1].email
                           ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> Contact.objects.all()[1].email
'asharmunir642@gmail.com'
>>>  if i want to filter like ma cha rhi hu kai muje koi specific name mily tu hum filter 
use krty hai like we write Contact.objects.filter(name="name")Contact.objects.filter(name="name")"""
