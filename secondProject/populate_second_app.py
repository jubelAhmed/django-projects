import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondProject.settings')

import django
django.setup()

import random
from secondApp.models import AccessRecord,WebPage,Topic
from faker import Faker
fake = Faker()

def addTopic():
    topics = ['News','Social Media','Games','Edcation','Currency']
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    return t

def populate(N=5):
    for entry in range(N):
        ## create new topic
        new_topic = addTopic()
        fake_name = fake.company()
        fake_url = fake.url()
        fake_date = fake.date()
        
        ## create new webpage 
        web_page = WebPage.objects.get_or_create(topic= new_topic,name = fake_name,url=fake_url)[0]
        
        ## create Access Record
        
        access_record = AccessRecord.objects.get_or_create(name=web_page,date=fake_date)[0]
        

if __name__ == "__main__":
    print('Populating Script')
    populate(20)
    print('populating Complete')
        
        
        
        
        
        
        



