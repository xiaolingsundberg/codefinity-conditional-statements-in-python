# Given temperature value
temperature = 21
weather_status = 'blank'
outdoor_advice = 'blank'

# Determine weather status
if temperature > 30:
    weather_status = "Hot"
elif 15 <= temperature <= 30:
    weather_status = "Warm"
elif 14 <= temperature <= 0:
    weather_status = "Cool"
else:
    weather_status = "Cold"

# Determine outdoor advice
if weather_status == 'Hot':
    outdoor_advice = "Stay hydrated"
elif weather_status == 'Warm' or 'Cool':
    outdoor_advice = "Great weather for a walk"
else:
    outdoor_advice = "Wear a coat"

# Testing the results
print("Weather status:", weather_status)
print("Outdoor advice:", outdoor_advice)