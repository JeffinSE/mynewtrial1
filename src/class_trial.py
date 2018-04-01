#! /usr/bin/python
# -*- coding: utf-8 -*-

"this is a sample of class in python"

import sys

class Student(object):
    "Student: name, sex, score"
    def __init__(self, name, sex, score):
        self.__name = name
        self.__sex = sex
        self.__score = score
        self.full = str(name) + ':' + str(self.__score)

    def register(self, school: str, date: str) -> str:
        "this is docString sample"
        self.register_date = str(date)
        if self.__sex == "male":
            hisorher = "his"
        elif self.__sex == "female":
            hisorher = "her"
        else:
            hisorher = "his"
        print(self.__name + "'s " + "register date is " + self.register_date)
        print("and %s school is %s, %s score is %s." % (hisorher, school, hisorher, self.__score))


def main():
    try:
        s1 = Student(arg*, "male", 98)
        s1.register('HUST', 19970901)
        s2 = Student("Kevin", 'male', 95)
        s2.register('Hammarby', 20160820)
        s3 = Student('Linda', 'female', 96)
        s3.register('FAF', 20170820)
        return 0
    except:
        return 1

if __name__ == "__main__":
    sys.exit(main())

print(__doc__)
print(Student.__doc__)
print(Student.register.__doc__)       # sample print