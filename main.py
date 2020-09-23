'''This app calculates how many slices of pizza each person gets. It also calculates the remaining number of slices.'''
print("---Welcome to Split my Pizza---")
print("How many slices are on the pizza?")
slices = int(input())
print("How many people are sharing?")
people = int(input())

slices_each = slices // people
remainder = slices % people
print(f"There will be {slices_each} slices of pizza for each person.")
print(f"There will be {remainder} slices remaining.")