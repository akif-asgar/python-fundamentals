#Password validation with loops

password = input("Enter your password: ")

essential_characters = "!@#$%^&*1234567890"

while True:
    
    enable = True
    
    if len(password) < 8:
        
        print("Password must be at least 8 characters")
        
        password = input("Enter your password again: ")
        enable = False
        
    if password.islower():
        
        print("Password must contain at least one uppercase letter")
        
        password = input("Enter your password again: ")
        enable = False
        
    for char in essential_characters:
        
        if char in password:
            break
        
        elif char == essential_characters[-1]:  # if we reach the end of essential characters without finding a match
            print(f"Password must contain at least one special character or number({essential_characters})")
            password = input("Enter your password again: ")
            enable = False

        
    for char in password:
        
        if char == " ":
            
            print("Password can not contain spaces")
            
            password = input("Enter your password again: ")
            enable = False
            break
    
    if enable:
        
        print("Your password is valid")
        break
    
    
    
        
        