import requests

# Step 1: Prompt user for vehicle mileage
mileage = float(input("Enter your vehicle's mileage: "))

# Step 2: Ask for current location and destination
current_location = input("Enter your current location: ")
destination = input("Enter your destination: ")

# Step 3: Calculate distance between current location and destination using Google Maps API
maps_url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={current_location}&destinations={destination}&mode=driving&key={YOUR_API_KEY}"
maps_response = requests.get(maps_url).json()
# distance in meters
distance = maps_response["rows"][0]["elements"][0]["distance"]["value"]

# Step 4: Retrieve current fuel price in current location using GasBuddy API
gas_url = f"https://api.gasbuddy.com/gasprices/location/{YOUR_LOCATION_ID}?apikey={YOUR_API_KEY}"
gas_response = requests.get(gas_url).json()
fuel_price = gas_response["FuelPrices"][0]["Price"]  # fuel price in USD

# Step 5: Calculate total cost of fuel for trip
total_cost = (distance / mileage) * fuel_price

# Step 6: Display total cost to user
print(f"The total cost of fuel for your trip will be ${total_cost:.2f}.")

'''
Please note that you need to replace "API_KEY" with your actual API key for the above code to work properly. 
Also, it is important to notice that the code above uses Indian Oil Corp API to get the fuel price, 
you should check if the API is available and working in your region, 
if not you should use another API that is available in your region.

'''
