import PySimpleGUI as sg
from parser import ParsAT
import threading
from time import sleep

def gui():
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [
        [sg.Text('Введите данные. Поля логин и пароль при необходимости, можно оставить пустыми')],
        [sg.Text('Логин', size=(15, 1)), sg.InputText(key='-LOGIN-')],
        [sg.Text('Пароль', size=(15, 1)), sg.InputText(key='-PASSWORD-')],
        [sg.Text('URL книги', size=(15, 1)), sg.InputText(key='-URL-')],
        [sg.Text('Имя файла', size=(15, 1)), sg.InputText(key='-NAME-')],
        [sg.Submit(), sg.Cancel()],
        [sg.Output(size=(65, 20), key='-OUTPUT-')]
    ]
    window = sg.Window('Simple data entry window', layout)
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break


        if event == 'Submit':
            login = values['-LOGIN-']
            password = values['-PASSWORD-']
            url = values['-URL-']
            name = values['-NAME-']
            pars = ParsAT(url, login, password, name)

            if login:
                my_thread = threading.Thread(target=pars.login)
                my_thread.start()
            else:
                my_thread = threading.Thread(target=pars.get_text)
                my_thread.start()

def main():
    gui()


if __name__ == '__main__':
    main()
