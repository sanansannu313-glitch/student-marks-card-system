class School:
    def __init__(self,name,age,id,marks):
        self.name = name
        self.age = age
        self.id = id
        self.marks = marks
    def display(self):
        print(f"name:{self.name}\n age:{self.age}\n id:{self.id}\n marks:{self.marks}\n")

    def search_student(name_to_find):
        for student in students:
            if student.name == name_to_find:
                student.display()

student_1 = School(name="Sanan",age=17,id=1,marks=100)
student_2 = School(name="Anand",age=17,id=2,marks=95)
student_3 = School(name="Kumar",age=16,id=3,marks=75)
student_4 = School(name="Antony",age=16,id=4,marks=70)
student_5 = School(name="Geetha",age=16,id=5,marks=93)
students = [student_1,student_2,student_3,student_4,student_5]
for student in students:
    student.display()

students.search_student(input("Enter student name: "))







