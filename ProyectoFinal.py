import csv

def read_csv():
    with open('./Movies.csv',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        
        return tuple(tuple(i) for i in reader)

if __name__=='__main__':
    a=2
    