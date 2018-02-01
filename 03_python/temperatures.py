# temperature conversion

temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
Temp_Kelvin = []
for theta in temperatures:
   T = (theta - 32) * (5/9) + 273.15
   Temp_Kelvin.append(T)


print("Conversion complete")
print(Temp_Kelvin)
