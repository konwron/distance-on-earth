from geopy.geocoders import Nominatim  # needed for finding geo-coordinates
import numpy as np  # needed for measuring distance

geolocator = Nominatim(user_agent="distance-between-cities")

location1 = geolocator.geocode("Wola Rzędzińska, Poland")  # finding 1st place
latitude1 = location1.latitude  # getting latitude of 1st place
longitude1 = location1.longitude  # getting longitude of 1st place

location2 = geolocator.geocode("Kraków, Poland")  # finding 2nd place
latitude2 = location2.latitude  # getting latitude of 2nd place
longitude2 = location2.longitude  # getting longitude of 2nd place

print((location1.address, location1.latitude, location1.longitude))
print((location2.address, location2.latitude, location2.longitude))
