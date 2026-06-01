def verificar_conexion(estados):
    cables= ('A', 'B', 'C', 'D', 'E')
    n=len(cables)

    for i in range(n):
        if estados[i] is False:
            print("El mensaje se quedó en el Servidor", i)
            return False
    else: 
        print("El mensaje llegó al Servidor", n-1)
        return True


# Ejemplo de uso
cables = [True, True, True, True, True]
verificar_conexion(cables)


