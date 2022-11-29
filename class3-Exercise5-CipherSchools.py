# Ask a user for name
# Example - Nishant Singh
# print count of each words
# output : 
        # N : 1
        # i : 2
        # s : 1
        # h : 3
        # a : 3
        # n : 2
        # t : 2
        #   : 1
        # S : 1


name = input("Enter your full name : ")

temp_var = ""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1    
