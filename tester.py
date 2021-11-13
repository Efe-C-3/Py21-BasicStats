def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance_calc = sum(deviations) / n
    return variance_calc

print(variance([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]))
print(variance([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.86]))


def zmode(list):
    y = {}
    for i in list:
        if not i in y:
            y[i] = 1
        else:
            y[i] += 1
    return [g for g, l in y.items() if l == max(y.values())]
