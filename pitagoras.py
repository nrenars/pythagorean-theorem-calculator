import math

def pitagors(x,y):
    return x * x + y * y

def drawing():
    print("""
                        *       calculate:
                      * *       c = ?
            c      *    *    
                *       *   a
             *          *   
          *             *      
       *                *   
    ********************* 
               b
    """)


while True:
    drawing()
    print('\nType 0 to exit')
    a = int(input('Whats the value of a? '))
    if a == 0:
        break
    b = int(input('Whats the value of b? '))
    if b == 0:
        break

    c = pitagors(a,b)
    answer = math.sqrt(c)
    print(f'\nThe value of c is: {int(answer)}')
