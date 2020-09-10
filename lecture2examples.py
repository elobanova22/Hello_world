#!/usr/bin/python3

# %%
'''
There are three numeric types:

integers (int)
floating point (float)
complex (complex)
Hopefully, we will not need the last one. But if you see something like 3+5j or 6-7J, you know you are looking at complex type.

Note that if you want to define a float, you have to use the dot (.), otherwise the output is an integer. For example,
'''

print(type(1))
print(type(1.))
print(type(float(1)))
print(type(int(1.)))
print(type(0))
print(type(0.))
print(type(.0))
print(type(0.0))

# %%

'''
This was extremely important in Python 2 and was the source of many inadvertent errors (try dividing 1 by 2 - you’d be surprised). With Python 3 not anymore, but the general advice of being explicit in what you mean is still there.

Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %:
'''

print(17 / 3)  # classic division returns a float

print(17 // 3)  # floor division discards the fractional part

print(17 % 3)  # the % operator returns the remainder of the division

print(5 * 3 + 2)  # result * divisor + remainder

# %%
'''
Notice one way of commenting your code: just use # after the code and before any text.

Calculating powers is done with ** operator.
'''

print(2**2)

print(3**3)

print(4**.5)

# %%

'''
Booleans
bool type is essential for any programming logic. Normally, truth and falcity are defined as True and False:
'''

# %%

x = True
print(x)
print(type(x))

y = False
print(y)
print(type(y))

# %%

'''
Additionally, all non-empty and non-zero values are interpreted by bool() function as True, while all empty and zero values are False:
'''

print(bool(1), bool(1.), bool(-.1))

print(bool(0), bool(.0), bool(None), bool(''), bool([]))

# %%

'''
Strings
Strings can be difined using both single ('...') or double quotes ("..."). Backslash can be used to escape quotes.
'''

print('spam eggs')  # single quotes

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," he said.')

print("\"Yes,\" he said.")

print('"Isn\'t," she said.')

# %%

'''
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
'''

print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote

# %%

'''
Python is very sensitive to code aesthetics (see Style Guide). In particular, you shoud restrict yourself to 79 characters in one line! Use parenthesis to break long strings:
'''

text = ('Put several strings within parentheses '
            'to have them joined together.')
print(text)

# %%

'''
Strings can be constructed using math operators and by converting numbers into strings via str() function:
'''

print(2 * 'a' + '_' + 3 * 'b' + '_' + 4 * (str(.5) + '_'))

# %%

'''
Note that Python can not convert numbers into strings automatically. Unless you use print() function or convert explicitly.:
'''

print('a' + 1) # Error

# %%

print('a' + str(1))

print('a', 1)

# %%

'''
Lists
Lists are very convenient and simplest data containers. Here is how we store a collection of numbers in a variable:
'''

a = [1, 3, 5]
print(a)

print(type(a))

# %%

'''
Lists are not restricted to be uniform in types of their elements:
'''

b = [5, 2.3, 'abc', [4, 'b'], a, print]
print(b)

# %%

'''
Lists can be modified:
'''

a[1] = 4
print(a)

# %%

'''
Lists can be merged or repeated:
'''

print(a + a)
print(3 * a)

# %%

'''
You can add one item to the end of the list inplace:
'''

a.append(7)
print(a)

# %%

'''
or add a few items:
'''

a.extend([0, 2])
print(a)

# %%

'''
Note the difference:
'''

a = [1, 3, 5]
b = [1, 3, 5]
a.append([2, 4, 6])
b.extend([2, 4, 6])
print(a)
print(b)

# %%
'''
If the end of the list is not what you want, insert the element after a specified position:
'''

a.insert(1, .5)
print(a)

# %%
'''
There are at least two methods to remove elements from a list:
'''

x = ['a', 'b', 'c', 'b']
x.remove('b')
print(x)

# %%

x.remove('b')
print(x)

# %%

x.remove('b') # Error

# %%

y = ['a', 'b', 'c', 'b']
print(y.pop())
print(y)

# %%

print(y.pop(1))
print(y)

# %%
'''
Here is how you sort a list without altering the original object, and inplace:
'''

x = ['a', 'b', 'c', 'b', 'a']
print(sorted(x))
print(x)

# %%

x.sort()
print(x)

# %%
'''
Tuples
On the first glance tuples are very similar to lists. The difference in definition is the usage of parentheses () (or even without them) instead of square brackets []:
'''

t = (12345, 54321, 'hello!')
print(t)
print(type(t))

# %%

t = 12345, 54321, 'hello!'
print(t)

# %%
'''
The main difference is that tuples are immutable (impossible to modify):
'''

t[0] = 10 # Error, similar to one we see for strings

# %%

'''
Here are the reasons you want to use tuples:

Tuples are faster than lists. If you’re defining a constant set of values
and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.
It makes your code safer if you “write-protect” data that doesn’t need to be changed.
Some tuples can be used as dictionary keys (specifically, tuples that contain immutable
values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.
'''

# %%

'''
Dictionaries
A dictionary is an unordered set of key-value pairs. There are some restrictions on what can be a key. In general, keys can not be mutable objects. Keys must be unique. Below are a few example of dictionary initialization:
'''

empty_dict = dict()
print(empty_dict)

# %%

empty_dict = {}
print(empty_dict)

print(type(empty_dict))

# %%

grades = {'Ivan': 4, 'Olga': 5}
print(grades)

# %%

grades['Petr'] = 'F'
print(grades)

# %%

print(grades['Olga'])

# %%
'''
Keys and values can be accessed separately if needed:
'''

print(grades.keys())
print(grades.values())

# %%
'''
Sets
A set is an unordered collection of unique values. A single set can contain values of any immutable datatype. Once you have two sets, you can do standard set operations like union, intersection, and set difference. Here is a brief demonstration:
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print(type(basket))

# %%

print('orange' in basket)
print('cucumber' in basket)

# %%
'''
Let’s create a second set and see what we can do with both:
'''

bag = {'banana', 'peach'}
print(basket - bag)
print(basket | bag)
print(basket & bag)
print(basket ^ bag)

'''
Indexing
Python data containers (including strings and lists) can be sliced to access their specific parts. Counting in Python starts from zero. Keep this in mind when you want to access a specific character of a string:
'''

word = 'Python'
print(word[0])  # character in position 0

print(word[5])  # character in position 5

# %%
'''
Indices may also be negative numbers, to start counting from the right:
'''

print(word[-1])  # last character

print(word[-2])  # second-to-last character

print(word[-6])

# %%

'''
Going beyond a single charcter:
'''

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)

print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

# %%
'''
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.:
'''

print(word[:2])  # character from the beginning to position 2 (excluded)

print(word[4:])  # characters from position 4 (included) to the end

print(word[-2:]) # characters from the second-last (included) to the end

# %%
'''
One could be interested only in even/odd characters in the string. In that case, we need a third index in the slice:
'''

print(word[::2])

print(word[1::2])

# %%
'''
Negative index in the third position of the slice reverses the count:
'''

print(word[::-1])

print(word[::-2])

# %%
'''
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

# %%
'''
Indexing with lists works in the same way. But on top of that, if your list contains other lists, or strings (or other iterables), then indexing becomes “layered”:
'''

x = [[1, 3, 5], ['c', 'a', 'b']]
print(x[0][1])

print(x[1][-2:])

# %%
'''
Control flow

if/elif/else
Writing conditional statements in Python is very easy. Start from if, continue with elif, and finish with else. For example,
'''

if 2**2 == 4:
    print('Should be True')

# %%
'''
Be careful to respect the indentation depth. The Ipython shell automatically increases the indentation depth after a column : sign; to decrease the indentation depth, go four spaces to the left with the Backspace key. Press the Enter key twice to leave the logical block.
'''

a = 10

if a == 1:
    print(1)
elif a == 2:
    print(2)
elif a == 3:
    print(3)
else:
    print('A lot')

# %%
'''
Besides checking for equality as in the previous examples, you can check for other statements evaluating to bool. These are comparison operators: <, >, <=, =>. Testing for equality of two objects is done with is operator:
'''

a, b = 1, 1.
print(a == b)

print(a is b)

# %%
'''
You can test whether an object belongs to a collection using in operator. Note that if a collection is of type dict, then the search is done over dictionaries:
'''

a = [1, 2, 4]
print(2 in a, 4 in a)

# %%

b = {'a': 3, 'c': 8}
print('c' in b)

# %%
'''
Loops
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
'''

for i in range(4):
    print(i)

# %%
'''
The for statement in Python differs a bit from what you may be used to in other programming languages. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as in C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
'''

words = ['cat', 'window', 'bird']
for w in words:
    print(w, len(w))

# %%
'''
Here is another example.
'''

for letter in 'Python':
    print(letter)

# %%
'''
Coming back to range() function. It can have at most three arguments, range(first, last, step). Given this knowledge we can generate various sequences. Note that this function returns neither a list not a tuple. In fact, it is an object itself. In order to check what are the indices if we use range in a for loop, we can convert it to list using list() function. The reason behind this behavior is to save memory: range does not store the whole list, only its definition.
'''

print(range(2, 10))

# %%

print(list(range(2, 10)))

print(list(range(2, 10, 3)))

print(list(range(-2, -10, -3)))

# %%
'''
If you need to break out of the loop or skip an iteration, then you need to know two statements, break and continue, respectively.
'''

a = [1, 0, 2, 4]
for element in a:
    if element == 0:
        continue
    print(1 / element)

# %%

a = [1, 0, 2, 4]
for element in a:
    if element == 0:
        break
    print(1. / element)

# %%
'''
Common use case is to iterate over items while keeping track of current index. Quick and dirty way to do this is:
'''

words = ('cool', 'powerful', 'readable')
for i in range(0, len(words)):
    print(i, words[i])

# %%
'''
Yet, Python provides a much more elegant approach:
'''

for index, item in enumerate(words):
    print(index, item)

# %%
'''
Try iterating over dictionaries yourslef. You should find out that Python iterates over keys only. In order to have access to the whole pair, one should use items() method:
'''

grades = {'Ivan': 4, 'Olga': 5, 'Petr': 4.5}
for key, val in grades.items():
    print('%s has grade: %s' % (key, val))

# %%
'''
Here is how you might compute Pi:
'''

pi = 2
a = 2
for i in range(1, 10):
    a *= 2 * i**2 / (2*i) / (2*i+1) 
    pi += a
print(pi)

# %%
'''
Or if you want to stop after certain precision was achieved (a common use case), you might want to use while loop:
'''

pi, error, a, i = 2, 1e10, 2, 1
while error > 1e-10 / 2:
    prevpi = pi
    a *= 2 * i**2 / (2*i) / (2*i+1) 
    pi += a
    error = pi - prevpi
    i += 1
print(pi)

# %%
'''
List comprehensions
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
'''

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# %%

'''
As always, Python has a more elegant solution with the same result:
'''

squares = [x**2 for x in range(10)]
print(squares)

# %%
'''
List comprehensions can include more for statements and even if statements:
'''

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

'''
which creates a list of pairs with distinct elements. Equivalenly, one could write this over several lines:
'''

# %%

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

# %%
'''
Below are a few more examples:
'''

vec = [-4, -2, 0, 2, 4]
# a list with the values doubled
print([x*2 for x in vec])

# %%

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# %%

# apply a function to all the elements

print([abs(x) for x in vec])

# %%

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# %%

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# %%

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# %%
'''
Finally, we can transpose a “matrix” represented as a list of lists in the following several ways.
'''

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

'''
First, the longest but clearest:
'''
# %%

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# %%
'''
Next uses one list comprehension:
'''

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# %%
'''
Or, one single nested list comprehension:
'''

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

# %%
'''
And, finally, the most elegant (in the context of standard library) way:
'''

transposed = list(zip(*matrix))
print(transposed)

# %%
'''
Functions
Functions are well defined logically complete blocks of actions combined to serve a specific purpose. Functions are separated from the main script to be reused again and again in other projects.

Function definition
The simplest function definition is illustrated in the following example:
'''

def simplest_function():
    print('I\'m your function!')

# %%
'''
which after calling produces the following output:
'''

print(simplest_function())

# %%
'''
The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

A slightly more complicated example to compute Fibbonaci series:
'''

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

# %%
'''
Let’s try and call this function to find out all Fibonacci numbers up to 2000:
'''

fib(2000)

# %%
'''
Notice the line below function name in tripled quotes. This is called docstring. We will come back to it in Documenenting your code.

The result of running function above is just a screen output. If we try to assign the result of this function to a new variable, we will only get None:
'''

out = fib(0)
print(out)

# %%

'''
What if you want to store the result? Then you have to use return statement and say explicitely what your function should produce in the end.
'''

def fib(n):
    """Compute a Fibonacci series up to n and return the result."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# %%
'''
Now let’s try this function instead:
'''

out = fib(2000)
print(out)

# %%
'''
Now variable out is non-empty. It holds the list of Fibonacci numbers.

Above examples have shown how to define functions without any arguments and with just one argument. In fact, function definition is much more flexible than that. Read on.

Positional arguments
Passing several arguments to a function is done with their order in mind.
'''

def power(x, a):
    """Take a power"""
    return x**a

# %%
'''
If you make a mistake in the order of arguments, the function has no way to see that:
'''

print(power(2, 3), power(3, 2))

# %%
'''
Default argument values
Some arguments may have default values. This is used to simplify function calls especially if arguments are numerous. Default arguments always follow positional ones.
'''

def power(x, a=2):
    """Take a power"""
    return x**a

# %%
'''
Here is how you call it:
'''

print(power(2), power(3))

# %%
'''
The default values are evaluated once at function definition.
'''

i = 5

def fun(arg=i):
    print(arg)

# %%

i = 6
'''
The call to this function prduces:
'''
print(fun())

# %%
'''
The side effect is that the default value is shared between the calls:
'''

def fun(a, L=[]):
    L.append(a)
    return L

print(fun(1))
print(fun(2))
print(fun(3))

'''
This prints

[1]
[1, 2]
[1, 2, 3]
Here is one possible way to overcome this:
'''

# %%

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# %%
'''
Keyword arguments
If keeping the order of the arguments becomes a problem, then keyword (or optional) arguments are here to help. These are the same arguments with default values but redefined in function calls.
'''

def slicer(seq, start=None, stop=None, step=None):
        return seq[start:stop:step]

# %%
'''
This function has three default values. They all follow the variable without default. Here are a few examples of using this function:
'''
rhyme = ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']
print(rhyme)

print(slicer(rhyme))

print(slicer(rhyme, step=2))

print(slicer(rhyme, 1, step=2))

print(slicer(rhyme, stop=4, step=2, start=1))

print(slicer(rhyme, 1, 4, 2))

# %%
'''
The following are invalid calls:

slicer()                     # required argument missing
slicer(start=2, 'Python')    # non-keyword argument after a keyword argument
slicer('Python', 2, start=3) # duplicate value for the same argument
slicer(actor='John Cleese')  # unknown keyword argument
'''

# %%
'''
Arbitrary argument lists
If you do not know in advance how many arguments you will need to pass to a function, then you can use function definition as follows:
'''

def fun(var, *args, **kwargs):
    print('First mandatory argument:', var)
    if len(args) > 0:
        print('\nOptional positional arguments:')
    for idx, arg in enumerate(args):
        print('Argument number "%s" is "%s"' % (idx, arg))
    if len(kwargs) > 0:
        print('\nOptional keyword arguments:')
    for key, value in kwargs.items():
        print('Argument called "%s" is "%s"' % (key, value))

# %%
'''
Calling this function produces:
'''

print(fun(2, 'a', 'Python', method='OLS', limit=1e2))
'''
First mandatory argument: 2

Optional positional arguments:
Argument number "0" is "a"
Argument number "1" is "Python"

Optional keyword arguments:
Argument called "method" is "OLS"
Argument called "limit" is "100.0"
At the same time, calling this function with the only mandatory argument results in a much simple output:
'''
# %%

print(fun(2))
'''
First mandatory argument: 2
Placing a star in front of args makes interpreter to expect a tuple of arbitrary length which is then unpacked to separate arguments. Placing two stars in front of kwargs makes Python unpack it as a dictionary into key-value pairs. So, you can pass arguments as tuples and dictionaries which sometimes significantly improves readability of the code. The following lines produce the same output as in the first example of this subsection:
'''

args = ('a', 'Python')
kwargs = {'method': 'OLS', 'limit': 1e2}
print(fun(2, *args, **kwargs))

# %%
'''
Lambda functions
Small anonymous functions can be created with the lambda keyword. Lambda functions can be used wherever function objects are required. They are restricted to be one-liners. Here is an example of a function that returns another function:
'''

def make_power(n):
    return lambda x: x ** n

# %%

'''
And the way to use it is as follows:
'''
power = make_power(3)
print(power(0), power(2))

# %%
'''
Another example shows how to pass a function as an argument without formally defining it:
'''

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# %%
'''
Passing by value
In Python parameters to functions are references to objects, which are passed by value. When you pass a variable to a function, Python passes the reference to the object to which the variable refers (the value). Not the variable itself.

If the value passed in a function is immutable, the function does not modify the caller’s variable. If the value is mutable, the function may modify the caller’s variable in-place:
'''

def try_to_modify(x, y, z):
    x = 23 # immutable object
    y.append(42)
    z = [99] # reference to new object
    print(x, y, z)

# %%
'''
Here is what happens if we call this function:
'''

a = 77    # immutable variable
b = [99]  # mutable variable
c = [28]
print(try_to_modify(a, b, c))
print(a, b, c)


# %%
'''
Classes
Python supports object-oriented programming (OOP). The goals of OOP are:

to organize the code, and
to re-use code in similar contexts.

Modules and Packages
If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:
'''

# Fibonacci numbers module

def fib(n):
    """write Fibonacci series up to n"""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """return Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# %%
'''
Now enter the Python interpreter and import this module with the following command:
'''

import fibo

'''
This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there. Using the module name you can access the functions:
'''

# %%

fibo.fib(1000)

print(fibo.fib2(100))

# %%

print(fibo.__name__)

# %%
'''
If you intend to use a function often you can assign it to a local name:
'''
fib = fibo.fib
fib(500)

# %%
'''
A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement.

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names are placed in the importing module’s global symbol table.

There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table. For example:
'''

from fibo import fib, fib2
fib(500)
print(fib2(500))

# %%
'''
There is even a variant to import all names that a module defines:
'''

from fibo import *
print(fib2(500))

# %%
'''
Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

Probably the safest way of importing objects from modules is through a short reference to the module name:
'''

import fibo as fb
print(fb.fib2(500))

# %%
'''
This way you may safely define another fibo function and it will not create any conflict with unambiguously different function fb.fib.

When you run a Python module with:

python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with the __name__ set to “__main__”. That means that by adding this code at the end of your module:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

$ python fibo.py 50
1 1 2 3 5 8 13 21 34
If the module is imported, the code is not run:
'''
