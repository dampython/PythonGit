class Mascota:#clase padre
    
    def comer(self):
        print('la mascota come')
    
    def dormir(self):
        print('la mascota duerme')

class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota,Felino):#Clase hija
    pass

tutuca = Gato()
tutuca.comer()
tutuca.dormir()
tutuca.cazar()
