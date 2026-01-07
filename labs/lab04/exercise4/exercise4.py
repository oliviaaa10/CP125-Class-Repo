
def analyze_performance(lap_times):
    total_laps = len(lap_times)
    mid = (total_laps + 1) // 2

    first_half = lap_times[:mid]
    second_half = lap_times[mid:]

    first_sum = 0
    for i in first_half :
        first_sum += i
    first_avg = first_sum / len(first_half)

    second_sum = 0
    for i in second_half : 
        second_sum += i
    second_avg = second_sum / len(second_half)

    if second_avg > first_avg :
        return True
    else : 
        return False

    


# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
