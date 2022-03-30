
#import sympy
from sympy import Symbol
from sympy import factor
x= Symbol('x')
#let the given polynomial be exp

exp = x*x*x+x*x-4*x-4
#for checking exp(a) is 0  or not by substituting
res_exp = exp.subs(x,2)
if res_exp==0:
    
   print("x-2 is a factor of exp")
   
else :

   print("x-2 is not a factor of exp")
   
#for further factorising the expression
print(factor(exp))