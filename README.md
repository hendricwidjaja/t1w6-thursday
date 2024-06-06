## Control Flow
Order in which lines of code are executed in a program.

# Sequential control flow
Execution of code statements one after another, in the order they appear in the program

print("Hello, welcome to programming with Python")

a = 10
b = 5
result = a + b

print(f"The result of adding {a} and {b} is {result}")

print("Thank you")

# Conditional Control Flow / Control Flow
Execution of code statements based on some input

if tomorrow is Saturday
    set alarm for 7
if tomorrow is Tuesday
    set alarm for 6

# Boolean Data Type Re-visit
Data type that has two values: True and False. Boolean values are used to control the flow of the program

# Comparison Operators / Relational Operators
Decide the relationship between the operands. Result of comparison is a boolean value (True/False)

if tomorrow == Saturday:
    set alarm for 7
if tomorrow == Tuesday:
    set alarm for 6

# if, elif, else
Simplest form of AI (you could say)
'if' checks the condition, if true, the indented blocks get executed, if false, it skips the indented.

today = "Tuesday"

if today == "Monday":
    print ("Set alarm for 5am")
if today == "Tuesday":
    print ("Set alarm for 6am")
if today == "Saturday":
    print("Set alarm for 7am")

# Pass
Does nothing, just ... passes ... for now (placeholder)

# Boolean Operaters
AND, OR, NOT. Operands need to be boolean as well.

# Ternary Operator
Condense series of code into one line (when applicable)

age = 20
has_permission = False
if age >= 18:
    if has_permission:
        print("Access Granted")
    else:
        print("Access Denied")
else:
    print("Access Denied")

if age >=18 and has_permission:
    print("Access granted")
else:
    print("Access Denied")

print("Access Granted") if age >=18 and has_permission else print ("Access Denied")

# Match-case
Control-flow, similar to switch statement in other programming languages

day_number = 3

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"

print(day_name) = "Wednesday"
