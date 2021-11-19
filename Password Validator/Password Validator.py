def password(text):
      
    SpecialSym =['$', '@', '#', '%','!','&','*']
    
      
    if len(text) < 8:
        print('length should be at least 8')
        print("Password is Invalid!")
        
          
    elif len(text) > 15:
        print('length should be not be more than 15')
        print("Password is Invalid!")
          
    elif not any(char.isdigit() for char in text):
        print('Password should have at least one numeral')
        print("Password is Invalid!")
          
    elif not any(char.isupper() for char in text):
        print('Password should have at least one uppercase letter')
        print("Password is Invalid!")
          
    elif not any(char.islower() for char in text):
        print('Password should have at least one lowercase letter')
        print("Password is Invalid!")
          
    elif not any(char in SpecialSym for char in text):
        print('Password should have at least one of the symbols $@#')
        print("Password is Invalid!")
    else:
        print("Password is valid!")


password(input("Enter your password which you want to check it's validity:-\n"))

