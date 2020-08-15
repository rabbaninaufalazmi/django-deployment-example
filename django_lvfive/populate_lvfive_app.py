import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_lvfive.settings')

import django
django.setup()

import random
from faker import Faker
from lvfive_app.models import UserInput


def populate(N=5):
    fakegen = Faker()
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = UserInput.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == "__main__":
    print("Start populating!")
    populate(100)
    print("POPULATIN FINISH")
