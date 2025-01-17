import PySimpleGUI as sg
import string
import random

def gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais):
    caracteres = string.ascii_lowercase

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

layout = [
    [sg.Text('Gerador de Senhas', font=('Helvetica', 24, 'bold'), justification='center')],
    [sg.Text('Comprimento da Senha:', font=('Helvetica', 14)),
     sg.Slider(range=(8, 32), default_value=12, orientation='h', key='-COMPRIMENTO-', resolution=1, 
     font=('Helvetica', 12), tick_interval=0)],
    [sg.Column([
        [sg.Checkbox('Incluir letras maiúsculas', key='-MAIUSCULAS-', default=True, font=('Helvetica', 12))],
        [sg.Checkbox('Incluir números', key='-NUMEROS-', default=True, font=('Helvetica', 12))],
        [sg.Checkbox('Incluir caracteres especiais', key='-ESPECIAIS-', default=True, font=('Helvetica', 12))]
    ], element_justification='left')],
    [sg.Button('Gerar Senha', font=('Helvetica', 14), button_color=('white', '#46CC08')),
     sg.Button('Sair', font=('Helvetica', 14), button_color=('white', '#DC3545'))],
    [sg.Text('Senha gerada:', font=('Helvetica', 14)),
     sg.InputText(key='-SENHA-', size=(35, 2), font=('Helvetica', 14), readonly=True)],
    [sg.Text('', key='-ERRO-', font=('Helvetica', 12), text_color='red')]
]

window = sg.Window('Gerador de Senhas', layout, finalize=True, resizable=True, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event =='Gerar Senha':
        comprimento = int(values['-COMPRIMENTO-'])
        incluir_maiusculas = values['-MAIUSCULAS-']
        incluir_numeros = values['-NUMEROS-']
        incluir_especiais = values['-ESPECIAIS-']

        senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais)
        window['-SENHA-'].update(senha)

window.close()