from geopy.geocoders import Nominatim       # biblioteka potrzebna do pobierania współrzędnych
from math import *                          # biblioteka potrzebna do obliczania dystansu
from tkinter import *                       # GUI


def main(loc1_name, loc2_name):
    geolocator = Nominatim(user_agent="distance-on-earth")  # wybór API do wyszukania miejsc - Nominatim (OpenStreetMap)
    loc1 = geolocator.geocode(loc1_name.get())  # szukanie współrzędnych 1 miejsca
    loc2 = geolocator.geocode(loc2_name.get())  # szukanie współrzędnych 2 miejsca
    radius = 6371  # promień: 6371 km lub 3959 mil (Wikipedia)

    result = haversine_formula(loc1, loc2, radius)

    print("Odległość: {}".format(result))


# Metoda Haversine'a
def haversine_formula(loc1, loc2, rad):

    lat1 = loc1.latitude  # szerokość geograficzna 1 miejsca
    lon1 = loc1.longitude  # długość geograficzna 1 miejsca

    lat2 = loc2.latitude  # szerokość geograficzna 2 miejsca
    lon2 = loc2.longitude  # długość geograficzna 2 miejsca

    deg_to_rad = float(pi / 180.0)

    lat_distance = (lat2 - lat1) * deg_to_rad  # zamiana stopni na radiany
    lon_distance = (lon2 - lon1) * deg_to_rad

    # obliczanie na podstawie wzoru (https://en.wikipedia.org/wiki/Haversine_formula)
    a = pow(sin(lat_distance / 2), 2) + cos(lat1 * deg_to_rad) * cos(lat2 * deg_to_rad) * pow(sin(lon_distance / 2), 2)

    c = round(2 * atan2(sqrt(a), sqrt(1 - a)), 3)  # wynik zaokrąglony do 3 miejsc po przecinku

    return rad * c


# tworzenie GUI (interfejsu użytkownika)
window = Tk()       # tworzenie okna głównego programu
window.geometry("600x400")      # rozmiar okna programu
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.title("Oblicz odległość pomiędzy dwoma punktami na kuli ziemskiej")      # ustawienie tytułu okna

loc1_input = StringVar()
loc1_description = Label(window, text="Podaj pierwszą lokalizację").pack()
loc1_entry = Entry(window, width=40)
loc1_entry.pack()     # miejsce do wprowadzenia nazwy pierwszego miasta


loc2_input = StringVar()
loc2_description = Label(window, text="Podaj drugą lokalizację").pack()
loc2_entry = Entry(window, width=40)
loc2_entry.pack()     # miejsce do wprowadzenia nazwy drugiego miasta


# rb_var = StringVar()  # zmienna sterująca zaznaczeniem kontrolki
# rb_kilometres = Radiobutton(window, variable=rb_var, value=6371, text="kilometry")        # kontrolka pierwsza
# rb_miles = Radiobutton(window, variable=rb_var, value=3959, text="mile")
# rb_var.set("km")    # ustawiam zaznaczenie na kontrolkę dla opcji kilometres
# rb_kilometres.pack()
# rb_miles.pack()     # Radiobutton z wyborem miar długości (km/miles)

lokalizacja = Button(window, text="Oblicz", width=20, command=lambda: main(loc1_entry, loc2_entry))
lokalizacja.pack()   # wynik: wypisana będzie wartość adekwatna do miary długości

window.bind('<Return>', lambda event: main(loc1_entry, loc2_entry))

window.mainloop()       # wywołanie głównej pętli programu

















# print("Odlegość między tymi miejscami wynosi: {} km".format(haversine_formula(location1, location2)))
