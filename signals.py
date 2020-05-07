import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import calc
import GUI


def syg_sin(A, T, t1, d, fs, filename):
    f = 1/T
    # TODO:Może jakoś lepiej zabezpieczyć się przed nie spełnieniem twierdzenia o próbkowaniu
    if((fs/2)<f):
        np.savez(filename, 0, 0)
        return (0, 0)

    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    sinus = A*np.sin(2*np.pi*f * n)
    x = calc.calc_signal(A, T, t1, d, fs, 0, sinus)
    params = np.array([t1, fs, A, T, d, 0])
    np.savez(filename, params, sinus)

    return params, sinus

def syg_sin_jednopolowkowo(A, T, t1, d, fs, filename):
    f = 1/T
    if((fs/2)<f):
        np.savez(filename, 0, 0)
        return (0, 0)

    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    sinus = 0.5*A*(np.sin(2*np.pi*f * n) + np.fabs(np.sin(2*np.pi*f * n)))
    x = calc.calc_signal(A, T, t1, d, fs, 0, sinus)
    params = np.array([t1, fs, A, T, d, 0])
    np.savez(filename, params, sinus)

    return params, sinus


def syg_sin_dwupolowkowo(A, T, t1, d, fs, filename):
    f = 1/T
    if((fs/2)<f):
        np.savez(filename, 0, 0)
        return (0, 0)

    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    sinus = A*np.fabs(np.sin(2*np.pi*f * n))
    x = calc.calc_signal(A, T, t1, d, fs, 0, sinus)
    params = np.array([t1, fs, A, T, d, 0])
    np.savez(filename, params, sinus)

    return params, sinus

def syg_prostokatny(A, T, t1, d, fs, kw, filename):
    f = 1/T
    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    prostokat = (A/2)*sig.square(2 * np.pi * f * n, duty=kw)+(A/2)

    x = calc.calc_signal(A, T, t1, d, fs, kw, prostokat)
    params = np.array([t1, fs, A, T, d, kw])
    np.savez(filename, params, prostokat)

    return params, prostokat


def syg_prostokatny_sym(A, T, t1, d, fs, kw, filename):
    f = 1/T
    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    prostokat = A*sig.square(2 * np.pi * f * n, duty=kw)

    x = calc.calc_signal(A, T, t1, d, fs, kw, prostokat)
    params = np.array([t1, fs, A, T, d, kw])
    np.savez(filename, params, prostokat)

    return params, prostokat


def syg_trojkatny(A, T, t1, d, fs, kw, filename):
    f = 1/T
    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    trojkat = (A/2)*sig.sawtooth(2 * np.pi * f * n, kw)+(A/2)

    x = calc.calc_signal(A, T, t1, d, fs, kw, trojkat)
    params = np.array([t1, fs, A, T, d, kw])
    np.savez(filename, params, trojkat)

    return params, trojkat


def szum_jedn(A, t1, d, N, filename):
    fs = d/N
    szum = np.random.uniform(-A, A, N)

    x = calc.calc_signal(A, 0, t1, d, fs, 0, szum)
    params = np.array([t1, fs, A, 0, d, 0])
    np.savez(filename, params, szum)

    return params, szum


def unit_impulse(A, t1, d, fs, filename):
    ns = int(GUI.values['_ns_'])
    t2 = t1 + d
    N = int(d * fs)
    n = np.linspace(t1, t2, N)
    impuls = A*sig.unit_impulse(N, ns)
    x = calc.calc_signal(A, 0, t1, d, fs, 0, impuls)
    params = np.array([t1, fs, A, 0, d, 0])
    np.savez(filename, params, impuls)

    return params, impuls


def draw(signal, discrete, x):
    histogram = GUI.values['_histogram_']
    params = signal[0]
    t1 = params[0]
    fs = params[1]
    time_signal = np.linspace(t1, (t1+(1/fs)*len(signal[1])), len(signal[1]))
    plt.figure(x)
    plt.subplot(3, 1, 1)
    if discrete == False:
        plt.scatter(time_signal, signal[1], linewidth=1)
    else:
        plt.plot(time_signal, signal[1])
    plt.xlabel('czas [s]')
    plt.ylabel('amplituda')
    plt.title('Sygnał')
    plt.axhline(y=0, color='k', lw=0.2)
    plt.axvline(x=0, color='k', lw=0.2)

    plt.subplot(3, 1, 3)
    plt.hist(signal[1], histogram, facecolor='blue', alpha=0.75)

    plt.show(block=False)


def signal_operation(signal1, signal2):
    input_params1 = signal1[0]
    input_signal1 = signal1[1]
    input_params2 = signal2[0]
    input_signal2 = signal2[1]
    A_1 = input_params1[2]      #amplituda
    A_2 = input_params2[2]
    T_1 = input_params1[3]      #okres
    T_2 = input_params2[3]
    t1_1 = input_params1[0]     #czas początkowy
    t1_2 = input_params2[0]
    d_1 = input_params1[4]      #czas trwania
    d_2 = input_params2[4]
    fs_1 = input_params1[1]     #czestotliwosc probkowania
    fs_2 = input_params2[1]
    kw_1 = input_params1[5]     #wspolczynnik wypelnienia
    kw_2 = input_params2[5]

    #jeśli częstotliwości sygnałów nie są sobie równe, należy je przesamplować
    if(fs_1 != fs_2):
        if(fs_1 > fs_2):
            input_signal2 = sig.resample_poly(input_signal2, fs_1, fs_2)
            fs_2 = fs_1
        if (fs_2 > fs_1):
            input_signal1 = sig.resample_poly(input_signal1, fs_2, fs_1)
            fs_1 = fs_2

    if t1_1 == t1_2:
        if d_1 > d_2:
            input_signal2 = input_signal2.tolist()
            empty_signal = [0 for i in range(int((d_1-d_2)/(1/fs_1)))]
            input_signal2.extend(empty_signal)
            input_signal2 = np.array(input_signal2)
        elif d_2 > d_1:
            input_signal1 = input_signal1.tolist()
            empty_signal = [0 for i in range(int((d_2-d_1)/(1/fs_2)))]
            input_signal1.extend(empty_signal)
            input_signal1 = np.array(input_signal2)

        if GUI.values['_operation_'] == "Dodawanie":
            output_signal = input_signal1 + input_signal2
        elif GUI.values['_operation_'] == "Odejmowanie":
            output_signal = input_signal1 - input_signal2
        elif GUI.values['_operation_'] == "Mnożenie":
            output_signal = input_signal1 * input_signal2
        elif GUI.values['_operation_'] == "Dzielenie":
            output_signal = np.divide(input_signal1, input_signal2, out=np.zeros_like(input_signal1), where=input_signal2 != 0)
        output_signal_parmas = np.array([t1_1, fs_1])

    elif t1_1 > t1_2:
        a = int((t1_1-t1_2)/(1/fs_1))
        tmp_signal = [0 for i in range(a)]
        tmp_signal.extend(input_signal1)
#        empty_signal = [0 for i in range(a)]
        input_signal2 = input_signal2.tolist()
#        input_signal2.extend(empty_signal)
        d_1 = d_1 + (1/fs_1)*a
        if(d_1 > d_2):
            empty_signal = [0 for i in range(int((d_1-d_2)/(1/fs_1)))]
            input_signal2.extend(empty_signal)
        elif(d_2 > d_1):
            empty_array = [0 for i in range(int((d_2-d_1)/(1/fs_2)))]
            tmp_signal.extend(empty_array)
        tmp_signal = np.array(tmp_signal)
        input_signal2 = np.array(input_signal2)

        if GUI.values['_operation_'] == "Dodawanie":
            output_signal = tmp_signal + input_signal2
        elif GUI.values['_operation_'] == "Odejmowanie":
            output_signal = tmp_signal - input_signal2
        elif GUI.values['_operation_'] == "Mnożenie":
            output_signal = tmp_signal * input_signal2
        elif GUI.values['_operation_'] == "Dzielenie":
            output_signal = np.divide(tmp_signal, input_signal2, out=np.zeros_like(tmp_signal), where=input_signal2 != 0)
        output_signal_parmas = np.array([t1_2, fs_1])

    elif(t1_2 > t1_1):
        a = int((t1_2-t1_1)/(1/fs_2))
        tmp_signal = [0 for i in range(a)]
        tmp_signal.extend(input_signal2)
#        empty_signal = [0 for i in range(a)]
        input_signal1 = input_signal1.tolist()
#        input_signal1.extend(empty_signal)
        d_2 = d_2 + (1/fs_2)*a
        if(d_1 > d_2):
            empty_signal = [0 for i in range(int((d_1-d_2)/(1/fs_1)))]
            tmp_signal.extend(empty_signal)
        elif(d_2 > d_1):
            empty_array = [0 for i in range(int((d_2-d_1)/(1/fs_2)))]
            input_signal1.extend(empty_array)
        tmp_signal = np.array(tmp_signal)
        input_signal1 = np.array(input_signal1)

        if GUI.values['_operation_'] == "Dodawanie":
            output_signal = tmp_signal + input_signal1
        elif GUI.values['_operation_'] == "Odejmowanie":
            output_signal = tmp_signal - input_signal1
        elif GUI.values['_operation_'] == "Mnożenie":
            output_signal = tmp_signal * input_signal1
        elif GUI.values['_operation_'] == "Dzielenie":
            output_signal = np.divide(tmp_signal, input_signal1, out=np.zeros_like(tmp_signal), where=input_signal1 != 0)

        output_signal_parmas = np.array([t1_1, fs_2])

    filename = GUI.values['_filename_']
    np.savez(filename, output_signal_parmas, output_signal)
    return output_signal_parmas, output_signal
