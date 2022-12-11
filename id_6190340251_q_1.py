days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start = 18

symbol="#"
line_space=18

print("##################")
for i in range(7):
    day="{0:<9}".format(days[i])
    print(symbol, end=' ')
    print(day, end=' ')
    print(symbol, end=' ')
    print(start+i, end=' ')
    print(symbol)
print("##################")
