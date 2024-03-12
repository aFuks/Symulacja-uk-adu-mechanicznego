import tkinter as tk
import tkinter.messagebox
import matplotlib.pyplot as plt
import numpy as np

n1 = 1  # zębatka 1
n2 = 1  # zębatka 2
j1 = 1  # wał 1
j2 = 1  # wał 2
k = 1  # spręzyna
b = 1  # tłumik
h = 0.1  # stała całkowania

# listy z obliczonymi przez alhgorytm wartościami
x1 = []
x2 = []
x1euler = []
x2euler = []
# liczniki do zabezpieczeń 
licznik = 0 
licznik2 = 0
licznik3 = 0
licznik4 =0

t = [] # kolejne próbki czasu

#parametry sygnału wejściowego
phi = 0 
amp = 10
frq = 1
czasTrwania = 50

#funkcja przypisująca podane parametry sygnału do odpowiednich zmiennych
def change_signal(entryp, entrya, entryf, entryt, entryhh):
    global phi, amp, frq, czasTrwania, h
    if isfloat(entryp.get()):
        phi = float(entryp.get())
    if isfloat(entrya.get()):
        amp = float(entrya.get())
    if isfloat(entryf.get()):
        frq = float(entryf.get())
    if isfloat(entryt.get()):
        czasTrwania = float(entryt.get())
    if isfloat(entryhh.get()):
        h = float(entryhh.get())

#fukcje tworzące sygnał wejściowy. Odpowiednio: sinusoidalny, prostokątny i trójkątny
def wakeUpWithSin(aktualnyczas):
    tm = np.sin(2 * np.pi * frq * aktualnyczas + phi)
    return tm


def wakeUpWithRec(aktualnyczas):
    global amp
    value = 0
    tm = np.sin(2 * np.pi * frq * aktualnyczas + phi)
    if tm >= 0:
        value = amp
    else:
        value = 0
    return value

def wakeUpWithTri(aktualnyczas):
    tm = np.arcsin(np.sin(2 * np.pi * frq * aktualnyczas + phi)) * 2 / np.pi
    return tm


# sprawdzanie poprawności wprowadzonych danych
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# pobieranie danych z okienka i przypisanie do odpowiedniej zmiennej
def checkData(someEntry):
    global licznik, licznik2
    wejscie = someEntry.get()
    if wejscie != "":
        if isfloat(wejscie):
            licznik2 += 1
        elif licznik == 0:
            tkinter.messagebox.showerror(title="Podana wartość nie jest liczbą.",
                                         message="Sprawdź czy użyłeś kropki dziesiętnej")
            licznik = 1


# pobieranie danych z okienka i przypisanie do odpowiedniej zmiennej
def checkSignal(someEntry):
    global licznik3, licznik4
    wejscie = someEntry.get()
    if wejscie != "":
        if isfloat(wejscie):
            licznik4 += 1
        elif licznik3 == 0:
            tkinter.messagebox.showerror(title="Podana wartość nie jest liczbą.",
                                         message="Sprawdź czy użyłeś kropki dziesiętnej")
            licznik3 = 1


def checkczywszytstkogit():
    global licznik2
    if licznik2 == 6:
        tkinter.messagebox.showinfo(message="Wartości zapisane poprawnie")


