#Enfermedad
import numpy as np
import random

def simulacion_diagnostico(num_personas=1000000):
 
    Nombre_Enfermedad = input("Ingresa el nombre de la enfermedad: ")
    De_Cada = int(input("Ingresa la cantidad de integrantes de la muestra: "))
    Afecta_A = int(input("Ingresa a la cantidad de personas que afecta esta enfermedad: "))
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
    print(f"Número de personas con test positivo: {Test_Positivo}")
    print(f"Número de personas enfermas y test positivo: {Tiene_Enfermedad_Y_Test_Positivo}")
    print(f"Probabilidad empírica de que la persona seleccionada esté enferma dado que el test dió un resultado positivo: {Prob_Empirica}")
    
    return Prob_Empirica


def detectarEnfermedad_Exacto ():
    Nombre_Enfermedad = input("Ingresa el nombre de la enfermedad: ")
    De_Cada = int(input("Ingresa la cantidad de integrantes de la muestra: "))
    Afecta_A = int(input("Ingresa a la cantidad de personas que afecta esta enfermedad: "))
    

    Prob_FalsoPositivo = 0.02 #P(Positivo | NoEnfermo)
    Prob_FalsoNegativo = 0.01 #P(Negativo | Enfermo)
    Prob_VerdaderoPositivo = 1 - Prob_FalsoNegativo #P(Positivo | Enfermo)
    Prob_VerdaderoNegativo = 1 - Prob_FalsoPositivo #P(Negativo | NoEnfermo)
    Prob_Enfermo= Afecta_A/De_Cada
    Prob_NoEnfermo = 1 - Prob_Enfermo

    #P(Enfermo|Positivo) = P(Positivo | Enfermo) P(Enfermo) / P(Positivo)

    Prob_Positivo = (Prob_VerdaderoPositivo * Prob_Enfermo) + (Prob_FalsoPositivo * Prob_NoEnfermo)
    
    resultado_Enfermo_Dado_Positivo = (Prob_VerdaderoPositivo * Prob_Enfermo)/Prob_Positivo
    
    print(f"\n=== RESULTADOS EXACTOS ===")
    print(f"Nombre de la enfermedad: {Nombre_Enfermedad}")
    print(f"Número de personas enfermas: {Prob_Enfermo}")
    print(f"Número de personas con test positivo: {Prob_Positivo}")
    print(f"Número de personas enfermas y test positivo: {Prob_VerdaderoPositivo}")
    print(f"Probabilidad exacta de que la persona seleccionada esté enferma dado que el test dió un resultado positivo: {resultado_Enfermo_Dado_Positivo}")
    
    return resultado_Enfermo_Dado_Positivo

#simulacion_diagnostico()
detectarEnfermedad_Exacto()


