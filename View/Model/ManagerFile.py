from io import open

from Model.Arist import Arist
from Model.Vertexx import Vertexx


class ManagerFile(object):

    __instance = None

    def new(cls, *args, **kwargs):
        if ManagerFile.__instance is None:
            ManagerFile.instance = object.new(cls)
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
        # Avenidas plazas y zonas importantes
        g.addVertex(Vertexx('AV.ada,Av.America', (205, 72)))
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
        g.addVertex(Vertexx('Av.Libertador, Av.Humbold', (561, 437)))
        g.addVertex(Vertexx('Av.America, Av.Libertador', (1106, 478)))

        ##calles superior izquierda Aylin
        g.addVertex(Vertexx('C.cap,C.fashion', (52, 310)))
        g.addVertex(Vertexx('C.leather,C.fashion', (50, 285)))
        g.addVertex(Vertexx('Av.hopper ,C.fashion', (55, 330)))
        g.addVertex(Vertexx('Av.hopper ,C.hoodie', (144, 327)))
        g.addVertex(Vertexx('Av.hopper ,C.hoodie', (144, 327)))
        g.addVertex(Vertexx('Av.sergeybrin,C.hoodie', (144, 327)))
        g.addVertex(Vertexx('C.silk,C.hoodie', (148, 306)))
        g.addVertex(Vertexx('C.silk,C.leather', (151, 285)))
        g.addVertex(Vertexx('C.jacket,C.jeans', (97, 207)))
        g.addVertex(Vertexx('C.jeans,C.joggers', (151, 205)))
        g.addVertex(Vertexx('C.sugla,C.joggers', (152, 185)))
        g.addVertex(Vertexx('C.sugla,C.jacket', (86, 188)))
        g.addVertex(Vertexx('C.mul,C.rive', (48, 25)))
        g.addVertex(Vertexx('AV.ada,C.lexin', (100, 73)))
        g.addVertex(Vertexx('AV.ada,C.downing', (158, 70)))
        g.addVertex(Vertexx('C.Delacey,C.cand', (272, 49)))
        g.addVertex(Vertexx('C.ancacey,C.riving', (307, 20)))
        g.addVertex(Vertexx('C.Delacey,C.cend', (356, 57)))
        g.addVertex(Vertexx('C.ancacey,AV.ada', (370, 67)))
        g.addVertex(Vertexx('C.ancacey,C.cend', (351, 45)))
        g.addVertex(Vertexx('AV.allen,C.cend', (414, 20)))
        g.addVertex(Vertexx('AV.allen,C.gyuntaro', (514, 76)))
        g.addVertex(Vertexx('AV.allen,C.rengoku', (539, 91)))
        g.addVertex(Vertexx('AV.libertador,C.uzui', (550, 134)))
        g.addVertex(Vertexx('AV.libertador,C.deyers', (528, 151)))
        g.addVertex(Vertexx('AV.libertador,C.program', (495, 156)))
        g.addVertex(Vertexx('C.microsoft,C.tomioka', (435, 150)))
        g.addVertex(Vertexx('C.poncho,C.toga', (620, 174)))
        g.addVertex(Vertexx('C.scarf,C.toga', (678, 204)))
        g.addVertex(Vertexx('C.pino,C.toga', (595, 155)))
        g.addVertex(Vertexx('C.scraf,C.peac', (673, 215)))
        g.addVertex(Vertexx('C.romper,C.peac', (679, 251)))
        g.addVertex(Vertexx('C.me,AV.allen Newell', (685, 163)))

        ##Cuandrante Derecho superior central Aylin
        g.addVertex(Vertexx('AV.Hopper,C.grapes', (337, 331)))
        g.addVertex(Vertexx('AV.Hopper,C.lemon', (254, 334)))
        g.addVertex(Vertexx('C.doraemon,C.lemon', (250, 304)))
        g.addVertex(Vertexx('C.locust,C.grapes', (339, 237)))
        g.addVertex(Vertexx('C.lime,C.lemon', (251, 270)))
        g.addVertex(Vertexx('C.lime,C.orange', (295, 264)))
        g.addVertex(Vertexx('C.lime,C.plum', (292, 253)))
        g.addVertex(Vertexx('C.plum,C.grapes', (341, 254)))
        g.addVertex(Vertexx('AV.libertador,C.locust', (429, 234)))
        g.addVertex(Vertexx('C.doraemon,C.grapes', (340, 303)))
        g.addVertex(Vertexx('C.rive,C.Delacey', (55, 51)))
        g.addVertex(Vertexx('C.lexin,C.bleeker', (103, 22)))
        g.addVertex(Vertexx('C.bleeker,C.downing', (157, 25)))
        g.addVertex(Vertexx('C.rive,C.Delacey', (55, 51)))
        g.addVertex(Vertexx('Av.america,C.flannel', (205, 111)))
        g.addVertex(Vertexx('Av.america,C.microsoft', (203, 219)))
        g.addVertex(Vertexx('C.christo,C.delancey', (212, 44)))
        g.addVertex(Vertexx('C.flannel,C.olive', (271, 115)))
        g.addVertex(Vertexx('C.olive,C.Zenitsu', (283, 167)))
        g.addVertex(Vertexx('C.Zenitsu,C.nezuko', (329, 139)))
        g.addVertex(Vertexx('C.tokito,C.nezuko', (307, 117)))
        g.addVertex(Vertexx('C.tokito,C.inoske', (333, 109)))
        g.addVertex(Vertexx('C.Zenitsu,C.inoske', (357, 121)))
        g.addVertex(Vertexx('C.Zenitsu,C.tanjiro', (395, 99)))
        g.addVertex(Vertexx('C.tokito,C.akaza', (385, 77)))
        g.addVertex(Vertexx('C.Zenitsu,C.inoske', (399, 137)))
        g.addVertex(Vertexx('C.gyuntaro,C.akaza', (461, 107)))
        g.addVertex(Vertexx(' C.rengoku , C.uzui', (515, 109)))
        g.addVertex(Vertexx(' C.gyuntaro , C.uzui', (481, 89)))
        g.addVertex(Vertexx('C.pin,C.paz', (163, 363)))
        g.addVertex(Vertexx('C.paz,C.cran', (161, 391)))
        g.addVertex(Vertexx('C.melon,C.cran', (114, 392)))
        g.addVertex(Vertexx('C.straw,C.melon', (94, 391)))
        g.addVertex(Vertexx('C.blue,C.goose', (81, 428)))
        g.addVertex(Vertexx('C.blue,C.mango', (42, 453)))
        g.addVertex(Vertexx('C.berry,C.mango', (59, 466)))
        g.addVertex(Vertexx('C.berry,C.love', (16, 488)))
        g.addVertex(Vertexx('C.black,C.den', (75, 482)))
        g.addVertex(Vertexx('C.black,C.goose', (128, 451)))
        g.addVertex(Vertexx('C.jersey,C.fashion', (55, 379)))
        g.addVertex(Vertexx('Av.sergey brin,C.madison', (475, 296)))

        ## zona superior central plaza luna Aylin
        g.addVertex(Vertexx('C.madison, C.roadway', (479, 263)))
        g.addVertex(Vertexx('C.madison, C.buu', (477, 237)))
        g.addVertex(Vertexx('C.madison, C.fifth', (477, 211)))
        g.addVertex(Vertexx(' C.roadway ,C.lexington', (547, 259)))
        g.addVertex(Vertexx(' C.wery ,C.lexington', (543, 225)))

        # Cuadrante izquierdo inferior Adrian
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
        g.addVertex(Vertexx('C.Lenny, C.Bouvier', (99, 583)))
        g.addVertex(Vertexx('C.Leonard, C.Lovejoy', (189, 573)))
        g.addVertex(Vertexx('Av.America, C.Lovejoy', (317, 497)))
        g.addVertex(Vertexx('C.Quimby, C.Spruce', (335, 548)))
        g.addVertex(Vertexx('C.Mayor, C.Spruce', (289, 573)))
        g.addVertex(Vertexx('C.Edna, C.Spruce', (237, 604)))
        g.addVertex(Vertexx('Av.Humbold, C.Selma', (338, 611)))
        g.addVertex(Vertexx('Av.Humbold, C.Muntz', (376, 578)))
        g.addVertex(Vertexx('C.Muntz, C.Cielo', (439, 604)))
        g.addVertex(Vertexx('C.12, C.Naruto', (396, 507)))
        g.addVertex(Vertexx('C.12, Haruno', (421, 491)))
        g.addVertex(Vertexx('C.12, C.Uzumaki', (470, 449)))
        g.addVertex(Vertexx('Av.America, C.12', (369, 529)))
        g.addVertex(Vertexx('Av.Humbold, Haruno', (463, 511)))
        g.addVertex(Vertexx('Av.Humbold, C.10', (591, 413)))
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
        g.addVertex(Vertexx('Av.Libertador, C.Cielo', (625, 459)))
        g.addVertex(Vertexx('C.Bosque, C.Camino', (537, 605)))
        g.addVertex(Vertexx('Av.America, C.Cielo', (513, 550)))
        g.addVertex(Vertexx('Pza.Milagros', (565, 580)))
        g.addVertex(Vertexx('C.Estrella,C.Mar', (630, 581)))
        g.addVertex(Vertexx('C.Mar, C.Montaña', (630, 623)))
        g.addVertex(Vertexx('C.Estrella, C.Nube', (722, 583)))
        g.addVertex(Vertexx('Av.Humbold, C.Bulevar', (508, 481)))
        g.addVertex(Vertexx('Pla.Sol', (608, 511)))
        g.addVertex(Vertexx('C.Pueblo, C.Nube', (722, 518)))
        g.addVertex(Vertexx('Av.Carrillo,C.Pueblo', (767, 508)))
        g.addVertex(Vertexx('Av.America, C.Bosque', (595, 557)))
        g.addVertex(Vertexx('Av.Libertador, C.Wal', (679, 474)))

        # cuadrante inferior derecho Adrian
        g.addVertex(Vertexx('C.Nube, C.Flor', (722, 610)))
        g.addVertex(Vertexx('Av.Carrillo, C.Na', (768, 619)))
        g.addVertex(Vertexx('Av.America, C.Sol', (854, 556)))
        g.addVertex(Vertexx('Cruce Av.America', (928, 549)))
        g.addVertex(Vertexx('Av.America, C.Park', (1018, 516)))
        g.addVertex(Vertexx('Av.America, C.Encanto', (1008, 580)))
        g.addVertex(Vertexx('Av.America, C.Bolivia', (1073, 611)))
        g.addVertex(Vertexx('C.Azul, C.Japon', (851, 611)))
        g.addVertex(Vertexx('C.Encanto, C.Japon', (847, 578)))
        g.addVertex(Vertexx('C.Valley, C.Azul', (936, 605)))
        g.addVertex(Vertexx('Hospital CBBA', (858, 511)))
        g.addVertex(Vertexx('Pza.Estudiante', (1080, 640)))
        g.addVertex(Vertexx('C.Mexico, C.Chile', (1123, 508)))
        g.addVertex(Vertexx('Av.Libertador, C.Valley', (935, 473)))

        #Cuadrante Superior central Bianca
        g.addVertex(Vertexx('C.Microsoft,C.Ellie Way', (967, 23)))
        g.addVertex(Vertexx('C.Microsoft,C.Shira', (895, 50)))
        g.addVertex(Vertexx('C.Microsoft,C.DiegoL', (869, 65)))
        g.addVertex(Vertexx('C.Manny,C.Shira', (864, 31)))
        g.addVertex(Vertexx('C.Manny,C.DiegoL', (837, 47)))
        g.addVertex(Vertexx('C.Soto,C.DiegoL', (793, 20)))
        g.addVertex(Vertexx('C.Buck,C.DiegoL', (762, 7)))
        g.addVertex(Vertexx('Av.Harrys,C.Chambray', (690, 58)))
        g.addVertex(Vertexx('Av.Harrys,C.Fedora', (649, 82)))
        g.addVertex(Vertexx('C.Pinstri,C.Chambray', (733, 82)))
        g.addVertex(Vertexx('C.Pinstri,C.Fedora', (682, 108)))
        g.addVertex(Vertexx('C.Pinstri,C.Tunic', (701, 99)))
        g.addVertex(Vertexx('C.Poncho,C.Carg', (713, 120)))
        g.addVertex(Vertexx('C.Carg,C.Espadri', (737, 140)))
        g.addVertex(Vertexx('C.Poncho,C.Chambray', (757, 97)))
        g.addVertex(Vertexx('C.Microsoft,C.Mules', (791, 175)))
        g.addVertex(Vertexx('C.Microsoft,C.Scarf', (806, 193)))
        g.addVertex(Vertexx('C.Microsoft,C.Bikini', (839, 212)))
        g.addVertex(Vertexx('C.Microsoft,C.Bodys', (882, 233)))
        g.addVertex(Vertexx('C.Scarf,C.Jumps', (770, 194)))
        g.addVertex(Vertexx('C.Jumps,C.Anorak', (784, 209)))
        g.addVertex(Vertexx('C.Jumps,C.Bikini', (816, 229)))
        g.addVertex(Vertexx('C.Jumps,C.Bodys', (845, 251)))
        g.addVertex(Vertexx('C.Toshiba,C.Circle', (855, 294)))
        g.addVertex(Vertexx('C.Sony,C.Circle', (881, 304)))
        g.addVertex(Vertexx('C.Microsoft,C.Circle', (910, 312)))
        g.addVertex(Vertexx('C.Nokia,C.Microsoft', (851, 343)))
        g.addVertex(Vertexx('C.Nokia,C.Sony', (840, 327)))
        g.addVertex(Vertexx('C.Nokia,C.Toshiba', (825, 309)))

        # Cuadrante Derecho superior Bianca
        #g.addVertex(Vertexx('Av.Elon,C.Iron', (1159, 48)))
        #g.addVertex(Vertexx('Av.Elon,C.Witch', (1124, 66)))
        g.addVertex(Vertexx('Av.Elon,C.Scarlet', (1083, 84)))
        g.addVertex(Vertexx('Av.Elon,C.Parkway', (1043, 106)))
        # g.addVertex(Vertexx('Av.Elon,C.Spider', (999, 127)))
        # g.addVertex(Vertexx('C.Scarlet,C.Falcon', (1057, 67)))
        g.addVertex(Vertexx('C.Witch,C.Falcon', (1089, 50)))
        g.addVertex(Vertexx('C.Marvel,C.Falcon', (1032, 82)))
        # g.addVertex(Vertexx('C.Witch,C.Falcon', (1089, 50)))
        # g.addVertex(Vertexx('C.Parkway,C.Span', (1005, 91)))
        g.addVertex(Vertexx('C.Parkway,C.Main', (974, 72)))
        g.addVertex(Vertexx('C.Spider,C.Span', (973, 107)))
        # g.addVertex(Vertexx('C.Span,C.Split', (951, 118)))
        g.addVertex(Vertexx('C.Split,C.Main', (925, 98)))
        # g.addVertex(Vertexx('C.Marvel,C.Main', (1000, 58)))
        g.addVertex(Vertexx('C.Scarlet,C.Main', (1021, 47)))
        g.addVertex(Vertexx('C.Witch,C.Main', (1063, 37)))
        # g.addVertex(Vertexx('C.Iron,C.Main', (1116, 29)))
        g.addVertex(Vertexx('C.Parkway,C.Capitan', (1112, 150)))
        # g.addVertex(Vertexx('C.Hulk,C.Capitan', (1138, 137)))
        # g.addVertex(Vertexx('C.Scarlet,C.Capitan', (1159, 124)))
        g.addVertex(Vertexx('C.Witch,C.Capitan', (1186, 107)))
        g.addVertex(Vertexx('C.Stark,C.Hulk', (1100, 115)))
        # g.addVertex(Vertexx('C.Stark,C.Scarlet', (1119, 102)))
        # g.addVertex(Vertexx('C.Stark,C.Iron', (1184, 68)))
        g.addVertex(Vertexx('C.Stark,C.Witch', (1154, 86)))
        g.addVertex(Vertexx('C.Parkway,C.Stark', (1075, 130)))
        # g.addVertex(Vertexx('C.Parkway,C.Alley', (1144, 170)))
        g.addVertex(Vertexx('C.Boule,C.Alley', (1123, 183)))
        g.addVertex(Vertexx('C.Capitan,C.America', (1068, 179)))
        g.addVertex(Vertexx('C.America,C.Hawkeye', (1115, 225)))
        g.addVertex(Vertexx('C.Panther,C.Vision', (1123, 248)))
        g.addVertex(Vertexx('C.Vision,C.Alan T', (1121, 274)))
        g.addVertex(Vertexx('C.Vision,C.Marge', (1121, 318)))
        g.addVertex(Vertexx('C.Vision,C.Homer', (1121, 350)))
        # g.addVertex(Vertexx('C.Vision,C.Road', (1121, 373)))
        g.addVertex(Vertexx('C.Elmwood,C.Lane', (1124, 400)))
        g.addVertex(Vertexx('C.Cedar,C.Lane', (1124, 445)))
        g.addVertex(Vertexx('C.Elmwood,C.Grove', (1065, 401)))
        # g.addVertex(Vertexx('C.Cedar,C.Grove', (1067, 446)))
        g.addVertex(Vertexx('C.Cedar,C.Park', (1022, 446)))
        g.addVertex(Vertexx('C.Homer,C.Ralph', (1022, 351)))
        g.addVertex(Vertexx('C.Apu,C.Homer', (985, 352)))
        g.addVertex(Vertexx('C.Apu,C.Bart', (969, 378)))
        g.addVertex(Vertexx('C.Apu,C.Lisa', (942, 394)))
        g.addVertex(Vertexx('C.Apu,C.Maggie', (902, 410)))
        g.addVertex(Vertexx('C.Apu,C.Ned', (843, 419)))
        # g.addVertex(Vertexx('C.Ned,C.Moe', (844, 400)))
        g.addVertex(Vertexx('C.Ned,C.Waylon', (844, 379)))
        g.addVertex(Vertexx('C.Homer,C.Waylon', (924, 350)))
        g.addVertex(Vertexx('C.Marge,C.Waylon', (967, 317)))
        g.addVertex(Vertexx('C.Elm,C.Oak', (928, 173)))
        g.addVertex(Vertexx('C.Oak,C.Thanos', (889, 154)))
        g.addVertex(Vertexx('C.Oak,C.Main', (861, 134)))
        g.addVertex(Vertexx('C.Oak,C.Hawkeye', (997, 225)))
        g.addVertex(Vertexx('C.Oak,C.Hawkeye', (997, 225)))

#------------------------------------------------------------
        # Creacion de aristas inferior izquierda
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Carison'), g.getVertex('Av.Sengey, C.Papaya')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Carison'), g.getVertex('Av.Sengey, C.Tony')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Tony'), g.getVertex('Av.Sengey, C.Fat')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Fat'), g.getVertex('Av.Sengey, C.Goose')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Goose'), g.getVertex('Pza. La Paz')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Uzuamki'), g.getVertex('Pza. La Paz')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Uzuamki'), g.getVertex('Pza. Avaroa')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Uzuamki'), g.getVertex('C.Lenny, C.Uzumaki')))
        g.addArist(Arist(g.getVertex('C.Lenny, C.Naruto'), g.getVertex('C.Lenny, C.Uzumaki')))
        g.addArist(Arist(g.getVertex('C.Uchiha, C.Naruto'), g.getVertex('C.Lenny, C.Naruto')))
        g.addArist(Arist(g.getVertex('C.Uchiha, C.Naruto'), g.getVertex('Av.America, C.Lovejoy')))
        g.addArist(Arist(g.getVertex('C.Lenny, C.Uzumaki'), g.getVertex('C.12, C.Uzumaki')))
        g.addArist(Arist(g.getVertex('C.12, Haruno'), g.getVertex('C.12, C.Uzumaki')))
        g.addArist(Arist(g.getVertex('C.12, Haruno'), g.getVertex('C.12, C.Naruto')))
        g.addArist(Arist(g.getVertex('Av.America, C.12'), g.getVertex('C.12, C.Naruto')))
        g.addArist(Arist(g.getVertex('Av.America, C.12'), g.getVertex('Av.America, Av.Humbold')))
        g.addArist(Arist(g.getVertex('Av.Humbold, Haruno'), g.getVertex('Av.America, Av.Humbold')))
        g.addArist(Arist(g.getVertex('Av.Humbold, Haruno'), g.getVertex('Av.Humbold, C.Bulevar')))
        g.addArist(Arist(g.getVertex('Av.Libertador, Av.Humbold'), g.getVertex('Av.Humbold, C.Bulevar')))
        g.addArist(Arist(g.getVertex('Av.Libertador, Av.Humbold'), g.getVertex('Pza. Avaroa')))
        g.addArist(Arist(g.getVertex('Av.America, C.Lenny'), g.getVertex('C.Lenny, C.Naruto')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Papaya'), g.getVertex('C.Papaya, C.Lenny')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Carison'), g.getVertex('C.Carison, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Papaya, C.Lenny'), g.getVertex('C.Carison, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Carison, C.Lenny'), g.getVertex('C.Fat, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Fat, C.Lenny'), g.getVertex('Av.America, C.Lenny')))
        g.addArist(Arist(g.getVertex('Av.Sengey, C.Fat'), g.getVertex('C.Fat, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Papaya, C.Lenny'), g.getVertex('C.Lenny, C.Bouvier')))
        g.addArist(Arist(g.getVertex('C.Lenny, C.Bouvier'), g.getVertex('C.Leonard, C.Bouvier')))
        g.addArist(Arist(g.getVertex('C.Leonard, C.Lovejoy'), g.getVertex('C.Leonard, C.Bouvier')))
        g.addArist(Arist(g.getVertex('C.Leonard, C.Lovejoy'), g.getVertex('C.Carison, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Leonard, C.Lovejoy'), g.getVertex('Av.America, C.Lovejoy')))
        g.addArist(Arist(g.getVertex('Av.America, C.Lenny'), g.getVertex('Av.America, C.Lovejoy')))
        g.addArist(Arist(g.getVertex('Av.America, C.12'), g.getVertex('Av.America, C.Lovejoy')))
        g.addArist(Arist(g.getVertex('C.Papaya, C.Lenny'), g.getVertex('C.Carison, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Mayor, C.Spruce'), g.getVertex('C.Fat, C.Lenny')))
        g.addArist(Arist(g.getVertex('C.Edna, C.Spruce'), g.getVertex('C.Fat, C.Lenny')))
        g.addArist(Arist(g.getVertex('Av.America, C.Lenny'), g.getVertex('C.Fat, C.Lenny')))
        g.addArist(Arist(g.getVertex('Av.America, C.Lenny'), g.getVertex('Pza. La Paz')))
        g.addArist(Arist(g.getVertex('C.Mayor, C.Spruce'), g.getVertex('C.Quimby, C.Spruce')))
        g.addArist(Arist(g.getVertex('Av.America, C.12'), g.getVertex('C.Quimby, C.Spruce')))
        g.addArist(Arist(g.getVertex('C.Mayor, C.Spruce'), g.getVertex('Av.Humbold, C.Selma')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.Muntz'), g.getVertex('C.Quimby, C.Spruce')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.Muntz'), g.getVertex('Av.Humbold, C.Selma')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.Muntz'), g.getVertex('Av.America, Av.Humbold')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.Muntz'), g.getVertex('C.Muntz, C.Cielo')))
        g.addArist(Arist(g.getVertex('Av.America, C.Cielo'), g.getVertex('C.Muntz, C.Cielo')))
        g.addArist(Arist(g.getVertex('Av.America, C.Cielo'), g.getVertex('Av.America, Av.Humbold')))
        g.addArist(Arist(g.getVertex('C.Bosque, C.Camino'), g.getVertex('Av.America, Av.Humbold')))
        g.addArist(Arist(g.getVertex('C.Bosque, C.Camino'), g.getVertex('Pza.Milagros')))
        g.addArist(Arist(g.getVertex('Av.America, C.Bosque'), g.getVertex('Pza.Milagros')))
        g.addArist(Arist(g.getVertex('Av.America, C.Bosque'), g.getVertex('Pla.Sol')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.Bulevar'), g.getVertex('Pla.Sol')))
        g.addArist(Arist(g.getVertex('Av.America, C.Cielo'), g.getVertex('Av.America, C.Bosque')))
        g.addArist(Arist(g.getVertex('Av.America, C.Bosque'), g.getVertex('Av.America, Av.Carrillo')))
        g.addArist(Arist(g.getVertex('Av.Libertador, C.Cielo'), g.getVertex('Av.Libertador, Av.Humbold')))
        g.addArist(Arist(g.getVertex('Av.Libertador, C.Cielo'), g.getVertex('Aylin')))
        g.addArist(Arist(g.getVertex('Av.Libertador, C.Cielo'), g.getVertex('Av.Libertador, C.Wal')))
        g.addArist(Arist(g.getVertex('Av.Libertador, C.Wal'), g.getVertex('Adrian')))
        g.addArist(Arist(g.getVertex('Pza. Quintanilla'), g.getVertex('Av.Libertador, C.Wal')))
        g.addArist(Arist(g.getVertex('Av.Libertador, C.Wal'), g.getVertex('Pla.Sol')))
        g.addArist(Arist(g.getVertex('C.Pueblo, C.Nube'), g.getVertex('Pla.Sol')))
        g.addArist(Arist(g.getVertex('C.Pueblo, C.Nube'), g.getVertex('C.Estrella, C.Nube')))
        g.addArist(Arist(g.getVertex('C.Pueblo, C.Nube'), g.getVertex('Av.Carrillo,C.Pueblo')))
        g.addArist(Arist(g.getVertex('Av.Carrillo,C.Pueblo'), g.getVertex('Av.America, Av.Carrillo')))
        g.addArist(Arist(g.getVertex('C.Nube, C.Flor'), g.getVertex('Av.Carrillo, C.Na')))
        g.addArist(Arist(g.getVertex('C.Estrella,C.Mar'), g.getVertex('C.Mar, C.Montaña')))
        g.addArist(Arist(g.getVertex('C.Estrella,C.Mar'), g.getVertex('Pza.Milagros')))
        g.addArist(Arist(g.getVertex('C.Estrella,C.Mar'), g.getVertex('C.Estrella, C.Nube')))
        g.addArist(Arist(g.getVertex('Av.Carrillo, C.Na'), g.getVertex('Av.America, Av.Carrillo')))

        # Aristas centro izquierdo inferior
        g.addArist(Arist(g.getVertex('C.12, C.10'), g.getVertex('C.10, Cedar')))
        g.addArist(Arist(g.getVertex('Ash, Bird'), g.getVertex('Bird, C.10')))
        g.addArist(Arist(g.getVertex('Bird, C.10'), g.getVertex('C.12, C.10')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.10'), g.getVertex('Av.Libertador, Av.Humbold')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.10'), g.getVertex('C.12, C.10')))
        g.addArist(Arist(g.getVertex('Av.Humbold, C.10'), g.getVertex('Aylin')))
        g.addArist(Arist(g.getVertex('Bianca'), g.getVertex('Aylin')))
        g.addArist(Arist(g.getVertex('Adrian'), g.getVertex('Bianca')))


        ##### creacion de aristas de la parte superior
        g.addArist(Arist(g.getVertex('AV.ada,C.lexin'), g.getVertex('AV.ada,C.downing')))
        g.addArist(Arist(g.getVertex('AV.ada,C.downing'), g.getVertex('C.ancacey,AV.ada')))
        g.addArist(Arist(g.getVertex('C.ancacey,AV.ada'), g.getVertex('AV.ada,Av.America')))

        return g



