BASE_FARE = 50
RATE_PER_KM = 10


def calculate_fare(distance):
    return BASE_FARE + (distance * RATE_PER_KM)


# Example usage
trips = [5, 10, 3]
total_fare = 0

for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total_fare}")
