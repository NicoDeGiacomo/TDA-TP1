class Heap:
    def __init__(self):
        """
        Inicia el Heap, es Heap de Minimos(con func. de comparacion, proximamente)       """
        # if funcion_comparacion == None:
        #     raise ValueError("No se entregó una funcion de comparacion")
        self.arreglo = []
        self.cantidad = 0
  
    def __str__(self): 
        return str(self.arreglo)
    
    def __len__(self): 
        return self.cantidad
    
    def Esta_Vacia(self):
        """
        Devuelve si el Heap esta vacio o No
        """
        return self.cantidad == 0

    def VerMin(self):
        """
        Nos permite ver el Minimo elemento del Heap
        """
        if self.Esta_Vacia():
            raise ValueError("El Heap está Vacio.")
        return self.arreglo[0]

    def Encolar(self,dato):
        """
        Encola en el Heap el elemento, y se hace upheap si es necesario.
        """
        self.arreglo.append(dato)
        upheap(self.arreglo,self.cantidad)
        self.cantidad+=1
    
    def Desencolar(self):
        """
        Nos permite sacar el minimo elemento del Heap y tenerlo
        """
        if self.Esta_Vacia():
            raise ValueError("El Heap está Vacio.")
        self.cantidad-=1
        self.arreglo[0],self.arreglo[self.cantidad] = self.arreglo[self.cantidad],self.arreglo[0]
        dato_a_devolver = self.arreglo.pop()
        downheap(self.arreglo,0,self.cantidad)
        return dato_a_devolver

def upheap(arreglo,indice):
    if indice == 0:
        return
    padre = (indice -1) // 2
    if arreglo[indice] < arreglo[padre]:
        arreglo[indice],arreglo[padre] = arreglo[padre],arreglo[indice]
        upheap(arreglo,padre)

def downheap(arreglo,indice,cantidad):
    if indice > len(arreglo) // 2:
        return

    izq = indice * 2 + 1
    der = indice * 2 + 2
    if izq >= cantidad and der >= cantidad: # ambos fuera de indice
        return
    maximo = 0
    if der >= cantidad: # solo Izquierdo
        if arreglo[izq] < arreglo[indice]:
            maximo = izq
        else:
            maximo = indice
    else:
        maximo = maximo_3_indices(arreglo,indice,izq,der)

    if maximo != indice:
        arreglo[indice],arreglo[maximo] = arreglo[maximo],arreglo[indice]
        downheap(arreglo,maximo,cantidad)

def maximo_3_indices(arreglo,indice,izq,der):
    valor_p = arreglo[indice]
    valor_i = arreglo[izq]
    valor_d = arreglo[der]

    if valor_p <= valor_i and valor_p <= valor_d:
        return indice
    else:
        if valor_i <= valor_d:
            return izq
        return der

# def main():
#     # h = Heap()
#     # h.Encolar("E")
#     # h.Encolar("B")
#     # h.Encolar("A")
#     # h.Encolar("C")
#     # h.Encolar("D")
#     # h.Encolar("F")

#     # print(h)
#     # print(h.Desencolar())
#     # print(h.Desencolar())
#     # print(h.Desencolar())
#     # print(h.Desencolar())
#     # print(h.Desencolar())
#     # print(h.Desencolar())

#     # h1 = Heap()
#     # h1.Encolar(5)
#     # h1.Encolar(2)
#     # h1.Encolar(3)
#     # h1.Encolar(1)
#     # h1.Encolar(0)
#     # h1.Encolar(4)

#     # print(h1)
#     # print(h1.Desencolar())
#     # print(h1.Desencolar())
#     # print(h1.Desencolar())
#     # print(h1.Desencolar())
#     # print(h1.Desencolar())
#     # print(h1.Desencolar())

#     heap = Heap()
#     heap.Encolar((0,"A"))
#     heap.Encolar((5,"F"))
#     heap.Encolar((1,"B"))
#     heap.Encolar((4,"E"))
#     heap.Encolar((3,"D"))
#     heap.Encolar((2,"C"))
#     print(heap)

#     print(heap.Desencolar())
#     print(heap.Desencolar())
#     print(heap.Desencolar())
#     print(heap.Desencolar())
#     print(heap.Desencolar())
#     print(heap.Desencolar())

# main()