#Exercise 2: Task list manager (with separate module) 
def add_task(task_list, task): 
    task_list.append(task)

def remove_task(task_list, task): 
    if task in task_list: 
        task_list.remove(task)


#Exercise 3: Class and inheritance  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student1 = Student("Shanti", 29, "S1122")

student1.greet()
print("Student ID:", student1.student_id)

#Exercise 4: Math quiz with exception handling 

import random 

num1=random.randint(1,10)
num2=random.randint(1,10)

answer=input(f"what is {num1} + {num2}?")

try:
    if int(answer) == num1 + num2: 
        print("Correct")
    else: 
        print("Incorrect") 

except ValueError:
    print("Invalid input")
