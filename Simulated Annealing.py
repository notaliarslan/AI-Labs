import random
import math


def solutionCost(solution):
    cost = int(0)
    for i in range(len(solution) - 1):
        city = solution[i] + solution[i + 1]
        cost += citiesDist[city]
    return cost


def paths(prev_path):
    newpath = prev_path
    randomIndex = random.randint(0, len(newpath) - 1)
    randomIndex1 = random.randint(0, len(newpath) - 1)
    temp = newpath[randomIndex]
    newpath[randomIndex] = newpath[randomIndex1]
    newpath[randomIndex1] = temp
    return newpath


def simulatedAnnealing(problem):
    current = problem
    next = []
    best = current
    temperature = 50
    coolingRate = 0.02
    while temperature > 1:
        next = paths(current[:])
        E = solutionCost(current) - solutionCost(next)
        if E > 0:
            current = next
            print("Good Move: ", current)
        else:
            probabilty = math.exp(E/temperature)
            current=next
            print("Bad Move: {} with probability {}".format(current, probabilty))
        if solutionCost(current) < solutionCost(best):
            best = current
        temperature -= coolingRate

    print("\n")
    print("Best solution is {} with cost {}".format(best, solutionCost(best)))


cities = ['A', 'B', 'C', 'D']
citiesDist = {
     'AB': 25,
     'AD': 15,
     'BD': 45,
     'BC': 10,
     'CD': 5,
     'AC': 10,
     'BA': 25,
     'DA': 15,
     'DB': 45,
     'CB': 10,
     'DC': 5,
     'CA': 10}

simulatedAnnealing(cities)
