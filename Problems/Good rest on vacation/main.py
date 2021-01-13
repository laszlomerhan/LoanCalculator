days = int(input())
food_per_day = int(input())
one_way_flight_cost = int(input())
one_night_cost = int(input())
total = days * food_per_day + 2 * one_way_flight_cost + (days - 1) * one_night_cost

print(total)
