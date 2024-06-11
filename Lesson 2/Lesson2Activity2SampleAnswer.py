firstString = input("What is the first string: ")
secondString = input("What is the second string: ")

middleFirstString = int(len(firstString) / 2)
firstStringLength = len(firstString)

firstHalf = firstString[0:middleFirstString]
secondHalf = firstString[middleFirstString:firstStringLength]

print(firstHalf + secondString + secondHalf)