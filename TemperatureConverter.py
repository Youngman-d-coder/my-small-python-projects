print('Temperature Conversion Program')
print('Selections:::\nPress 1 to Enter Celcius\nPress 2 to Enter Farenheit\nPress 3 to Enter Kelvin')
 
choice = int(input('Enter your selection: '))
 
if choice > 3:
   print('Invalid Option')
 
if choice==1: 
   temp = float(input('Enter temperature in Celcius: '))
   # Rounding to 2 decimal places
   farenheit = round((((9/5)*temp)+32), 2)
   kelvin = round((temp+273.15), 2)
   print('Temperature in Farenheit: ', farenheit, 'deg F')
   print('Temperature in Kelvin: ', kelvin, 'deg K')
 
elif choice==2: 
   temp = float(input('Enter temperature in Farenheit: '))
   celcius = round(((5/9)*(temp-32)), 2)
   kelvin = round(((temp+459.67)*(5/9)), 2)
   print('Temperature in Celcius: ', celcius, 'deg C')
   print('Temperature in Kelvin: ', kelvin, 'deg K')
 
elif choice==3:
   temp = float(input('Enter temperature in Kelvin: '))
   celcius = round((temp-273.15), 2)
   farenheit = round(((temp*(9/5))-459.67), 2)
   print('Temperature in Farenheit: ', farenheit, 'deg F')
   print('Temperature in Celcius: ', celcius, 'deg C')
