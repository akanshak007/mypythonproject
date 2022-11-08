from myfunction_dir import add_Num, sub_Num, prod_Num 
import startMath

def coh():
    print (" choiceofMath.py :Choose your math program")
    d1a = input("Do you want : \n A) Addition of 2 numbers . B) Substraction of 2 numbers. C) Product of 2 numbers [A/B/C]? : ")
    if d1a == "A":
        sum = add_Num.plus_Num()
        print ("Your sum is ", sum)
    elif d1a == "B":
        diff = sub_Num.diff_Num()
        print ("Your difference is", diff)
    elif d1a == "C":
        prod = prod_Num.multiply_Num()
        print ("Your product is", prod)

# ch= input ("Do you want to repeat this program [Y/N]\n: ")
# if ch=='Y' or ch=='y':
#     startMath.sm()
# else:
#     print ("Goodbye!")



