
def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    round_trip_km =  one_way_km * 2
    cost = ( round_trip_km / km_per_liter)* price_per_liter

    if budget >= cost : 
        budget = True
    else:
        budget = False

    return budget
     
    
result = is_budget_sufficient (15, 10, 50, 500)
print(f"Is budget sufficient = {result}")

if result:
    print("Your budget is enough for round trip")
else:
    print("Your budget isn't enough for round trip")