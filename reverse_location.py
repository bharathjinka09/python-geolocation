from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="reverse_location")

location = geolocator.reverse("14.9069559, 78.0097071")
print(location.address)
# Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
print((location.latitude, location.longitude))
# (52.5094982, 13.3765983)
print(location.raw)