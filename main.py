from geopy.geocoders import Nominatim       # needed for finding geo-coordinates
from math import *                          # needed for measuring distance
# from tkinter import *                       # GUI
# from tkinter import filedialog, constants, messagebox


deg_to_rad = float(pi / 180.0)
radius = 6371       # 6371 km OR 3959 miles according to wikipedia

loc1_input = input("Wpisz pierwszą lokalizację: ")
loc2_input = input("Wpisz drugą lokalizację: ")

geolocator = Nominatim(user_agent="distance-on-earth")
location1 = geolocator.geocode(loc1_input)      # find 1st location
location2 = geolocator.geocode(loc2_input)      # find 2nd location


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


# tkinter configuration


# window = Tk()       # tworzenie okna głównego programu
#
# window.geometry("600x400")      # rozmiar okna programu
# window.columnconfigure(0, weight=1)
# window.rowconfigure(0, weight=1)
# window.title("Oblicz odległość pomiędzy dwoma punktami na kuli ziemskiej")      # ustawienie tytułu okna
#
#
# location1_input = StringVar()
# location1_description = Label(window, text="Podaj pierwszą lokalizację").pack()
# location1_entry = Entry(window, width=40)
# location1_entry.pack()     # Miejsce do wprowadzenia nazwy pierwszego miasta
#
#
# location2_input = StringVar()
# location2_description = Label(window, text="Podaj drugą lokalizację").pack()
# location2_entry = Entry(window, width=40)
# location2_entry.pack()     # Miejsce do wprowadzenia nazwy drugiego miasta
#
#
# rb_var = StringVar()  # zmienna sterująca zaznaczeniem kontrolki
# rb_kilometres = Radiobutton(window, variable=rb_var, value=6371, text="kilometry")        # kontrolka pierwsza
# rb_miles = Radiobutton(window, variable=rb_var, value=3959, text="mile")
# rb_var.set("km")    # ustawiam zaznaczenie na kontrolkę dla opcji kilometres
# rb_kilometres.pack()
# rb_miles.pack()     # Radiobutton z wyborem miar długości (km/miles)
#
# lokalizacja = Button(window, text="Oblicz", width=20, command=haversine_formula)
# lokalizacja.pack()   # Wynik: w zaleźności od wyboru km lub mil wypisana będzie dana wartość adekwatna do miary długości
#
# window.bind('<Return>', haversine_formula)
#
# window.mainloop()       # wywołanie głównej pętli programu


# print(haversine_formula(location1, location2))

print("Odlegość między tymi miejscami wynosi: {} km".format(haversine_formula(location1, location2)))
