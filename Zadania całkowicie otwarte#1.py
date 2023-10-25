import PySimpleGUI as sg

zadania = []
poprawna_liczba = False

sg.theme('DarkTeal11')
def widocznosc_wykoniania():
    if zadania:
        return True
    else:
        return False


def okno_listy():
    layout = [
        [sg.Text("Lista dodanych zadań.")],
        [sg.Column([[]], key='-KOL_ZAD-')]
    ]

    window = sg.Window("Menedżer zadań", layout, modal=True)

    #if zadania:
    #    window['-WYKONAJ-'].update(visible=True)

    for i in range(len(zadania)):
        window.extend_layout(window['-KOL_ZAD-'],[[sg.Text(zadania[i]), sg.VSeparator(), sg.Text(f" Zadanie nr {i+1}", key=f'-ZAD{i}-')]])

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED():
            break

    return None

layout = [
    [sg.Button('Dodaj zadanie', key='-DODAJ-', expand_x=True)],
    [sg.Button('Wyświetl zadania', key='-WYSWIETL-', expand_x=True)],
    [sg.Button("Wykonaj zadanie", key='-WYKONAJ-')],
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
            if do_usuniecia == None:
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

    if event == '-WYKONAJ-':
        wykonywanie = True
        do_wykonania = sg.popup_get_text('Wpisz numer zadania do oznaczenia jako wykonane.')
        while wykonywanie:
            if do_wykonania == None:
                wykonywanie = False
            elif not do_wykonania.isnumeric():
                do_wykonania = sg.popup_get_text("Nieprawidłowa odpowiedź. Wpisz numer zadania do oznaczenia jako wykonane.")
            else:
                numer_indeksu = int(do_wykonania) - 1
                if '[x]' in zadania[numer_indeksu]:
                    do_wykonania = sg.popup_get_text("To zadanie jest już oznaczone jako wykonane. Wpisz numer zadania do oznaczenia jako wykonane.")
                else:
                    var = '[x] ' + zadania[numer_indeksu]
                    zadania[numer_indeksu] = var
                    wykonywanie = False




window.close()
