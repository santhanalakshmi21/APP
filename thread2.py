# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:55:23 2020

@author: Admin
"""

from threading import Thread,current_thread
class mythread(Thread):
    def run(self):
        for x in range(7):
            print("Hi from child")
a = mythread()
a.start()
a.join()
for i in range(10):
    print(i)
print("Bye from",current_thread().getName())
