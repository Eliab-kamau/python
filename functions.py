#Functions

# example of flow of execution of functions

def hello():
    print("good morning")
    print("kibabii university")
print('hello')
print("how are you doing")
hello()
print("done!")

#Parameters and arguments

       #parameters are passsed durin function defination

#function defination
def add(a,b):
    return a+b


      #Arguments are passed during function call
      
#fuction call

results=add(12,48)
print (results)



#function syntax

#Syntax:
def functionname():

#statements
 
 
 
 functionname()
'''Function definition consists of following components:
1. Keyword def indicates the start of function header.
2. A function name to uniquely identify it. Function naming follows the same rules of writing 
identifiers in Python.
3. Parameters (arguments) through which we pass values to a function. They are optional.
4. A colon (:) to mark the end of function header.
5. Optional documentation string (docstring) to describe what the function does.
6. One or more valid python statements that make up the function body. Statements must have 
same indentation level (usually 4 spaces).
7. An optional return statement to return a value from the function.'''

#Example:


def hf():
 print("hello world")    #function definition

hf()      #function call


'''In the above example we are just trying to execute the program by calling the function. So it 
will not display any error and no output on to the screen but gets executed.
To get the statements of function need to be use print().'''

#calling function in python:


def hf():
 print("hello world")
hf()


'''Output:
hello world
--------------------------'''

def hf():
 print("hw")
 print("gh kfjg 66666")
hf()
hf()
hf()

def my_function(fname):
    print(fname  + "Kamau")
    
my_function("Eliab  ")
my_function('Dennis  ')