string_to_parse="yes"

target='r'
pos=0

while string_to_parse:
    if string_to_parse[pos]==target:
        print("Found \'%c\' stops" %target)
        break
    print(string_to_parse[pos])
    pos+=1
    if pos==len(string_to_parse):
        print("Did not find \'%c\' in \'%s\'" %(target, string_to_parse))
        break
