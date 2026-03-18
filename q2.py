class Student:
    school="Lycee"
    
    def __init__(self):
        self.__marks=156
    def display(self):
        print(self.__marks)
        
obj=Student()
obj.display() 
print(obj.school)

"""I have made changes to this file"""