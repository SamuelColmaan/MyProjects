# Estou criando um programa que me permita 
# automatizar todas as tarefas do computador


import pyautogui as pa
import time
from datetime import datetime

pa.PAUSE = 1.5

# Obter a hora atual
agora = datetime.now()

# Obter a hora atual (somente a parte da hora)
hora_atual = agora.hour

# Determinar a saudação com base na hora atual
if 5 <= hora_atual < 12:
    saudacao = "Bom dia, Samuel"
elif 12 <= hora_atual < 18:
    saudacao = "Boa tarde, Samuel"
else:
    saudacao = "Boa noite, Samuel"
print(saudacao)
print()

if 5 <= hora_atual < 12:
    saudacao2 = "Tenha um bom dia, Samuel"
elif 12 <= hora_atual < 18:
    saudacao2 = "tenha uma boa tarde, Samuel"
else:
    saudacao2 = "Tenha um boa noite, Samuel"

palavra1 = 'devocional'
palavra2 = 'faculdade'
palavra3 = 'seminario'
palavra4 = 'sair'
palavra5 = 'filme'

while True:
    decisao = input('Diga-me o que deseja fazer agora: ').lower()

    # DEVOCIONAL
    if palavra1 in decisao:
        print('Ok! Vou abrir o seu material de devocional')
        time.sleep(1.5)
        pa.press('win')
        pa.write('chrome')
        pa.press('enter')
        time.sleep(2.5)
        pa.moveTo(857, 64)
        pa.click()
        pa.write('https://www.youtube.com/watch?v=BoM5Kmm0Qig&list=PLQ__KBt7xtI95xrCEtK1k6uwdsWfupUTT')
        pa.press('enter')
        chrome_x, chrome_y = 1085, 102  # coordenadas da janela do Chrome

        pa.moveTo(chrome_x, chrome_y)
        pa.click()
        pa.press('m')
        time.sleep(1)
        pa.hotkey('ctrl', 't')
        pa.write('https://www.bibliaonline.com.br/naa/livros')
        pa.press('enter')
        pa.hotkey('ctrl', 't')
        pa.write('https://docs.google.com/document/d/10XrhbFmah9NwkRBl7CsRUh88qeXd55tocxasPulSkOo/edit')
        pa.press('enter')

    elif palavra2 in decisao or 'faculddade' in decisao or 'faculdadde' in decisao or 'faculddadde' in decisao:
        print('Ok! Vou abrir o seu material da faculdade')
        pa.press('win')
        pa.write('chrome')
        pa.press('enter')
        time.sleep(2.0)
        pa.moveTo(857, 64)
        pa.click()
        pa.write('https://portalaluno.uva.br/Login')
        pa.press('enter')
        chrome_x, chrome_y = 195, 593  # coordenadas da janela do Chrome
        time.sleep(1)
        pa.moveTo(chrome_x, chrome_y)
        pa.click()
        time.sleep(16)
        pa.moveTo(166, 318)
        pa.click()
        pa.moveTo(166, 318)
        pa.click()
        time.sleep(1.5)
        pa.moveTo(353, 746)
        pa.click()
        pa.click(1612, 272)

    # SEMINÁRIO
    elif palavra3 in decisao:
        print('Ok! Vou abrir o seu material do seminário')
        time.sleep(1.5)
        pa.press('win')
        pa.write('chrome')
        pa.press('enter')
        time.sleep(2.5)
        pa.moveTo(857, 64)
        pa.click()
        pa.write('https://escolateologicasadoutrina.club.hotmart.com/lesson/oODXLKdmOP/aula-03-interpretando-os-livros-historicos-parte-1')
        pa.press('enter')
        chrome_x, chrome_y = 1085, 102  # coordenadas da janela do Chrome
        pa.moveTo(chrome_x, chrome_y)
        pa.click()
        time.sleep(1)
        pa.moveTo(353, 746)
        pa.click()
        pa.click(1617, 307)

    elif palavra5 in decisao or 'série' in decisao or 'serie' in decisao or 'anime' in decisao or 'desenho' in decisao or 'assistir' in decisao:
        print('Vou abrir o seu streaming para você assistir algo!')
        pa.press('win')
        pa.write('chrome')
        pa.press('enter')
        time.sleep(2.5)
        pa.moveTo(857, 64)
        pa.click()
        pa.write('https://play.max.com/home')
        pa.press('enter')

    elif palavra4 in decisao or 'para' in decisao or 'encerrar' in decisao or 'tchau' in decisao or 'adeus' in decisao or 'tmj' in decisao or 'vlw' in decisao:
        print(saudacao2)
        break
