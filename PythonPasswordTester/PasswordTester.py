import string 

#Checks the password aganist list of 100k of the most common passwords by opening a text file and comparing it aganist
def check_commonpass(password):
    with open('100kcommonpass.txt', 'r') as g:
        common = g.read().splitlines()
    if password in common:
        return True
    return False

def pass_strength(password):
 grade = 0
 length = len(password)

 if length >= 7:
    grade += 1
 if length >= 10:
    grade += 1
 if length >= 13:
    grade += 1
 if length >= 16:
    grade += 1

 uppercase = any(i.isupper() for i in password)
 lowercase = any(i.islower() for i in password)
 specialchar = any(i in string.punctuation for i in password)
 digits = any(i.isdigit() for i in password)

 chars = [uppercase, lowercase, specialchar, digits]
 grade += sum(chars)
 if grade <= 3:
    return ("Weak", grade)
 elif grade == 4:
    return ("Poor Medium", grade)
 elif grade <= 5:
    return ("Okay Medium")
 else:
    return ("Strong", grade)
 

def password_advice(password):
 if check_commonpass(password) == True:
    return "Password is very common, Please change!"
 strength, grade = pass_strength(password)

 advice = (f"Your password strength is {strength}")
 return advice



input = str(input(("Enter password: ")))
print(password_advice(input))