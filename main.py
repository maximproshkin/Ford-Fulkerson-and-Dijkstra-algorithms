"""
1. Задать G1 − сеть для задачи о максимальном потоке (алгоритм Форда-Фалкерсона) с характеристиками:
G1(7, 12), где первое число − число вершин, второе число − число дуг.
Интервалы весов: 1-7

2. Задать G2 − сеть для задачи о кратчайшем пути (алгоритм Дейкстры) с характеристиками:
G2(6, 13), где первое число − число вершин, второе число − число дуг.
Интервалы весов: 1-7

Интервалы весов указывают границы изменения пропускных способностей и длин дуг.
"""

# ----------------------------------------------------------------------------------------------------------------------
#                                                           2
# ----------------------------------------------------------------------------------------------------------------------

'''СОЗДАДИМ ХЭШ-ТАБЛИЦУ ГРАФА G2 (изображение графа в папке img)'''

num_nodes = 4  # число вершин
seq = [_ for _ in range(num_nodes)]  # список вершин
G2 = dict.fromkeys(seq, {})
# установим связи между вершинами
G2[0] = {1: 6, 2: 2}  # ребро '01' имеет вес = 6, ребро '02' имеет вес = 2
G2[1] = {3: 1}
G2[2] = {1: 3, 3: 5}

print(G2)

'''СОЗДАДИМ ХЭШ-ТАБЛИЦУ ДЛЯ ХРАНЕНИЯ СТОИМОСТИ ВСЕХ УЗЛОВ'''
infinity = float("inf")
costs = {1: 6, 2: 2, num_nodes - 1: infinity}

'''КОД СОЗДАНИЯ ХЭШ-ТАБЛИЦЫ РОДИТЕЛЕЙ'''
parents = {1: 0, 2: 0, num_nodes - 1: None}

seq = []  # Массив для отслеживания всех обработанных узлов

'''
    ****    АЛГОРИТМ   ****

1. Пока остаются необработанные узлы ->
2. Взять узел, ближайший к началу ->
3. Обновить стоимости для его соседей ->
4. Если стоимости каких-либо соседей были обновлены, обновить и родителей ->
5. Пометить узел как обработанный ->
6. Вернуться в п. 1.  
'''


def find_lowest_cost_node(costs):
    pass
    return 0


node = find_lowest_cost_node(costs)  # Найти узел с наименьшей стоимостью среди необработанных
while node is not None:                 # Если обработаны все узлы, то цикл while завершен
    cost = costs[node]
    neighbors = G2[node]
    for n in neighbors.keys():      # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:     # Если к соседу можно быстрее добраться через текущий узел...
            costs[n] = new_cost     # ... обновить стоимость для этого узла
            parents[n] = node       # Этот узел становится новым родителем для соседа
    seq.append(node)                # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл
