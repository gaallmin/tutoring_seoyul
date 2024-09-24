# Student 클래스 정의

    # 학생 속성을 초기화 : name, age, grade를 입력값으로 받고 속성으로 저장하자
    def               :
        self.name =   # 학생 이름 속성
        self.age =    # 학생 나이 속성
        self.grade =   # 학생 성적 속성

    # 학생의 성적을 반환하는 메소드
    def get_grade(self):
        return self.grade

    # 학생의 설명을 반환하는 메소드
    def describe(self):
        return f"학생 이름: {self.name}, 나이: {self.age}, 성적: {self.grade}"

    # 학생의 성적을 업데이트하는 메소드
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}의 성적이 {self.grade}(으)로 업데이트되었습니다.")

# Student 클래스의 인스턴스 생성
student1 
student2


# describe method 사용
print(student1.describe())  # student1의 세부 정보를 출력
print(student2.describe())  # student2의 세부 정보를 출력

# 성적을 확인하는 method사용
print(f"{student1.name}의 성적은: {student1.get_grade()}")
print(f"{student2.name}의 성적은: {student2.get_grade()}")

# 학생의 성적 업데이트
student1                   # a+로 업데이트 해보자
student2                   # a로 업데이트 해보자

# 업데이트된 성적 확인
print()  # 업데이트된 student1의 세부 정보를 출력
print()  # 업데이트된 student2의 세부 정보를 출력
