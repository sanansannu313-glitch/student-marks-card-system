class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age

class School(Person):
    def __init__(self,name,age,id,marks):
        super().__init__(name,age)
        self.id = id
        self._marks = marks


    def display(self):
        print(f"name:{self.name}\n age:{self._age}\n id:{self.id}\n marks:{self._marks}\n")

    def search_student(self,name_to_find):
        for student in students:
            if student.name == name_to_find:
                student.display()
                break
        else:
            print("Name of your student its not exceeds")
    def set_marks(self,new_marks):
        if new_marks >100 or new_marks <0:
            print("Marks cannot be more than 100 and less than 0")
        else:
            self._marks = new_marks
    def set_age(self,new_age):
        if new_age > 20 or new_age <0:
            print("Age cannot be more than 100 and less than 0")
        else:
            self._age = new_age


student_1 = School(name="Sanan",age=17,id=1,marks=100)
student_2 = School(name="Anand",age=17,id=2,marks=95)
student_3 = School(name="Kumar",age=16,id=3,marks=75)
student_4 = School(name="Antony",age=16,id=4,marks=70)
student_5 = School(name="Geetha",age=16,id=5,marks=93)
students = [student_1,student_2,student_3,student_4,student_5]

student_1.search_student(input("Enter student name: "))
student_2.set_marks(int(input("Enter marks: ")))
student_2.display()
















