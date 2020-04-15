import GUI
import file_operator as files
import signals
import matplotlib.pyplot as plt


def main():
    signal = None
    discrete = False

    if GUI.values['_file_path_'] != '':
        signal = files.read_signal(GUI.values['_file_path_'])
    else:
        values = files.take_input()
        name = values[0]
        A = values[1]
        czestotliwosc_probkowania = values[2]
        t1 = values[3]
        d = values[4]
        T = values[5]
        kw = values[6]
        probki = values[7]
        ns = values[8]
        if name == "Szum o rozkładzie jednostajnym":
            signal = signals.szum_jedn(A, t1, d, probki, "sygnal1")
        elif name == "Sygnał sinusoidalny":
            signal = signals.syg_sin(A, T, t1, d, czestotliwosc_probkowania, "sygnal1")
        elif name == "Sygnał sinusoidalny wyprostowany dwupołówkowo":
            signal = signals.syg_sin_dwupolowkowo(A, T, t1, d, czestotliwosc_probkowania, "sygnal1")
        elif name == "Sygnał sinusoidalny wyprostowany jednopołówkowo":
            signal = signals.syg_sin_jednopolowkowo(A, T, t1, d, czestotliwosc_probkowania, "sygnal1")
        elif name == "Sygnał prostokątny":
            signal = signals.syg_prostokatny(A, T, t1, d, czestotliwosc_probkowania, kw, "sygnal1")
        elif name == "Sygnał prostokątny symetryczny":
            signal = signals.syg_prostokatny_sym(A, T, t1, d, czestotliwosc_probkowania, kw, "sygnal1")
        elif name == "Sygnał trójkątny":
            signal = signals.syg_trojkatny(A, T, t1, d, czestotliwosc_probkowania, kw, "sygnal1")
        elif name == "Impuls jednostkowy":
            discrete = True
            signal = signals.unit_impulse(A, t1, d, czestotliwosc_probkowania, ns, "sygnal1")
        else:
            print("Nie wybrano sygnału")

    signal2 = None
    if GUI.values['_file_path2_'] != '':
        signal2 = files.read_signal(GUI.values['_file_path2_'])
    else:
        values2 = files.take_input2()
        name2 = values2[0]
        A2 = values2[1]
        czestotliwosc_probkowania2 = values2[2]
        t12 = values2[3]
        d2 = values2[4]
        T2 = values2[5]
        kw2 = values2[6]
        probki2 = values2[7]
        ns2 = values[8]
        if name2 == "Szum o rozkładzie jednostajnym":
            signal2 = signals.szum_jedn(A2, t12, d2, probki2, "sygnal2")
        elif name2 == "Sygnał sinusoidalny":
            signal2 = signals.syg_sin(A2, T2, t12, d2, czestotliwosc_probkowania2, "sygnal2")
        elif name2 == "Sygnał sinusoidalny wyprostowany dwupołówkowo":
            signal = signals.syg_sin_dwupolowkowo(A2, T2, t12, d2, czestotliwosc_probkowania2, "sygnal2")
        elif name2 == "Sygnał sinusoidalny wyprostowany jednopołówkowo":
            signal = signals.syg_sin_jednopolowkowo(A2, T2, t12, d2, czestotliwosc_probkowania2, "sygnal2")
        elif name2 == "Sygnał prostokątny":
            signal = signals.syg_prostokatny(A2, T2, t12, d2, czestotliwosc_probkowania2, kw2, "sygnal2")
        elif name2 == "Sygnał prostokątny symetryczny":
            signal2 = signals.syg_prostokatny_sym(A2, T2, t12, d2, czestotliwosc_probkowania2, kw2, "sygnal2")
        elif name2 == "Sygnał trójkątny":
            signal = signals.syg_trojkatny(A2, T2, t12, d2, czestotliwosc_probkowania2, kw2, "sygnal2")
        elif name2 == "Impuls jednostkowy":
            signal = signals.unit_impulse(A2, t12, d2, czestotliwosc_probkowania2, ns2, "sygnal2")
        else:
            print("Nie wybrano sygnału")

    if GUI.values['_operation_'] == "Dodawanie":
        signal = signals.add(signal, signal2)

    signals.draw(signal, discrete)


if __name__ == "__main__":
    main()
