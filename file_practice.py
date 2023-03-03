'''This is the code that I wrote and I believe it works fine'''
def is_palindrome(str):
    #normal string
    normal = str
    #reversed string
    rev_str = str[::-1]
    if normal == rev_str:
        #print("yes")
        return "True"
    else:
        #print("no")
        return "False"

is_palindrome("level")

#___________________________________________________________________________________________________________________

'''This is my teachers code and I have no clue what the difference is'''
def is_palindrome(string):
    #reversed string is an empty list
    reversed_string= ""
    #position is the length of the string given minus one
    position = len(string) - 1
    while position >= 0:
        reversed_string += string[position]
        position -= 1
    if string == reversed_string:
        return True
    else:
        return False