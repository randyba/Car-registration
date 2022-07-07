# FUNCIONES PROPIAS -----------------------------------------------------------------------------------------#

def leer_modelo_auto(mensaje):
    """Función para corroborar que el modelo del auto no se pase de 10 caracteres"""
    #Solicitar y validar el modelo del auto
    Validar=True
    #Crear un ciclo while para validar el modelo
    
    while Validar:
        Modelo=input(mensaje)
        #Contar los caracteres del modelo
        MOD=len(Modelo)
        #Verificar que el modelo del auto no se pase de 10 caracteres
        if MOD <= 10:
            #Salimos del ciclo while
            Validar=False
        else:
            #Volvemos a solicitar el modelo y seguimos dentro del ciclo while
            print("No se puede registrar este modelo, ingrese uno con un máximo de 10 caracteres")
            #Repetimos en ciclo while
            Validar=True
    return Modelo

def leer_numero_entero_positivo(Mensaje):
    """Función para leer el año del auto y validar que este sea mayor a 1970 y menor a 2023"""
    # Solicitar y Validar año del auto.
    Validar = True
    # Crear ciclo While de validación para año.
    
    while Validar:
        # Solicitar año del Persona auto.
        Numero = input(Mensaje)
        # Verficiar que año sea un Número Entero.
        try:
            # Convertir Numero a Entero.
            Numero = int(Numero)
            # Revisar si Edad es un Entero Positivo.
            if Numero > 1969 and Numero < 2024:
                # Salir del Ciclo While Interno, pues año es Válido.
                Validar = False
            else:
                # Sigo en el ciclo While Interno, pues año es Inválido.
                Validar = True
                # Mensaje de Error.
                print("ERROR: El Número debe ser Positivo, mayor a 1969 y menor a 2024.")
        except ValueError:
            # año no es un Entero Valido.
            print("ERROR: El Número debe ser Entero.")
    return Numero

def preguntar_usuario_por_condicion(Mensaje):
    """Función para preguntar a usuario si quiere repetir la accion
    de ingresar más datos a según la cantidad de autos que hay"""
    # Preguntar a la Persona Usuaria si Desea Insertar otro Registro --------------------------------------
    Validar = True
    # Variable de Resultado.
    Resultado = True
    # Ciclo While Interno para Preguntar si se Deasea Repetir el Programa.
    
    while Validar:
        # Preguntar al Usuario si Desea Repetir el Programa.
        Letra = input(Mensaje)
        # Validación de Letra: Revisamos si Letra es (S/s) o (N/n)?
        if Letra == "S" or Letra == "s":
            # Letra es Valida, entonces salimos del Ciclo While Interno.
            Validar = False
            # Usuario Desea Repetir otra Vez el Programa.
            Resultado = True
        elif Letra == "N" or Letra == "n":
            # Letra es Valida, entonces salimos del Ciclo While Interno.
            Validar = False
            # Usuario Desea Repetir otra Vez el Programa.
            Resultado = False
        else:
            # Letra es Inválida, entonces volvemos a pedir una letra.
            print("ERROR: Letra Insertada es Inválida. Debe digitar (S/N)")
            Validar = True
    # Regresando al programa principal.
    return Resultado

def ordenar_lista_2D(lista_2D, columna):
    # Parámetros: Lista en 2D Original (lista_2D) y Posición o Columna de Referencia para Ordenamiento.
    # Crear una Lista Para los Datos de Referencia.
    columna_ref = []
    # Crear una Lista en 2D vacía para los datos ordenados.
    lista_2D_ord = []
    # Secuencia de Control.
    sec_control = range(len(lista_2D))
    # Ciclo FOR para Extraer Datos de Referencia de la Lista en 2D.
    
    for i in sec_control:
        # Extraer Dato de Referencia de Lista 2D.
        columna_ref += [lista_2D[i][columna]]
    # Ordenando los Datos de Referencia De Menor a Mayor.
    columna_ref_ord = sorted(columna_ref)
    # Ciclo FOR para Recorrer Datos Ordenados y Crear Lista Ordenada en 2D.
    
    for i in sec_control:
        # Tomar Valor de Referencia de la Columna Ordenada.
        referencia = columna_ref_ord[i]
        # Tomar Elemento de Datos Ordenados.
        i_ref = columna_ref.index(referencia)
        # Agregar Fila Correspondiente a Lista 2D Ordenada.
        lista_2D_ord += [lista_2D[i_ref]]
        # Para Evitar Problemas con Valores de Referencia Iguales.
        columna_ref[i_ref] = None
    # Retornando Lista 2D Ordenada.
    return lista_2D_ord  

#Librerías--------------------------------------------------------------------------------------------------#
from enum import auto
from prettytable import PrettyTable
import os
from audioop import reverse

# PROGRAMA PRINCIPAL ---------------------------------------------------------------------------------------#
# Pantalla Inicial.

print("********************************************************************")
print("**                                                                **")
print("**              Bienvenido al sistema de registro de              **")
print("**         La Corporación Automovilística de Costa Rica           **")
print("**                                                                **")
print("********************************************************************\n")
input("Presione ENTER para continuar")

# Borrar Pantalla.
os.system("cls")

#Se crea una lista en 2 dimenciones para llevar un control de los datos de los autos
Lista_Autos=[]

# Condición de Repetición del Programa Principal.
Repetir = True

# Ciclo While Para Solicitar Datos de Atletas.
while Repetir:
    # Borrar Pantalla.
    os.system("cls")
    # Encabezado.
    print("********************************************************************")
    print("**                 INGRESANDO DATOS DE LOS AUTOS                  **")
    print("********************************************************************\n")
    # Crear Nuevo Registro en Blanco (Lista Simple).
    Auto=[]
    # Solicitar marca del auto.
    Marca=input("MARCA: ")
    # Agregando Nombre a Registro de Atleta.
    Auto+=[Marca]
    # Solicitar El Modelo del Auto.
    Modelo= leer_modelo_auto("Ingrese el modelo del Auto: ")
    # Agregando el modelo a Registro de Auto.
    Auto+=[Modelo]
    # Solicitar el año del Auto.
    Año = leer_numero_entero_positivo("Inserte el Año del Auto: ")
    # Agregando el año al Registro de Auto.
    Auto+=[Año]
    # Solicitar el Color del Auto.
    Color=input("Ingrese el color del Auto: ")
    # Agregando el Color a Registro de Auto.
    Auto+=[Color]
    #Agregar los datos a la lista 2 dimenciones
    Lista_Autos+=[Auto]
    Repetir = preguntar_usuario_por_condicion("Desea Ingresar Datos de Otro Auto (S/N)? ")

# Borrar Pantalla, para posteriormente presentar todos los datos de los Autos ingresados.
os.system("cls")

# Encabezado.
print("********************************************************************")
print("**                     Mostrando la lista de                      **")
print("**                   Todos los autos ingresados                   **")
print("********************************************************************\n")    

#Mostrar la tabla con los resultados ingresados
Tabla=PrettyTable(["Marca", "Modelo", "Año", "Color"])

#Agregar las filas de la Lista en 2 dimenciones
Tabla.add_rows(Lista_Autos)

# Presentar Tabla en Pantalla.
print(Tabla)
print()

# Solicitar ENTER para Continuar.
input("Presione ENTER para Continuar...")

# Borrar Pantalla.
os.system("cls")

# Encabezado.
print("********************************************************************")
print("**                     Presentando los autos                      **")
print("**                  De más viejos a más nuevos                    **")
print("********************************************************************\n")

# Mostrar una Tabla con los años de los Autos Ordenados de menor a mayor.
Lista_Autos_Ordenados = ordenar_lista_2D(Lista_Autos, 2)

# Crear un Nuevo Objeto de Tabla.
Tabla=PrettyTable(["Marca", "Modelo", "Año", "Color"])

# Agregar los Datos de la Lista en 2D Ordenada.
Tabla.add_rows(Lista_Autos_Ordenados)

# Mostrar la Tabla en Pantalla de los Autos ya acomodados de menor a mayor según su año.
print(Tabla)
print()

# Solicitar al Usuario que Presione ENTER para continuar.
input("Presione ENTER para Continuar...")

# Borrar Pantalla, para posteriormente presentar el auto más moderno en pantalla.
os.system("cls")

# Encabezado.
print("********************************************************************")
print("**                   Presentando lo más moderno                   **")
print("**                            en Autos                            **")
print("********************************************************************\n")

# Crear un Nuevo Objeto de Tabla.
Tabla=PrettyTable(["Marca", "Modelo", "Año", "Color"])

#Se crea una secuencia de control para dar orden a un ciclo FOR
Sec_Control=range(len(Lista_Autos_Ordenados))

#Se crea una lista en 2 dimenciones con el o los autos más modernos
Autos_Modernos=[]

#Se crea un ciclo FOR para buscar los modelos más recientes
for i in Sec_Control:

    #Se buscan los modelos más recientes
    Moderno=Lista_Autos_Ordenados[-1][2]

    #Se verifica el que hay o si hay más
    if Lista_Autos_Ordenados[i][2]==Moderno:
        #Si hay una o más coincidencias se agregan a la lista en 2 dimenciones
        Autos_Modernos+=[Lista_Autos_Ordenados[i]]

#Agregar a la tlaba el o los Autos mas modernos.
Tabla.add_rows(Autos_Modernos)

# Mostrar la Tabla en Pantalla, con la información del Auto más moderno que se tiene en los registros.
print(Tabla)
print()

# Solicitar al Usuario que Presione ENTER para continuar.
input("Presione ENTER para Continuar...")

# Borrar Pantalla, para posteriormente presentar la despedida al usuario.
os.system("cls")

# Encabezado de despedida que se mostrará al usuario en pantalla.
print("********************************************************************")
print("**                        Fin del Sistema                         **")
print("**                Gracias por ejecutar el programa                **")
print("********************************************************************\n")

# Solicitar al Usuario que Presione ENTER para continuar.
input("Presione ENTER para Salir...")