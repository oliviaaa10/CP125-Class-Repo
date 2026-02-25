# Olivia Polus C01
# Create a program that accepts 5 integer input values from the user and is stored in a list.

def process_number():
    numbers = []

    for i in range (1, 6):
        num = int(input(f"Enter number {i} :"))
        numbers.append(num)

    numbers.sort()
    total = sum(numbers)
    largest = max(numbers)

    return numbers, total, largest
    
sorted_numbers, total_number, largest_number = process_number()

print("Numbers in ascending order:", sorted_numbers)
print("Sum of all numbers:", total_number)
print("Largest number:", largest_number)