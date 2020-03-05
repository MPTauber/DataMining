remainder = lambda num: num % 2 ## remaineder expects one argument (num) and does the calculation

print(remainder(5))


# Multiple arugments:
product = lambda x,y: x * y

print(product(2,3))

######################################################################################################################################################
# Taking argument and multiply by unknown number:
def testfunc(num):
    return lambda x: x * num ## do know that we want to set value at some point, so add "num" instead of hardcoding "10"

result1 = testfunc(10) ## 10 becomes "num"...
print(result1(9)) ## ... and 9 becomes "x"

result2 = testfunc(1000)
print(result2(9))
####################################### this would be useful with, for example, tax rates. So instead of result1 we might call it Florida and 
####################################### pass the tax rate 14% ---> Florida = testfunc(.14)
######################################################################################################################################################

## Another example:
def myfunc(n):
    return lambda a: a * n 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
######################################################################################################################################################

## Create lambda function to filter through a list:
num_list = [2,6,8,10,11,4,12,7,13,0,21]

filtered_list = list(filter(lambda num: (num > 7), num_list))
print(filtered_list)

######################################################################################################################################################

## Get even and uneven with remainders:
mapped_list = list(map(lambda num: num % 2, num_list))
print(mapped_list)
