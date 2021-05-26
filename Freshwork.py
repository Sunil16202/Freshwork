import threading 
from threading import*
import time
#data storage
d={}
def find_sum():
    return 10

def dev():
    return 100


def create(key,value,timeout=0):
    if key in d:
        print("Error: key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Error: Memory limit exceeded")
        else:
            print("Error: Invalid key")

            
def read(key):
    if key not in d:
        print("Error: Key doesn't exist")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error: Key Expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in d:
        print("Error: Key not found")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del d[key]
                print("key Deleted")
            else:
                print("Error: Key Expired")
        else:
            del d[key]
            print("Key Deleted")

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: Key doesn't Exists")
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: Key Expired")
    else:
        if key not in d:
            print("Error: Key doesn't Exists")
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l

create("Pink",111)
create("Nick",101,4000)
read("Pink")
read("Nick")
create("Pink",11)
modify("Pink",66)
delete("Pink")

#We can use the multiple threading like this to ensure the single process usage

# thread1=Thread(target=(create),args=("Pink",11,timeout)) 
# thread1.start()
# thread1.sleep()

# thread2 = Thread(target=(create or read or delete),args=("Pink",value,timeout))
# thread2.start()
# thread2.sleep()
