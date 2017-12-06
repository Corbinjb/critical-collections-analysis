import csv
import numpy as np
import pandas
import matplotlib.pyplot as plt

my_file = 'genre.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data

def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)

def get_basic_statistics(data):
    gc = []
    for genre in data:
        gc.append(float(genre[1]))
    return gc

def calculate_min_and_max(genre):
    return np.min(genre), np.max(genre)

def get_genre(count, min_max, data):
    genre=[]
    min_index = count.index(min_max[0])
    max_index = count.index(min_max[1])
    for count in data:
        genre.append(count[0])
    return genre[min_index], genre[max_index]


data = import_data(my_file)
seperate_headings_from_data(data)
gc = get_basic_statistics(data)
min_max = calculate_min_and_max(gc)
genre = get_genre(gc,min_max,data)
print "Genre with the greatest volume in the Claremont Colleges Library: {} at {}".format(
    (genre)[0], (min_max)[1])
print "Genre with the smallest volume in the Claremont Colleges Library: {} at {}".format(
    (genre)[1], (min_max)[0])
gen = []
tot = []
a=0
width = 0.2
for col in data:
    gen.append(col[0])
    tot.append(col[1])
    a+=1

ind = np.arange(a)

p1 = plt.bar(ind,tot,width,color='r')
p2 = plt.xticks(ind+width,gen,rotation=90)
plt.ylabel('Count')
plt.title('Count of the entries by Genre')

plt.show()