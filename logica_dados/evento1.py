from constantes import PRIMER_NOMBRE

def evento1(nombres_seleccionados:tuple[str], turnos_no_se_ha_bloqueado:dict, nombres:str) -> None:
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