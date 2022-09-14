# 3. Filter the price in a dictionary, check if the price of the item is
# greater than 2000, between 3000-7000 and so on
# Ex:
# smart_phone_dict = {'Samsung': 35500, 'Realme': 14000, 'Moto G10 Power': 3500, 'OnePlus 8 Pro':50000,
# 'Samsung 2': 6000, 'Lika': 1500, 'Lava': 2500, 'Redme': 4500}

smart_phone = {'Samsung': 35500, 'Realme': 14000, 'Moto G10 Power': 3500, 'OnePlus 8 Pro':50000,
 'Samsung 2': 6000, 'Lika': 1500, 'Lava': 2500, 'Redme': 4500}

a=dict()
b=dict()
c=dict()
for key,value in smart_phone.items():
    if 3000 > value > 2000:
        a[key]=value
    elif 3000 < value <= 7000:
        b[key]=value
    else:
        c[key]=value
print(a)
print(b)
print(c)

