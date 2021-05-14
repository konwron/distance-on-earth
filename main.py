from geopy.geocoders import Nominatim       # needed for finding geo-coordinates
from math import *                          # needed for measuring distance

deg_to_rad = float(pi / 180.0)
radius = 6371       # 6371 km OR 3959 miles according to wikipedia
# !!! zamienić na wartość odpowiadającą zaznaczonemu radio buttonowi !!!

geolocator = Nominatim(user_agent="distance-on-earth")
location1 = geolocator.geocode("Rzeszów")       # find 1st location
location2 = geolocator.geocode("Kraków")        # find 2nd location
# !!! zamienić stringi na wartości inputów !!!


# haversine formula
def haversine_formula(loc1, loc2):

    lat1 = loc1.latitude        # get latitude of 1st location
    lon1 = loc1.longitude       # get longitude of 1st location

    lat2 = loc2.latitude        # get latitude of 2nd location
    lon2 = loc2.longitude       # get longitude of 2nd location

    lat_distance = (lat2 - lat1) * deg_to_rad
    lon_distance = (lon2 - lon1) * deg_to_rad

    a = pow(sin(lat_distance / 2), 2) + cos(lat1 * deg_to_rad) * cos(lat2 * deg_to_rad) * pow(sin(lon_distance / 2), 2)

    c = round(2 * atan2(sqrt(a), sqrt(1 - a)), 3)

    return radius * c


print(haversine_formula(location1, location2))
