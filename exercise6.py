
print('This calculator will change the temperature from Fahrenite to Celcius. Check it out!\nTemperature in Fahrenheit!')
temp_nite = int(input())
def convert_temp(nite):
    return ((temp_nite - 32) * 5/9)
def converted_temp(cel):
    return "The temperature is {} in celcius.".format(cel)

result = convert_temp(temp_nite)
celcius = converted_temp(result)
print(celcius)