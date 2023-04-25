'''
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
'''

#function with two parameters
def foo1(name1, name2):
    print(name1, name2)

#function with three parameters
def foo2(name1, name2, name3):
    print(name1, name2, name3)

#function with one parameter, and one default parameter
#non-default arguments cannot appear after default arguments
def foo3(name1, name2='Dragonite'):
    print(name1, name2)

#function with non-keyword arguments
#args will be tuple
def foo4(*args):
    print(args)

#function with keyword arguments
#kwargs will be dict
def foo5(**kwargs):
    print(kwargs)


#call with positional arguments
foo1('Jigglypuff','Dragonite')

#call with keyword arguments
foo2(name2='Ditto', name3='Jigglypuff', name1='Lapras')

#call with mixing positional arguments & keyword arguments
#positional arguments cannot appear after keyword arguments
foo2('Ditto', name3='Lapras', name2='Mew')

#call with only one argument
foo3('Jigglypuff')

#call with arbitrary number of arguments
foo4('Mew', 'Ditto', 'Lapras', ('Plusle','Minun'))

#call with arbitrary number of arguments, each argument's types are key=value
foo5(name1='Mew', name2='Ditto', name3='Lapras', name4='Snorlax')
