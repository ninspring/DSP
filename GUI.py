import PySimpleGUI as sg
import main
import numpy as np

sg.theme('LightBlue6')
# ------ Column Definition ------ #
column1 = [[sg.Text('Wgraj z pliku:')],
            [sg.Input(key='_file_path_'), sg.FileBrowse()],
            [sg.InputCombo(('Szum o rozkładzie jednostajnym', 'Sygnał sinusoidalny',
                        'Sygnał sinusoidalny wyprostowany jednopołówkowo',
                        'Sygnał sinusoidalny wyprostowany dwupołówkowo',
                        'Sygnał prostokątny', 'Sygnał prostokątny symetryczny', 'Sygnał trójkątny', 'Skok jednostkowy',
                        'Impuls jednostkowy', 'Szum impulsowy', 'draw'), key='_generate_what_', size=(50, 1))],
            [sg.Text('Amplituda (A)'), sg.Input('5', key='_amplitude_', size=(5, 1))],
            [sg.Text('Częstotliwość próbkowania'), sg.Input('1', key='_czestotliwosc_probkowania_', size=(5, 1)), sg.Text('Hz')],
            [sg.Text('Czas początkowy (t1)'), sg.Input('0', key='_t1_', size=(5, 1))],
            [sg.Text('Czas trwania sygnału (d)'), sg.Input('1', key='_d_', size=(5, 1)), sg.Text('s')],
            [sg.Text('Okres podstawowy (T)'), sg.Input('0', key='_T_', size=(5, 1)), sg.Text('s')],
            [sg.Spin([i for i in np.arange(0.1, 1.1, 0.1)], initial_value=0.5, key='_kw_'), sg.Text('Współczynnik wypełnienia (kw)')],
            [sg.Spin([i for i in range(1, 1000000, 100)], initial_value=1000, key='_probki_'), sg.Text('Liczba póbek')],
            [sg.Text('Numer próbki skoku (ns)'), sg.Input('0', key='_ns_', size=(5, 1))]]
column2 = [[sg.Text('Wgraj z pliku:')],
            [sg.Input(key='_file_path2_'), sg.FileBrowse()],
            [sg.InputCombo(('Szum o rozkładzie jednostajnym', 'Sygnał sinusoidalny',
                        'Sygnał sinusoidalny wyprostowany jednopołówkowo',
                        'Sygnał sinusoidalny wyprostowany dwupołówkowo',
                        'Sygnał prostokątny', 'Sygnał prostokątny symetryczny', 'Sygnał trójkątny', 'Skok jednostkowy',
                        'Impuls jednostkowy', 'Szum impulsowy'), key='_generate_what2_', size=(50, 1))],
            [sg.Text('Amplituda (A)'), sg.Input('5', key='_amplitude2_', size=(5, 1))],
            [sg.Text('Częstotliwość próbkowania'), sg.Input('1', key='_czestotliwosc_probkowania2_', size=(5, 1)), sg.Text('Hz')],
            [sg.Text('Czas początkowy (t1)'), sg.Input('0', key='_t12_', size=(5, 1))],
            [sg.Text('Czas trwania sygnału (d)'), sg.Input('1', key='_d2_', size=(5, 1)), sg.Text('s')],
            [sg.Text('Okres podstawowy (T)'), sg.Input('0', key='_T2_', size=(5, 1)), sg.Text('s')],
            [sg.Spin([i for i in np.arange(0.1, 1.1, 0.1)], initial_value=0.5, key='_kw2_'), sg.Text('Współczynnik wypełnienia (kw)')],
            [sg.Spin([i for i in range(1, 1000000, 100)], initial_value=1000, key='_probki2_'), sg.Text('Liczba póbek')],
            [sg.Text('Numer próbki skoku (ns)'), sg.Input('0', key='_ns2_', size=(5, 1))]]

layout = [
    [sg.Text('Generator sygnału', size=(30, 1), font=("Helvetica", 25), text_color='black')],
    [sg.Frame('Generacja sygnałów', [[
        sg.Column(column1),
        sg.Column(column2),
        sg.Spin([i for i in range(5,21,5)], initial_value=15, key='_histogram_'), sg.Text('Liczba przedziałów histogramu')]])],

    [sg.Frame('Operacja na sygnałach', [[
        sg.InputCombo(('Dodawanie', 'Odejmowanie', 'Mnożenie', 'Dzielenie'), key='_operation_', size=(50, 1)),
        sg.Text('Nazwa pliku wynikowego'), sg.Input('output_file', key='_filename_', size=(20, 1))]])],

    [sg.Output (size=(100, 10),
                key='_output_',
                visible=True)],
    [sg.Submit(), sg.Button('Sygnał'), sg.Cancel()]]

window = sg.Window('Generator sygnału').Layout(layout).Finalize()


while True:
    event, values = window.Read()
    if event == 'Sygnał':
        main.main()

window.close()
