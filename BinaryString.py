import random
import copy

class Individual:

    def __init__(self):
        self.fitness = 0
        self.length = 7
        self.genes = [random.choice((0, 1)) for i in range(self.length)]

    def calc_fitness(self):
        self.fitness = self.genes.count(1)


class Population:

    def __init__(self):
        self.pop_size = 10
        self.individuals = [Individual() for i in range(self.pop_size)]

    def calculate_fitness(self):
        for i in range(self.pop_size):
            self.individuals[i].calc_fitness()
        self.individuals.sort(key = lambda x:x.fitness)
        self.max_fitness = self.individuals[self.pop_size-1].fitness

    #Tournament Selection Technique for selecting parents
    def selection(self):
        parents = []
        k = 2
        for i in range(2):
            idxs = random.sample(range(0, self.pop_size), k)
            idx = max(idxs)
            parents.append(copy.deepcopy(self.individuals[idx]))
        return parents

    #Add offspring to the population and throw away worst individual from population
    def changepopulation(self, offspring):
        if offspring.fitness >= self.individuals[0].fitness:
            print('changing population')
            print('thrown:{}'.format(self.individuals[0].genes))
            print('Added:{}'.format(offspring.genes))
            self.individuals[0] = copy.deepcopy(offspring)
        else:
            print("Weak offspring, No change in population")
        print()


class Genetic:

    def __init__(self):
        self.population = Population()
        self.population.calculate_fitness()
        self.parents = []
        iter = 0
        while self.population.max_fitness < 7:
            iter+=1
            print('{}:'.format(iter))
            print('Max fitness of population:{}'.format(self.population.max_fitness))
            self.parents = self.population.selection()
            print('Before CrossOver')
            print('parent1:{}'.format(self.parents[0].genes))
            print('parent2:{}\n'.format(self.parents[1].genes))
            self.crossover()
            print('After CrossOver')
            print('offspring1:{}'.format(self.parents[0].genes))
            print('offspring2:{}\n'.format(self.parents[1].genes))
    
            x = random.choice(range(1,11))
            if x<3:
                print('Mutating:')
                self.mutate()
                print('Mutated offspring1:{}'.format(self.parents[0].genes))
                print('Mutated offspring2:{}\n'.format(self.parents[1].genes))
            
            offspring = self.getfittestoffspring()
            self.population.changepopulation(offspring)
            self.population.calculate_fitness()
            print()

        print('Total Iterations:{}'.format(iter))
        print(self.population.individuals[self.population.pop_size-1].genes)

    def getfittestoffspring(self):
        for x in self.parents:
            x.calc_fitness()
        if self.parents[0].fitness >= self.parents[1].fitness:
            return self.parents[0]
        return self.parents[1]

    #Mutation by flipping one randomly selected bit
    def mutate(self):
        x = random.choice(range(0, 7))
        if self.parents[0].genes[x]:
            self.parents[0].genes[x] = 0
        else:
            self.parents[0].genes[x] = 1

        y = random.choice(range(0, 7))
        if self.parents[1].genes[y]:
            self.parents[1].genes[y] = 0 
        else:
            self.parents[1].genes[y] = 1
         
    #CrossOver using One Point CrossOver Technique
    def crossover(self):
        crossover_point = random.choice(range(1, 8))
        self.parents[0].genes[0:crossover_point], self.parents[1].genes[0:crossover_point] = self.parents[1].genes[0:crossover_point], self.parents[0].genes[0:crossover_point]


def main():
    demo = Genetic()

if __name__=='__main__':
    main()
    



