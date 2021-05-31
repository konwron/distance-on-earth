from geopy.geocoders import Nominatim       # biblioteka potrzebna do pobierania współrzędnych
from math import *                          # biblioteka potrzebna do obliczania dystansu
from tkinter import *                       # GUI


def main(*args):    # główna funkcja programu z opcjonalnymi argumentami

    geolocator = Nominatim(user_agent='distance-on-earth')  # wybór API do wyszukania miejsc - Nominatim (OpenStreetMap)
    loc1 = geolocator.geocode(loc1_entry.get())  # szukanie współrzędnych 1 miejsca
    loc2 = geolocator.geocode(loc2_entry.get())  # szukanie współrzędnych 2 miejsca
    try:
        radius = 3958.8 if (radius_rb.get()) == 'mi' else 6371      # promień Ziemi: 6371 km lub 3958.8 mi (Wikipedia)

        result = haversine_formula(loc1, loc2, radius)

        print('Odległość między {} i {} wynosi {} {}.\n'.format(loc1_entry.get(), loc2_entry.get(), result, radius_rb.get()))
    except AttributeError:
        print(loc1, loc2)
        if not loc1:
            print('Podaj istniejącą lokalizację')
        if not loc2:
            print('Podaj istniejącą lokalizację')


# Metoda Haversine'a
def haversine_formula(loc1, loc2, radius):

    lat1 = loc1.latitude        # szerokość geograficzna 1 miejsca
    lon1 = loc1.longitude       # długość geograficzna 1 miejsca

    lat2 = loc2.latitude        # szerokość geograficzna 2 miejsca
    lon2 = loc2.longitude       # długość geograficzna 2 miejsca

    deg_to_rad = float(pi / 180.0)

    lat_distance = (lat2 - lat1) * deg_to_rad       # zamiana stopni na radiany
    lon_distance = (lon2 - lon1) * deg_to_rad

    # obliczanie na podstawie wzoru (https://en.wikipedia.org/wiki/Haversine_formula)
    a = pow(sin(lat_distance / 2), 2) + cos(lat1 * deg_to_rad) * cos(lat2 * deg_to_rad) * pow(sin(lon_distance / 2), 2)

    c = round(2 * atan2(sqrt(a), sqrt(1 - a)), 3)       # wynik zaokrąglony do 3 miejsc po przecinku

    return radius * c


def Quit(event):
    quit()


# tworzenie GUI (interfejsu użytkownika)
window = Tk()       # tworzenie okna głównego programu
window.geometry('600x400')      # rozmiar okna programu
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.title('Oblicz odległość pomiędzy dwoma punktami na kuli ziemskiej')      # ustawienie tytułu okna

loc1_input = StringVar()
loc1_description = Label(window, text='Podaj pierwszą lokalizację').pack()
loc1_entry = Entry(window, width=40)
loc1_entry.pack()     # miejsce do wprowadzenia nazwy pierwszego miasta

loc2_input = StringVar()
loc2_description = Label(window, text='Podaj drugą lokalizację').pack()
loc2_entry = Entry(window, width=40)
loc2_entry.pack()     # miejsce do wprowadzenia nazwy drugiego miasta

radius_rb = StringVar()  # zmienna sterująca zaznaczeniem kontrolki
rb_frame = LabelFrame(window, text='Wybierz jednostkę miary')
rb_frame.pack()
km_rb = Radiobutton(rb_frame, variable=radius_rb, value='km', indicator=0, text='kilometry')
km_rb.pack(fill=X, ipady=5)
mi_rb = Radiobutton(rb_frame, variable=radius_rb, value='mi', indicator=0, text='mile')
mi_rb.pack(fill=X, ipady=5)
radius_rb.set('km')    # ustawiam początkowe zaznaczenie na kontrolkę km

run = Button(window, text='Oblicz', width=20, command=main)
run.pack()   # wypisana będzie wartość adekwatna do miary długości

window.bind('<Return>', main)
window.bind("<KeyPress-Escape>", Quit)

window.mainloop()       # nasłuchiwanie zdarzeń z Tkintera

# WERSJA UNIWERSALNA, Z UŻYCIEM LAMBDA (lambda jest potrzebna, by przekazać argumenty do wywoływanej funkcji)

# def main(loc1_name, loc2_name, unit):
#     geolocator = Nominatim(user_agent="distance-on-earth")
#     loc1 = geolocator.geocode(loc1_name)
#     loc2 = geolocator.geocode(loc2_name)
#
#     radius = 3958.8 if unit == "mi" else 6371
#
#     result = haversine_formula(loc1, loc2, radius)
#
#     print("Odległość między {} i {} wynosi {} {}.\n".format(loc1_name, loc2_name, result, unit))

# run = Button(window, text="Oblicz", width=20, command=lambda: main(loc1_entry.get(), loc2_entry.get(), radius_rb.get()))

# window.bind('<Return>', lambda event: main(loc1_entry.get(), loc2_entry.get(), radius_rb.get()))