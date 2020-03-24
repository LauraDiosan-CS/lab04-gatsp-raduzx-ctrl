from copy import deepcopy


def readGraph(filename):
    file = open(filename, "r")
    n = int(file.readline())
    m = []
    for line in file:
        m.append([])
        for elem in line.split(","):
            m[-1].append(int(elem))
    network = {}
    network["noNodes"] = n
    network["matrix"] = m
    return network
