from lab4.chromosome import Chromosome
import numpy

def get_random(nr):
    return int(numpy.random.rand(1) * 1000) % nr

def get_fitness(matrix,chromosome):
    sum=0.0
    permutation=chromosome.repres
    for i in range(0,len(permutation)-1):
        sum+=matrix[permutation[i]][permutation[i+1]]
    sum+=matrix[permutation[-1]][permutation[0]]
    return sum

def findBestPath(network, probMutation,populationSize):
    p={}
    p["value"]=0
    p["path"]=[]
    population=[]
    n=network["noNodes"]
    m=network["matrix"]
    dim=int(n*populationSize)
    problParam={}
    problParam["noNodes"]=n
    for i in range(dim):
        population.append(Chromosome(problParam))
        population[-1].fitness=get_fitness(m,population[-1])

    for k in range(2*dim):
        for i in range(dim):
            c=population[get_random(dim)]
            c2=population[get_random(dim)]
            population.append(c.crossover(c2))
            population[-1].fitness=get_fitness(m,population[-1])
        newDim=int(dim*probMutation)
        for i in range(newDim):
            nr=get_random(2*dim)
            population[nr].mutation()
            population[nr].fitness=get_fitness(m,population[nr])
        population.sort(key= lambda Chromosome:Chromosome.fitness)
        for i in range(n):
            population.pop()
    p["value"]=population[0].fitness
    perm=population[0].repres
    for i in range(0,len(perm)):
        perm[i]=perm[i]+1
    p["path"]=perm
    return p