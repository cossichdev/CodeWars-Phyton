#nos pasan un input en corchetes, por lo que sabemos que es una lista, y caba entrada de la lista tiene 2 variables:
#
# input =[[0, 1],[0, 1],[0, 1],[0, 1],[0, 1]]
#
# nos piden crear una funcion con dos condicionales: al menos 55 a;os (0 > 54 o 0 >= 55) y un handicap superior a 7 (1=7). De cumplirse ambas condicionales (Y) se debe asignar el nombre de "Senior" y si falla se asigna "Open", esto en un output con formato de lista: "x = []"

data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

def open_or_senior(data): # creamos una funcion "open_or_senior" y le damos el parametro de data, el cual es la lista que contiene listas.

    return ['Senior' #1) si se cumplen ambas variables de cada lista, se ingresa en la variable de senior
            if (x[0] > 54 and x[1] > 7)  #2) cada lista hay que descomponerla para evaluar sus variables por separado, por lo que debemos asignar una variable a cada pedazo de bloque de cada lista, en este caso cada lista solo trae edad y handicap por lo que enumeramos con base al espacio que ocupan, siempre empezando desde 0
            else 'Open'#3)si no se cumple la condicion, damos solo una opcion mas
            for x in data] #4) Se crean una variable cualquiera, en este caso asignamos 'X' y la linkeamos a data
    
    #El odigo se lee por bloques y sigue la siguiente enumeracion:(4,2,1,3), se lee asi:  PARA X (variable asignada para las listas) EN data, si se cumplen las siguientes condiciones ... se retorna la variable Senior, si no cumple se retorna la variable Open


print(open_or_senior(data)) #imprimimos la funcion para evaluar su veracidad

#el codigo se puede ejecutar como un arbol de condicionales o sea de forma anidada pero mientras mas compacto es mejor.