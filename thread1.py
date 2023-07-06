# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:44:38 2020

@author: Admin
"""

#from threading import *
from threading import Thread,current_thread
print(current_thread().getName())
def mt():
    print("Child Thread")
    for i in range(11,20):
            print(i*2)
def disp():
   for i in range(10):
            print(i*2)	
child=Thread(target=mt)
child.start()
disp()
print("Executing thread name :",current_thread().getName())
