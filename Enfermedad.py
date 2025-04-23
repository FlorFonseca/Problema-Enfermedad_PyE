#Enfermedad
import numpy as np
import random

def simulacion_diagnostico(num_personas=1000000):
 
    Nombre_Enfermedad = input("Ingresa el nombre de la enfermedad: ")
    De_Cada = 10000
    Afecta_A = 1
    Prob_Enfermedad = Afecta_A/De_Cada
    Prob_FalsoPositivo = 0.02 #P(Positivo | NoEnfermo)
    Prob_FalsoNegativo = 0.01 #P(Negativo | Enfermo)

    Tiene_Enfermedad = 0
    Test_Positivo = 0
    Tiene_Enfermedad_Y_Test_Positivo = 0
    
    for _ in range(num_personas):
        # deterina si la persona tiene la enfermedad según la Prob_Enfermedad
        if random.random() < Prob_Enfermedad:
            Tiene_Enfermedad += 1
            if random.random() >= Prob_FalsoNegativo:
                Test_Positivo += 1
                Tiene_Enfermedad_Y_Test_Positivo += 1
        else:
            # Si no tiene la enfermedad, entonces se chequea si es faldo positivo
            if random.random() < Prob_FalsoPositivo:
                Test_Positivo += 1
    
    Prob_Empirica = Tiene_Enfermedad_Y_Test_Positivo / Test_Positivo if Test_Positivo > 0 else 0
    
    print(f"\n=== RESULTADOS DE LA SIMULACIÓN (n={num_personas}) ===")
    print(f"Nombre de la enfermedad: {Nombre_Enfermedad}")
    print(f"Número de personas enfermas: {Tiene_Enfermedad}")
    print(f"Probabilidad de personas con test positivo: {Test_Positivo:.6f}")
    print(f"Probabilidad de personas enfermas y test positivo: {Tiene_Enfermedad_Y_Test_Positivo:.6f}")
    print(f"Probabilidad empírica de que la persona seleccionada esté enferma dado que el test dió un resultado positivo: {Prob_Empirica:.6f}")
    
    return Prob_Empirica

def simulacion_diagnostico_configurable(num_personas=1000000):
    #PErmitimos que el usuario pueda configurar los valores del diagnósitoco
    Nombre_Enfermedad = input("Ingresa el nombre de la enfermedad: ")
    De_Cada = int(input("Ingresa la cantidad de integrantes de la muestra (número entero): "))
    Afecta_A = int(input("Ingresa a la cantidad de personas que afecta esta enfermedad (número entero): "))
    
    # preguntamos al usuario las tasas de falsos positivos y negativos
    print("Recuerda que la probabilidad de falso positivo es la probabilidad de que el test sea positivo dado que la persona no tiene la enfermedad.") #P(Positivo | NoEnfermo)
    print("Al ingresar un número decimal utiliza el punto (.) como separador decimal.")
    Prob_FalsoPositivo = float(input("Ingresa la probabilidad de falso positivo (0-1): "))
    print("Recuerda que la probabilidad de falso negativo es la probabilidad de que el test sea negativo dado que la persona tiene la enfermedad.") #P(Negativo | Enfermo)
    print("Al ingresar un número decimal utiliza el punto (.) como separador decimal.")
    Prob_FalsoNegativo = float(input("Ingresa la probabilidad de falso negativo (0-1): "))
    
    Prob_Enfermedad = Afecta_A/De_Cada
    Tiene_Enfermedad = 0
    Test_Positivo = 0
    Tiene_Enfermedad_Y_Test_Positivo = 0
    
    for _ in range(num_personas):
        # determina si la persona tiene la enfermedad según la Prob_Enfermedad
        if random.random() < Prob_Enfermedad:
            Tiene_Enfermedad += 1
            if random.random() >= Prob_FalsoNegativo:
                Test_Positivo += 1
                Tiene_Enfermedad_Y_Test_Positivo += 1
        else:
            # si no tiene la enfermedad, entonces se chequea si es falso positivo
            if random.random() < Prob_FalsoPositivo:
                Test_Positivo += 1
    
    Prob_Empirica = Tiene_Enfermedad_Y_Test_Positivo / Test_Positivo if Test_Positivo > 0 else 0
    
    print(f"\n=== RESULTADOS DE LA SIMULACIÓN (n={num_personas}) ===")
    print(f"Nombre de la enfermedad: {Nombre_Enfermedad}")
    print(f"Probabilidad previa (prevalencia): {Prob_Enfermedad:.6f}")
    print(f"Tasa de falsos positivos: {Prob_FalsoPositivo:.6f}")
    print(f"Tasa de falsos negativos: {Prob_FalsoNegativo:.6f}")
    print(f"Número de personas enfermas: {Tiene_Enfermedad:}")
    print(f"Probabilidad de personas con test positivo: {Test_Positivo:.6f}")
    print(f"Probabilidad de personas enfermas y test positivo: {Tiene_Enfermedad_Y_Test_Positivo:.6f}")
    print(f"Probabilidad empírica P(Enfermo|Positivo): {Prob_Empirica:.6f}")
    
    return Prob_Empirica


def detectarEnfermedad_Exacto ():
    # calculamos la probabilidad exacta utilizando los valores del ejercicio
    Nombre_Enfermedad = input("Ingresa el nombre de la enfermedad: ")
    De_Cada = 10000
    Afecta_A = 1

    Prob_FalsoPositivo = 0.02 #P(Positivo | NoEnfermo)
    Prob_FalsoNegativo = 0.01 #P(Negativo | Enfermo)
    Prob_VerdaderoPositivo = 1 - Prob_FalsoNegativo #P(Positivo | Enfermo)
    Prob_VerdaderoNegativo = 1 - Prob_FalsoPositivo #P(Negativo | NoEnfermo)

    Prob_Enfermo= Afecta_A/De_Cada
    Prob_NoEnfermo = 1 - Prob_Enfermo

    
    #P(Positivo) = P(Positivo | Enfermo) P(Enfermo) + P(Positivo | NoEnfermo) P(NoEnfermo)
    Prob_Positivo = (Prob_VerdaderoPositivo * Prob_Enfermo) + (Prob_FalsoPositivo * Prob_NoEnfermo)
    #P(Enfermo|Positivo) = P(Positivo | Enfermo) P(Enfermo) / P(Positivo)
    resultado_Enfermo_Dado_Positivo = (Prob_VerdaderoPositivo * Prob_Enfermo)/Prob_Positivo
    
    print(f"\n=== RESULTADOS EXACTOS ===")
    print(f"Nombre de la enfermedad: {Nombre_Enfermedad}")
    print(f"Probabilidad de personas enfermas: {Prob_Enfermo:.6f}")
    print(f"Probabilidad de personas con test positivo: {Prob_Positivo:.6f}")
    print(f"Probabilidad de personas enfermas y test positivo: {Prob_VerdaderoPositivo:.6f}")
    print(f"Probabilidad exacta de que la persona seleccionada esté enferma dado que el test dió un resultado positivo: {resultado_Enfermo_Dado_Positivo:.6f}")
    
    return resultado_Enfermo_Dado_Positivo

def detectarEnfermedad_Exacto_Configurable():
    # utilizamos esta función para hacer el cálculo exacto pero permitiendo al usuario ingresar los valores a aplicar
    Nombre_Enfermedad = input("Ingresa el nombre de la enfermedad: ")
    De_Cada = int(input("Ingresa la cantidad de integrantes de la muestra (número entero): "))
    Afecta_A = int(input("Ingresa a la cantidad de personas que afecta esta enfermedad (número entero): "))
    
    # permitimos que ingrese las porbabilidades
    print("Recuerda que la probabilidad de falso positivo es la probabilidad de que el test sea positivo dado que la persona no tiene la enfermedad.") #P(Positivo | NoEnfermo)
    print("Al ingresar un número decimal utiliza el punto (.) como separador decimal.")
    Prob_FalsoPositivo = float(input("Ingresa la probabilidad de falso positivo (0-1): ")) #P(Positivo | NoEnfermo)
    print("Recuerda que la probabilidad de falso negativo es la probabilidad de que el test sea negativo dado que la persona tiene la enfermedad.")
    print("Al ingresar un número decimal utiliza el punto (.) como separador decimal.")
    Prob_FalsoNegativo = float(input("Ingresa la probabilidad de falso negativo (0-1): ")) #P(Negativo | Enfermo)
    
    Prob_VerdaderoPositivo = 1 - Prob_FalsoNegativo #P(Positivo | Enfermo)
    Prob_VerdaderoNegativo = 1 - Prob_FalsoPositivo #P(Negativo | NoEnfermo)

    Prob_Enfermo = Afecta_A/De_Cada 
    Prob_NoEnfermo = 1 - Prob_Enfermo

    #P(Positivo) = P(Positivo | Enfermo) P(Enfermo) + P(Positivo | NoEnfermo) P(NoEnfermo)
    Prob_Positivo = (Prob_VerdaderoPositivo * Prob_Enfermo) + (Prob_FalsoPositivo * Prob_NoEnfermo)
    #P(Enfermo|Positivo) = P(Positivo | Enfermo) P(Enfermo) / P(Positivo)
    resultado_Enfermo_Dado_Positivo = (Prob_VerdaderoPositivo * Prob_Enfermo)/Prob_Positivo
    
    print(f"\n=== RESULTADOS EXACTOS ===")
    print(f"Nombre de la enfermedad: {Nombre_Enfermedad}")
    print(f"Probabilidad previa (prevalencia): {Prob_Enfermo:.6f}")
    print(f"Tasa de falsos positivos: {Prob_FalsoPositivo:.6f}")
    print(f"Tasa de falsos negativos: {Prob_FalsoNegativo:.6f}")
    print(f"Probabilidad de test positivo: {Prob_Positivo:.6f}")
    print(f"Probabilidad exacta P(Enfermo|Positivo): {resultado_Enfermo_Dado_Positivo:.6f}")
    
    return resultado_Enfermo_Dado_Positivo


def menu_principal():
    #Creamos un menú para que el usuario elija la función que desea ejecutar
    while True:
        print("\n=== SIMULADOR DE PRUEBAS DIAGNÓSTICAS ===")
        print("1. Simulación de diagnóstico con valores del ejercicio")
        print("2. Cálculo exacto con valores del ejercicio")
        print("3. Simulación de diagnóstico con valores configurables")
        print("4. Cálculo exacto con valores configurables")
        print("5. Comparar simulación y cálculo exacto (parámetros ejericio)")
        print("6. Comparar simulación y cálculo exacto (configurable)")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción (0-6): ")
        
        if opcion == "1":
            simulacion_diagnostico()
        elif opcion == "2":
            detectarEnfermedad_Exacto()
        elif opcion == "3":
            simulacion_diagnostico_configurable()
        elif opcion == "4":
            detectarEnfermedad_Exacto_Configurable()
        elif opcion == "5":
            print("\n--- COMPARACIÓN ENTRE SIMULACIÓN Y RESULTADO EXACTO (parámetros fijos) ---")
            resultado_simulado = simulacion_diagnostico()
            resultado_exacto = detectarEnfermedad_Exacto()
            diferencia = abs(resultado_simulado - resultado_exacto)
            print(f"\nDiferencia entre simulación y resultado exacto: {diferencia:.6f}")
        elif opcion == "6":
            print("\n--- COMPARACIÓN ENTRE SIMULACIÓN Y RESULTADO EXACTO (configurable) ---")
            resultado_simulado = simulacion_diagnostico_configurable()
            resultado_exacto = detectarEnfermedad_Exacto_Configurable()
            diferencia = abs(resultado_simulado - resultado_exacto)
            print(f"\nDiferencia entre simulación y resultado exacto: {diferencia:.6f}")
        elif opcion == "0":
            print("Gracias por usar el simulador. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()



