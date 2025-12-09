
import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    total_tent = math.ceil(participants / tent_capacity)
    meal_cost = meal_price * participants
    tent_cost = total_tent * tent_price

    cost = meal_cost + tent_cost

    return cost

# Test your code here
print("Testing Camping Logistics...")
result = calculate_event_cost(10, 5, 15, 10)
print(f"Your total cost is = {result}")

