
import math
def find_roots(a,b,c): 
    D = (b ** 2) - (4 * a * c) #discriminant
    
    if D<0:
         x1 = x2 = round( (-b / (2 * a)),4)
         imaginary = round((math.sqrt(-D) / (2 * a)),4)
         print("The roots are imaginary:", x1 ,"+", imaginary,"i", ",", x2, "-", imaginary,"i")
         
    elif D==0:
         x = round((-b / (2 * a)),4)
         print("There is a single root:", x)
         
    elif D>0:
        x1 = round(((-b + math.sqrt(D)) / (2 * a)),4)
        x2 = round(((-b - math.sqrt(D)) / (2 * a)),4)
        print("The roots are real:", x1 , "," , x2)
    

try:
    while True:
        inp = [int(x) for x in input("Enter coefficients:").split(',')] 
        if len(inp) != 3:
            print("You must enter three coeffients.")
            
        elif inp[0]==0:
            print("Not a quadratic polynomial.")
            
        else:
            k=inp[0] 
            l=inp[1] 
            m=inp[2]
            find_roots(k,l,m)       
except KeyboardInterrupt:
    pass


