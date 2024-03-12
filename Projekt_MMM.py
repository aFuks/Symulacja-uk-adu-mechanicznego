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

def checkczySignalgit():
    global licznik4
    if licznik4 == 4:
        tkinter.messagebox.showinfo(message="Wartości zapisane poprawnie")

def changelicznik():
    global licznik
    licznik = 0


def changelicznik2():
    global licznik2
    licznik2 = 0

def changesignalliczniki():
    global licznik3, licznik4
    licznik4 = 0
    licznik3 = 0
def changen1(entry1, entry2, entry3, entry4, entry5, entry6):
    global n1, n2, j1, j2, k, b
    if isfloat(entry1.get()):
        n1 = float(entry1.get())
    if isfloat(entry2.get()):
        n2 = float(entry2.get())
    if isfloat(entry3.get()):
        j1 = float(entry3.get())
    if isfloat(entry4.get()):
        j2 = float(entry4.get())
    if isfloat(entry5.get()):
        b = float(entry5.get())
    if isfloat(entry6.get()):
        b = float(entry6.get())


def rownanienax1(x2poprzedni):
    x1prim = x2poprzedni
    return x1prim


def rownanienax2(x2poprzedni, x1poprzedni, aktualnyczas, option):
    global amp
    value = option.get()
    if value == "sine":
        x2prim = (-b * x2poprzedni * n2 / n1 - k * x1poprzedni + wakeUpWithSin(aktualnyczas) * amp * n2 / n1) / (
                j1 + j2 * n2 / n1)
    elif value == "rectangle":
        x2prim = (-b * x2poprzedni * n2 / n1 - k * x1poprzedni + wakeUpWithRec(aktualnyczas) * amp * n2 / n1) / (
                j1 + j2 * n2 / n1)
    elif value == "triangle":
        x2prim = (-b * x2poprzedni * n2 / n1 - k * x1poprzedni + wakeUpWithTri(aktualnyczas) * amp * n2 / n1) / (
                j1 + j2 * n2 / n1)

    return x2prim

def RungeKutta4stopnia(option):
    x1.clear()
    x2.clear()
    t.clear()
    x1.append(0)
    x2.append(0)
    t.append(0)
    tnowy = 0

    # liczenie kolejnych wartości x2 i x1
    for i in range(1, int(czasTrwania / h)):
        k1 = h * rownanienax2(x2[i - 1], x1[i - 1], t[i - 1], option)
        l1 = h * rownanienax1(x2[i - 1])

        k2 = h * rownanienax2(x2[i - 1] + k1 / 2, x1[i - 1] + h / 2, t[i - 1], option)
        l2 = h * rownanienax1(x2[i - 1] + h / 2)

        k3 = h * rownanienax2(x2[i - 1] + k2 / 2, x1[i - 1] + h / 2, t[i - 1], option)
        l3 = h * rownanienax1(x2[i - 1] + h / 2)

        k4 = h * rownanienax2(x2[i - 1] + k3, x1[i - 1] + h, t[i - 1], option)
        l4 = h * rownanienax1(x2[i - 1] + h)

        x2nowy = x2[i - 1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x2.append(x2nowy)
        x1nowy = x1[i - 1] + 1 / 6 * (l1 + 2 * l2 + 2 * l3 + l4)
        x1.append(x1nowy)
        tnowy = tnowy + h
        t.append(tnowy)


def euler(option):
    x1euler.clear()
    x2euler.clear()
    x1euler.append(0)
    x2euler.append(0)
    t.clear()
    t.append(0)
    tnowy = 0

    for i in range(1, int(czasTrwania / h)):
        k1 = h * rownanienax2(x2euler[i - 1], x1euler[i - 1], t[i - 1], option)
        l1 = h * rownanienax1(x2euler[i - 1])

        x2nowye = x2euler[i - 1] + k1
        x2euler.append(x2nowye)
        x1nowye = x1euler[i - 1] + l1
        x1euler.append(x1nowye)
        tnowy = tnowy + h
        t.append(tnowy)

def rysujx2x1():
    fig, axs = plt.subplots(4)
    fig.suptitle('Angle and Angular Velocity Respectivly')
    axs[0].plot(t, x1)
    axs[1].plot(t, x2)
    axs[2].plot(t, x1euler)
    axs[3].plot(t, x2euler)
    plt.show()
    for i in range(1, 500):
        print(x2[i])
        print(x2euler[i])


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Projekt MMM')
        self.geometry("900x700")

        opcja = tk.StringVar()

        # inputs
        entryn1 = tk.Entry(width=9, border=5)
        entryn1.place(x=40, y=20)
        entryn1.insert(0, "1")
        entryn2 = tk.Entry(width=9, border=5)
        entryn2.place(x=40, y=70)
        entryn2.insert(0, "1")
        entryj1 = tk.Entry(width=9, border=5)
        entryj1.place(x=40, y=120)
        entryj1.insert(0, "1")
        entryj2 = tk.Entry(width=9, border=5)
        entryj2.place(x=40, y=170)
        entryj2.insert(0, "1")
        entryk = tk.Entry(width=9, border=5)
        entryk.place(x=40, y=220)
        entryk.insert(0, "1")
        entryb = tk.Entry(width=9, border=5)
        entryb.place(x=40, y=270)
        entryb.insert(0, "1")
        entrytime = tk.Entry(width=9, border=5)
        entrytime.place(x=270, y=20)
        entrytime.insert(0, "50")
        entryamp = tk.Entry(width=9, border=5)
        entryamp.place(x=270, y=70)
        entryamp.insert(0, "10")
        entryfrq = tk.Entry(width=9, border=5)
        entryfrq.place(x=270, y=120)
        entryfrq.insert(0, "1")
        entryphase = tk.Entry(width=9, border=5)
        entryphase.place(x=270, y=170)
        entryphase.insert(0, "1")
        var = tk.IntVar()
        # labels that show values of variables
        labeln1 = tk.Label(text="n1 =")
        labeln1.place(x=10, y=20)

        labeln2 = tk.Label(text="n2 =")
        labeln2.place(x=10, y=70)

        labelj1 = tk.Label(text="j1 =")
        labelj1.place(x=10, y=120)

        labelj2 = tk.Label(text="j2 =")
        labelj2.place(x=10, y=170)

        labelk = tk.Label(text="k =")
        labelk.place(x=10, y=220)

        labelb = tk.Label(text="b =")
        labelb.place(x=10, y=270)

        labeltime = tk.Label(text="simulation time:")
        labeltime.place(x=160, y=20)

        labelAmp = tk.Label(text="amplitude =")
        labelAmp.place(x=160, y=70)

        labelFrq = tk.Label(text="frequency =")
        labelFrq.place(x=160, y=120)

        labelphase = tk.Label(text="phase =")
        labelphase.place(x=160, y=170)
