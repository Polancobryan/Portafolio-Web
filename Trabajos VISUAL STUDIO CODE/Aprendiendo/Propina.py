mensaje = float (input("¿Cuál es la factura total de hoy, por favor?"))
if mensaje <= 50:
    porcentaje = mensaje % 18
    suma = porcentaje + mensaje
    print ("La propina aplicando el 18% es",porcentaje, "y el total seria de:" ,suma)
    elif mensaje >=50 and 