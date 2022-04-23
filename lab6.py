#question1
mylist = []
def funct(n):
    while n != 0:
        function = (n - 3) / (n * n)
        lam = lambda a: function * a
        mylist.append(lam(1))
        n -= 1
    return lam


usernum = int(input("enter how many numbers you want to add\n"))
funct(usernum)(1)  # n=5  a=1

print("summation of the elements using sum() is ", sum(mylist))

summation = 0
for i in mylist:
    summation = summation + i

print("summation of the elements using loop is ", summation)



# question 2

global answer  # global variable

def func(n):
    """This function multiplies the numbers according to the given function."""
    answer = 1
    function = (n / (n + 2)) - 10
    answer *= function

    if n == 1:
        return answer

    return answer * func(n - 1)

print("")
print(func.__doc__)
print(func(3))




