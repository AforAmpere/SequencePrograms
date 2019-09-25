a,t,n=1,[1],0;from itertools import*
while n<100000:
 print(a);q=set(t)
 if a%4!=0 and((int(str(a)[0])+a)not in q):a+=int(str(a)[0])
 elif a%4==0 and a/2 not in q:a=int(a/2)
 else:a=next(filterfalse(q.__contains__,count(a)))
 t+=[a];n+= 1
