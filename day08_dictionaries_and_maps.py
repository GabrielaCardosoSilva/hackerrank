'''
Task
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. For each name queried, print the 
associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
'''

n = int(input())
phone_dict = {}

for i in range(n):
    text = input().split()
    phone_dict[text[0]] = text[1]

while True:
    try:
        key_input = input()
        
        if key_input != "":
            if key_input in phone_dict:
                print("{}={}".format(key_input, phone_dict[key_input]))
            else:
                print("Not found")
        else:
            break
        
    except EOFError:
        break