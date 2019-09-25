a,qtotal,n=1,{1},0;import time;start=time.time()
from itertools import*
while n < 100000000:
        #print(a)
        #qtotal = set(total)
        if a%4 != 0 and ((int(str(a)[0])+a) not in qtotal):
                a = a + int(str(a)[0])
        elif a%4 == 0 and a/2 not in qtotal:
                a = int(a/2)
        else:
                a = next(filterfalse(qtotal.__contains__, count(a)))
        n+=1;qtotal.add(a)
        if n%200000 == 0:
                print ("At ",n)
                print ("Total time: ",str(time.time()-start)[:5])
                print ("Rate: ",str(int(float(n)/(time.time()-start))))
for a in range(1,60000000):
        if a not in qtotal:
               print (a)
