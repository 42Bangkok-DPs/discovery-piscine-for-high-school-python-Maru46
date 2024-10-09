#!/usr/bin/env python3

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
mult = a * b
print(f"{a} x {b} = {mult}")
if mult < 0:
	print("The result is negative.")
elif mult > 0:
	print("The result is positive.")
else:
	print("The result is positive and negative.")
