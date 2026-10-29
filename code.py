temperature = int(input("Enter today's temperature in Celsius:"))

if temperature < 20:
    outfit = "jacket"
    print("It's a cold day.")
    print("Wear a", outfit)

else:
    outfit = "t-shirt"
    print("It's a warm day.")
    print("Wear a", outfit)

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter today's wind speed in km/h:"))

if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over you", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today.")
    print("No windbreaker needed over you", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no):")
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

print("")
print("Weather check complete!")

print("=====Weather Outfit Picker=====")
print("temperature:", temperature,)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("================================")