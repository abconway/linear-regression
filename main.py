import csv

import numpy as np
import matplotlib.pyplot as plt


DATA_FILENAME = 'data.csv'


def load_data():
    x = []
    y = []

    with open(DATA_FILENAME) as fp:
        reader = csv.reader(fp)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    return (x, y)


def plot_data(x, y, y2):
    plt.scatter(x, y)
    plt.plot(x, y2)
    plt.show()


def main():
    data = load_data()

    x = np.array(data[0])
    y = np.array(data[1])

    x2 = x**2
    yx = x * y
    
    denominator = x2.mean() - x.mean()**2
    a = (yx.mean() - y.mean() * x.mean()) / denominator
    b = (y.mean() * x2.mean() - yx.mean() * x.mean()) / denominator

    y_predicted = a*x + b

    plot_data(x, y, y_predicted)


if __name__ == '__main__':
    main()
