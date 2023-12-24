print("Hello, wolcome to Registration form to check your elgibility criteriya")

name = "abc"
pwd1 = 1234

while True:
    user_name = input("Enter your username: ")
    pwd2 = int(input("Enter your Password: "))
    if name == user_name and pwd1 == pwd2:
        print("Successfully, Log-in into your account")
        break
    else:
        print("Try again")

print("========================================================")
print("              REGISTRATION FORM                         ")
print("========================================================")
nam = input("Enter your fullname as per as SSC:")
mobile = int(input("Enter your contact number:"))
email = input("Enter your Email-id: ")
print("********************************************************")
print("              EDUCATION QUALIFICATION                   ")
print("********************************************************")
tenth = int(input("enter your 10th Percentage:"))
tweleth = int(input("Enter your 12th Percentage:"))
hgh = input("Enter your Highest Qualification:")
psd = int(input("Enter your Year of Passedout:"))
pct = int(input("Enter your Percentage of Highest Qualification:"))

if tenth >= 70 and tweleth >= 70:
    if pct >= 65 and psd == 2023:
        print("congrates, Your eligble!")
        print("*******************************************************")
        print("                 Personal Information                  ")
        print("*******************************************************")
        print("Full-Name:", nam)
        print("Contact:", mobile)
        print("Email-Id:", email)
        print("Highest Qualification:", hgh)
        print("Year of Passed-out:", psd)
        sub = input("If you want submit(yes/no):")
        if sub == "yes":
            print("Successfully submited your application")
        else:
            print("**** Thank You ****")

    else:
        print("You cannot eligble for further process")
else:
    print("You cannot eligble for further process")

