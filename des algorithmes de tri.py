from random import randint
import time

temps_w = []
temps_py = []
temps_a = []
temps_d = []

e_liste = 20  # nombre d'éléments dans la liste
rep = 1       # nombre de fois que le tri s'effectue (moyenne des temps à la fin)

for _ in range(rep):

    w = [randint(0, 100) for i in range(e_liste)]
    py = w.copy()
    a = w.copy()
    d = w.copy()

    # print(w)
    # print(py)
    # print(a)   # enlever tous les # du programme pour le visualiser les tris
    # print(d)
    # print("")
    # print("")

    ''' METHODE Wandrille '''

    # print(w)
    start_time = time.time()

    z = max(w)
    while z >= 0:
        n = 0
        for i in w:
            if z == w[n]:
                w.append(w[n])
                del w[n]
            else:
                n += 1
        z -= 1
    w.reverse()

    temps_w.append((time.time() - start_time))
    # print(w)
    # print("")

    ''' METHODE Python (sort) '''

    start_time = time.time()

    py.sort()

    temps_py.append((time.time() - start_time))

    ''' METHODE ALEXANDRE '''

    # print(a)
    start_time = time.time()

    for k in range(len(a)):
        intable = a[k]
        n = k-1
        while n >= 0 and a[n] > intable:
            a[n+1] = a[n]
            n = n-1
            a[n+1] = intable

    temps_a.append(time.time() - start_time)
    # print(a)
    # print("")

    ''' METHODE DJEBRIL '''

    # print(d)
    start_time = time.time()

    d_2 = []

    for i in range(len(d)):
        x = min(d)
        d_2.append(x)
        d.remove(x)

    temps_d.append((time.time() - start_time))
    # print(d_2)
    # print("")

    print("{} sur {}".format(_ + 1, rep))  # sert à voir l'avancement des tris

# print(w)
# print(py)
# print(a)
# print(d_2)

print("")
print("Méthode Wandrille : ", (sum(temps_w) / rep))
print("Méthode Python : ", (sum(temps_py) / rep))
print("Méthode Alexandre : ", (sum(temps_a) / rep))
print("Méthode Djebril : ", (sum(temps_d) / rep))
