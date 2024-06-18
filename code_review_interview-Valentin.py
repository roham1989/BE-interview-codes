# 1.

def not_string(str):
    key = "not"
    if str[0:3] == key:
        print(str)
    else:
        print("not" + str)


# 2. 

if x == y:
    return True
else:
    return False


# 3.

import a
a.show()


# 4. 

def add_to_list(lst=[]):
    lst.append('hi')
    return lst

add_to_list()
add_to_list()

# 5.
result = sum(x*x for x in [item for sublist in [[j if j % 2 == 0 else 0 for j in range(i, i + 3)] for i in range(1, 10)] for item in sublist if item != 0]) 

# 6.
def create_report(first_name, last_name, age, address, city, state, zipcode, phone, email,
                  is_married, num_children, occupation, salary, favorite_color, favorite_food, 
                  favorite_movie, favorite_song, car_model, car_year, hobbies):
    # ... Do something with all the parameters
    print(f"Creating report for {first_name} {last_name}...")
    # ...

# 7.
def qz(a1, a2):
    z1 = 0
    for i in a1:
        if i in a2:
            z1 += 1
    return z1

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

r = qz(lst1, lst2)
print(r)


# 8.

def calculator(expression):
    return eval(expression)

# user input
user_input = input("Enter a simple math expression: ")

result = insecure_calculator(user_input)

print(f"Result: {result}")

# 9.

from c import *
from d import *

result = common_function()
print(result)

result_c = unique_function_c()
result_d = unique_function_d()
print(result_c)
print(result_d)

# 10.

x = 10
def foo():
    print(x)
    x += 1
foo()

# 11.

odd = lambda x : bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        del numbers[i]

# 12.

def func_x(param):
    if param:
        return 200, {"message": f"{param}"}
    else:
        return 400, "A useful error message"

# 13. 
try:
    item = dictionary["key"]
except KeyError:
    item = ""

# 14.

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def generate_report(self):
        # Formatting the report content
        formatted_content = f"Title: {self.title}\nContent: {self.content}\n"
        
        # Saving the report to a text file
        with open('report.txt', 'w') as f:
            f.write(formatted_content)
        
        # Printing the report to the console
        print(formatted_content)
        
        # Sending the report by email (Simulated)
        print(f"Sending Email...\nTo: admin@example.com\nSubject: {self.title}\nBody: {self.content}")
        

# Create a report
report = Report("Monthly Sales", "The sales of this month increased by 20%.")
report.generate_report()

# 15.
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Developer:
    def __init__(self, experience: float, github_link: str) -> None:
        self._experience = experience
        self._github_link = github_link

    @property
    def experience(self) -> float:
        return self._experience

    @property
    def github_link(self) -> str:
        return self._github_link


@dataclass
class Manager:
    def __init__(self, experience: float, github_link: str) -> None:
        self._experience = experience
        self._github_link = github_link

    @property
    def experience(self) -> float:
        return self._experience

    @property
    def github_link(self) -> str:
        return self._github_link


def get_developer_list(developers: List[Developer]) -> List[Dict]:
    developers_list = []
    for developer in developers:
        developers_list.append({
            'experience': developer.experience,
            'github_link': developer.github_link
        })
    return developers_list


def get_manager_list(managers: List[Manager]) -> List[Dict]:
    managers_list = []
    for manager in managers:
        managers_list.append({
            'experience': manager.experience,
            'github_link': manager.github_link
        })
    return managers_list


## create list objects of developers
company_developers = [
    Developer(experience=2.5, github_link='https://github.com/1'),
    Developer(experience=1.5, github_link='https://github.com/2')
]
company_developers_list = get_developer_list(developers=company_developers)

## create list objects of managers
company_managers = [
    Manager(experience=4.5, github_link='https://github.com/3'),
    Manager(experience=5.7, github_link='https://github.com/4')
]
company_managers_list = get_manager_list(managers=company_managers)

# 16.

# Low-level class
class MySQLDatabase:
    def fetch_data(self):
        return "data from MySQL"

# Low-level class
class MongoDB:
    def get_data(self):
        return "data from MongoDB"

# High-level class
class ReportGenerator:
    def __init__(self, db_type):
        if db_type == 'MySQL':
            self.db = MySQLDatabase()
        elif db_type == 'MongoDB':
            self.db = MongoDB()

    def generate(self):
        if isinstance(self.db, MySQLDatabase):
            data = self.db.fetch_data()
        elif isinstance(self.db, MongoDB):
            data = self.db.get_data()
        return f"Generated report with {data}"

# Usage
report1 = ReportGenerator('MySQL')
print(report1.generate())  # Output: "Generated report with data from MySQL"

report2 = ReportGenerator('MongoDB')
print(report2.generate())  # Output: "Generated report with data from MongoDB"

# 17.

from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Person

class CreatePersonView(APIView):
    def post(self, request):
        name = request.data['name']
        age = request.data['age']
        Person.objects.create(name=name, age=age)
        return Response({"status": "Person created"})

# 18.

from django.db import connection

def get_books():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM myapp_book")
        books = cursor.fetchall()
    return books

# 19.

from django.urls import path
from . import views

urlpatterns = [
    path('getBooks/', views.BookListView.as_view(), name='get-books'),
    path('CreateAuthor/', views.AuthorCreateView.as_view(), name='create-author'),
    path('Delete_Book/<int:pk>/', views.BookDeleteView.as_view(), name='delete-book'),
]

# 20.

class DeleteUserView(APIView):
    def get(self, request, pk):
        User.objects.filter(pk=pk).delete()

# 21.

def create_user(request):
    User.objects.create(...)
    return Response({"message": "User created"}, status=200) 


