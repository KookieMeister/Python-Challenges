#!/usr/bin/python
#by Kris Downs KookieMeister
#Reverse a string the hard way

inputstring=raw_input("Please enter  a string to reverse: ")
reversedstring = ""
lettersInInput=[]
reversedLetters=[]
inputLength=len(inputstring)
print inputLength

for each in inputstring:
    lettersInInput.append(each)
    reversedLetters.append(each)

print "Original List: ", lettersInInput
print "Original String: ", inputstring



#Reversing String TODO
for each in lettersInInput:
    reversedLetters[inputLength-1] = each
    inputLength = inputLength - 1

reversedstring = ''.join(reversedLetters)
print "Reversed List: ", reversedLetters
print "Reversed String: ", reversedstring