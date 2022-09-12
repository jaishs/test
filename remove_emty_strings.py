"""Wite a function to print empty elemets in list
	Ex: Input [apple, '', 123, [], 22, 45, -30, None]
"""
Input = ["apple", '', 123, [], 22, 45, -30, None]
for i in Input:
    if not i:
        Input.remove(i)
print(Input)

