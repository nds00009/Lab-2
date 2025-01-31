[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gJF2d8vH)
# Lab 2

## Collaboration

Students may collaborate, but each student must submit their own work in their own words/code.

## Topics

- Arithetic, Variables, and Types
- Importing and using the `math` module
- Basic User Input
- Strings and basic strings operations
- Expressions vs. Statements
- Debugging and Error Types

## Mini Lesson

### User Input

In Python, your programs can receive user input using the `input()` function. This function always returns a **string**, so if you need a number, you must convert it using `int()` or `float()`. The value can then be assigned to a variable just like any other statement.

### String Formatting

You've seen examples of using `print()` to output strings and joining strings with `+`. While this works, it can become tedious, and **concatenation does not automatically handle spaces**. A better method is to use **f-strings**, which allow you to insert variables directly into a string. This is called **string interpolation**.

### Example

Here is a *very basic* program that asks for the user's name and returns a friendly message:

```python
name = input("What is your name?: ")
print(f"Nice to meet you, {name}!")
```

### Key Takeaways

- Notice the extra space after the colon (`:`). The user will type in their input on the same line as this message.
- Code inside `{}` executes as if it were outside the string.
  
  ```python
  print(f"{2 + 2}") # identical to print(4)
  ```
  
  This means you can include calculations, function calls, and even formatted numbers inside an f-string.

## Instructions

In your terminal, execute:

```shell
uv sync
```

This will create the Python virtual environment with the required dependencies. Then, complete the `exercise.md` and answer the `theory-questions.md`.
