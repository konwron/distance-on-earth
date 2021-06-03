from geopy.geocoders import Nominatim       # biblioteka potrzebna do pobierania współrzędnych
from math import *                          # biblioteka potrzebna do obliczania dystansu
from tkinter import *                       # GUI


def main(*args):    # główna funkcja programu z opcjonalnymi argumentami

    geolocator = Nominatim(user_agent='distance-on-earth')  # wybór API do wyszukania miejsc - Nominatim (OpenStreetMap)
    loc1 = geolocator.geocode(loc1_entry.get())             # szukanie współrzędnych 1 miejsca
    loc2 = geolocator.geocode(loc2_entry.get())             # szukanie współrzędnych 2 miejsca

    loc1_error_text.set('')
    loc2_error_text.set('')
    result_text.set('')
    try:
        radius = 3958.8 if (radius_rb.get()) == 'mi' else 6371      # promień Ziemi: 6371 km lub 3958.8 mi (Wikipedia)

        result = haversine_formula(loc1, loc2, radius)

        result_text.set('{} {}'.format(result, radius_rb.get()))
        print(loc1, loc2)
    except AttributeError:      # obsługa błędu, gdy nic nie zostanie wpisane przez użytkownika, lub zostanie wpisana nieistaniejąca lokalizacja
        print(loc1, loc2)
        if not loc1:
            loc1_error_text.set('Podaj istniejącą lokalizację')
        if not loc2:
            loc2_error_text.set('Podaj istniejącą lokalizację')


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

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return round(radius * c, 3)     # wynik zaokrąglony do 3 miejsc po przecinku


def Quit(event):        # funkcja zamykająca program
    quit()


# tworzenie GUI (interfejsu użytkownika)
window = Tk()                                                               # tworzenie okna głównego programu
window.configure(padx=80, pady=30)                                          # ustawienie marginesów w oknie
window.title('Oblicz odległość pomiędzy dwoma punktami na kuli ziemskiej')  # ustawienie tytułu okna

loc1_description = Label(window, text='Podaj pierwszą lokalizację')
loc1_description.grid(row=0, column=0)                              # ustawienie położenia na podstawie siatki (0,0)
loc1_entry = Entry(window)                                          # miejsce do wprowadzenia nazwy pierwszego miejsca
loc1_entry.grid(row=0, column=1, sticky=EW)                         # ustawienie położenia na podstawie siatki (0,1)

loc1_error_text = StringVar()                                           # tekst błędu
loc1_error_msg = Label(window, textvariable=loc1_error_text, fg='red')  # błąd wyskakujący po wprowadzeniu błędnej nazwy
loc1_error_msg.grid(row=1, column=1, pady=(0, 15))                      # ustawienie położenia na podstawie siatki (1,1)

loc2_description = Label(window, text='Podaj drugą lokalizację')
loc2_description.grid(row=2, column=0)                                  # ustawienie położenia na podstawie siatki (2,0)
loc2_entry = Entry(window)                                              # miejsce do wprowadzenia nazwy drugiego miejsca
loc2_entry.grid(row=2, column=1, sticky=EW)                             # ustawienie położenia na podstawie siatki (2,1)

loc2_error_text = StringVar()                                           # tekst błędu
loc2_error_msg = Label(window, textvariable=loc2_error_text, fg='red')  # błąd wyskakujący po wprowadzeniu błędnej nazwy
loc2_error_msg.grid(row=3, column=1, pady=(0, 15))                      # ustawienie położenia na podstawie siatki (3,1)

radius_rb = StringVar()     # zmienna przechowująca wartość (value) zaznaczonej kontrolki
rb_frame = LabelFrame(window, text='Wybierz jednostkę miary')       # przestrzeń z kontrolkami
rb_frame.grid(row=4, column=0, rowspan=2)
km_rb = Radiobutton(rb_frame, variable=radius_rb, value='km', indicator=0, text='kilometry')    # kontrolka - kilometry
km_rb.pack(fill=X, ipady=5, padx=5)
mi_rb = Radiobutton(rb_frame, variable=radius_rb, value='mi', indicator=0, text='mile')         # kontrolka - mile
mi_rb.pack(fill=X, ipady=5, padx=5, pady=5)
radius_rb.set('km')    # początkowe zaznaczenie na kontrolkę km

result_label = Label(window, text='Odległość: ', font=25)
result_label.grid(row=6, column=0, pady=5)
result_text = StringVar()       # zmienna przechowująca wynik (odległość)
result_entry = Entry(window, textvariable=result_text, state=DISABLED, font=25, fg='black', cursor='arrow')
result_entry.grid(row=6, column=1, pady=5, padx=5)

run = Button(window, text='Oblicz', command=main)                # przycisk - wciśnięcie powoduje wywołanie funkcji main
run.grid(row=7, column=1, ipadx=50, ipady=10, padx=5, sticky=E)  # wypisana będzie wartość adekwatna do miary długości

window.bind('<Return>', main)               # uruchomienie programu po wciśnięciu Enter
window.bind("<KeyPress-Escape>", Quit)      # obsługa wyjścia z GUI za pomocą przycisku Esc

window.mainloop()       # nasłuchiwanie zdarzeń z Tkintera
