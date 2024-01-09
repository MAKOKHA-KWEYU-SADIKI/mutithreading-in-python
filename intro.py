#print("hello welcome back")
import threading
import time
numb=[1,2,3,4,5,6,7,8]
def cal_sqr(numb):
    for num in numb:
       print(num,":",num**2)
       time.sleep(0.0001)
def cal_cube(numb):
    for num in numb:
       print(num,":",num**3)    
       time.sleep(0.0001)
t1=threading.Thread(target=cal_sqr,args=(numb,))
t2=threading.Thread(target=cal_cube,args=(numb,))
t1.start()
time.sleep(0)
t2.start()
t1.join()
t2.join()
#time.sleep(1)
