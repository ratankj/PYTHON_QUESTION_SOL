
"""


Task 23: Password Strength Checker
Description: Develop a program that evaluates the strength of a user's password based on
 certain criteria (e.g., length, complexity).
Example Input: "Pa$$w0rd"
Example Output: "The password is strong."

"""

"""

32. In a portal login website, you are asked to write a function get_password_strength to decide 
the strength of a password. The strength is decided based on the total score of the password, Use 
following conditions:
1) If password has length greater than 7 then score increases by one point.
2) If password has at least one upper case and one lower case alphabets score increases by one point.
3) If password has at least one number and no consecutive numbers like 12 or 234 then score 
increases by one point.
4) If password has at least one special character (any character other than numbers and alphabets) then 
score increases by one point.
5) If password contains username, then it is invalid password.
If the password has score of four points, three points, two points, or one point then print Very 
Strong, Strong, Moderate, or Weak respectively. If the password is invalid, then 
print PASSWORD SHOULD NOT CONTAIN USERNAME and If the score is zero, then print Use a 
different password.The arguments to the function are username and password which are 
already defined

"""

capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
special_char = "!@#$%^&*-+=~`|\/:;\"'?.,_()[]{}<>"

flag_a = False
flag_b = False
flag_c = False
flag_d = False

length = 0
password_strength = input("Enter your password: ")

for i in password_strength:
    length += 1

print(f"The length of the password is: {length}")

count = 0

if length > 7:
    count += 1

for i in password_strength:
    if i in capital:
        flag_a = True
    elif i in small:
        flag_b = True
    elif i in num:
        flag_c = True
    elif i in special_char:
        flag_d = True
    else:
        print("empty")



if flag_d:
    count += 1

if flag_a:
    count += 1

if flag_b:
    count += 1

if flag_c:
    count += 1

print(count)

if count == 5:
    print("very strong")

elif count == 4:
    print('Very strong')
elif count == 3:
    print('Strong')
elif count == 2:
    print('Moderate')
elif count < 2:
    print('Weak')

