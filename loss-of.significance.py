import matplotlib.pylab as plt

number = 0
real = 0
count = 0
lista = []
for i in range(10000):
    number += 1/3
    count += 1
    if count == 3:
        real += 1
        count = 0
        error = real - number
        print("Suposed number: " + str(real) + "  Actual number: " + str(number) + " Error: " + str(error))
        lista.append(error)
plt.plot(lista)
plt.show()