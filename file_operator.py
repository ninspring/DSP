import GUI
import numpy as np


def take_input():
    file_1_path = GUI.values['_file_path_']
    name = GUI.values['_generate_what_']
    A = float(GUI.values['_amplitude_'])
    czestotliwosc_probkowania = int(GUI.values['_czestotliwosc_probkowania_'])
    t1 = int(GUI.values['_t1_'])
    d = float(GUI.values['_d_'])
    T = float(GUI.values['_T_'])
    kw = float(GUI.values['_kw_'])
    probki = int(GUI.values['_probki_'])
    ns = int(GUI.values['_ns_'])

    return name, A, czestotliwosc_probkowania, t1, d, T, kw, probki, file_1_path, ns

def take_input2():
    file_2_path = GUI.values['_file_path2_']
    name = GUI.values['_generate_what2_']
    A = float(GUI.values['_amplitude2_'])
    czestotliwosc_probkowania = int(GUI.values['_czestotliwosc_probkowania2_'])
    t1 = int(GUI.values['_t12_'])
    d = float(GUI.values['_d2_'])
    T = float(GUI.values['_T2_'])
    kw = float(GUI.values['_kw2_'])
    probki = int(GUI.values['_probki2_'])
    ns2 = int(GUI.values['_ns2_'])

    return name, A, czestotliwosc_probkowania, t1, d, T, kw, probki, file_2_path, ns2

def write_to_file(signal):
    f = open("signal.txt", "w+")
    f.write(signal)
    f.close()

def read_signal(sig_name):
    npzfile = np.load(sig_name)

    params = npzfile['arr_0']
    signal = npzfile['arr_1']

    return(params, signal)