username = input("Enter your username:")
print(username)
correct_password = ("Naruto")
attempts = 3

print("Welcome! You have only 3 attempts to log in.")

while attempts > 0:

    user_password = input("Enter the Password :")
    
    if user_password !="Naruto":
        
        attempts = attempts -1 
        
        print("Wrong password", attempts, "attempts left")
        
    else:
        print("Access Granted!")
        break
if attempts == 0:
    print("Please try again later.")
