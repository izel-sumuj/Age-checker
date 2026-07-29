user_name = input("Enter your Name: ")
print(f"welcome, {user_name}! ")

age_prompt = f"{user_name}, please Enter your age:"
age= int(input(age_prompt))

match age:   
    case _ if age < 18:
        print(f"Access denied!,\nYou are a minor" )
        print("Hence,you cannot proceed further. ")
        
    case _ if age>=18:
        print("[SUCCESS] Access granted!")
        print("You may now proceed. ")
