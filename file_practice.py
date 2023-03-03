def is_palindrome(string):
    reversed_string= ""
    position = len(string) - 1
    while position >= 0:
        reversed_string += string[position]
        position -= 1
    if string == reversed_string:
        return True
    else:
        return False
    
#______________________________________________________________________________________
#teachers code
def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
      return(n1 + n2) / 2
    except TypeError:
      return("Please use two numbers as parameters")
    
#________________________________________________________________________________________

evens = []
odds = []
def odds_and_evens(bool,my_list):
  if bool == True:
    for num in my_list:
      if num % 2 == 0:
        evens.append(num)
    print(evens)
  elif bool == False:
    for num in my_list:
      if num % 2 != 0:
        odds.append(num)
    print(odds)

odds_and_evens(False, [13, 22, 8, 31] )


#________________________________________________________________________________________

#teachers code
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
      if my_bool:
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(num)
                
    return return_list

#_______________________________________________________________________________________
#my code
def search_list(my_list, search_term):
  for i in range(len(my_list)):
    search_term = search_term.lower()
    my_list[i] = my_list[i].lower()
  if updated_list[i] == update_term:
      return i
  
#_______________________________________________________________________________________
#teachers code
def search_list(lst, term):
    """Search for item in a list
    Return the index if found
    Return -1 if not found"""
    for item in lst:
        if item.lower() == term.lower():
            return lst.index(item)
    return -1

#_______________________________________________________________________________________
#I could not figure out this one so my teachers code is here

import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
    """Read a CSV of baseball data.
    Return the team name with the most wins"""
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        most_wins = 0
        best_team = ""
        for row in reader:
            if int(row[3]) > most_wins:
                most_wins = int(row[3])
                best_team = row[0]
        return best_team




'''This is the code that I wrote and I believe it works fine for Functions 5'''
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