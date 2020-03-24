from lab4.TSP import findBestPath
from lab4.utils import readGraph

if __name__ == '__main__':
    fileName = input("Dati numele fisierului: ")
    probMutation = float(input("Probabilitatea de mutation (0-1): "))
    populationSize= float(input("Dimensiunea populatiei(1-aceeasi cu numarul de orase): "))

    #fileName = "easy_03_tsp.txt"
    #probMutation=0.3
    #populationSize=2


    network = readGraph(fileName)
    d = findBestPath(network,probMutation,populationSize)
    print(d["value"])
    print(d["path"])
