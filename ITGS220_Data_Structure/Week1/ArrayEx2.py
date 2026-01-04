# Example of using Python array to store a list of fruits
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Watermelon']

# Accessing elements by index
print("First fruit:", fruits[0])  # Output: First fruit: Apple
print("Third fruit:", fruits[2])   # Output: Third fruit: Orange

# Modifying elements
fruits[1] = 'Mango'
print("Modified fruits list:", fruits)  # Output: Modified fruits list: ['Apple', 'Mango', 'Orange', 'Grapes', 'Watermelon']

# Iterating through elements
print("Fruits list:")
for fruit in fruits:
    print(fruit)
