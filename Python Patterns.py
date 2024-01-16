# *  
# * *  
# * * *  
# * * * *  
# * * * * *
def pattern(height):
    for i in range(height+1):
        for k in range(1,i+1):
            print("*",end=" ")
        print(" ")
    
height = int(input("Enter pattern height :: "))
pattern(height)



# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5
def pattern(height):
    for i in range(height+1):
        for k in range(1,i+1):
            print(k,end=" ")
        print(" ")
    
height = int(input("Enter pattern height :: "))
pattern(height)



# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5
def pattern(height):
    for i in range(height+1):
        print("#", end=" ")
        for k in range(1,i+1):
            print(i,end=" ")
        print(" ")
    
height = int(input("Enter pattern height :: "))
pattern(height)



# *****
# ****
# ***
# **
# *
def pattern(height):
    for i in range(height,0,-1):
        print("*"*i)
    
height = int(input("Enter pattern height :: "))
pattern(height)



# 55555
# 4444
# 333
# 22
# 1
def pattern(height):
    a = height
    for i in range(height,0,-1):
        print(str(a)*i)
        a -= 1

height = int(input("Enter pattern height :: "))
pattern(height)



# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
def pattern(height):
    a = height
    for i in range(height,0,-1):
        for k in range(1,i+1):
            print(k,end=" ")
        print("")

height = int(input("Enter pattern height :: "))
pattern(height)



# 1  
# 2 1  
# 3 2 1  
# 4 3 2 1  
# 5 4 3 2 1
def pattern(height):
    for i in range(1,height+1):
        for k in range(i,0,-1):
            print(k,end=' ')
        print(' ')
    
height = int(input("Enter pattern height :: "))
pattern(height)



# 0 1 2 3 4 5  
# 0 1 2 3 4  
# 0 1 2 3  
# 0 1 2  
# 0 1
def pattern(height):
    for i in range(height,0,-1):
        for k in range(0,i+1):
            print(k,end=' ')
        print(' ')
    
height = int(input("Enter pattern height :: "))
pattern(height)



# 10  
# 10 8  
# 10 8 6  
# 10 8 6 4  
# 10 8 6 4 2
def pattern(height):
    for i in range(1,height+1):
        a = 10
        b = 0
        for k in range(i):
            print((k+a)-b,end=' ')
            b += 3
        print(' ')

height = int(input("Enter pattern height :: "))
pattern(height)