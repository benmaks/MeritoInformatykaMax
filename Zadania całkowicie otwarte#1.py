import PySimpleGUI as sg

zadania = []
poprawna_liczba = False

def okno_listy():
    layout = [
        [sg.Text("Lista dodanych zadań.")],
        [sg.Column([[]], key='-KOL_ZAD-')]
    ]

    window = sg.Window("Menedżer zadań", layout, finalize=True)

    for i in range(len(zadania)):
        window.extend_layout(window['-KOL_ZAD-'], [[sg.Text(zadania[i]), sg.VSeparator(), sg.Text(f" Zadanie nr {i}")]])

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED():
            break
    return None

layout = [
    [sg.Button('Dodaj zadanie', key='-DODAJ-', expand_x=True)],
    [sg.Button('Wyświetl zadania', key='-WYSWIETL-', expand_x=True)],
    [sg.Button("Usuń zadanie", key='-USUN-', expand_x=True)],
    [sg.Button('Zakończ program', key='-ZAKONCZ-', expand_x=True)]
]

window = sg.Window("Menedżer zadań", layout)

while True:
    event, values = window.read()

    if event in [sg.WIN_CLOSED, '-ZAKONCZ-']:
        break

    if event == '-DODAJ-':
        nowe_zadanie = sg.popup_get_text("Podaj treść zadania.")
        zadania.append(nowe_zadanie)

    if event == '-USUN-':
        usuwanie = True
        do_usuniecia = sg.popup_get_text('Wpisz numer zadania do usunięcia.')
        while usuwanie:
            if do_usuniecia == "None":
                usuwanie = False
            elif not do_usuniecia.isnumeric():
                do_usuniecia = sg.popup_get_text("Nieprawidłowa odpowiedź. Wpisz numer zadania do usunięcia.")
            else:
                numer_indeksu = int(do_usuniecia) - 1
                try:
                    zadania.pop(numer_indeksu)
                except IndexError:
                    do_usuniecia = sg.popup_get_text("Nie ma zadania o takim numerze. Wpisz numer zadania do usunięcia.")
                else:
                    usuwanie = False

    if event == '-WYSWIETL-':
        try:
            okno_listy()
        except:
            pass



window.close()
