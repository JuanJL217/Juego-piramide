from constantes import PRIMER_NOMBRE, AUMENTA_EN_UNO, PALITO_COMÚN, ESPACIO_VACÍO
from main import reacomodar_tablero, imprimir_tablero_con_indices, contar_espacios_vacios_de_la_piramide, lista_de_palitos_de_la_piramide
from random import randint

def evento2(tablero:list[str], nombres_seleccionados:tuple[str], nombres:str) -> list[str]:
    '''
    PRE CONDICIÓN: SE TIENE QUE ELEGIR UN VALOR NUMÉRICO ENTRE 1 Y M PALITOS, PARA QUE
                   SE PUEDA EJECUTAR EL EVENTO Y NO ROMPA.

    POST CONDICIÓN: SE IMPLEMENTA LA CANTIDAD DE PALITOS ELEGIDA Y SE
                    MOSTRARÁN EN EL TABLERO.
    '''
    
    tablero = reacomodar_tablero(tablero)
    imprimir_tablero_con_indices(tablero)
    cantidad_de_espacios_vacios = contar_espacios_vacios_de_la_piramide(lista_de_palitos_de_la_piramide(tablero))
    FILAS = len(tablero)
    COLUMNAS = len(tablero[0])
    YO = nombres_seleccionados[PRIMER_NOMBRE]

    if nombres == YO:
        cantidad_palitos_para_agregar:str = int(input(f'¿Cuantos palitos desea agregar?, puede ser entre 1 a {cantidad_de_espacios_vacios} palitos: '))
    else: 
        cantidad_palitos_para_agregar:int = randint(1,cantidad_de_espacios_vacios)

    contador_palitos_agregados:int = 1
    for iterar_elementos_de_la_piramide in range(FILAS):
        for encontrar_espacio_vacío in range(COLUMNAS):
            if contador_palitos_agregados<=cantidad_palitos_para_agregar:
                if tablero[iterar_elementos_de_la_piramide][encontrar_espacio_vacío] == ESPACIO_VACÍO:
                    tablero[iterar_elementos_de_la_piramide][encontrar_espacio_vacío] = PALITO_COMÚN
                    contador_palitos_agregados+=AUMENTA_EN_UNO

    imprimir_tablero_con_indices(tablero)
    input(f'se agregaron los {cantidad_palitos_para_agregar} palitos solicitados')

    return tablero