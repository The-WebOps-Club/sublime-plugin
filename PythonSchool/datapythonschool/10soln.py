n = raw_input()
a,b=0,1
while 1:
    a,b=b,a+b
    print (a)
    if b > int(n):
        break
    
