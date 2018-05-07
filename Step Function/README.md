# The three week course at Step Function

A course to bring absolute beginners to writing one hundred line programs
in three weeks.

### Day - 1
### Material Covered

- Variable
- Basic Python built-in function (print,len,type)
- Python Data Type
   - Numeric (float, int)
   - Sequence (string, list)
- Syntax  and Style

### Day - 2
### Material Covered

- Logic
  - Boolean Value
  - Boolean Expression
  - Logical Operators
  - Chaining Logical Operators
  - Python Truthiness

- Control Flow
  - Conditional Statement
  - For Loop
  - While Loop

- Exercise:
 - Guessing Game
 - Rolling the dice

### Day - 3
### Material Covered

Non-Primative Data Structures

  - Dictionaries
  - Tuples

*Cheat sheet*

     * *Lists* should be your default choice. You can put anything in there and they support most operations you'll be interested in, even if they're not always the fastest option.

    If you're going to use something other than a list, make sure you know exactly why!

    * *Dictionaries* ("dicts") should be your second choice. A dict maps keys to values.

    For example, a person dict might contain the keys name, age and postcode, with suitable values for each.

    * *Tuples* are basically immutable lists. Use them when you don't want your data to change.

    * *Sets* are a bit like lists but every element is unique. Use them when you need to quickly perform membership testing, remove duplicates or perform set operations like intersection, union or difference.

The choice between using a List or a Dictionary is a Trade-off between space and time.

### Day - 4
### Material Covered


*Functions* - A Function is a bundled set of instructions that you want to use repeatedly or that, because of their complexity, are better self-contained in a sub-program and called only when needed.

They are written to carry out a specified task. To carry out that specific task, the function might or might not need multiple inputs. When the task is carried out, the function can or can not return one or more values

*The Two Common Python Functions*
Built-in functions, such as help(), print() to print an object to the terminal, len() to get the length of a sequence data type, etc.


User-Defined Functions (UDFs), which are functions that users create to help them out. These functions are declared with *def* before the name of the function. Where *def* here stands for define.


*args & **kwargs
The special syntax, *args and **kwargs in function definitions is used to pass a variable number of arguments to a function.

The single asterisk form (*args) is used to pass a non-keyworded, variable-length arguments , and the double asterisk form (**kwargs) is used to pass a keyworded, variable-length arguments.

*args - Is packed into a tuple

**kwargs - Is packed into a dictionary
