#ıdentity Operator: is

x = y = [1,2,3]
z= [1, 2, 3]
print(x==y)
print(x==z)
print(x is y)           #True
print(x is z)           #False

x= [1, 2, 3]
y= [2, 4]
del x[2]
y[1]=1
y.reverse()
print(x==y)          #True
print(x is y)        #False
print(x is not y)    #True
#Membership Operator: in

x=['apple', 'banana']
print('banana' in x)

name='Çınar'

print('a' in name)
print('a' not in name)
