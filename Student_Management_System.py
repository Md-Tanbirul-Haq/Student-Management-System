class StudentDatabase:
    student_list=[]
    def add_student(self,student_):
        self.student_list.append(student_)

class Student:
    def __init__(self,student_id,name,department,is_enrolled):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=is_enrolled
    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_department(self):
        return self.__department
    
    def get_is_enrolled(self):
        return self.__is_enrolled
    
    def enroll_student(self,is_enrolled_):
        if is_enrolled_==False:
            self.__is_enrolled=True
    def drop_student(self,is_enrolled_):
        if is_enrolled_==True:
            self.__is_enrolled=False

        
    def __repr__(self):
        return f'\n Student_id : {self.__student_id} Name : {self.__name} Department : {self.__department} is_enrolled : {self.__is_enrolled}'
database= StudentDatabase()
student_1 = Student(1,"student_name_1","department_1",False)
student_2 = Student(2,"student_name_2","department_2",False)
student_3 = Student(3,"student_name_3","department_3",False)
database.add_student(student_1)
database.add_student(student_2)
database.add_student(student_3)

def menu():
    print()
    print("------ Student Management System ------ ")
    print('''
Select options:
1. View All Students
2. Enroll Student
3. Drop Student
4. Exit
          
''')
    print("\nEnter your choice : ",end="")
    a = int(input())
    if a==1:
        for i in database.student_list:
            print(i)
    elif a==2:
        print("\nEnter student id : ",end="")
        b = int(input())
        for i in database.student_list:
            if i.get_student_id()==b:
                if i.get_is_enrolled()==True:
                    print(f"\nName : {i.get_name()} , student id : {i.get_student_id()} is already enrolled")
                    break
                else:
                    i.enroll_student(i.get_is_enrolled())
                    print(f"\nName : {i.get_name()} , student id : {i.get_student_id()} is enrolled")
                    break
    elif a==3 : 
        print("Enter student id : ",end="")
        c = int(input())
        for i in database.student_list:
            if i.get_student_id()==c:
                if i.get_is_enrolled()==False:
                    print(f"\nName : {i.get_name()} , student id : {i.get_student_id()} is not enrolled \n")
                    break
                else:
                    i.drop_student(i.get_is_enrolled())
                    print(f"\nName : {i.get_name()} , student id : {i.get_student_id()} is Drop \n")
                    break
                         
    elif a==4:
        exit()
    else:
        
        print("\nInvalid Input. \n")
   
    menu()
menu()