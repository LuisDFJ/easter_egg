import os
from tqdm import trange
from time import sleep

def msj1():
    current_path = os.getcwd()
    print(f'''
-----------------------------------------------
(admin) {current_path}> cd semana7/miercoles/sorpresas''')
    sleep(1)
    print(f'''(admin) {current_path}\\semana7\\miercoles\\sorpresas> simulacion.exe''')
    sleep(2)
    print(f'''   -simulacion.exe is running-
-----------------------------------------------
    ''')
    for epoch in trange(5 , ncols=75):
        sleep(0.5)
    print(f'''WAR[0]: simulacion.exe requiere confirmacion de identidad''')
    sleep(2)
    print(f'''Activando webcam''')
    sleep(5)
    print(f'''Presiona: ''')
    sleep(1)
    print(f'''espacio - tomar foto''')
    sleep(1)
    print(f'''q - para continuar''')
    sleep(1)


def msj2():
    sleep(0.5)
    print(f'''AUTENTIFICANDO''')
    sleep(2)

def msj3():
    sleep(0.5)
    print(f'''
RECONOCIMIENTO DE CARITA CONFIRMADO
''')
    sleep(5)
    print(f'''(Deivi) C:\\> No se que tenga tu voz''')
    sleep(1)
    print(f'''(Deivi) C:\\> que hasta a un loco calma''')
    sleep(1)
    print(f'''(Deivi) C:\\> un loco en simulacion''')
    sleep(1)
    print(f'''(Deivi) C:\\> con una loca del alma''')
    sleep(1)
    print(f'''(Deivi) C:\\> Aun hay una sorpresa''')
    sleep(1)
    print(f'''(Deivi) C:\\> Pero tendras que esperar''')
    sleep(1)
    print(f'''(Deivi) C:\\> Solo un poco ...''')
    sleep(1)
    print(f'''(Deivi) C:\\> https://github.com/LuisDFJ/Sirio''')
    sleep(1)
