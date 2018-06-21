
def sortByStrings(s,t):
    d = {}
    ##add all the letters in s to a dictionary
    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    result = []
    for letter in t:
        if letter in d:
            freq = d[letter]
            result.append(letter*freq)
            # print(letter*freq)
    # print(result)
    return (''.join(result))

print(sortByStrings("weather", "therapyw"))