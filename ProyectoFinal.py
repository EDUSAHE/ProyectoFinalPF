import functools, operator, csv, heapq

def read_csv():
    with open('./Movies.csv',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        return tuple(tuple(i) for i in reader)

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
    tupla_pelis = read_csv()

    # print(movies6(tupla_pelis))

    # fun = movies7('Universal Pictures')
    # print(fun(tupla_pelis))
    # fun = movies7('Marvel Studios')
    # print(fun(tupla_pelis))

    # fun = movies8(tupla_pelis)
    # print(fun())

    # fun = movies9(input("Ingrese el idioma: "), input("Ingrese el año: "))
    # print(fun(tupla_pelis))

    # print(list(movies10(tupla_pelis)))
