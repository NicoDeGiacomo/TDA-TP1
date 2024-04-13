from Grafo import Grafo
from Heap import Heap


#ENUNCIADO
"""
Parte 2: Reunión de camaradería
****************************************
Una gran empresa realizará una reunión de camaradería para sus empleados. Sin embargo, para evitar problemas que ocurrieron en eventos anteriores,
 no quieren que jefes y empleados directos se mezclen. Es decir que si se invita al jefe, no se puedo invitar a sus subordinados directos. 
 Contamos con el organigrama de la empresa (que tiene una estructura de árbol) y deseamos determinar a quién invitar para lograr 
 la mayor asistencia posible.

Se pide:

1-Determinar y explicar cómo se resolvería este problema utilizando la metodología greedy.

2-Brinde pseudocódigo y estructuras de datos a utilizar.

3-De un ejemplo paso a paso. ¿Qué complejidad temporal y espacial tiene la solución?

4-Justifique por qué corresponde su propuesta a la metodología greedy.

5-Demuestre que su solución es óptima.

"""

#RESOLUSION
"""
EJEMPLO ESTRUCTURA
                        ---------A-----
                        |     |    |  |
                      --B--  -C-   D  E
                      | | |  | |   |
                      F G H  I J  -K-
                                  |||      
                                  LMN 

La opción que pensamos es prorizar invitar a las hojas, e ir de abajo hacia arriba, no invitando a los jefes directos de los ya invitados.
Esto lo podemos hacer con una cola de proridad(Heap) de minimos, en que guardemos todos los nodos con su correspondiente padre(Jefe) y la cantidad de empleados.
Al ser de minimos, las hojas saldran primeros y seran invitadas, y los jefes directos seran guardados en una estructura para indicar que NO deben ser invitados.
Asi lograremos invitar a la mayor cantidad de empleados, y cumplir la norma(en teoria, falta demostrarlo como en el PDF).


Entonces, en el ejemplo, guardamos en la cola de prioridad:
Ej. Tupla = (Nodo,Padre,hijos)

COLA_Prioridad: [ (L,K,0), (M,K,0), (N,K,0), (J,C,0), (I,C,0), (H,B,0), (G,B,0), (F,B,0), (E,A,0), (D,A,1), (C,A,2), (K,D,3), (B,A,3), (A,None,4) ]


Sacamos todas las hojas, las invitamos, y descartamos a los padres(se guardan en set ambas cosas):

Invitados: [ F, G, H, I, J, L, M, N, E]
EVITAR: [ B,C,K,E]

COLA_Prioridad: [ (D,A,1), (C,A,2), (K,D,3), (B,A,3), (A,None,4) ]

al sacar D como la que menos hijos tiene, y ver que no aparece en EVITAR, podemos agregarlo.


Invitados: [ F, G, H, I, J, L, M, N, E, D]
EVITAR: [ B,C,K,E,A]

COLA_Prioridad: [ (C,A,2), (K,D,3), (B,A,3), (A,None,4) ]

Todos los demas van a ser rechazados ya que tienen empleados ya en la fiesta.

TOTAL invitados = 10.

*******************************************************
Es greedy?(Segun ChatGPT):

La solución que propones prioriza invitar a las hojas del organigrama, es decir, a los empleados que no tienen subordinados directos. 
Luego, avanzas hacia los niveles superiores del organigrama, evitando invitar a los jefes directos de los empleados ya invitados. 
Esta estrategia utiliza una cola de prioridad (Heap) de mínimos para gestionar la invitación de los empleados de manera eficiente.

*Análisis de la Solución Propuesta:
Cola de Prioridad (Heap) de Mínimos: Utilizas una cola de prioridad para garantizar que las hojas del organigrama 
(empleados sin subordinados directos) sean las primeras en ser invitadas.
 Esto es coherente con la estrategia greedy de tomar la mejor decisión localmente en cada paso.

Evitar Jefes Directos: Mantienes una estructura adicional para registrar los jefes directos de los empleados ya invitados y asegurarte de no 
invitarlos, cumpliendo así con la restricción del problema.

Respuesta a tu Pregunta:
Sí, la solución que propones puede considerarse un algoritmo greedy. A continuación, se describen los componentes clave 
que confirman esta clasificación:

    Elección Greedy: En cada paso, eliges invitar al empleado con la menor cantidad de subordinados directos (hoja) 
que aún no ha sido excluido debido a sus jefes directos. Este enfoque localmente óptimo debería conducir a una solución globalmente óptima.

    Subestructuras Óptimas: Al priorizar las hojas y evitar los jefes directos de los empleados ya invitados, estás aprovechando subestructuras óptimas
 del problema para construir una solución globalmente óptima.

    Estructura del Problema: El problema tiene una estructura jerárquica que permite aplicar un enfoque greedy eficiente, 
ya que puedes navegar de manera eficaz a través del organigrama utilizando una cola de prioridad.

Por lo tanto, la solución que has propuesto es coherente con la metodología greedy y debería ser capaz de proporcionar 
una solución óptima para el problema de determinar a quién invitar a la reunión de camaradería.
    

"""


# ALGORITMO:



    

def obtener_maximos_invitados_trabajo(organigrama_laboral):
    invitados = set()
    no_invitar= set()
    cola_heap = Heap() #Guardar tupla con formato (cantidad de Hijos,nodo,padre) -asi ordena con el numero primero-
    armado_Heap_preorder("A",None,cola_heap,organigrama_laboral)
    while not cola_heap.Esta_Vacia():
        _,nodo,jefe = cola_heap.Desencolar()
        if (nodo in invitados) or (nodo in no_invitar):
            continue
        invitados.add(nodo)
        no_invitar.add(jefe)
    
    return invitados



def armado_Heap_preorder(nodo,padre,heap,grafo):
    if nodo == None:
        return
    heap.Encolar((len(grafo.Adyacentes(nodo)),nodo,padre))
    for empleado in grafo.Adyacentes(nodo):
        armado_Heap_preorder(empleado,nodo,heap,grafo)

def armar_arbol_ejemplo1():
    """
    EJEMPLO ESTRUCTURA
                        ---------A-----
                        |     |    |  |
                      --B--  -C-   D  E
                      | | |  | |   |
                      F G H  I J  -K-
                                  |||      
                                  LMN 
    """
    organigrama = Grafo(True,["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]) #ARBOL DEBE SER DIRIGIDO EL GRAFO
    organigrama.Agregar_Arista("A","B")
    organigrama.Agregar_Arista("A","C")
    organigrama.Agregar_Arista("A","D")
    organigrama.Agregar_Arista("A","E")

    organigrama.Agregar_Arista("B","F")
    organigrama.Agregar_Arista("B","G")
    organigrama.Agregar_Arista("B","H")

    organigrama.Agregar_Arista("C","I")
    organigrama.Agregar_Arista("C","J")

    organigrama.Agregar_Arista("D","K")

    organigrama.Agregar_Arista("K","L")
    organigrama.Agregar_Arista("K","M")
    organigrama.Agregar_Arista("K","N")

    return organigrama

    


def main():
    
    organigrama_laboral = armar_arbol_ejemplo1()
    print(obtener_maximos_invitados_trabajo(organigrama_laboral)) # {'J', 'L', 'M', 'H', 'N', 'I', 'F', 'G', 'D', 'E'} parece funcionar

main()