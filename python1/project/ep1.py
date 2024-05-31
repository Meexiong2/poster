temp = input('Enter the temperature : ')
degree = int(temp[:-1])
unit = temp[-1].upper()

if unit == 'C':
    result = (9*degree)/5+32 
    unit_result = 'fahrenheit'
    unit_degree = '°F'
if unit == 'F':
    result = (degree-32)*5/9
    unit_result = 'celsius'
    unit_degree = '°C'

print(f'change the number = {temp} to {unit_result} = {result}{unit_degree} ')
    