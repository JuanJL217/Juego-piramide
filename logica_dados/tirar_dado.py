from constantes import PRIMER_NOMBRE, MÍN_VALOR_DEL_DADO, MÁX_VALOR_DEL_DADO
from random import randint


def tirar_dado(nombres_jugadores:tuple[str], nombres:str)->None:
    '''
    PRE CONDICIÓN: SE ELEJIRÁ UN NÚMERO AL AZAR ENTRE EL 1 Y 6.

    POST CONDICIÓN: UNA VEZ TENIENDO ESE VALOR, DEPENDIENDO DE QUIEN SEA EL
                    TURNOS (USUARIO O BOT), SALDRÁ UN MENSAJE DISTINTO 
                    ('AGARRASTE' O 'AGARRÓ').
    '''
    
    YO = nombres_jugadores[PRIMER_NOMBRE]
    número_de_dado = randint(MÍN_VALOR_DEL_DADO,MÁX_VALOR_DEL_DADO)

    if nombres == YO:
        input('Agarraste palito rojo')
        input('Tirando dado...')
        input(f'Salió el número {número_de_dado}')

        return número_de_dado
    
    else:
        input('Agarró un palito rojo')
        input('Tirando dado...')
        input(f'Le salió el número {número_de_dado}')

        return número_de_dado