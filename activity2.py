class student:
    grade = 6
    name = "Aprameya Das"
    def introduction(self):
        print("hi I am a student")
    def details(self):
        print("my name is", self.name)
        print("I study in grade", self.grade)
ob = student()
ob.introduction()
ob.details