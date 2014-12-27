#### OUTPUT START ####
n = raw_input("Enter the number n: ")
a,b=0,1
while 1:
    a,b=b,a+b
    print (a)
    if b > int(n):
        break
#### OUTPUT END ####    
