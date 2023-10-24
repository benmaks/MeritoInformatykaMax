import PySimpleGUI as sg

zadania = ('test', 'niewykonane'), ('test2', 'niewykonane'), ('test3', 'wykonane')

layout = [
    [sg.Text("Zadania", pad=[5, 5])],
    [sg.Listbox(zadania, key='-LISTA-', select_mode='LISTBOX_SELECT_MODE_SINGLE_SINGLE', expand_y=True, expand_x=True)],
    [sg.Button('Wykonane'), sg.Button('Od-wykonane')],
    [sg.Button("Dodaj nowe zadanie")],
    [sg.Push(), sg.Button('Zamknij')]


]

window = sg.Window('Lista zadań', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
