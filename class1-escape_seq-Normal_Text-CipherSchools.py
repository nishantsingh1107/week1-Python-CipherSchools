# Escape Sequence As Normal Text 

# to use escape seq. as text we have add one extra backslash just b/f the required escape seq. 
# for example- to print \n as text then we write like \\n

# output : Line A \n Line B
print("Line A \\n Line B")

# output : Line 1 \t Line 2
print("Line 1 \\t Line 2")

print("This is 4 Backslash \\\\\\\\")

# output : \" \'
print(" \\\" \\\' ")

# \\ = \ (a)
# \" = " (b)
# \\\" = \" (a+b)

# Shortcut to use escape sequence as normal text-

# output : Line 1 \n Line 2
print(r"Line 1 \n Line 2")
