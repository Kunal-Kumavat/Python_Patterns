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