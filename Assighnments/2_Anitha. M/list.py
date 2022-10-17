#call by reference 
def add(list):
    list.append(50) 
    print(list)
mylist=[10,20]
add(mylist)
print("outert__"+mylist)