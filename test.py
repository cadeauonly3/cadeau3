class Myworker:
    name="IRASUBIZA Jean Cadeau"
    def set_marks(self):
       self.__marks=int(input("Enter marks"))
       if __marks>=0 and __marks<=100:
          self.__marks=__marks
       else:
           print("Please enter valid message")
    def get_marks(self):
        print(self.__marks)


obj=Myworker()
obj.get_marks()
print("Names: ",obj.name)
