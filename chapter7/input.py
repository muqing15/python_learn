message = input("Tell me something, Then I will repeat it back to you: ")
print(message)

#----------------
height = input("How tall are you, in inches?\n")
height = int(height)

if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")
#----------------
arr = []
while True:
    str = input()
    if str == "01":
        break
    arr.append(int(str))
print(arr)