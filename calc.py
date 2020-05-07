import numpy as np
import math
import scipy.signal as sig
import sympy

def calc_signal(A, T, t1, d, fs, kw, values):

    samples_per_period = int(T/(1/fs))
    period_values = values[:samples_per_period]

    srednia = round((1/(period_values[-1]-period_values[0] + 1)) * sum(period_values), 2)
    srednia_bezwzglednia = round((1 / (period_values[-1] - period_values[0] + 1)) * sum(map(lambda x: math.fabs(x), period_values)), 2)
    moc_srednia = round((1 / (period_values[-1]-period_values[0] + 1)) * sum(map(lambda x: x * x, period_values)), 2)
    wariancja = round((1 / (period_values[-1] - period_values[0] + 1)) * sum(map(lambda x: math.pow((x - srednia), 2), period_values)), 2)
    wartosc_skuteczna = round(math.sqrt(moc_srednia), 2)

    print("Obliczone parametry:")
    print("------------------------------")
    print("Wartość średnia sygnału: ", srednia)
    print("Wartość średnia bezwzględna: ", srednia_bezwzglednia)
    print("Moc średnia sygnału: ", moc_srednia)
    print("Wariancja sygnału w przedziale wokół wartości średniej: ", wariancja)
    print("Wartość skuteczna: ", wartosc_skuteczna)
    print("------------------------------")

    return srednia, srednia_bezwzglednia, moc_srednia, wariancja, wartosc_skuteczna

def calc_szum(szum):
    signal = szum
    signal_n1 = szum[0]
    signal_n2 = szum[:1]

    srednia = (1/(signal_n2-signal_n1+1)) * sum(signal)
    srednia_bezwzglednia = (1/(signal_n2-signal_n1+1)) * math.fabs(sum(signal))
    moc_srednia = (1 / (signal_n2 - signal_n1 + 1)) * sum(map(lambda x: x * x, signal))
    wariancja = (1 / (signal_n2 - signal_n1 + 1)) * math.fabs(sum(map(lambda x: x - srednia, signal)))
    wartosc_skuteczna = math.sqrt(moc_srednia)

    print("Obliczone parametry:")
    print("------------------------------")
    print("Wartość średnia sygnału: ", srednia)
    print("Wartość średnia bezwzględna: ", srednia_bezwzglednia)
    print("Moc średnia sygnału: ", moc_srednia)
    print("Wariancja sygnału w przedziale wokół wartości średniej: ", wariancja)
    print("Wartość skuteczna: ", wartosc_skuteczna)

    return srednia, srednia_bezwzglednia, moc_srednia, wariancja, wartosc_skuteczna