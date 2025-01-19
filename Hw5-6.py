#1023
x,y = map(float,input().split())
if x<0 and y>0:
 print('Yes')
else:
 print('No')
#1024
x,y = map(int,input().split())
if x>0 and y>0:
 print(1)
elif x<0 and y>0:
 print(2)
elif x<0 and y<0:
 print(3)
elif x>0 and y<0:
 print(4)
#1025
x,y,z = map(int,input().split())
if x+y>z and y+z>x and x+z>y:
 print('Yes')
else:
 print('No')
 #1026
 a, b, c, d = map(int, input().split())
 if a < b < c < d:
     print('Yes')
 else:
     print('No')
