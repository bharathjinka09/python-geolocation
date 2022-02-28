from geopy.geocoders import Nominatim
# user_agent is python file name (if app.py then app)

geolocator = Nominatim(user_agent="app")
location = geolocator.geocode("Tadipatri")
print(location)
print("--------------")
print(location.address)
# Tadipatri, Tadpatri, Anantapur, Andhra Pradesh, 515400, India
print((location.latitude, location.longitude))
# (40.7410861, -73.9896297241625)
print(location.raw)