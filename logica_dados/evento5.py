from main import imprimir_tablero_con_indices, armar_piramide, creación_de_palitos

def evento5(cantiadd_filas_de_palitos:int, tablero:list[str]) -> list[str]:
    '''
    CREA UN NUEVO TABLERO
    '''
    
    imprimir_tablero_con_indices(tablero)
    input('Haciendo nuevo tablero...')

    return armar_piramide(cantiadd_filas_de_palitos, creación_de_palitos(cantiadd_filas_de_palitos))