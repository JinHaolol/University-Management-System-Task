class Person:
    def __init__ (self,name,age,gender):

        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def get_details(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student(Person):
    def __init__(self,name,age,gender,student_id,course,):
        super().__init__(name,age,gender)
        self.student_id = student_id
        self.course = course
        self.grades = []

    def set_student_details(self, student_id,course):
        self.student_id = student_id
        self.course = course
        
    def add_grade(self):
        self.grades.append(int(input("Add grade:")))

    def caculate_average_grade():
        if grades > 0:
            return sum(int(grades))/len(grades)
        else:
            return (0)

    def get_student_summary(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Student ID: {self.student_id}, Course {self.course}, Grades {self.grades}")





















Khaled = Person("Khaled", "9", "Male")
Khaled.set_details("Khaled", "16", "Male")
Khaled.get_details()
    