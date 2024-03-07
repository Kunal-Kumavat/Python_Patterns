# *  
# * *  
# * * *  
# * * * *  
# * * * * *
def pattern(height):
    for i in range(1,height+1):
        print("* "*i)  
        
height = int(input('Enter Pattern Height :: '))
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



# 5 4 3 2 1  
# 4 3 2 1  
# 3 2 1  
# 2 1  
# 1
def pattern(height):
    for i in range(height,0,-1):
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



# 10 8 6 4 2  
# 10 8 6 4  
# 10 8 6  
# 10 8  
# 10
def pattern(height):
    a = 0
    for i in range(height,0,-1):
        for k in range(i,0,-1):
            print((k+a)*2,end=' ')
        a += 1
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



# 5 4 3 2 1  
# 5 4 3 2  
# 5 4 3  
# 5 4  
# 5
def pattern(height):
    a = 0
    for i in range(height,0,-1):
        for k in range(i,0,-1):
            print(k+a,end=' ')
        a+=1
        print(' ')

height = int(input("Enter pattern height :: "))
pattern(height)



# 1 
# 1 2 
# 1 2 4 
# 1 2 4 8 
# 1 2 4 8 16 
def pattern(height):
    for i in range(1,height+1):
        for k in range(i):
            print(2**k,end=' ')
        print("")
        
height = int(input("Enter pattern height :: "))
pattern(height)



# 1  
# 2 1  
# 4 2 1  
# 8 4 2 1  
# 16 8 4 2 1  
def pattern(height):
    for i in range(height):
        for k in range(i,-1,-1):
            print(2**k,end=' ')
        print(" ")
        
height = int(input("Enter pattern height :: "))
pattern(height)



# 1  
# 1 2 1  
# 1 2 4 2 1  
# 1 2 4 8 4 2 1  
# 1 2 4 8 16 8 4 2 1
def pattern(height):
    for i in range(height):
        for k in range(i+1):
            print(2**k,end=' ')
        for j in range(i-1,-1,-1):
            print(2**j,end=' ')
        print(" ")
        
height = int(input("Enter pattern height :: "))
pattern(height)



# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10 
def pattern(height):
    a = 0
    for i in range(1,height+1):
        for k in range(i):
            a +=1
            print(a,end=' ')
        print(' ')
 
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 1
# 3 2 
# 6 5 4 
# 10 9 8 7 
def pattern(height):
    a = 1
    for i in range(1, height+1):
        for k in range(1,i+1):
            print(a,end=' ')
            a -=1
        a += 1+(2*i)
        print(' ')

height = int(input('Enter Pattern Height :: '))
pattern(height)



# 1  
# 2 3 4  
# 5 6 7 8 9
def pattern(height):
    a = 1
    b = 1
    for i in range(1,height+1):
        for k in range(b):
            print(a,end=' ')
            a += 1
        b += 2
        print(' ')
        
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 1  
# 2 4  
# 3 6 9  
# 4 8 12 16  
# 5 10 15 20 25
def pattern(height):
    a = 1
    for i in range(1, height+1):
        for k in range(1,i+1):
            print(a*k,end=' ')
        a += 1
        print(' ')
    
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 0  
# 0 1  
# 0 2 4  
# 0 3 6 9  
# 0 4 8 12 16  
# 0 5 10 15 20 25
def pattern(height):
    a = 0
    for i in range(1, height+1):
        for k in range(i):
            print(a*k,end=' ')
        a += 1
        print(' ')
    
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 1 2 3 4 5
# 2 3 4 5
# 3 4 5 
# 4 5 
# 5
def pattern(height):
    a = 0
    for i in range(height,0,-1):
        for k in range(1,i + 1):
            print(k+a,end=' ')
        a += 1
        print(' ')
        
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 1  
# 3 3 3  
# 5 5 5 5 5  
# 7 7 7 7 7 7 7  
# 9 9 9 9 9 9 9 9 9
def pattern(height):
    for i in range(1,height*2,2):
        for k in range(1,i+1):
            print(i,end=' ')
        print(' ')
        
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 12345 
# 22345 
# 33345 
# 44445 
# 55555 
def pattern(height):
    for i in range(1, height+1):
        print(str(i)*i,end='')
        for j in range(1+i,height+1):
            print(j, end='')
        print(' ')
        
height = int(input('Enter Pattern Height :: '))
pattern(height)



# 5 4 3 2 1 1 2 3 4 5  
# 4 3 2 1     1 2 3 4  
# 3 2 1         1 2 3  
# 2 1             1 2  
# 1                 1
def pattern(height):
    a = 0
    for i in range(height,0,-1):
        for k in range(i,0,-1):
            print(k, end=' ')
        print(' '*a,end='')
        for j in range(1,i+1):
            print(j,end=' ')
        a += 4
        print(' ')
height = int(input('Enter Pattern Height :: '))
pattern(height)



#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      *
def pattern(height):
    for i in range(height,0,-1):
        print (' '*(height-i)+'* '*i)
    
height = int(input('Enter Pattern Height :: '))
pattern(height)



#  * 
#  * * 
#  * * * 
#  * * * * 
#  * * * * * 
#  * * * * 
#  * * * 
#  * * 
#  *
def pattern(width):
    for i in range(1,width):
        print("* "*i)
    for k in range(width,0,-1):
        print("* "*k)
    print("")
    
width = int(input("Enter Pattern Width :: "))
pattern(width)



#          * 
#        * * 
#      * * * 
#    * * * * 
#  * * * * *
def pattern(height):
    for i in range(1,height+1):
        #print("  "*(height-i),"* "*i) #Passing Double "   " white_spaces
        print(" "*((height-i)*2),"* "*i) #Passing Single " " white space
        
height = int(input("Enter Pattern Height :: "))
pattern(height)



#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * *
def pattern(height):
    for i in range(1,height+1):
        print(" "*(height-i),"* "*i)

height = int(input("Enter Pattern Height :: "))
pattern(height)



# * 
# * * 
# * * * 
# * * * * 
# 
# * * * * 
# * * * 
# * * 
# *
def pattern(width):
    for i in range(1,width+1):
        print("* "*i)
    print(" ")
    for i in range(width,0,-1):
        print("* "*i)

pattern(int(input("Enter Pattern Width :: ")))



#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 
def pattern(size):
    for i in range(1,size):
        print(" "*(size-i),"* "*i)
    for i in range(size,0,-1):
        print(" "*(size-i),"* "*i)
    
pattern(int(input("Enter Pattern Size :: ")))



#  ***** - *****
#  **** --- ****
#  *** ----- ***
#  ** ------- **
#  * --------- *
def pattern(height):
    a = 1
    for i in range(height,0,-1):
        print("*"*i,"-"*a,"*"*i)
        a += 2
        
pattern(int(input("Enter Pattern Height :: ")))



# 1 * 2 * 3 * 4 * 5 
# 1 * 2 * 3 * 4 
# 1 * 2 * 3 
# 1 * 2 
# 1
def pattern(height):
    a = 1
    for i in range(height,0,-1):
        print(a,end=" ")
        for k in range(2 ,i+1):
            print("*",k,end=' ')
        print('')
            
pattern(int(input("Enter Pattern Height :: ")))



#  P
#  Py
#  Pyt
#  Pyth
#  Pytho
#  Python
def pattern(word):
    for i in range(1,len(word)+1):
        print(word[0:i])

pattern(str(input("Enter Word :: ")))



# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# P Q R S T U 
# V W X Y Z [ \
asciiNumber = 65
def pattern(height):
    global asciiNumber
    for i in range(1,height+1):
        for k in range(1,i+1):
            print(chr(asciiNumber),end=' ')
            asciiNumber += 1
        print('')
    
height = int(input("Enter Pattern Height :: "))
pattern(height)



# A B C D E F G 
# H I J K L M 
# N O P Q R 
# S T U V 
# W X Y 
# Z [ 
# \
def pattern(height):
    asciiNumber = 65
    for i in range(height,0,-1):
        for k in range(1,i):
            print(chr(asciiNumber),end=' ')
            asciiNumber += 1
        print("")
        
height = int(input("Enter Pattern Height :: "))
pattern(height)