from Grafo import Grafo

def armado_lista(i,grafo):
    #Si i = 0-> devuelve preorder
    #Si i = 1-> devuelve postorder
    lista = []
    padre = "A"
    if i == 0:
        armado_lista_preorder(padre,None,lista,grafo)
    else:
        armado_lista_postorder(padre,None,lista,grafo)
    return lista



def armado_lista_preorder(nodo,padre,lista,grafo):
    if nodo == None:
        return
    lista.append(nodo)
    for empleado in grafo.Adyacentes(nodo):
        armado_lista_preorder(empleado,nodo,lista,grafo)


def armado_lista_postorder(nodo,padre,lista,grafo):
    if nodo == None:
        return
    
    for empleado in grafo.Adyacentes(nodo):
        armado_lista_preorder(empleado,nodo,lista,grafo)
    lista.append(nodo)

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
    print(armado_lista(0,organigrama_laboral_1))
    print(armado_lista(1,organigrama_laboral_1))
    organigrama_laboral_2 = armar_arbol_ejemplo2()
    print(armado_lista(0,organigrama_laboral_2))
    print(armado_lista(1,organigrama_laboral_2))
    


main()