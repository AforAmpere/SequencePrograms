a,t,n=1,[1],0;from itertools import*
while 1:
 print(a)
 if a%4!=0 and int(str(a)[0])+a not in t:a+=int(str(a)[0])
 elif a%4==0 and a/2 not in t:a=int(a/2)
 else:a=next(filterfalse(t.__contains__,count(a)))
 t+=[a]
