#Section 1 — Lists and Tuples

#1.Print the third room price.
room_prices = [2500, 3200, 4500, 2800, 5000, 3800, 4200]

room_types = [
    "Standard",
    "Deluxe",
    "Suite",
    "Standard",
    "Suite",
    "Deluxe",
    "Premium"
]

hotel_details = ("Grand Palace", "Jaipur", 120)

print(room_prices[2])
#2.Print the last three room prices using slicing.
print(room_prices[-3:])
#3.Change the second room price to 3500.
room_prices[1] = 3500
print(room_prices[1])
#4.Add a new room price of 5500.
room_prices.append(5500)
print(room_prices)
#5.Remove the room price 2800.
room_prices.remove(2800)
print(room_prices)
#6.Sort the room prices in ascending order.
room_prices.sort()
print(room_prices)
#7.Find the highest and lowest room prices.
print(max(room_prices))
print(min(room_prices))
#8.Calculate the average room price.
total = sum(room_prices)
avg_price = total/len(room_prices)
print(round(avg_price,2))
#9.Create a new list containing only room prices above 4000 using list comprehension.
new_list = [
    price for price in room_prices if price > 4000
]
print(new_list)
#10.Print the hotel name, city and total number of rooms using tuple indexing.
print(hotel_details[0])   #printing hotel name
print(hotel_details[1])   #printing city
print(hotel_details[2])   #printing number of rooms.

#11.Explain why a tuple may be suitable for storing fixed hotel details.
'''A tuple may be suitable for storing fixed hotel records because a tuple is immutable i.e. the elements cannot be
changed after it's creation.'''