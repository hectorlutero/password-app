## PASSWORD VALIDATION WITH PYTHON
## NAIVE METHOD

## CREATE A FUNCTION TO CREATE THE METHOD ##

def password_validation(password):
    SpecialSymbols = ['@', '#', '$', '%']
    val = True
    
    if len(password) < 8:
        print('length should be at least 8 digits long')
        val = False
        
    if len(password) > 20:
        print('length should be at most 20')
        val = False
    
    if not any(char.isdigit() for char in password):
        print('Password should have at least one digit')
        val = False
    
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase character')
        val = False
    
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase character')
        val = False
        
    if not any(char in SpecialSymbols for char in password):
        print('Password should contain at least one special symbol such as @, #, $, %')
        val = False
        
    if val:
        return val
    
## MAIN METHOD ##

def main():
    password = input('Your password: ')
    
    if (password_validation(password)):
        print('Password is valid')
    else:
        print('Password is invalid')
        if __name__ == '__main__':
            main()
        
        
# Driver Code

if __name__ == '__main__':
    main()