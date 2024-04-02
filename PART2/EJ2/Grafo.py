from random import randint

class Grafo: 
    def __init__(self,es_dirigido,lista_vertices = None):
        """
        Inicia el Grafo, puede recibir una lista de vertices a Agregar
        """
        self.dic_de_dic = {}
        self.es_dirigido = es_dirigido
        if lista_vertices != None:
            for v in lista_vertices:
                self.dic_de_dic[v] = {}
  
    def __str__(self): 
        arreglo = []
        for vertice in self.dic_de_dic:
            subarreglo = []
            for adyacente in self.dic_de_dic[vertice]:
                subarreglo.append((adyacente,self.dic_de_dic[vertice][adyacente]))
            arreglo.append((vertice,subarreglo))
        return str(arreglo)
    
    def __len__(self): 
        return len(self.dic_de_dic)

    def Agregar_Vertice(self,vertice):
        """
        Agrega un Vertice si Pertenece al Grafo
        """
        self.dic_de_dic[vertice] = {}

    def Pertenece_Vertice(self,vertice):
        """
        Devuelve Si el Vertice Pertenece al Grafo
        """        
        if vertice in self.dic_de_dic:
            return True
        return False

    def Agregar_Arista(self,vertice_a, vertice_b,peso = None):
        """
        Agrega una arista entre 2 vertices(si estan ambos en el Grafo), y agrega su inverso si es No Dirigido
        Se le da peso a la arista si se recibe un peso
        """
        if peso is None:
            peso_arista = 0
        else:
            peso_arista = peso
        if not(vertice_a in self.dic_de_dic) or not(vertice_b in self.dic_de_dic):
            raise ValueError("Alguno de Los Vertices no pertenecen al Grafo")
        self.dic_de_dic[vertice_a][vertice_b] = peso_arista
        if not self.es_dirigido:
            self.dic_de_dic[vertice_b][vertice_a] = peso_arista

    def Son_Adyacentes(self,vertice_a, vertice_b):
        """
        Devuelve si los dos vertices son Adyacentes o No(si estan ambos en el Grafo)
        """
        if not(vertice_a in self.dic_de_dic) or not(vertice_b in self.dic_de_dic):
            raise ValueError("Alguno de Los Vertices no pertenecen al Grafo")
        if vertice_b in self.dic_de_dic[vertice_a]:
            return True
        return False

    def Vertices(self):
        """
        Devuelve un arreglo de todos los vertices del Grafo
        """
        arreglo = []
        for vertice in self.dic_de_dic:
            arreglo.append(vertice)
        return arreglo

    def Adyacentes(self,vertice):
        """
        Devuelve un arreglo de todos los adyacentes del vertice(si está en el Grafo)
        """
        if not(vertice in self.dic_de_dic):
            raise ValueError("El Vertice no pertenecen al Grafo")
        arreglo = []
        for adyacente in self.dic_de_dic[vertice]:
            arreglo.append((adyacente))
        return arreglo
    
    def Peso(self,vertice_a, vertice_b):
        """
        Devuelve el Peso de la arista entre A y B, si existe(en ese orden)
        Si el grafo no se le dio peso, se devolverá cero.
        """
        if not(vertice_a in self.dic_de_dic) or not(vertice_b in self.dic_de_dic):
            raise ValueError("Alguno de Los Vertices no pertenecen al Grafo")
        if vertice_b not in self.dic_de_dic[vertice_a]:
            raise ValueError("El segundo vertice no esta conectado al primer vertice")
        return self.dic_de_dic[vertice_a][vertice_b]
    
    def Vertice_Aleatorio(self):
        """
        Devuelve un Vertice al Azar del grafo.
        """
        if len(self.dic_de_dic) == 0:
            raise ValueError("El Diccionario no tiene Vertices.")
        indice = 0
        indice_azar = randint(0,len(self.dic_de_dic)-1)
        for k,_ in self.dic_de_dic.items():
            if indice == indice_azar:
                return k
            indice+=1

