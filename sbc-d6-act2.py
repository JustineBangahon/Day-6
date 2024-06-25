r = int(input("Enter Number of Row: "))
c = int(input("Enter Number of Column: "))
cs = 0
while cs < c:
    rs = 0 #1,2,3,4
    while rs < r:
        if rs == 0 or rs == r - 1 or cs == 0 or cs == c -1:
            print("*", end="") 
        else:
            print(" ", end="")
        rs += 1
    print()
    cs += 1
    
    # ****

