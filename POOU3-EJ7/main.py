from menu import Menu
from manejador import Manejador as M

if __name__=='__main__':
    m=M()
    m.cargarlista()
    menu=Menu()
    menu.opciones(m)