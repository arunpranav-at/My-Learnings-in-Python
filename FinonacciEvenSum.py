nooftestcases=int(input("ENTER NUMBER OF TEST CASES (1-n): "))
list1=[]
for i in range(0, nooftestcases):
    testval=int(input("ENTER TEST VALUE: "))
    list1.append(testval)
fibolist=[0,1]
maxelement=max(list1) #finding the end range for fibonacci series
while fibolist[-1]<=maxelement:
    fibolist.append(fibolist[-1]+fibolist[-2])
for k in list1:
    if k<0:
        print(0)
    else:
        sum1=0
        for j in fibolist:
            if j<=k and j%2==0:
                sum1+=j
        print(sum1)
            
    
