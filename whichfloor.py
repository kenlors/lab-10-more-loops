maximum_stories = 100
userstring = input("On what floor of the building is your office?")
usernum = int(userstring, 10)

while (usernum > maximum_stories):
print("You entered: " + usernum + " but there are only " + maximum_stories + " floors in this building. Try again...")
userstring = input("You entered: " + usernum + " but there are only " + maximum_stories + " floors in this building. Try again...")
usernum = int(userstring, 10):

print("Congrats! You work on: " + usernum)
