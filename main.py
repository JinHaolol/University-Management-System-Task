class Person:
    def __init__ (self,name="",age=0,gender=""):

        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def get_details(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


#Student
class Student(Person):
    def __init__(self,name="",age=0,gender="",student_id="",course=""):
        super().__init__(name,age,gender)
        self.student_id = student_id
        self.course = course
        self.grades = []

    def set_student_details(self, student_id,course):
        self.student_id = student_id
        self.course = course
        
    def add_grade(self, grade):
        self.grades.append(grade)

    def caculate_average_grade():
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def get_student_summary(self):
        average_grade = self.calculate_average_grade()
        return f"{self.get_details()}, ID: {self.student_id}, Course: {self.course}, Average Grade: {average_grade:.2f}"


   #Profressor
class Professor(Person):
    def __init__(self, name="", age=0, gender="", staff_id="", department="", salary=0.0):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def get_professor_summary(self):
        return f"{self.get_details()}, ID: {self.staff_id}, Department: {self.department}, Salary: £{self.salary:.2f}"


class Administrator(Person):
    def __init__(self, name="", age=0, gender="", admin_id="", office="", years_of_service=0):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def increment_service_years(self):
        self.years_of_service += 1

    def get_admin_summary(self):
        return f"{self.get_details()}, ID: {self.admin_id}, Office: {self.office}, Years of Service: {self.years_of_service}"


#Create Objects
student1 = Student()
student1.set_details("Alice Johnson", 20, "Female")
student1.set_student_details("S5678", "Physics")

student2 = Student()
student2.set_details("Bob Smith", 22, "Male")
student2.set_student_details("S1234", "Computer Science")

professor1 = Professor()
professor1.set_details("Dr. Smith", 45, "Male")
professor1.set_professor_details("P1234", "Mathematics", 55000)

professor2 = Professor()
professor2.set_details("Dr. White", 50, "Female")
professor2.set_professor_details("P5678", "History", 62000)

administrator = Administrator()
administrator.set_details("Jane Doe", 40, "Female")
administrator.set_admin_details("A4321", "Room 12, Admin Block", 15)

student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
print(student1.get_student_summary())

# Professor's feedback
professor1.give_feedback(student1, "Great work on your assignment!")

# Increase professor salary
professor1.increase_salary(10)
print(professor1.get_professor_summary())

#years of service
administrator.increment_service_years()
print(administrator.get_admin_summary())

# Print summaries of all objects
print(student2.get_student_summary())
print(professor2.get_professor_summary())



















Khaled = Person("Khaled", "9", "Male")
Khaled.set_details("Khaled", "16", "Male")
Khaled.get_details()
    