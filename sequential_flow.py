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

temperature = 30

# if temperature > 30:
#     message = "It's hot outside"
# else:
#     message = "It's not hot outside"

# print(message)

message = "It's hot outside" if temperature > 30 else "It's not hot outside"
print(message)

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

print(day_name)