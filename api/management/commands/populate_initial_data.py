from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Client, Project
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate initial data for the database'

    def handle(self, *args, **kwargs):
        # Create initial users
        user1 = User.objects.create_user(username='rohit', email='rohit@example.com', password='password')
        user2 = User.objects.create_user(username='ganesh', email='ganesh@example.com', password='password')
        user3 = User.objects.create_user(username='priya', email='priya@example.com', password='password')
        user4 = User.objects.create_user(username='nisha', email='nisha@example.com', password='password')

        # Create initial clients
        client1 = Client.objects.create(client_name='Nimap', created_by=user1)
        client2 = Client.objects.create(client_name='Infotech', created_by=user1)
        client3 = Client.objects.create(client_name='Tech Solutions', created_by=user2)

        # Create initial projects and assign users
        project1 = Project.objects.create(project_name='Project A', client=client1, created_by=user2)
        project1.users.add(user1, user3)

        project2 = Project.objects.create(project_name='Project B', client=client2, created_by=user3)
        project2.users.add(user2, user4)

        project3 = Project.objects.create(project_name='Project C', client=client3, created_by=user1)
        project3.users.add(user1, user2, user3, user4)

        self.stdout.write(self.style.SUCCESS('Successfully populated initial data'))
