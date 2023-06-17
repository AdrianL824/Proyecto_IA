from io import open

from Model.Arist import Arist
from Model.Vertexx import Vertexx


class ManagerFile(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if ManagerFile.__instance is None:
            ManagerFile.__instance = object.__new__(cls)
        return ManagerFile.__instance

    def obtenerGrafo(self):
        fileedge = open("aristaGra.txt","r")
        listAr = fileedge.readlines()
        fileedge.close()
        return listAr

    def obtenerNodesMana(self,graph):
        var = graph.getNodeslist()
        return var
        #print("prueba funciona la obteccion de nodos")
    def obGrafoSinText(self,graph):
        #g = GrafoNoDirigido()
        g = graph()
        #Avenidas plazas y zonas importantes
        g.addVertex(Vertexx('Av.Ada, Av.America', (205, 72)))
        g.addVertex(Vertexx('Pza. La Paz', (203, 443)))
        g.addVertex(Vertexx('Pza. Avaroa', (407, 332)))
        g.addVertex(Vertexx('Pza. Avaroa', (746, 274)))
        g.addVertex(Vertexx('Pza. Mayor', (581, 117)))
        g.addVertex(Vertexx('Pza. Encantados', (1060, 275)))
        g.addVertex(Vertexx('Pza. Quintanilla', (769, 472)))
        g.addVertex(Vertexx('Av.America, Av.Humbold', (416, 557)))
        g.addVertex(Vertexx('Av.America, Av.Grace Hopper', (208, 333)))
        g.addVertex(Vertexx('Av.Ada, Av.Allen Newell', (500, 73)))
        g.addVertex(Vertexx('Av.Linus, Av.Harrys', (727, 34)))
        g.addVertex(Vertexx('Av.Linus, Av.Elon', (957, 156)))
        g.addVertex(Vertexx('Av.America, Av.Carrillo', (769, 549)))
        g.addVertex(Vertexx('Av.Libertad, Av.Humblot', (561, 437)))

        #Cuadrante izquierdo inferios
        g.addVertex(Vertexx('Av.Sengey, C.Carison', (78, 514)))
        g.addVertex(Vertexx('Av.Sengey, C.Papaya', (51, 532)))
        g.addVertex(Vertexx('Av.Sengey, C.Tony', (108, 502)))
        g.addVertex(Vertexx('Av.Sengey, C.Fat', (146, 477)))
        g.addVertex(Vertexx('Av.Sengey, C.Goose', (170, 464)))
        g.addVertex(Vertexx('Av.Sengey, C.Naruto', (238, 425)))
        g.addVertex(Vertexx('Av.Sengey, C.Uzuamki', (329, 375)))
        g.addVertex(Vertexx('C.Papaya, C.Lenny', (119, 568)))
        g.addVertex(Vertexx('C.Carison, C.Lenny', (144, 551)))
        g.addVertex(Vertexx('C.Fat, C.Lenny', (215, 514)))
        g.addVertex(Vertexx('Av.America, C.Lenny', (276, 475)))
        g.addVertex(Vertexx('C.Lenny, C.Naruto', (309, 463)))
        g.addVertex(Vertexx('C.Lenny, C.Uzumaki', (402, 414)))
        g.addVertex(Vertexx('C.Uchiha, C.Naruto', (346, 483)))
        g.addVertex(Vertexx('C.Leonard, C.Bouvier', (185, 626)))
        g.addVertex(Vertexx('C.Lennt, C.Bouvier', (99, 583)))
        g.addVertex(Vertexx('C.Leonard, C.Lovejoy', (189, 573)))
        g.addVertex(Vertexx('Av.America, C.Lovejoy', (317, 497)))
        g.addVertex(Vertexx('C.Quimby, C.Spruce', (335, 548)))
        g.addVertex(Vertexx('C.Mayor, C.Spruce', (289, 573)))
        g.addVertex(Vertexx('C.Edna, C.Spruce', (237, 604)))
        g.addVertex(Vertexx('Av.Humbold, C.Selma', (338, 611)))
        g.addVertex(Vertexx('Av.Humbolt, C.Muntz', (376, 578)))
        g.addVertex(Vertexx('C.Muntz, C.Cielo', (439, 604)))
        g.addVertex(Vertexx('C.12, C.Naruto', (396, 507)))
        g.addVertex(Vertexx('C.12, Haruno', (421, 491)))
        g.addVertex(Vertexx('C.12, C.Uzumaki', (470, 449)))
        g.addVertex(Vertexx('Av.America, C.12', (369, 529)))
        g.addVertex(Vertexx('Av.America, Haruno', (463, 511)))
        g.addVertex(Vertexx('Av.America, C.10', (591, 413)))
        g.addVertex(Vertexx('C.12, C.10', (545, 392)))
        g.addVertex(Vertexx('Av.Alan, Ash', (498, 283)))
        g.addVertex(Vertexx('Av.Alan, Lexingtong', (541, 273)))
        g.addVertex(Vertexx('Av.Alan, Acer', (661, 274)))
        g.addVertex(Vertexx('Ash, Bird', (564, 336)))
        g.addVertex(Vertexx('Bird, C.10', (514, 366)))
        g.addVertex(Vertexx('C.10, Cedar', (604, 344)))
        g.addVertex(Vertexx('Acer, Lenovo', (700, 317)))
        g.addVertex(Vertexx('Acer, Av.Carrillo', (767, 320)))
        g.addVertex(Vertexx('Bianca', (684, 415)))
        g.addVertex(Vertexx('Aylin', (652, 438)))
        g.addVertex(Vertexx('Adrian', (738, 425)))



        return g

"""""
        g.addArist(Arist(g.getVertex('e1'), g.getVertex('n1')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('e2'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('e1'), g.getVertex('n1')))
        g.addArist(Arist(g.getVertex('e3'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('e4'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('n3'), g.getVertex('n9')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n9')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n7')))


        #g.addArist(Arist(g.getVertex('n7'), g.getVertex('e11')))
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('n4'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('e5'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n4'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n10'), g.getVertex('n14')))
        g.addArist(Arist(g.getVertex('n14'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n13')))
        g.addArist(Arist(g.getVertex('n13'), g.getVertex('n14')))
        g.addArist(Arist(g.getVertex('n12'), g.getVertex('n13')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n12')))
        g.addArist(Arist(g.getVertex('n13'), g.getVertex('n14')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n11')))
        g.addArist(Arist(g.getVertex('e10'), g.getVertex('n11')))
        g.addArist(Arist(g.getVertex('n11'), g.getVertex('n15')))
        g.addArist(Arist(g.getVertex('n12'), g.getVertex('n15')))
        g.addArist(Arist(g.getVertex('n15'), g.getVertex('n16')))
        g.addArist(Arist(g.getVertex('e9'), g.getVertex('n16')))
        g.addArist(Arist(g.getVertex('e8'), g.getVertex('n17')))
        g.addArist(Arist(g.getVertex('n16'), g.getVertex('n17')))
        g.addArist(Arist(g.getVertex('n14'), g.getVertex('n17')))
        g.addArist(Arist(g.getVertex('n14'), g.getVertex('n18')))
        g.addArist(Arist(g.getVertex('n5'), g.getVertex('n6')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n18')))
        g.addArist(Arist(g.getVertex('e7'), g.getVertex('n18')))
        g.addArist(Arist(g.getVertex('e6'), g.getVertex('n6')))
        g.addArist(Arist(g.getVertex('n3'), g.getVertex('n4')))
        return g """
"""
#Todo: este es el grafo anterior con valores incorrectos

        g.addVertex(Vertexx('e1', (10, 228)))
        g.addVertex(Vertexx('e2', (460, 10)))
        g.addVertex(Vertexx('e3', (828, 10)))
        g.addVertex(Vertexx('e4', (1100, 10)))
        g.addVertex(Vertexx('e5', (1200, 76)))
        g.addVertex(Vertexx('e6', (1200, 650)))
        g.addVertex(Vertexx('e7', (828, 650)))
        g.addVertex(Vertexx('e8', (368, 650)))
        g.addVertex(Vertexx('e9', (10, 570)))
        g.addVertex(Vertexx('n1', (184, 228)))
        g.addVertex(Vertexx('n2', (368, 228)))
        g.addVertex(Vertexx('n3', (828, 76)))
        g.addVertex(Vertexx('n4', (1100, 76)))
        g.addVertex(Vertexx('n5', (552, 226)))
        g.addVertex(Vertexx('n6', (828, 226)))
        g.addVertex(Vertexx('n7', (230, 418)))
        g.addVertex(Vertexx('n8', (506, 494)))
        g.addVertex(Vertexx('n9', (828, 494)))
        g.addVertex(Vertexx('n10', (1000, 418)))
        g.addVertex(Vertexx('n11', (1140, 226)))# Todo: numero de nodos o vertices es de 20 :(

        g.addArist(Arist(g.getVertex('e1'), g.getVertex('n1')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n7')))
        g.addArist(Arist(g.getVertex('e2'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('e9'), g.getVertex('n7')))
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('e8'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n5'), g.getVertex('n6')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('e3'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('n3'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('e4'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('n4'), g.getVertex('e5')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('n11'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n9')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('e7')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('n10'), g.getVertex('e6')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n11')))
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n2')))
        return g
"""
# Todo El grafo dirigido tiene 24 aristas
# Todo el grafo no dirigido tiene 48 aristas
# arreglar el alritmos de bidireccion de grafo en el metodo grafo no dirijido




