import PySimpleGUI as sg

zadania = []



sg.theme('SystemDefault')

dodaj_layout = [
    [sg.Text("Dodaj zadanie do listy")],
    [sg.Input(key='-DODAJ_ZADANIE-')],
    [sg.Button('OK', key='-POTWIERDZ_DODANIE-')]
]

wyswietl_layout = [
    [sg.Text("Zadania wykonane oznaczone są [x]")],
    [sg.Multiline(auto_size_text=True, write_only=True, auto_refresh=True, key="-LISTA_ZADAN-")]
]

usun_layout = [
    [sg.Text("Wybierz numer zadania do usunięcia.")]

]

layout = [
    [sg.TabGroup([[sg.Tab('Wyświetl zadania', wyswietl_layout), sg.Tab('Dodaj zadanie', dodaj_layout), sg.Tab('Usuń zadanie', usun_layout)]])]
]

window = sg.Window('Menedżer zadań', layout)

while True:
    event, values = window.read()

    if event == "-POTWIERDZ_DODANIE-":
        zadania.append(values['-DODAJ_ZADANIE-'])


    if event == sg.WIN_CLOSED:
        break

window.close()
