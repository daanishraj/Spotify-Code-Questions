
def decodeString(s):

    listStr = [] #creating an empty list that will hold all substrings
    chars = ""
    listStr.append(chars)

    for c in s: #iterate through the input string
        if c == "[":
            newChars = ""
            listStr.append(newChars)
        elif c == "]":
            if len(listStr) > 1:
                currentChars = listStr[-1]
                prevChars = listStr[-2]
                lastChar = prevChars[-1]
                if lastChar.isdigit(): #if last char of previous string was a number
                    tempIdx = len(prevChars) - 1
                    while prevChars[tempIdx].isdigit() and tempIdx >= 0:
                        tempIdx -= 1
                    lastChar = prevChars[tempIdx + 1:]

                    charsToAdd = int(lastChar) * currentChars
                    newChars = prevChars[:tempIdx + 1] + charsToAdd
                    listStr[-2] = newChars
                else: #if last char of previous string was not a number, then we can concatenate the substrings
                    listStr[-2] = prevChars + currentChars

                listStr = listStr[:-1] #remove the last substring from list
        else:
            changedChars = listStr[-1] + c
            listStr[-1] = changedChars

        # print(listStr[-1])

    # print(len(listStr))
    return (listStr[-1])


# s1 = "3[a]2[bc]"  #return "aaabcbc".
# s2 = "3[a2[c]]" #return "accaccacc".
# s3 = "2[abc]3[cd]ef" #return "abcabccdcdcdef"
# s4 = "4[ab]" #"abababab" 
# s5 = "2[b3[a]]" #"baaabaaa"
# s6 = "100[dog]"
# print(decodeString(s1))
# print(decodeString(s2))
# print(decodeString(s3))
# print(decodeString(s4))
# print(decodeString(s5))
# print(decodeString(s6))
