from threading import *
import time
from threading import *
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("good evening",end='')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args={'jyothi'})
t2=Thread(target=wish,args={'mark'})
t3=Thread(target=wish,args={'mich'})
t1.start()
t2.start()
t3.start()