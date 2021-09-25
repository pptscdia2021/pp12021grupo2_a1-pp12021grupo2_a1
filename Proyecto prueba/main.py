from producto import producto
from resta import resta
from suma import suma
from imprimir import imprimir

operaciones = {'suma' : suma, 'resta' : resta, 'producto' : producto}
valores = []

if __name__ == "__main__":
    opcion = int(input('Operacion:\n1- {0}\n2- {1}\n3- {2}\nSeleccione: '.format(*map(lambda x: x.capitalize(),list(operaciones.keys())))))
    valores.extend(map(int, list(input('Ingrese 2 valores separados por espacio: ').split())))
    imprimir(list(operaciones.keys())[opcion-1].capitalize(), operaciones[list(operaciones.keys())[opcion-1]](*valores))