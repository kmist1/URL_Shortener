import re

def isEmail_valid(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    try:
        if (re.search(regex,email)):
            print("Valid Email")
            return True
        else:
            print("Error: Email is not valid")
            return False
    except Exception as e:
        print("Error: ",e)
        return False
