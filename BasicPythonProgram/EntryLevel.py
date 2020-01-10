# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:59:54 2019

@author: rgupta4
"""
#This is if condition
class ParentClass():
   def __init__(self, Name, Class):
       self.StudentName = Name
       self.StudentClass = Class
       print('I m Parent')
       
   def PrintModel(self):
      print('Student Name is :'+ self.StudentName+ ' and class is :'+ self.StudentClass )


class ChildClass(ParentClass):
    def __init__(selfi, Namee, Classs):
        ParentClass.__init__(selfi, Namee, Classs)
        print('I m child')
    
    def ChildClass(selfi):
        print('constructor')

    def PrintChildModel(selfi):
        print(selfi.StudentName)

x = ChildClass("Kamal", "12th")
x.PrintModel()
x.PrintChildModel()
x.ChildClass()