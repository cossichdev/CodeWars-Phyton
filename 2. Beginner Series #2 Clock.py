# Este ejercicio nos da un reloj el cual nos da el tiempo en formato hora, minuto y segundo (h,m,s), tenemos que crear una FUNCION que nos devuelva el tiempo en milisegundos.

# Ejemplo: 
# h=0
# m=1
# s=1
#  resultado en milisegundos= 61000

def past(h, m, s):  # creamos una funcion "past" y le damos los parametros de hora, minuto y segundo (h,m,s).
    return h*3600000 + m*60000 + s*1000 #retornamos un parametro el cual se basa en los respectivos parametros de la funcion "past" con la salvedad de haber agregado matematicamente las operaciones de sumatoria entre parametros con su respectiva conversion a milisegundos cada unp 

past(0,1,1) #invocacion por medio de la funcion, puede ser tambien por medio de un PRINT statment.