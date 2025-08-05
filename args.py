

def greet (*args):
    for arg in args:
        print("Hello", arg)

greet ("Jerry", "John", "Jane")


def sum (*args):
    total = 0
    for arg in args:
        total += arg
    return total

result = sum (1,2,3,4,5)
print (result)

def sum (*args):
    ans=0
    for arg in args:
        # print (f"{ans}={ans}+{n}")
        print ("ans=", ans)
        ans= ans + arg
    return ans   
sum (50, 100, 150, 200, 250)    