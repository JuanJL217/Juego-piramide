from constantes import PRIMER_NOMBRE, DISMINUYE_EN_UNO, PALITO_COMÚN, PALITO_COLOR_ROJO, PALITO_COLOR_VERDE, ESPACIO_VACÍO
from main import hay_palitos_en_la_fila, imprimir_tablero_con_indices
from random import randint

def evento4(tablero:list[str], nombres_seleccionados:tuple[str], nombres:str)->list[str]:
    '''
    PRE CONDICIÓN: SE TIENE QUE ELEGIR ENTRE LA CANTIDAD DE FILAS QUE HAYA, OBLIGATORIAMENTE.
                   ASÍ NO ROMPE, SI PONEMOS CUALQUIER OTRO VALOR QUE NO SEA NÚMERICO.

    POST CONDICIÓN: DICHA FILA, LOS PALITOS SERAN ELIMINADOS.
    '''

    YO = nombres_seleccionados[PRIMER_NOMBRE]
    CANTIDAD_DE_COLUMNAS:int = len(tablero[0])
    fila_no_hay_palitos:bool = True

    while fila_no_hay_palitos:

        if nombres == YO:

            fila:str=int(input('¿Cuál fila desea sacar los palitos: '))
            if hay_palitos_en_la_fila(tablero,fila):
                fila_no_hay_palitos:bool = False

        else:

            fila:int = randint(1, len(tablero))
            if hay_palitos_en_la_fila(tablero,fila):
                input(f'{nombres} eligió la fila {fila}')
                fila_no_hay_palitos:bool = False


    for elementos in range(CANTIDAD_DE_COLUMNAS):
        if (tablero[fila-DISMINUYE_EN_UNO][elementos] == PALITO_COMÚN or 
            tablero[fila-DISMINUYE_EN_UNO][elementos] == PALITO_COLOR_ROJO or 
            tablero[fila-DISMINUYE_EN_UNO][elementos] == PALITO_COLOR_VERDE):

            tablero[fila-DISMINUYE_EN_UNO][elementos] = ESPACIO_VACÍO

    imprimir_tablero_con_indices(tablero)

    return tablero