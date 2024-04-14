from Grafo import Grafo
import queue


#ENUNCIADO *****************************************************************************************************
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

#RESOLUCIÓN  *****************************************************************************************************
"""
Identificamos que al ser un arbol jerarquico, tendremos una estructura de piramide mientras mas profundo sea el arbol. Con esta idea entendemos que es mejor arrancar agregando
las hojas del arbol antes que el nodo raiz. 
Por lo tanto, se propone el siguiente algoritmo greedy:
    1- Realizar un recorrido BFS para obtener los nodos en orden de jerarquia.
    2- Creo lista de invitados y lista de no invitar
    3- Recorrer la lista desde el final al principio de forma invertida: 
        Si el nodo no esta en lista de no invitar:
            agrego al nodo a lista de invitados
            agrego nodo padre a lista de no invitar
    4-Devuelvo lista de invitados
    
Otra forma seria realizar el recorrido bfs y no invertir la lista. Pero se considera que es mejor empezar por las hojas, ya que haciendo pruebas sobre el ejemplo 1, se obtiene una cantidad
inferior de invitados.

    EJEMPLO 1:
                            --------A------
                            |     |    |  |
                          --B--  -C-   D  E
                          | | |  | |   |
                          F G H  I J  -K-
                                      |||
                                      LMN 


    1. Realizar recorrido BFS = A B C D E F G H I J K L M N
    2. Invertir la lista = N M L K J I H G F E D C B A
    3. Agarrar el primero, revisar si es evitar: 
            N = evitar? NO ---> agrego INVITADOS = [ N ]
            evitar padre N---> K: EVITAR = [ K ]
            ....
    4. Resultado = [ N, M, L, J, I, H, G, F, D, E ]

    EJEMPLO 2:
                                    
                            ---------A-----
                            |     |    |  |
                            B    -C-   D  E
                                 | |   |
                                 F G   H
                                 |
                                 I
    1. Realizar recorrido BFS = A B C D E F G H I 
    2. Invertir la lista = I H G F E D C B A
    3. Agarrar el primero, revisar si es evitar:
            ...

    4. Resultado = [ I, H, G, E, B ]


Analisis de complejidad temporal
    - del Recorrido BFS tenemos O(N)
    - Como mejora no se invirtio la lista y se la recorrio de atras a adelante, el recorrido de la lista es O(N)
    - Estar en la lista de evitados es O(1) por usar un set.
    - Total: O(n)

Analisis de complejidad espacial
    - para el listado_bfs se utiliza O(N)
    - para los conjuntos invitados y no_invitar se utiliza O(N) entre ambos
    - Total: O(N)

"""




# ALGORITMO: *****************************************************************************************************
def obtener_maximos_invitados_trabajo_bfs(organigrama_laboral,jefe) -> set:
    listado_bfs = []
    diccionario_jefe = {}

    armado_lista_bfs(jefe,listado_bfs,organigrama_laboral,diccionario_jefe)
    
    invitados = []
    no_invitar = set()

    for i in range(len(listado_bfs) - 1, -1, -1):
        nodo = listado_bfs[i]
        padre = diccionario_jefe[nodo]
        if nodo in no_invitar:
            continue
        invitados.append(nodo)
        no_invitar.add(padre)
    return invitados
    


def armado_lista_bfs(nodo,lista,grafo,diccionario):
    #Recorre por niveles el grafo, y agrega a la lista los nodos por niveles, y guarda en el diccionario a sus padres
    if nodo == None:
        return
    cola = queue.Queue()
    cola.put(nodo)
    diccionario[nodo] = None
    while not cola.empty():
        nodo = cola.get()
        lista.append(nodo)
        for empleado in grafo.Adyacentes(nodo):
            diccionario[empleado] = nodo
            cola.put(empleado)
    

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

def armar_arbol_ejemplo2():
    """
    EJEMPLO ESTRUCTURA
                            ---------A-----
                            |     |    |  |
                            B    -C-   D  E
                                 | |   |
                                 F G   H
                                 |
                                 I
                                 
    """
    organigrama = Grafo(True,["A","B","C","D","E","F","G","H","I"]) #ARBOL DEBE SER DIRIGIDO EL GRAFO
    organigrama.Agregar_Arista("A","B")
    organigrama.Agregar_Arista("A","C")
    organigrama.Agregar_Arista("A","D")
    organigrama.Agregar_Arista("A","E")

    organigrama.Agregar_Arista("C","F")
    organigrama.Agregar_Arista("C","G")

    organigrama.Agregar_Arista("D","H")

    organigrama.Agregar_Arista("F","I")

    return organigrama

    
def main():
    
    ceo = "A"

    organigrama_laboral_1 = armar_arbol_ejemplo1()
    print(obtener_maximos_invitados_trabajo_bfs(organigrama_laboral_1, ceo)) # {'J', 'L', 'M', 'H', 'N', 'I', 'F', 'G', 'D', 'E'} parece funcionar

    organigrama_laboral_2 = armar_arbol_ejemplo2()
    print(obtener_maximos_invitados_trabajo_bfs(organigrama_laboral_2, ceo)) # {'B','I','G','H','E'} parece funcionar


main()