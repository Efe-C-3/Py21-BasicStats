import pandas as pd
import math
from collections import Counter

db_zero = pd.read_csv('dataZero.csv')
# print(db_zero)

db_zero_columns = db_zero.columns
# print(db_zero_columns)

column_x = db_zero['x']
column_y = db_zero['y']


def zcount(list):
    counted = 0
    for element in list:
        counted += 1
    return counted


def zmean(list):
    mean = float(round((sum(list) / zcount(list)), 2))
    return mean


def zmode(list):
    mode = max(set(list), key=list.count)
    return mode


def zmedian(list):
    n = int(zcount(list))
    index = n // 2
    if n % 2:
        return sorted(list)[index]
    return sum(sorted(list)[index - 1:index + 1])


def zvariance(list):
    n = zcount(list)
    mean = zmean(list)
    for x in list:
        deviation = [(x - mean) ** 2]
    variance = round((sum(deviation) / n), 2)
    return variance

def zstddev(list):
    var = zvariance(list)
    standard_dev = round(math.sqrt(var), 2)
    return standard_dev

def zstderr(list):
    standard_dev = zstddev(list)
    n = zcount(list)
    standard_err = round(standard_dev / math.sqrt(n), 2)
    return standard_err

def zcorr(listx, listy):
    # assuming len(listx) = len(listy)
    n = len(listx)
    sum_x = float(sum(listx))
    sum_y = float(sum(listy))
    sum_x_sq = sum(xi * xi for xi in listx)
    sum_y_sq = sum(yi * yi for yi in listy)
    psum = sum(xi * yi for xi, yi, in zip(listx, listy))
    num = psum - ((sum_x * sum_y) / n)
    den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y,2) / n), 0.5)
    if den == 0:
        return 0
    else:
        return round((num / den), 3)

#print(zcorr(column_x, column_y))

#print(zstderr(column_x))
#print(zstderr(column_y))

#print(zstddev(column_x))
#print(zstddev(column_y))

print(zvariance(column_x))
print(zvariance(column_y))

#print(zmedian(column_x))
#print(zmedian(column_y))

#print(zmode(column_x))
#print(zmode(column_y))

#print(zmean(column_x))
#print(zmean(column_y))

#print(zcount(column_x))
#print(zcount(column_y))
