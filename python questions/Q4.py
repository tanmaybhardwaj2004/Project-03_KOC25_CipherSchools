# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

st = "1234abcd"
newSt = ""

for i in st:
	newSt = i+ newSt

print(newSt)