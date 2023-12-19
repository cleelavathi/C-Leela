#lambda
def f(x):
    print(x-6)
f(8)
g = lambda x,y:x+y
print(g(3,4))

l=lambda x,y:x*y
print(l(2,8))
#filter
#map

my_list = [1,5,4,6,8,11,3,12]

new_list =tuple(filter(lambda x:(x%2==0),my_list))
print(new_list)

ls = ['hello','ratan','anu','durga']

ss = list(filter(lambda x:'hello' in x,ls ))
print(ss)
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l1 = list(filter(isEven,my_list))
print(l1)
m1=[2,3,4,5,6]
mm=list(filter(lambda x:x**2==6 in x,m1))
print(mm)

def doubleIt(l):
    for i in l:
     print(i*2)
l = [2,4,6,8]
doubleIt(l)
def term(t):
    for i in t:
        print(i-2)
t=[2,3,4,5,6,7]
term(t)
def m1(x):
    return 2*x
ll = list(map(m1,l))
print(ll)
l2=[2,3,8,9]
l0 = list(map(lambda x:x*2,l2))
print(l0)

ls2 = ['raju','anusha','damu']
ls4 = list(map(lambda x:x + "it",ls2))
print(ls4)
ls6 = [9,8,7]
ls7 = list(map(lambda x:x + 4,ls6))
print(ls7)
l6 = [9,8,7]
l7 = list(filter(lambda x:x + 4,l6))
print(l7)
l6 = [9,8,7]
l7 = list(filter(lambda x:x%3,l6))
print(l7)
l6 = [9,8,7,4]
l7 = list(filter(lambda x:x%2==0,l6))
print(l7)








