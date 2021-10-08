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