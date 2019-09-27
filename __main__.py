import numpy as np
import random

class Ant:
    def __init__(self, allowed_nodes,start_node):
        self.start_node = start_node
        self.current_node = start_node
        self.end_node = start_node
        self.tabu_nodes = [start_node]
        self.allowed_nodes = allowed_nodes.copy()
        self.allowed_nodes.remove(self.start_node)
        self.length = 0
        
def transition_propability(nodes, i, j):
    sum = 0
    # Высчитываем вероятность перехода из вершины i в вершину j
    for node in nodes:
        sum += (t[i,node]**a)/(w[i,node]**b)
    return ((t[i,j]**a)/(w[i,j]**b)) / sum

def evaporate_pheromones():
    global t
    # Испаряем феромоны на всех рёбрах
    for i in range(w.shape[0]):
        for j in range(w.shape[1]):
            t[i,j] = (1 - p)*t[i,j]
            if t[i,j] < 1/w.shape[0]:
                t[i,j] = 1/w.shape[0]

def update_pheromones(ants):
    global t
    # Обновляем феромоны на путях муравьев
    for ant in ants:
        for ind in range(1,w.shape[0]+1):
            t[ant.tabu_nodes[ind - 1], ant.tabu_nodes[ind]] += q/ant.length
            
if __name__ == "__main__":

    np.random.seed = 7 
    # Инициализация параметров алгоритма
    a = 1   # Чем меньше a, тем наиболее вероятен выбор ближайшего города
    b = 1   # Чем меньше b, тем наиболее вероятен выбор города на основании феромонов
    q = 100 # Параметр, имеющий значение порядка цены оптимального решения
    p = 0.2 # Интенсивность испарения
    L = float('inf')
    T = []
    w = [] 
    # Ввод матрицы
    while True:
        w.append(list((map(int,input().split()))))
        if(len(w[0]) == len(w)):
            break
    w = np.array(w)
    n = m = w.shape[0]
    nodes = list(range(0,n))
    # Создаём список феромонов на рёбрах
    t = np.ones((n,m))

    ants_num = n
    iter_num = 10*n
    
    # Цикл итераций алгоритма
    for i in range(iter_num):
        # Создание муравьев
        ants = [Ant(nodes,np.random.randint(n)) for j in range(ants_num)]
        # Поиск кратчайшего пути для каждого муравья
        for ant in ants:
            while ant.allowed_nodes:
                # Поиск перехода
                not_chosen = True
                next_node = 0
                while not_chosen:
                    for node in ant.allowed_nodes:
                        rand = random.random()
                        prob = transition_propability(ant.allowed_nodes, ant.current_node, node)
                        if prob >= rand:
                            not_chosen = False
                            next_node = node
                            break
                # Обновление данных для муравья
                ant.length += w[ant.current_node, next_node]    
                ant.current_node = next_node
                ant.allowed_nodes.remove(ant.current_node)
                ant.tabu_nodes.append(ant.current_node) 
            # Добавляем переход в начальную точку
            ant.tabu_nodes.append(ant.end_node)
            ant.length += w[ant.current_node, ant.end_node]
            # Проверяем на минимальность длины пути
            if ant.length < L:
                L = ant.length
                T = ant.tabu_nodes.copy()
        # Испоряем феромоны на всех ребрах и обновляем феромоны на путях муравьев
        evaporate_pheromones()            
        update_pheromones(ants)
    
    print(L)
