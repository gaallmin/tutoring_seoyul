class Student:
    
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age    
        self.grade = grade 

    # 학생의 성적을 얻는 method
    def get_grade(self):
        return self.grade

    # 학생의 신상을 나타내는 method
    def describe(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    # 학생의 점수 업데이트
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to: {self.grade}")

# object / instance 만들기
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B")


print(student1.describe()) 
print(student2.describe())  

# Calling a method to get the student's grade
print(f"{student1.name}'s grade is: {student1.get_grade()}")
print(f"{student2.name}'s grade is: {student2.get_grade()}")


student1.update_grade("A+")
student2.update_grade("A")


print(student1.describe())  
print(student2.describe())  
