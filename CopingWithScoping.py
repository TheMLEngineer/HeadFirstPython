name = "KK"
def func():
    print(name)
    name = name + ' is a great Book!'
    print(name)

func()
print(name)

'''
It gives , 
UnboundLocalError: local variable 'name' referenced before assignment
coz , in python we can access the global variable but we can't change it.
in this code it looks for a local variable 'name'
it dosen't find it so it throws UnboundLocalError.

'''
