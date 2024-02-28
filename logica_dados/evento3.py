from main import lista_de_palitos_de_la_piramide, contar_palitos_normales_o_rojos_de_la_piramide, armar_piramide
from constantes import ESPACIO_VACÍO, PALITO_COLOR_VERDE, PORCENTAJE_PARA_BLOQUEAR_PALITOS
from random import sample

def evento3(tablero:list[str]) -> list[str]:
    '''
    SE BLOQUEARÁN EL 20% DE PALITOS COMUNES Y ROJOS QUE HAYAN
    EN LA PIRAMIDE. SERÁN DE COLOR VERDE.
    SI EL 20% DE PALITO ES MENOS A 1, SE TOMA COMO 1.
    '''
    
    CANTIDAD_DE_FILAS:int = len(tablero)
    lista_todos_los_elementos:list = lista_de_palitos_de_la_piramide(tablero)
    CANTIDAD_DE_ELEMENTOS:int = len(lista_todos_los_elementos)
    posición_palitos:list = []
    contador_palitos_no_verdes:int = contar_palitos_normales_o_rojos_de_la_piramide(lista_todos_los_elementos)

    for guardar_posiciones_palitos_totales in range(CANTIDAD_DE_ELEMENTOS):
        if (not lista_todos_los_elementos[guardar_posiciones_palitos_totales] == ESPACIO_VACÍO 
            and not lista_todos_los_elementos[guardar_posiciones_palitos_totales] == PALITO_COLOR_VERDE):
            posición_palitos.append(guardar_posiciones_palitos_totales)

    porcentaje_palitos:int = round(contador_palitos_no_verdes * PORCENTAJE_PARA_BLOQUEAR_PALITOS)
    palitos_a_pintar = sample(posición_palitos,porcentaje_palitos)
    for color in palitos_a_pintar:
        lista_todos_los_elementos[color] = PALITO_COLOR_VERDE

    return armar_piramide(CANTIDAD_DE_FILAS, lista_todos_los_elementos)