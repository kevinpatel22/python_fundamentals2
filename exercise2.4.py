def typ(words):
    letter = len(words)
    return bool(letter > 8)

result = typ('Fahrenheit')
result1 = typ('parameter')
result2 = typ('function')
result4 = typ('return')
result3 = typ('number')

print(result)
print(result1)
print(result2)
print(result3)
print(result4)