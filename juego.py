from colored import Fore, Style
import random
import os

PALITO_COMÚN:str='|'
PALITO_COLOR_ROJO:str='\x1b[38;5;1m|\x1b[0m'
PALITO_COLOR_VERDE:str='\x1b[38;5;2m|\x1b[0m'
ESPACIO_VACÍO=' '
MÁX_PALITOS:int=3
MÍN_PALITOS:int=1
UN_PALITO:int=1
MÍN_VALOR_DEL_DADO:int=1
MÁX_VALOR_DEL_DADO:int=6
PRIMERA_FILA:int=1
FUERA_DE_LA_PIRAMIDE:str='\x1b[38;5;0m*\x1b[0m'
ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO:int=1
UNA_FILA_ANTES_DE_LA_MÁXIMA:int=11
PORCENTAJE_MÍNIMO:float=0.2
PORCENTAJE_MÁXIMO:float=0.3
INDICE_CON_2_DIGITOS:int=10
DE_DOS_EN_DOS:int=2
COLUMNAS:int=0
PORCENTAJE_PARA_BLOQUEAR_PALITOS:float=0.2
PRIMER_NOMBRE:int=0
AUMENTA_EN_UNO:int=1
DISMINUYE_EN_UNO:int=1
INICIAR_CONTADOR:int=0
PRIMERA_COORDENADA:int=0
SEGUNDA_COORDENADA:int=1
SE_ACABÓ_EL_TIEMPO:int=0


def limpiar_pantalla()->None:
    return os.system('cls')

def menú_cantidad_jugadores(jugadores:tuple[str])->int:
    '''
    PRE CONDICIÓN: INGRESAR ÚNICAMENTE UN VALOR NUMERICO QUE SE MUESTRE COMO OPCIONES.

    POST CONDICIÓN: LA FUNCIÓN RETORNARÁ ESE NÚMERO PARA LA LÓGICA DE SELECCIONAR LOS NOMBRES Y DEMÁS, 
                    EN LAS DISTINTAS FUNCIONES.
    '''

    limpiar_pantalla()
    print("ESTOS PALITOS SON UN CHINO")
    input('Presiona "ENTER" para iniciar')
    limpiar_pantalla()
    print('CANTIDAD DE JUGADORES')

    for cantidad in range(len(jugadores)):
        print(jugadores[cantidad])

    return int(input('¿Cuántos jugadores seremos?: '))


def fijar_jugadores(nombre_de_la_tupla_de_jugadores:tuple[str],cantidad_de_jugadores:int)->tuple[str]:
    '''
    PRE CONDICIÓN: 
    1) PONDREMOS UN NOMBRE DE USUARIO, UNA CADENA Y SE CONVERTIRÁ EN MAYÚSCULA
    2) JUNTO CON LA CANTIDAD DE JUGADORES QUE ELEGIDOS EN LA FUNCIÓN ANTERIOR, SIENDO "N" LA CANTIDAD DE JUGADORES ELEGIDOS,
       LA CANTIDAD DE BOTS ES "N-1".

    POST CONDICIÓN: RETORNARÁ UNA TUPLA CON LA CANTIDAD DE JUGADORES, SIENDO LA PRIMERA POSICIÓN EL NOMBRE
                    DEL USUARIO Y EL RESTO, NOMBRES ALEATORIOS DE UNA TUPLA DE POSIBLES NOMBRES QUE ESTÁ EN EL MAIN.
    '''

    limpiar_pantalla()
    jugadores_totales:list=[]

    nombre_yo:str=str(input('Nombre de Usuario: ')).upper()
    limpiar_pantalla()

    print('LOS JUGADORES SON:')
    jugadores_totales.append(nombre_yo)
    nombres_elegidos:list=(random.sample(nombre_de_la_tupla_de_jugadores,cantidad_de_jugadores-DISMINUYE_EN_UNO))

    for elementos in range(len(nombres_elegidos)):
        jugadores_totales.append(nombres_elegidos[elementos])

    for nombres in range(len(jugadores_totales)):
        print(f'Jugador{nombres+AUMENTA_EN_UNO} -> {jugadores_totales[nombres]}')
    input()

    return tuple(jugadores_totales)


def marcador_jugadores(nombres:tuple[str],palitos_retirados_de_cada_jugador:dict)->None:
    '''
    MODIFICA UN DICCIONARIO VACÍO CON TAL DE LLEVAR EL CONTEO DE LOS PALITOS QUE CADA JUGADOR
    RETIRE DURANTE LA PARTIDA {jugador1:{'contador palitos retirados':0}, jugador2:...}. SE INICIA 
    EL CONTEO CON TODOS LOS JUGADORES TENIENDO 0 PALITOS.
    '''
    for elementos in nombres:
        palitos_retirados_de_cada_jugador[elementos]={'contador palitos retirados':INICIAR_CONTADOR}


def seguimiento_turnos(jugadores_seleccionados:dict,turnos_jugadores:dict)->None:
    '''
    MDIFICA UN DICCIONARIO VACÍO PARA LLEVAR EL CONTROL DE LOS TURNOS BLOQUEADOS POR EL EVENTO 1.
    LA FORMA ES QUE CADA JUGADOR TENDRÁ INICIALMENTE EL VALOR BOOLEANO DE TRUE, CUANDO EN EL TURNO DE
    UN JUGADOR LE SALGA EL EVENTO 1, SU BOOLEANO TRUE CAMBIAR A UN FALSE, LO QUE HACE QUE EN LA SIGUIENTE
    TURNO DONDE DEBA ESCOGER LA CANTIDAD DE PALITOS SALTE AL SIGUIENTE JUGADOR, QUE TENGA EL BOOLEANO TRUE
    Y EL BOOLEANO DEL JUGADOR EN FALSE, VUELVA A UN TRUE (LO QUE SIGNIFICA QUE YA PUEDE VOLVER A JUGAR
    EL PRÓIMO TURNO).
    '''

    for nombres in jugadores_seleccionados:
        turnos_jugadores[nombres]=True


def menú_cantidad_filas(cantidad_de_jugadpres:int)->int:
    '''
    SE MOSTRARÁ UN MENÚ DE FILAS Y CADA FILA SE MUESTRA LA CANTIDAD DE PALITOS HASTA DICHA FILA.
    DEPENDIENDO LA CANTIDAD DE JUGADORES ELEGIDA, LA CANTIDAD MÍNIMA DE FILAS EN EL MENÚ, CAMBIARÁ.

    PRE CONDICIÓN: SE PIDE INGRESAR UN VALOR NUMERICO DE LA CANTIDAD DE FILAS QUE DESEE EL JUGADOR,
                   NO PUEDE ELEGIR UN VALOR INFERIOR O SUPERIOR AL MÍNIMO Y MÁXIMO DE FILAS QUE SE MUESTRE
                   EN PANTALLA.

    POST CONDICIÓN: USAREMOS ESE VALOR NUMERICO DE LA CANTIDAD DE FILAS ELEGIDAS PARA MUCHAS DE LAS FUNCIONES.
    '''

    limpiar_pantalla()
    print('NIVELES - CANTIDAD DE PALITOS')
    palitos:int=((cantidad_de_jugadpres+2)*(cantidad_de_jugadpres+3)/2)-cantidad_de_jugadpres-2
    filas:int=cantidad_de_jugadpres+AUMENTA_EN_UNO

    for cantidad in range(cantidad_de_jugadpres,UNA_FILA_ANTES_DE_LA_MÁXIMA):
        filas+=AUMENTA_EN_UNO
        palitos+=filas
        print(f'{filas} filas -> {int(palitos)} palitos')

    return int(input('¿Con cuántas filas jugaremos?: '))


def creación_de_palitos(filas_de_palitos:int)->list[str]:
    '''
    UNA VEZ ELEGIDO LA CANTIDAD NUMERICA DE FILAS A QUERER JUGAR, EN ESTA FUNCIÓN, PODREMOS
    RETORNAR UNA LISTA DE PALITOS, TANTO DE PALITOS COMUNES, COMO DE PALITOS DE COLOR ROJO EN 
    POSICIONES ALEATORIAS.
    '''

    lista_palitos=[]
    contador:int=INICIAR_CONTADOR

    for crear_palitos in range(filas_de_palitos+AUMENTA_EN_UNO):
        contador+=crear_palitos

    valor_mín_rojo:int=round(contador*PORCENTAJE_MÍNIMO)
    valor_máx_rojo:int=round(contador*PORCENTAJE_MÁXIMO)
    cantidad_rojo:int=random.randint(valor_mín_rojo,valor_máx_rojo)

    for agregar in range(contador):
        lista_palitos.append(PALITO_COMÚN)

    palitos_a_pintar=random.sample((range(len(lista_palitos))),cantidad_rojo)

    for color in palitos_a_pintar:
        lista_palitos[color]=PALITO_COLOR_ROJO

    return lista_palitos


def armar_piramide(cantidad_de_filas:int,lista_palitos:list[str])->list[str]:
    '''
    TENIENDO EN CUENTA LA CANTIDAD DE FILAS ELEJIDA Y LA LISTA DE PALITOS CREADA, PODREMOS
    FORMAR LA PIRAMIDE. HICE UN TABLERO DE "N" FILAS Y "N-1" COLUMNAS, SE RELLENÓ DE ASTERISCOS
    COLOR NEGRO Y LUEGO SE AGREGA LOS ELEMENTOS DE LA LISTA DE PALITOS CREADA Y DAR FORMA DE PIRAMIDE
    EN EL TABLERO
    '''

    tablero=[]
    CANTIDAD_DE_COLUMNAS:int=2*cantidad_de_filas-DISMINUYE_EN_UNO
    for rellenar_filas in range(cantidad_de_filas):
        filas=[]
        for rellenar_columnas in range(2*cantidad_de_filas-DISMINUYE_EN_UNO):
            filas.append(FUERA_DE_LA_PIRAMIDE)
        tablero.append(filas)

    palito_de_la_lista_de_palitos:int=0
    for filas in range(cantidad_de_filas):
        orden:int=cantidad_de_filas-filas-DISMINUYE_EN_UNO
        for acomodar_palitos in range(orden,CANTIDAD_DE_COLUMNAS-orden,DE_DOS_EN_DOS):
            tablero[filas][acomodar_palitos]=lista_palitos[palito_de_la_lista_de_palitos]
            orden-=DISMINUYE_EN_UNO
            palito_de_la_lista_de_palitos+=AUMENTA_EN_UNO

    return tablero


def reglas(tablero)->None:
    '''
    IMPRIME LAS REGLAS DEL JUEGO Y LOS EVENTOS RELACIONADOS SI ELEGIMOS UN
    PALITO COLOR ROJO
    '''
    
    limpiar_pantalla()

    print(f'''LAS REGLAS SON LAS SIGUIENTES:
CADA JUGADOR PUEDE ELEGIR ENTRE 1 A 3 PALITOS
LOS PALITOS DE COLOR ROJOS TIENE "EVENTOS" REFERENTE
A CADA VALOR NUMERICO DEL DADO:
    1: EL JUGADOR PIERDE SU PRÓXIMO TURNO
    2: SE AGREGAN ENTRE 1 Y "M" PALITOS
    3: SE BLOQUEAN EL 20% DE PALITOS DURANTE 3 TURNOS
    4: EL JUGADOR DEBE RETIRAR UNA FILA COMPLETA A SU ELECCIÓN
    5: SE GENERA UNA NUEVA PIRAMIDE, DEL MISMO TAMAÑO QUE EL ORIGINAL
    6: NO HACE NADA
{Fore.red}EL JUGADOR QUE RETIRE EL ÚLTIMO PALITO ¡PIERDE!{Style.reset}
          ''')
    
    input('Presiona "ENTER" para iniciar el juego')
    imprimir_tablero_con_indices(tablero)


def imprimir_tablero_con_indices(tablero:list[str])->None:
    '''
    TENEMOS COMO PARÁMETRO EL TABLERO CREADO, CUAL EN ESTA FUNCIÓN, IMPLEMENTAREMOS VISUALMENTE EL
    ARREGLO DEL TABLERO MÁS LOS ÍNDICES NUMERICOS EN LA PARTE DE SUPERIOR E IZQUIERDA
    DEL TABLERO, EN PANTALLA.
    '''

    limpiar_pantalla()

    for indice_superior in range(1, len(tablero[0])+1):
        if indice_superior >= INDICE_CON_2_DIGITOS:
            print(f'  {Fore.blue}{indice_superior}{Style.reset}', end='')
        else:
            print(f'   {Fore.blue}{indice_superior}{Style.reset}', end='')
    print()
    print()

    for indice_izquierdo in range(1,len(tablero)+1):
        print(f'{Fore.blue}{indice_izquierdo}{Style.reset}', end=' ')
        for elemento in tablero[indice_izquierdo-1]:
            print(f' {elemento} ', end=' ')
        print()
        print()


def elegir_cantidad_de_palitos(MÍN_PALITOS:int,MÁX_PALITOS:int)->int:
    '''
    FUNCIÓN DESTINADA A VALIDAR SI LA CANTIDAD DE PALITOS ELEGIDA ES UN NÚMERO Y
    SI ESTÁ DENTRO DEL MARGEN ENTRE 1 (MÍN_PALITOS) Y 3 (MÁX_PALITOS), Y CASO DE SER
    CORRECTO, DEVOLVERÁ DICHO VALOR NUMERICO INT.
    '''
    
    print()

    cantidad_de_palitos_aceptada:bool=False
    while not cantidad_de_palitos_aceptada:
        cantidad_elejida_de_palitos:str=str(input('¿Cuantos palitos desea sacar?: '))
        if (cantidad_elejida_de_palitos.isdigit() and cantidad_elejida_de_palitos.isdecimal() and 
            int(cantidad_elejida_de_palitos)<=MÁX_PALITOS and int(cantidad_elejida_de_palitos)>=MÍN_PALITOS):
                cantidad_de_palitos_aceptada:bool=True

                return int(cantidad_elejida_de_palitos)
        
def cantidad_de_palitos_bots(MÍN_PALITOS:int, MÁX_PALITOS:int)->int:
    '''
    ELIJE UN NÚMERO ENTRE EL 1 Y 3 ALEATORIAMENTE PARA CADA BOT, LA CUAL SERÁ
    LA CANTIDAD DE PALITOS A SACAR.
    '''

    return random.randint(MÍN_PALITOS, MÁX_PALITOS)


def coordenadas_del_tablero(tablero:list[str],sacar_cantidad_palitos:int,cantidad_elejida_de_palitos:int)->tuple[int]:
    '''
    FUNCIÓN DESTINADA A VALIDAD QUE LOS VALORES SELECCIONADOS SEAN UN NÚMERO Y QUE ESTEN DENTRO DEL
    RANGO DE CANTIDAD DE FILAS Y CANTIDAD DE COLUMNAS DEL TALBERO, DE SER CORRECTO, DE VOLVERA UNA
    TUPLA DE LA FORMA (X,Y)
    '''
    
    print()

    imprimir_tablero_con_indices(tablero)
    mostrar_cantidad_de_palitos_a_sacar(  sacar_cantidad_palitos,cantidad_elejida_de_palitos)
    CANTIDAD_DE_FILAS:int=len(tablero)
    CANTIDAD_DE_COLUMNAS:int=len(tablero[0])
    fil_correcta:bool=False
    while not fil_correcta:
        fil:str=str(input('Elija fila: '))
        if fil.isdigit() and fil.isdecimal():
            fil_correcta:bool=True
            col_correcta:bool=False
            while not col_correcta:
                col:str=str(input('Elija columna: '))
                if col.isdigit() and col.isdecimal():
                    col_correcta:bool=True
                    if int(fil)<=CANTIDAD_DE_FILAS and int(col)<=CANTIDAD_DE_COLUMNAS:

                        return int(fil),int(col)
                    else:

                        print(input('Está fuera del rango de la piramide'))
                        fil_correcta:bool=False


def coordenadas_bots(cantidad_de_filas:int,cantidad_de_columnas:int)->tuple[int]:
    '''
    DEVUELVE UNA CORRDENADA (X,Y) ALEATORIA QUE ESTÉN DENTRO DEL RANGO DEL TABLERO
    '''

    fil:int=random.randint(PRIMERA_FILA,cantidad_de_filas)
    col:int=random.randint(PRIMERA_FILA,cantidad_de_columnas)

    return fil,col


def posición_hay_palito_rojo(tablero:list[str],coordenadas:tuple[int])->bool:
    '''
    ACLARACIÓN PARA LOS DEMÁS BOOLEANOS: SE RESTA 1 A CADA COORDENADA X E Y, PORQUE EL TABLERO ESTÁ
                VISUALMENTE INICIANDO DESDE EL 1, PERO PYTHON INICIA DESDE EL 0, POR ESO SI
                ALGUIEN ELIJE LA COORDENADA (5,6), EN REALIDAD ES LA COORDENADA (4,5) PARA
                PYTHON
                
    PRE CONDICIÓN: INGRESA UNA COORDENADA (X,Y) DEL TABLERO

    POST CONDICIÓN: RETORNA UN BOOLEADO IDENTIFICANDO SI EFECTIVAMENTE EN LA COORDENADA HAY
                    UN PALITO ROJO O NO
    '''
    
    if (PALITO_COLOR_ROJO in 
        tablero[coordenadas[PRIMERA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]
        [coordenadas[SEGUNDA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]):

        return True
    
    else:
        return False
    

def posición_es_vacío(tablero:list[str],coordenadas:tuple[int])->bool:
    '''
    PRE CONDICIÓN: INGRESA UNA COORDENADA (X,Y) DEL TABLERO.

    POST CONDICIÓN: RETORNA UN BOOLEADO IDENTIFICANDO SI EFECTIVAMENTE EN LA COORDENADA NO SE
                    PUEDE SELECCIONAR PORQUE HAY NADA, TENIENDO EN CONDIDERACIÓN SI HAY UN 
                    ELEMENTO VACÍO O SI ESTÁ FUERA DE CADA ELEMENTO DE LA PIRAMIDE.
    '''

    if (ESPACIO_VACÍO in 
        tablero[coordenadas[PRIMERA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]
        [coordenadas[SEGUNDA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO] 
        or
        FUERA_DE_LA_PIRAMIDE in 
        tablero[coordenadas[PRIMERA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]
        [coordenadas[SEGUNDA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]):
    
        return True
    
    else:
        return False
    
    
def posición_está_bloqueado(tablero:list[str],coordenadas:tuple[int])->bool:
    '''
    PRE CONDICIÓN: INGRESA UNA COORDENADA (X,Y) DEL TABLERO.

    POST CONDICIÓN: RETORNA UN BOOLEADO IDENTIFICANDO SI EFECTIVAMENTE EN LA COORDENADA
                    ESTÁ BLOQUEADO POR EL EVENTO 3.
    '''

    if (PALITO_COLOR_VERDE in 
        tablero[coordenadas[PRIMERA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]
        [coordenadas[SEGUNDA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]):
        
        return True
    
    else:
        return False


def sacar_palito(tablero:list[str],coordenadas:tuple[int])->None:
    '''
    PRE CONDICIÓM: QUE LA COORDENADA SEA UN PALITO COMÚN O UN PALITO COLOR ROJO.

    POST CONDICIÓN: INTERCAMBIA EL VALOR DE LA COORDENADA POR UN VALOR VACÍO.
    '''

    (tablero[coordenadas[PRIMERA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO]
        [coordenadas[SEGUNDA_COORDENADA]-ARREGLAR_POSICIÓN_POR_INDICE_DEL_TABLERO])=ESPACIO_VACÍO
    imprimir_tablero_con_indices(tablero)


def imprimir_cantidad_de_palitos_elegidos(cantidad_elejida_de_palitos:int)->None:
    '''
    TOMAR EL VALOR SELECCIONADO ALEATORIAMENTE DEL BOT E IMPRIME EN PANTALLA
    CUANTOS HA ELEGIDO
    '''
    
    print()
    input(f'Elijió {cantidad_elejida_de_palitos} palitos')
    print()


def mostrar_cantidades_de_palitos_a_sacar_y_coordenadas(tablero:list[str], sacar_cantidad_palitos:int, 
                                                        cantidad_elejida_de_palitos:int, coordenadas:tuple[int])->None:
    '''
    MUESTRA EN PANTALLA LA CANTIDAD DE PALITOS QUE ELIGIÓ Y EL NÚMERO DEL PALITO QUE LE
    CORRESPONDE SACAR, 'PALITO 1 DE 3' INDICANDO QUE ES EL PRIMER PALITO QUE VA A RETIRAR EL BOT.
    Y TAMBIEN SE MUESTRA LA COORDENADA QUE EL BOT ELEIGIÓ.
    '''
    
    imprimir_tablero_con_indices(tablero)
    print(f'Palito {sacar_cantidad_palitos} de {cantidad_elejida_de_palitos}')
    print()
    input(f'Elijió la filia {coordenadas[PRIMERA_COORDENADA]} y columna {coordenadas[SEGUNDA_COORDENADA]}')


def mostrar_cantidad_de_palitos_a_sacar(sacar_cantidad_palitos:int,cantidad_elejida_de_palitos:int)->None:
    '''
    MUESTRO EN PANTALLA EL NUMERO DEL PALITO QUE TIENE QUE SACAR Y LA CANTIDAD QUE SELECCIONÓ.
    LO MISMO QUE EL PROCEDIMIENTO ANTEIOR, SOLO QUE SIN MOSTRAR LAS COORDENADAS.
    '''
    
    print(f'Palito {sacar_cantidad_palitos} de {cantidad_elejida_de_palitos}')


def mencionar_turno(nombres:str,tablero:list[str])->None:
    '''
    MUESTRA EN PANTALLA EL TURNO DEL NOMBRE DEL JUGADOR EN ESE MOMENTO.
    '''

    imprimir_tablero_con_indices(tablero)
    input(f'TURNO DE {nombres}')
        

def mensaje_posición_es_vacía(tablero:list[str])->None:
    '''
    SI EL USUARIO SELECCIONA UN ESPACIO VACIO, SADRLÁ ESTE MENSAJE.
    '''
    
    print(input('No se puede seleccionar un espacio vacío'))
    imprimir_tablero_con_indices(tablero)


def mensaje_posición_está_bloqueada(tablero:list[str])->None:
    '''
    SI EL USUARIO SELECCIONA UN PALITO BLOQUEADO, SALDRÁ ESE MENSAJE.
    '''
    
    imprimir_tablero_con_indices(tablero)
    input('Palito bloqueado, saque otro')


def lista_de_palitos_de_la_piramide(tablero:list[str])->list[str]:
    '''
    TOMA LOS ELEMENTOS DE LA PIRAMIDE DEL TABLERO Y LOS PONE
    EN UNA LISTA, LA CUAL RETORNAREMOS.
    '''

    FILAS:int=len(tablero)
    COLUMNAS:int=2*FILAS-DISMINUYE_EN_UNO
    lista_todos_los_palitos=[]
    for seleccionar_palitos in range(FILAS):
        orden:int=FILAS-seleccionar_palitos-DISMINUYE_EN_UNO
        for guardar_elemento in range(orden,COLUMNAS-orden,DE_DOS_EN_DOS):
            lista_todos_los_palitos.append(tablero[seleccionar_palitos][guardar_elemento])

    return lista_todos_los_palitos


def reacomodar_tablero(tablero:list[str])->list[str]:
    '''
    ESTA FUNCIÓN TOMA LOS ELEMENTOS DE LA PIRAMIDE DEL TABLERO Y LOS REORGANIZA
    MANDANDO LOS ESPACIOS VACIOS HACIA ARRIBA DE LA PIRAMIDE Y LOS PALITOS COMUNES
    Y ROJOS, LOS ARRASTRA A ABAJO, RELLENANDO LOS ESPACIOS VACIOS QUE DEJARON LOS
    JUGADORES AL RETIRAR PALITOS DESPUÉS DE CADA TURNO.
    LOS PALITOS VERDE NO CAEN, SE QUEDAN EN SU MISMA POSICIÓN.
    '''
    
    lista_posiciones=lista_de_palitos_de_la_piramide(tablero)
    CANTIDAD_DE_ELEMENTOS_DE_LISTA_DE_POSICIONES:int=len(lista_posiciones)
    posición_a_bloquear:list=[]
    FILAS_DEL_TABLERO:int=len(tablero)
    lista_reacomodar=[]

    for buscar_lugar_de_verdes in range(CANTIDAD_DE_ELEMENTOS_DE_LISTA_DE_POSICIONES):
        if lista_posiciones[buscar_lugar_de_verdes]==PALITO_COLOR_VERDE:
            posición_a_bloquear.append(buscar_lugar_de_verdes)

    for vacios in lista_posiciones:
        if vacios==ESPACIO_VACÍO:
            lista_reacomodar.append(vacios)

    for palitos_comumen_o_rojos in lista_posiciones:
        if palitos_comumen_o_rojos==PALITO_COMÚN or palitos_comumen_o_rojos==PALITO_COLOR_ROJO:
            lista_reacomodar.append(palitos_comumen_o_rojos)

    for agregar_verdes in posición_a_bloquear:
        lista_reacomodar.insert(agregar_verdes,PALITO_COLOR_VERDE)

    return armar_piramide(FILAS_DEL_TABLERO,lista_reacomodar)


def contar_palitos_normales_o_rojos_de_la_piramide(lista_de_palitos_sacado_de_la_piramide:list[str])->int:
    '''
    DE LA LISTA DE LA FUNCIÓN ANTERIOR, CONTARÁ TODOS LOS PALITOS COMUNES
    O DE COLOR ROJO QUE HAYA EN ESA LISTA Y RETORNAÁ DICHA CANTIDAD.
    '''
    
    contador_de_palitos:int=INICIAR_CONTADOR
    for palitos in lista_de_palitos_sacado_de_la_piramide:
        if palitos==PALITO_COMÚN or palitos==PALITO_COLOR_ROJO:
            contador_de_palitos+=AUMENTA_EN_UNO

    return contador_de_palitos


def contar_espacios_vacios_de_la_piramide(lista_de_palitos_sacado_de_la_piramide:list[str])->int:
    '''
    HACE LO MISMO QUE LA FUNCIÓN ANTERIOR, PERO EN VEZ DE CONTAR LOS PALITOS, CONTARÁ
    LOS ESPACIOS VACÍOS DENTRO DE LA LISTA Y RETORNARÁ DICHA CANTIDAD.
    '''
    
    contador_de_espacios_vacios:int=INICIAR_CONTADOR
    for espacios_vacío in lista_de_palitos_sacado_de_la_piramide:
        if espacios_vacío==ESPACIO_VACÍO:
            contador_de_espacios_vacios+=AUMENTA_EN_UNO

    return contador_de_espacios_vacios


def hay_palitos_en_la_fila(tablero:list[str],fila:int)->bool:
    '''
    VERIFICA QUE EN LA FILA SELECCIONADA, PARA EL EVENTO 4, HAYA PALITOS.
    EN EL CASO DE QUE NO HAYA, VUELVE A SELECCIONAR OTRA FILA, TANTO
    PARA EL USUARIO, COMO PARA LOS BOTS.
    '''
    
    contar_palitos:int=INICIAR_CONTADOR
    CANTIDAD_DE_COLUMNAS:int=len(tablero[0])
    for palitos in range(CANTIDAD_DE_COLUMNAS):

        if (tablero[fila-DISMINUYE_EN_UNO][palitos]==PALITO_COMÚN or 
            tablero[fila-DISMINUYE_EN_UNO][palitos]==PALITO_COLOR_ROJO):
            contar_palitos+=AUMENTA_EN_UNO

    if contar_palitos>=UN_PALITO:
        return True
    
    else:
        return False

    
def tirar_dado(nombres_jugadores:tuple[str],nombres:str)->None:
    '''
    PRE CONDICIÓN: SE ELEJIRÁ UN NÚMERO AL AZAR ENTRE EL 1 Y 6.

    POST CONDICIÓN: UNA VEZ TENIENDO ESE VALOR, DEPENDIENDO DE QUIEN SEA EL
                    TURNOS (USUARIO O BOT), SALDRÁ UN MENSAJE DISTINTO 
                    ('AGARRASTE' O 'AGARRÓ').
    '''
    
    YO=nombres_jugadores[PRIMER_NOMBRE]
    número_de_dado=random.randint(MÍN_VALOR_DEL_DADO,MÁX_VALOR_DEL_DADO)

    if nombres==YO:
        input('Agarraste palito rojo')
        input('Tirando dado...')
        input(f'Salió el número {número_de_dado}')

        return número_de_dado
    
    else:
        input('Agarró un palito rojo')
        input('Tirando dado...')
        input(f'Le salió el número {número_de_dado}')

        return número_de_dado


def evento1(nombres_seleccionados:tuple[str],turnos_no_se_ha_bloqueado:dict,nombres:str)->None:
    '''
    MODIFICARÁ EL DICCIONARIO DE CONTROL DE TURNOS Y CAMBIARÁ EL VALOR
    PARA QUE EN SU SIGUIENTE TURNO, NO PUEDA JUGAR, Y PASE AL GUIENTE.
    LUEGO VUELVE A CAMBIARSE NUEVAMENTE EL VALOR DEL DICCIONARIO DE ESE JUGADOR
    PARA QUE PUEDA VOLVER A JUGAR EL PRÓXIMO TURNO CON NORMALIDAD.
    '''
    
    YO=nombres_seleccionados[PRIMER_NOMBRE]

    if nombres==YO:
        input('pierdes el próximo turno')
        turnos_no_se_ha_bloqueado[YO]=False

    else:
        input('pierde el próximo turmo')
        turnos_no_se_ha_bloqueado[nombres]=False


def evento2(tablero:list[str],nombres_seleccionados:tuple[str],nombres:str)->list[str]:
    '''
    PRE CONDICIÓN: SE TIENE QUE ELEGIR UN VALOR NUMÉRICO ENTRE 1 Y M PALITOS, PARA QUE
                   SE PUEDA EJECUTAR EL EVENTO Y NO ROMPA.

    POST CONDICIÓN: SE IMPLEMENTA LA CANTIDAD DE PALITOS ELEGIDA Y SE
                    MOSTRARÁN EN EL TABLERO.
    '''
    
    tablero=reacomodar_tablero(tablero)
    imprimir_tablero_con_indices(tablero)
    cantidad_de_espacios_vacios=contar_espacios_vacios_de_la_piramide(lista_de_palitos_de_la_piramide(tablero))
    FILAS=len(tablero)
    COLUMNAS=len(tablero[0])
    YO=nombres_seleccionados[PRIMER_NOMBRE]

    if nombres==YO:
        cantidad_palitos_para_agregar:str=int(input(f'¿Cuantos palitos desea agregar?, puede ser entre 1 a {cantidad_de_espacios_vacios} palitos: '))
    else: 
        cantidad_palitos_para_agregar:int=random.randint(1,cantidad_de_espacios_vacios)

    contador_palitos_agregados:int=1
    for iterar_elementos_de_la_piramide in range(FILAS):
        for encontrar_espacio_vacío in range(COLUMNAS):
            if contador_palitos_agregados<=cantidad_palitos_para_agregar:
                if tablero[iterar_elementos_de_la_piramide][encontrar_espacio_vacío]==ESPACIO_VACÍO:
                    tablero[iterar_elementos_de_la_piramide][encontrar_espacio_vacío]=PALITO_COMÚN
                    contador_palitos_agregados+=AUMENTA_EN_UNO

    imprimir_tablero_con_indices(tablero)
    input(f'se agregaron los {cantidad_palitos_para_agregar} palitos solicitados')

    return tablero


def evento3(tablero:list[str])->list[str]:
    '''
    SE BLOQUEARÁN EL 20% DE PALITOS COMUNES Y ROJOS QUE HAYAN
    EN LA PIRAMIDE. SERÁN DE COLOR VERDE.
    SI EL 20% DE PALITO ES MENOS A 1, SE TOMA COMO 1.
    '''
    
    CANTIDAD_DE_FILAS:int=len(tablero)
    lista_todos_los_elementos:list=lista_de_palitos_de_la_piramide(tablero)
    CANTIDAD_DE_ELEMENTOS:int=len(lista_todos_los_elementos)
    posición_palitos:list=[]
    contador_palitos_no_verdes:int=contar_palitos_normales_o_rojos_de_la_piramide(lista_todos_los_elementos)

    for guardar_posiciones_palitos_totales in range(CANTIDAD_DE_ELEMENTOS):
        if (not lista_todos_los_elementos[guardar_posiciones_palitos_totales]==ESPACIO_VACÍO 
            and not lista_todos_los_elementos[guardar_posiciones_palitos_totales]==PALITO_COLOR_VERDE):
            posición_palitos.append(guardar_posiciones_palitos_totales)

    porcentaje_palitos:int=round(contador_palitos_no_verdes*PORCENTAJE_PARA_BLOQUEAR_PALITOS)
    palitos_a_pintar=random.sample(posición_palitos,porcentaje_palitos)
    for color in palitos_a_pintar:
        lista_todos_los_elementos[color]=PALITO_COLOR_VERDE

    return armar_piramide(CANTIDAD_DE_FILAS,lista_todos_los_elementos)


def evento4(tablero:list[str],nombres_seleccionados:tuple[str],nombres:str)->list[str]:
    '''
    PRE CONDICIÓN: SE TIENE QUE ELEGIR ENTRE LA CANTIDAD DE FILAS QUE HAYA, OBLIGATORIAMENTE.
                   ASÍ NO ROMPE, SI PONEMOS CUALQUIER OTRO VALOR QUE NO SEA NÚMERICO.

    POST CONDICIÓN: DICHA FILA, LOS PALITOS SERAN ELIMINADOS.
    '''

    YO=nombres_seleccionados[PRIMER_NOMBRE]
    CANTIDAD_DE_COLUMNAS:int=len(tablero[0])
    fila_no_hay_palitos:bool=True

    while fila_no_hay_palitos:
        if nombres==YO:
            fila:str=int(input('¿Cuál fila desea sacar los palitos: '))
            if hay_palitos_en_la_fila(tablero,fila):
                fila_no_hay_palitos:bool=False
        else:
            fila:int=random.randint(1,len(tablero))
            if hay_palitos_en_la_fila(tablero,fila):
                input(f'{nombres} eligió la fila {fila}')
                fila_no_hay_palitos:bool=False


    for elementos in range(CANTIDAD_DE_COLUMNAS):
        if (tablero[fila-DISMINUYE_EN_UNO][elementos]==PALITO_COMÚN or 
            tablero[fila-DISMINUYE_EN_UNO][elementos]==PALITO_COLOR_ROJO or 
            tablero[fila-DISMINUYE_EN_UNO][elementos]==PALITO_COLOR_VERDE):

            tablero[fila-DISMINUYE_EN_UNO][elementos]=ESPACIO_VACÍO

    imprimir_tablero_con_indices(tablero)
    return tablero


def evento5(cantiadd_filas_de_palitos:int,tablero:list[str])->list[str]:
    '''
    CREA UN NUEVO TABLERO
    '''
    
    imprimir_tablero_con_indices(tablero)
    input('Haciendo nuevo tablero...')

    return armar_piramide(cantiadd_filas_de_palitos,creación_de_palitos(cantiadd_filas_de_palitos))


def evento6(tablero)->None:
    '''
    LITERALMENTE, NO PASA NADA. NO HAY EFECTOS.
    '''
    
    imprimir_tablero_con_indices(tablero)
    input('No pasó nada')


def eventos_totales(
        numero_dado, 
        tablero, 
        nombres_seleccionados, 
        nombres, turnos_jugadores,
        tiempo_palitos_bloqueados,
        coordenadas_guardadas,
        cantidad_filas_de_palitos)->list[str]:
    '''
    SECCIÓN DONDE TENGO LOS EVENTOS Y COSAS EXTRAS, PARA QUE EL PROGRAMA VAYA BIEN.
    '''
    
    if numero_dado == 1:
        evento1(nombres_seleccionados, turnos_jugadores, nombres)
    elif numero_dado == 2:
        tablero=evento2(tablero,nombres_seleccionados,nombres)
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


def ejecución_de_eventos(tablero:list[str], NOMBRES_SELECCIONADOS:tuple[str], 
                         nombres:str,turnos_jugadores:dict, 
                         tiempo_palitos_bloqueados:dict, 
                         coordenadas_guardadas:list[tuple[int]], 
                         CANTIDAD_FILAS_DE_PALITOS:int)->list[str]:
    '''
    FUNCIÓN QUE EJECUTA EL VALOR DE LA FUNCIÓN DEL DADO ALEATORIO Y EL NUEVO VALOR DEL TABLERO
    '''
    
    imprimir_tablero_con_indices(tablero)
    numero_dado=tirar_dado(NOMBRES_SELECCIONADOS,nombres)
    tablero=eventos_totales(numero_dado, tablero, 
                            NOMBRES_SELECCIONADOS, nombres, 
                            turnos_jugadores, tiempo_palitos_bloqueados, 
                            coordenadas_guardadas, CANTIDAD_FILAS_DE_PALITOS)
    
    return tablero


def guardar_coordenadas_y_turnos_de_palitos_bloqueados(tablero:list[str],tiempo_palitos_bloqueados:dict, 
                                                       coordenadas_guardadas:list[tuple[int]])->None:
    '''
    GUARDA, EN UN DICCIONARIO EN EL MAIN, LAS COORDENADAS NUEVAS, LA CANTIDAD DE PALITOS Y LA CANTIDAD DE TURNOS QUE ESTARÁN
    BLOQUEADOS LOS PALITOS DEL EVENTO 3.
    VERIFICA QUE LAS COORDENADAS SEAN NUEVAS Y CREA UNA NUEVA SECCIÓN. TODAS LAS COORDENADAS
    SE GUARDAN EN UNA LISTA EN EL MAIN.
    '''
    
    código:str='bloqueo ' + str(len(tiempo_palitos_bloqueados)+AUMENTA_EN_UNO)
    nuevas_coordenadas=[]
    cantidad_de_palitos_bloqueados:int=INICIAR_CONTADOR
    FILAS_DEL_TABLERO:int=len(tablero)
    COLUMNAS_DEL_TABLERO:int=len(tablero[COLUMNAS])

    for fila in range(FILAS_DEL_TABLERO):
        for columna in range(COLUMNAS_DEL_TABLERO):
            if tablero[fila][columna]==PALITO_COLOR_VERDE:
                if (fila,columna) not in coordenadas_guardadas:
                    nuevas_coordenadas.append((fila,columna))
                    cantidad_de_palitos_bloqueados+=AUMENTA_EN_UNO

    tiempo_palitos_bloqueados[código]={
        'turnos de vida'    :4, 
        'coordenadas'       :nuevas_coordenadas,
        'palitos bloqueados':cantidad_de_palitos_bloqueados
    }

    coordenadas_guardadas+=nuevas_coordenadas


def reducir_turnos_de_palitos_bloqueados(tablero:list[str],tiempo_palitos_bloqueados:dict,coordenadas_guardadas:list[tuple[int]])->None:
    '''
    CADA TURNO QUE PASE (CADA CAMBIO DE NOMBRE), SE REDUCIRÁ EN 1 EL VALOR NUMERICO DEL TIEMPO DE VIDA
    QUE TIENE EL BLOQUE DE PALITOS BLOQUEADOS, UNA VEZ QUE LLEGUE A 0, LOS VALORES EN EL DICCIONARIO
    NO DESAPARECERAN, PERO SÍ LAS COORDENADAS GUARDADAS EN LA LISTA.
    '''
    
    TURNOS_DE_VIDA_DE_PALITOS_VERDES:int=len(tiempo_palitos_bloqueados)
    if TURNOS_DE_VIDA_DE_PALITOS_VERDES>0:
        for bloqueos_guardados in tiempo_palitos_bloqueados:
            tiempo_palitos_bloqueados[bloqueos_guardados]['turnos de vida']-=DISMINUYE_EN_UNO
            if tiempo_palitos_bloqueados[bloqueos_guardados]['turnos de vida']==SE_ACABÓ_EL_TIEMPO:
                for coordenadas in tiempo_palitos_bloqueados[bloqueos_guardados]['coordenadas']:
                    tablero[coordenadas[PRIMERA_COORDENADA]][coordenadas[SEGUNDA_COORDENADA]]=PALITO_COMÚN
                coordenadas_guardadas=coordenadas_guardadas[tiempo_palitos_bloqueados[bloqueos_guardados]['palitos bloqueados']::]
                input(f'A continuación se desbloqueará los palitos del {bloqueos_guardados}')
    else:
        None


def se_acabaron_los_palitos(tablero:list[str])->bool:
    '''
    CUENTA LA CANTIDAD DE PALITOS COMUNES O PALITOS COLOR ROJOS. SI LA
    CANTIDAD ES IGUAL A 0, PODEMOS AVANZAR A LA SIGUIENTE FUNCIÓN DE ABAJO.
    EN EL CONTEO NO SE TOMA EN CONSIDERACIÓM LOS PALITOS COLOR VERDE, PORQUE
    SI ALGUIEN TEMRINA LA PARTIDA, Y HAY PALITOS VERDE, AL NO HABER OTRO PALITOS
    PARA RETIRAR, SE QUEDA EN UN BUCLE INFINITO, PORQUE NO SE PODRÁ
    PASAR DE TURNO.
    '''
    
    lista_de_palitos_sacado_de_la_piramide=lista_de_palitos_de_la_piramide(tablero)

    if contar_palitos_normales_o_rojos_de_la_piramide(lista_de_palitos_sacado_de_la_piramide)==INICIAR_CONTADOR:
        return True
    
    else:
        return False


def fin_de_la_partida(tablero:list[str],diccionario_jugadas_palitos:dict,perdedor:str)->None:
    '''
    MUESTRA POR PANTALLA QUIEN PERDIÓ (RETIRÓ EL ÚLTIMO PALITO COMÚN O PALITO COLOR ROJO),
    Y TAMBIEN LA CANTIDAD DE PALITOS QUE CADA JUGADOR RETIRÓ.
    NO SE TOMA EN CONSIDERACIÓN LA CANTIDAD DE PALITOS RETIRADO POR ELIMNAR
    UNA FILA.
    '''
    
    imprimir_tablero_con_indices(tablero)
    print('FIN DE LA PARTIDA')
    input(f'{Fore.red}¡PERDISTE {perdedor}!{Style.reset}')
    for jugadores in diccionario_jugadas_palitos:
        palitos=diccionario_jugadas_palitos[jugadores]['contador palitos retirados']
        print(f'{jugadores} sacó {palitos} palitos')


def main():
    palitos_retirados_de_cada_jugador:dict={}
    turnos_no_se_ha_bloqueado:dict={}
    coordenadas_guardadas:list=[]
    tiempo_palitos_bloqueados:dict={}
    CANTIDAD_DE_JUGADORES:tuple=(
        '2 jugadores',
        '3 jugadores',
        '4 jugadores',
        '5 jugadores'
        )
    NOMBRES_DE_JUGADORES:tuple=(
        'ALEJANDRO',
        'FIORELA',
        'MARTIN',
        'ALEXANDRA',
        'LEONARDO',
        'VANESSA'
        )
    NÚMERO_JUGADORES=menú_cantidad_jugadores(CANTIDAD_DE_JUGADORES)
    NOMBRES_SELECCIONADOS=fijar_jugadores(NOMBRES_DE_JUGADORES,NÚMERO_JUGADORES)
    seguimiento_turnos(NOMBRES_SELECCIONADOS,turnos_no_se_ha_bloqueado)
    CANTIDAD_FILAS_DE_PALITOS=menú_cantidad_filas(NÚMERO_JUGADORES)
    marcador_jugadores(NOMBRES_SELECCIONADOS,palitos_retirados_de_cada_jugador)
    tablero=armar_piramide(CANTIDAD_FILAS_DE_PALITOS,creación_de_palitos(CANTIDAD_FILAS_DE_PALITOS))
    reglas(tablero)
    YO=NOMBRES_SELECCIONADOS[PRIMER_NOMBRE]
    CANTIDAD_DE_FILAS:int=len(tablero)
    CANTIDAD_DE_COLUMNAS:int=len(tablero[0])
    sigamos_con_el_juego:bool=True
    seguir_actualizando_tablero:bool=True
    actualizar_jugada:bool=True

    while sigamos_con_el_juego:
        for nombres in NOMBRES_SELECCIONADOS:
            if actualizar_jugada:
                aún_no_se_seleccionó_palito_rojo:bool=True
                sacar_cantidad_palitos:int=MÍN_PALITOS
                
                if nombres==YO:
                    if turnos_no_se_ha_bloqueado[YO]:
                        mencionar_turno(nombres,tablero)
                        cantidad_elejida_de_palitos=elegir_cantidad_de_palitos(MÍN_PALITOS,MÁX_PALITOS)

                        while sacar_cantidad_palitos<=cantidad_elejida_de_palitos:
                            coordenadas=coordenadas_del_tablero(tablero,sacar_cantidad_palitos,cantidad_elejida_de_palitos)

                            if posición_es_vacío(tablero,coordenadas):
                                mensaje_posición_es_vacía(tablero)

                            elif posición_está_bloqueado(tablero,coordenadas):
                                mensaje_posición_está_bloqueada(tablero)
                                
                            elif posición_hay_palito_rojo(tablero,coordenadas):
                                sacar_palito(tablero,coordenadas)
                                if aún_no_se_seleccionó_palito_rojo:
                                    tablero=ejecución_de_eventos(tablero, NOMBRES_SELECCIONADOS, nombres, 
                                                                 turnos_no_se_ha_bloqueado, tiempo_palitos_bloqueados, 
                                                                 coordenadas_guardadas, CANTIDAD_FILAS_DE_PALITOS)
                                    aún_no_se_seleccionó_palito_rojo:bool=False
                                    if se_acabaron_los_palitos(tablero):
                                        sacar_cantidad_palitos=cantidad_elejida_de_palitos+AUMENTA_EN_UNO
                                        seguir_actualizando_tablero:bool=False
                                    imprimir_tablero_con_indices(tablero)
                                if se_acabaron_los_palitos(tablero):
                                    sacar_cantidad_palitos=cantidad_elejida_de_palitos+AUMENTA_EN_UNO
                                    seguir_actualizando_tablero:bool=False
                                imprimir_tablero_con_indices(tablero)
                                sacar_cantidad_palitos+=1
                                palitos_retirados_de_cada_jugador[YO]['contador palitos retirados']+=AUMENTA_EN_UNO

                            else:
                                sacar_palito(tablero,coordenadas)
                                if se_acabaron_los_palitos(tablero):
                                    sacar_cantidad_palitos=cantidad_elejida_de_palitos+AUMENTA_EN_UNO
                                    seguir_actualizando_tablero:bool=False
                                imprimir_tablero_con_indices(tablero)
                                sacar_cantidad_palitos+=1
                                palitos_retirados_de_cada_jugador[YO]['contador palitos retirados']+=AUMENTA_EN_UNO


                        if seguir_actualizando_tablero: 
                            reducir_turnos_de_palitos_bloqueados(tablero,tiempo_palitos_bloqueados,coordenadas_guardadas)
                            input('REACOMODANDO...')
                            tablero=reacomodar_tablero(tablero)
                            imprimir_tablero_con_indices(tablero)

                        else:
                            sigamos_con_el_juego:bool=False
                            actualizar_jugada:bool=False
                            perdedor=YO

                    else:
                        imprimir_tablero_con_indices(tablero)
                        reducir_turnos_de_palitos_bloqueados(tablero,tiempo_palitos_bloqueados,coordenadas_guardadas)
                        input(f'Perdiste el turno')
                        turnos_no_se_ha_bloqueado[YO]=True


                else:

                    if turnos_no_se_ha_bloqueado[nombres]:
                        mencionar_turno(nombres,tablero)
                        cantidad_elejida_de_palitos:int=cantidad_de_palitos_bots(MÍN_PALITOS,MÁX_PALITOS)
                        imprimir_cantidad_de_palitos_elegidos(cantidad_elejida_de_palitos)

                        while sacar_cantidad_palitos<=cantidad_elejida_de_palitos:
                            coordenadas=coordenadas_bots(CANTIDAD_DE_FILAS,CANTIDAD_DE_COLUMNAS)

                            if  posición_es_vacío(tablero,coordenadas) or posición_está_bloqueado(tablero,coordenadas):
                                None

                            elif posición_hay_palito_rojo(tablero,coordenadas):
                                mostrar_cantidades_de_palitos_a_sacar_y_coordenadas(tablero,sacar_cantidad_palitos,cantidad_elejida_de_palitos,coordenadas)
                                sacar_palito(tablero,coordenadas)
                                if aún_no_se_seleccionó_palito_rojo:
                                    tablero=ejecución_de_eventos(tablero, NOMBRES_SELECCIONADOS, nombres, 
                                                                 turnos_no_se_ha_bloqueado, tiempo_palitos_bloqueados, 
                                                                 coordenadas_guardadas, CANTIDAD_FILAS_DE_PALITOS)
                                    aún_no_se_seleccionó_palito_rojo=False
                                    if se_acabaron_los_palitos(tablero):
                                        sacar_cantidad_palitos=cantidad_elejida_de_palitos+AUMENTA_EN_UNO
                                        seguir_actualizando_tablero:bool=False
                                    imprimir_tablero_con_indices(tablero)
                                if se_acabaron_los_palitos(tablero):
                                    sacar_cantidad_palitos=cantidad_elejida_de_palitos+AUMENTA_EN_UNO
                                    seguir_actualizando_tablero:bool=False
                                imprimir_tablero_con_indices(tablero)
                                sacar_cantidad_palitos+=AUMENTA_EN_UNO
                                palitos_retirados_de_cada_jugador[nombres]['contador palitos retirados']+=AUMENTA_EN_UNO


                            else:
                                mostrar_cantidades_de_palitos_a_sacar_y_coordenadas(tablero,sacar_cantidad_palitos,cantidad_elejida_de_palitos,coordenadas)
                                sacar_palito(tablero,coordenadas)
                                if se_acabaron_los_palitos(tablero):
                                    sacar_cantidad_palitos=cantidad_elejida_de_palitos+AUMENTA_EN_UNO
                                    seguir_actualizando_tablero:bool=False
                                imprimir_tablero_con_indices(tablero)
                                sacar_cantidad_palitos+=AUMENTA_EN_UNO
                                palitos_retirados_de_cada_jugador[nombres]['contador palitos retirados']+=AUMENTA_EN_UNO


                        if seguir_actualizando_tablero:
                            input('REACOMODANDO...')
                            reducir_turnos_de_palitos_bloqueados(tablero,tiempo_palitos_bloqueados,coordenadas_guardadas)
                            tablero=reacomodar_tablero(tablero)
                            imprimir_tablero_con_indices(tablero)

                        else:
                            sigamos_con_el_juego:bool=False
                            actualizar_jugada:bool=False
                            perdedor=nombres

                            
                    else:
                        imprimir_tablero_con_indices(tablero)
                        reducir_turnos_de_palitos_bloqueados(tablero,tiempo_palitos_bloqueados,coordenadas_guardadas)
                        input(f'{nombres} perdió el turno')
                        turnos_no_se_ha_bloqueado[nombres]=True


    fin_de_la_partida(tablero,palitos_retirados_de_cada_jugador,perdedor)

main()