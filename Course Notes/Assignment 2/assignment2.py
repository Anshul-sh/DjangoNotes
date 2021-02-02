
f = open("catalog.txt", "r")

myitems = ['gym mats', 'rigs', 'boxing gloves', 'ropes', 'treadmill', 
            'elliptical', 'dumbbell', 'yoga ball']

d1 = {}

for item in myitems:
    while True:
        contain = f.readline()
        if(item in contain):
            d1[item] = (f.readline(),f.readline())
            break
        elif(contain == ''):
            print(item + "is not available in the catalog.")
            break
    f.seek(0,0)
    
print(d1)
while True:
    s = input("Enter Fitness Item: ")
    if(s in d1):
        print(s + "  has:\nCategory: " + d1[s][0]+"Value: "+ d1[s][1])
        while True:
            try:
                n = int(input("How many " + s +" do you want to order: "))
                if(n>0):
                    print("Your order is successful!")
                    break
                else:
                    print("Negative values not accepted! Please try again")
            except ValueError:
                print("Invalid quantity input")
        break
    else:
        print("Item does not exist. Please try again.")