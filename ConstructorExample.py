class Student:
    """
    here __init__ is called as constructor, 
    It will be called automatically when the object of this class is created
    """
    def __init__(self, name, rollno):
        self.studentName = name
        self.studentNo = rollno
        print("Contructor called")

    # Here self represent the current class's instance
    def printStudentDetails(self):
        print(f"Hello {self.studentName}, your roll no is {self.studentNo}")


obj = Student("Jayesh", 1)
obj1 = Student("Adi", 2)

obj.printStudentDetails()
obj1.printStudentDetails()

# print(obj.__doc__)
