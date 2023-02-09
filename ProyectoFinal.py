import csv
from statistics import mean
import matplotlib.pyplot as plot
from functools import partial
import matplotlib.pyplot as plt
from operator import itemgetter

def read_csv():
    with open('./Movies.csv',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        
        return tuple(tuple(i) for i in reader)
'''
1. Funcion que recibe y retorna una tupla de tuplas de las peliculas donde 'vote_average'
sea mayor o igual al promedio de todas las peliculas, el formato de la nueva tupla es: ('title','vote_average')
'''
def movies1(tupla:tuple)->tuple:
    promedio = mean([float(i[9]) for i in tupla])
    my_list = [(i[0],float(i[9])) for i in list(filter(lambda x:float(x[9])>=promedio, tupla))]
    #print(my_list)
    return tuple(my_list)

'''
2. Del resultado anterior, agrupar 'title' y 'vote_average' en listas por separado.
Ademas, realizar el histograma con las frecuencias de 'vote_average' agrupando en 4 clases.
'''
def movies2(tupla:tuple)->list:
    my_title, my_vote = list(zip(*tupla))    
    my_vote = list(my_vote)
    my_title = list(my_title)
    def graficar():
        intervalos = range(int(min(my_vote)), int(max(my_vote)) +1) #calculamos los extremos de los intervalos

        plot.hist(x=my_vote, bins=intervalos, color='lightgreen', rwidth=0.85)
        plot.title('Histograma de VOTE_AVERAGE')
        plot.xlabel('CALIFICACION')
        plot.ylabel('Frecuencia/Cantidad de Peliculas')
        plot.xticks(intervalos)
        plot.show() #dibujamos el histograma
 
    return graficar

'''
3. Funcion que recibe una tupla de tuplas donde filtre las peliculas de un genero en especifico,
porteriormente recira una cantidad de votos y retornara el porcentaje de las peliculas donde su campo 'vote_count' sea por lo menos esa cantidad.
Finalmente, mostrar una grafica de barras con los porcentajes y total del conteo de votos.
'''
def movies3(tupla:tuple, genero:str):
    my_list = list(filter(lambda x:x[1]==genero, tupla))
    #print(my_list)
    def movies33(voto:int):
        my_new_list = list(int(i[10]) for i in my_list)
        #print(my_new_list)
        m = list(map(partial(max, voto), my_new_list))
        #print(m)
        conteo = m.count(voto)
        #print(conteo)
        show_pastel(m,conteo)
        return str(int((m.count(100)/len(my_new_list))*100))+'%'
    return movies33 

def show_pastel(lista: list,conteo):
    my_conteo = [conteo, len(lista) - conteo]
    names = ["MenorVote","MayorVote"]
    colores = ["#EE6055","#60D394"]
    desfase = (0.1, 0)
    plt.pie(my_conteo, labels=names, autopct="%0.1f %%", colors=colores, explode=desfase)
    plt.axis("equal")
    plt.show()

'''
4. Funcion que recibe una tupla de tuplas y muestra los nombres y fecha de realizacion de cada una con el siguiente formato:
Nombre: {} - Dia:{} - Mes:{} - Anio:{}"
'''
def movies4(tupla:tuple):
    my_list = list((i[0],i[5]) for i in tupla)
    #print(my_tuple)
    m = list(map(format_movies, *zip(*my_list)))
    #print(m)
    return list(my_list)

def format_movies(name, date):
    return "Nombre: {} - Dia:{} - Mes:{} - Anio:{}".format(name, date[0:2],date[3:5],date[6:10])

'''
5. Funcion que recibe la lista anterior y un año determinado para posteriormente mostrar
una grafica de barras con los porcentajes de peliculas realizados por cada mes en el año indicado.
'''
def movies5(lista:list):
    def quartil(anio:str):
        my_count = list(int(i[1][3:5]) for i in lista if i[1][6:10]==anio)
        meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep" , "Oct", "Nov", "Dec"]
        my_lista = list(my_count.count(i) for i in range(1,13))      
        plt.pie(my_lista, labels=meses, autopct="%0.1f %%")
        plt.show()
    return quartil

if __name__=='__main__':
    my_movies = read_csv()
    #print(my_movies)
    
    #my_movies2 = movies1(my_movies)

    #my_fun = movies2(my_movies2)
    #my_fun()

    #my_fun = movies3(my_movies, 'Thriller')
    #print(my_fun(100))

    #my_list = movies4(my_movies)

    #my_fun = movies5(my_list)
    #my_fun('2022')

