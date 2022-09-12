# 9.Python function to convert Fahrenheit to Celsius
# celsius = (fahrenheit – 32) * 5/9.
def ftoc(ftemp):
    cel = (ftemp-32)/1.8
    return cel
ftemp=float(input("enter temp"))
print("Enter Temperature in Fahrenheit: ")
print("\nEquivalent Temperature in Celsius: ", ftoc(ftemp))
