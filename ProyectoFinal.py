import functools, operator, csv
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

# funcion que recibe una tupla de tuplas de peliculas que filtre las peliculas de la compania Marvel Studios,
# las ordene por vote average y las enumere de vote average mas alto al mas bajo y al final regrese una tupla de diccionarios
# solo con Titulo, genero, fecha, duracion y clasificaion
def movies6(tupla: tuple)->tuple:
    m = map(list, sorted(filter(lambda x: x[9] > '7.5' and x[4] == 'Marvel Studios', tupla), key = lambda x: x[9], reverse=True))
    dic = [{'Titulo': i[0],
            'Genero': i[1],
            'Fecha': i[5],
            'Duracion': i[8],
            'Calificacion': i[9],
                         } for i in list(m)]
    movies = enumerate(dic, 1)
    # print(type(movies))
    return tuple(movies)

# funcion que recibe una tupla de tuplas y filtre las peliculas que son de la compania que escribamos y calcule el promedio del
# vote_average de las peliculas de esa compania
def movies7(company: str):
    def prom(tupla: tuple)->float:
        promedio = map(lambda x: x[9], filter(lambda x: x[4]==company and x[9] > '0', tupla))
        prome = list(map(float, promedio))
        m = operator.truediv(functools.reduce(operator.add, prome,0), len((prome)))
        return m
    return prom

# funcion que recibe una tupla de tuplas y filtre una lista donde runtime sea mayor a 120 y un vote avegra > 7
# tendrán  los campos titulo, budget, original_language y production_companies
# se creearán 3 listas, una para el idioma francés, otra español y una para inglés. Despues se desplegará un menú en donde
# dependiendo el idioma que se selecione mostrará una tupla de esas peliculas pero con un budget mayor a 10000000
# y las enumere

def movies8(tupla: tuple):
    pelisen = [[i[0], i[6], i[2], i[4]] for i in tupla if i[2] == 'en' and i[8] >= '120' and i[9] > '7']
    pelises = [[i[0], i[6], i[2], i[4]] for i in tupla if i[2] == 'es' and i[8] >= '120' and i[9] > '7']
    pelisfr = [[i[0], i[6], i[2], i[4]] for i in tupla if i[2] == 'fr' and i[8] >= '120' and i[9] > '7']

    def menu():
        men = """
             1. Peliculas en Inglés
             2. Peliculas en Español
             3. Peliculas en Francés
            """
        print(men)
        opt = int(input("Ingresar opcion: "))

        if opt == 1:
            m = enumerate(list(filter(lambda x: x[1] > '10000000', pelisen)),1)
            return tuple(m)

        if opt == 2:
            m = enumerate(list(filter(lambda x: x[1] > '10000000' , pelises)),1)
            return tuple(m)

        if opt == 3:
            m = enumerate(list(filter(lambda x: x[1] > '10000000' , pelisfr)),1)
            return tuple(m)
    return menu

# funcion que recibe un idioma y un año para despues con un closure reciba una tupla de tuplas
# en donde se creará un conjunto de las películas que salieron en navidad en ese año y del idioma tecleeado
# al final regresará un conjunto con las películas que salieron en halowen y navidad
def movies9(idioma: str,anio: str):
    def pelis(tupla: tuple):
        navidad = {(i[0], i[5]) for i in tupla if i[2] == idioma and i[5][0:2] == '25' and i[5][3:5]=='12' and i[5][6:10] == anio}
        halloween = {(i[0], i[5]) for i in tupla if i[2] == idioma and i[5][0:2] == '31' and i[5][3:5]=='10' and i[5][6:10] == anio}
        final = navidad.union(halloween)
        return final
    return pelis

# funcion que recibe una tupla de tuplas y con el yield va regresando las peliculas de cada mes con el vote average mayor a 8
#  del año 2022
def peli (tupla, mes):
     return list(filter(lambda x: x[5][0:2] >= '01' and x[5][0:2] <= '31' and x[5][3:5]== mes and x[5][6:10] == '2022' and x[9] > '8', tupla))

def movies10(tupla: tuple):
    l = ['00', '01','02','03','04','05','06','07','08','09','10', '11','12']
    for  i in range(13):
        yield peli(tupla, l[i])

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

    # print(movies6(my_movies))

    # fun = movies7('Universal Pictures')
    # print(fun(my_movies))
    # fun = movies7('Marvel Studios')
    # print(fun(my_movies))

    # fun = movies8(my_movies)
    # print(fun())

    # fun = movies9(input("Ingrese el idioma: "), input("Ingrese el año: "))
    # print(fun(my_movies))

    # print(list(movies10(my_movies)))


