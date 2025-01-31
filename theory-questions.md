# Theory Questions

Edit this file to put your answers to the questions where marked and Commit to `main`.

---

1. Define "expression" and "statement" in Python. Give an example of each, and explain how the interpreter treats them differently.

    A Statement is a line of code that does something, for example it states that a variable is equal to something or prints something, while an expression is like a mathematical expression that calculates some value. Python treats these differently because expressions all need to be evaluated to some value, while statements don't neccesarily have to, and statements need to be executed, while expressions are not.

2. Describe the difference between the three types of errors covered in the **Debugging** section of Module 2. Provide an example of each type.

    The 3 main errors in code are syntax errors, runtime errors, and semantic errors.  Syntax errors are when the code does not fit into python's rules and gets stuck trying to execute the code, but cannot run because it doesn't make sense to python.  Runtime errors mean that the code starts running but fails during an execution, such as dividing a string by an integer.  Semantic errors is when the code runs fine in python, but produces and unintended result, and one that usually does not give the desired outcome. 

3. Explain what happens when you try to do arithmetic directly on a string, such as `"42" / 2`. How do you fix that so the arithmetic works? Provide a short example.

    When you try to do arithmetic on a string you will get a runtime error because the operation cannot be preformed.  You could fix this by using the int() function or float() function to change the string to an integer, which can be divided.

4. Why do we need to `import` modules in Python? Give an example of how failing to import a module leads to errors. (hint: What would happen if you tried to use `math.pi` without importing `math`.)

    We need to import modules to access different features of python, for example the "import math" module allows the user to use many different math functions by using math."function", many of which are not available in standard python.  If you would try to run math.pi without importing math, you would run into a syntax error, as python would not have the information to be able to complete this task and the code would not run.  

5. Why might `area_in_m2` be preferable to a shorter name like `a` in more complex code? When might an overly long variable name be counterproductive?

    This variable name might be better than a shorter variable name because the complex code could have many different variables that could signify a, and could get confusing as things are changed within the code.  This also makes it harder to spot bugs within a code and could be difficult to fix if something breaks in the future.  Unnecesarily long variable names could also have the same problem with reducing the ability to easily read the code and the increased ability to make a mistake or typo when using variable names.  The best type of variable name is one that is clear, however does not have any extra words that could lenthen the code unnecesarily.  
