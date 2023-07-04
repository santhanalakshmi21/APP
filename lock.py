import threading 
import time
import random
bal = 1000
_lock = threading.Lock()
 
def deposit(amt):
    #_lock.acquire()
    global bal
    #time.sleep(10)
    bal +=amt
    print("dep:",bal)
    #_lock.release()
    #time.sleep(random.randint(0, 1))
    
def withdrawl(amt):
   #_lock.acquire()
    global bal
    #time.sleep(10)
    bal -=amt
    print("withdrawal",bal)
    #_lock.release()
    #print(bal)

def main_task(): 
    global bal 
    #bal = 0
    t1 = threading.Thread(target=deposit,args=(5000,)) 
    t2 = threading.Thread(target=withdrawl,args=(1500,)) 
    t3 = threading.Thread(target=deposit,args=(4000,)) 
    t4 = threading.Thread(target=withdrawl,args=(7000,)) 
    t5 = threading.Thread(target=deposit,args=(4000,)) 
    # start threads 
    t1.start() 
    t2.start() 
    t3.start()
    t4.start() 
    t5.start()
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
    #print(bal)

main_task() 
        #print("Iteration {0}: Bal = {1}".format(i,bal)) 
