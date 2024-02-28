from evento1 import evento1
from evento2 import evento2
from evento3 import evento3
from evento4 import evento4
from evento5 import evento5
from evento6 import evento6
from main import imprimir_tablero_con_indices, guardar_coordenadas_y_turnos_de_palitos_bloqueados

def eventos_totales(
        numero_dado, 
        tablero, 
        nombres_seleccionados, 
        nombres, turnos_jugadores,
        tiempo_palitos_bloqueados,
        coordenadas_guardadas,
        cantidad_filas_de_palitos )-> list[str]:
    
    '''
    SECCIÓN DONDE TENGO LOS EVENTOS Y COSAS EXTRAS, PARA QUE EL PROGRAMA VAYA BIEN.
    '''
    
    if numero_dado == 1:
        evento1(nombres_seleccionados, turnos_jugadores, nombres)

    elif numero_dado == 2:
        tablero = evento2(tablero,nombres_seleccionados,nombres)

    elif numero_dado == 3:
        tablero = evento3(tablero)
        imprimir_tablero_con_indices(tablero)
        input('Los palitos verdes se quedan bloqueados por 3 rondas')
        guardar_coordenadas_y_turnos_de_palitos_bloqueados(tablero, tiempo_palitos_bloqueados, coordenadas_guardadas)

    elif numero_dado == 4:
        tablero=evento4(tablero, nombres_seleccionados, nombres)

    elif numero_dado == 5:
        tablero = evento5(cantidad_filas_de_palitos, tablero)

    elif numero_dado == 6:
        evento6(tablero)

    return tablero