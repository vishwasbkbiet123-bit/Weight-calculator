weight_pound = input("enter your weight in pound: ")
weight_kg = int(weight_pound)*0.45
print('your weight is :' + str(weight_kg) + 'kg')  


#To convert temperatue Fahrenheit to celsius

temp = float(input('enter temperature in Fahrenheit: '))
celsius = float((temp-32)*(5/9))
print(celsius)
print(type(celsius))  
