import queue
import random

from collections import deque

class Node:
  def __init__(self, i, j,id):
    self.i = i
    self.j = j
    self.id = id

def copyQueue(q1,q2):
    for i in q1.queue:
        q2.put(i)

def load_maze(file_name):
    f = open(file_name)
    maze = f.read()
    f.close()
    return maze

def conver_maze(maze):
    converted_maze = []
    lines = maze.splitlines()
    for line in lines:
        converted_maze.append(list(line))
    return converted_maze

def print_maze(maze):
    for row in maze:
        for item in row:
            print(item, end='')
        print()

def coordenates (maze):
    lines = maze[len(maze) - 2:]

    #finding start
    i=0
    if int(lines[0][0]) != 0:
        i=int(lines[0][0])*1000
    if int(lines[0][1]) != 0:
        i +=int(lines[0][1])*100
    if int(lines[0][2]) != 0:
        i +=int(lines[0][2])*10
    if int(lines[0][3]) != 0:
        i += int(lines[0][3])

    j = 0
    if int(lines[0][6]) != 0:
        j=int(lines[0][6])*1000
    if int(lines[0][7]) != 0:
        j +=int(lines[0][7])*100
    if int(lines[0][8]) != 0:
        j +=int(lines[0][8])*10
    if int(lines[0][9]) != 0:
        j += int(lines[0][9])
    guide = [i,j]

    #finding end
    k = 0
    if int(lines[1][0]) != 0:
        k = int(lines[1][0]) * 1000
    if int(lines[1][1]) != 0:
        k += int(lines[1][1]) * 100
    if int(lines[1][2]) != 0:
        k += int(lines[1][2]) * 10
    if int(lines[1][3]) != 0:
        k += int(lines[1][3])

    l = 0
    if int(lines[1][6]) != 0:
        l = int(lines[1][6]) * 1000
    if int(lines[1][7]) != 0:
        l += int(lines[1][7]) * 100
    if int(lines[1][8]) != 0:
        l += int(lines[1][8]) * 10
    if int(lines[1][9]) != 0:
        l += int(lines[1][9])
    end = [k, l]
    guide+=end
    return guide

def normalize_maze(maze):
    i = 0
    aux = []
    while (i<len(maze)-2):
        aux.append(maze[i])
        i+=1
    return aux

def find_end(closed_queue):
    if closed_queue.empty():
        return False
    else:
        aux = queue.Queue()
        copyQueue(closed_queue,aux)
        while not aux.empty():
            node = aux.get()
            if (node.i == guide[2] and node.j == guide[3]):
                return True
        return False

def get_best_node(open_queue, id):
    open_list = []
    for elem in open_queue.queue:
        open_list.append(elem)

    res = open_list[0]
    i=1
    pos = 0
    match id:
        case "G":
            while (i < len(open_list)):
                if calc_distance(res) >= calc_distance(open_list[i]):
                    pos = i
                i = i + 1
        case "A":
            while (i < len(open_list)):
                if calc_distance_star(res) >= calc_distance_star(open_list[i]):
                    pos = i
                i = i + 1

    res = open_list.pop(pos)
    with open_queue.mutex:
        open_queue.queue.clear()
    for elem in open_list:
        open_queue.put(elem)
    return res

def calc_distance(elem):
    x = elem.i
    if x < 0:
        x = x*-1
    y = elem.j
    if y < 0:
        y = y*-1
    origin = x+y

    end_x = guide[2]
    if end_x<0:
        end_x = end_x*-1
    end_y = guide[3]
    if end_y <0:
        end_y = end_y*-1
    end = end_y+end_x
    total = end - origin
    return total

def calc_distance_star(elem):
    x = elem.i
    if x < 0:
        x = x*-1
    y = elem.j
    if y < 0:
        y = y*-1
    origin = x+y

    end_x = guide[2]
    if end_x<0:
        end_x = end_x*-1
    end_y = guide[3]
    if end_y <0:
        end_y = end_y*-1
    end = end_y+end_x
    greedy = end - origin
    cost = 10
    total = greedy+cost
    return total

def valid_node(node,x, closed_queue, open_queue):
    check_node = Node(node.i, node.j, node.id)
    match x:
        case "L":
            check_node.i -= 1
        case "R":
            check_node.i += 1
        case "U":
            check_node.j -= 1
        case "D":
            check_node.j += 1
    if not(0 <= check_node.i < len(maze[0]) and 0 <= check_node.j < len(maze)):
        return False
    elif (maze[check_node.j][check_node.i] == "X"):
        return False
    for elem in closed_queue.queue:
        if elem.i == check_node.i and elem.j == check_node.j:
            return False
    for elem in open_queue.queue:
        if elem.i == check_node.i and elem.j == check_node.j:
            return False
    return True

def depth_valid_node(node,x, closed_queue, open_queue):
    check_node = Node(node.i, node.j, node.id)
    match x:
        case "L":
            check_node.i -= 1
        case "R":
            check_node.i += 1
        case "U":
            check_node.j -= 1
        case "D":
            check_node.j += 1
    if not(0 <= check_node.i < len(maze[0]) and 0 <= check_node.j < len(maze)):
        return False
    elif (maze[check_node.j][check_node.i] == "X"):
        return False
    for elem in closed_queue.queue:
        if elem.i == check_node.i and elem.j == check_node.j:
            return False
    for elem in open_queue:
        if elem.i == check_node.i and elem.j == check_node.j:
            return False
    return True

def calc_node(node,x,id_gen):
    check_node = Node(node.i, node.j, id_gen+1)
    match x:
        case "L":
            check_node.i -= 1
        case "R":
            check_node.i += 1
        case "U":
            check_node.j -= 1
        case "D":
            check_node.j += 1
    return check_node

def calc_traceback(closed_queue, register):
    path = queue.Queue()
    closed = []
    # Create the needed variables
    for i in closed_queue.queue:
        closed.append(i)
    # We dumped the que into a list so we can extract values from the end and from the begining
    n = closed[-1]
    closed.pop()
    # we remove from the list the last element
    path.put(n)
    while not n.id == 1:
        next_node_id=register[n.id]
        for cont in closed_queue.queue:
            if cont.id == next_node_id:
                n = Node(cont.i,cont.j,cont.id)
                path.put(n)
    return path

def print_result(maze, path):
    i = guide[0]
    j = guide[1]
    order_path = deque()
    pos = set()
    for elem in path.queue:
        order_path.append(elem)

    while not len(order_path) == 0:
        node = order_path.pop()
        pos.add((node.j, node.i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " " , end="")
        print()

def random_search():
    id_gen = 1
    n0 = Node(guide[0], guide[1], id_gen)
    closed_queue = queue.Queue()
    open_queue = queue.Queue()
    register = {n0.id: 0}
    open_queue.put(n0)
    while not find_end(closed_queue):
        #Here is where we make it random
        open_list = []
        for elem in open_queue.queue:
            open_list.append(elem)
        node = random.choice(open_list)
        closed_queue.put(node)
        for x in ["L", "R", "U", "D"]:
            if valid_node(node, x,closed_queue,open_queue):
                aux = calc_node(node, x, id_gen)
                id_gen += 1
                open_queue.put(aux)
                register[aux.id] = node.id
    path = calc_traceback(closed_queue, register)
    print_result(maze, path)

def depth_first_search():
    id_gen = 1
    n0 = Node(guide[0], guide[1], id_gen)
    closed_queue = queue.Queue()
    open_queue = deque()
    register = {n0.id: 0}
    open_queue.append(n0)
    while not find_end(closed_queue):
        node = open_queue.pop()
        closed_queue.put(node)
        for x in ["L", "R", "U", "D"]:
            if depth_valid_node(node, x, closed_queue, open_queue):
                aux = calc_node(node, x, id_gen)
                id_gen += 1
                open_queue.append(aux)
                register[aux.id] = node.id
    path = calc_traceback(closed_queue, register)
    print_result(maze, path)

def breadth_first_search():
    id_gen = 1
    n0 = Node(guide[0], guide[1], id_gen)
    closed_queue = queue.Queue()
    open_queue = queue.Queue()
    register = {n0.id: 0}
    open_queue.put(n0)
    while not find_end(closed_queue):
        node = open_queue.get()
        closed_queue.put(node)
        for x in ["L","R","U","D"]:
            if valid_node(node,x,closed_queue,open_queue):
                aux = calc_node(node,x,id_gen)
                id_gen+=1
                open_queue.put(aux)
                register[aux.id]=node.id
    path = calc_traceback(closed_queue, register)
    print_result(maze,path)

def greedy_search():
    id_gen = 1
    n0 = Node(guide[0], guide[1], id_gen)
    closed_queue = queue.Queue()
    open_queue = queue.Queue()
    register = {n0.id: 0}
    open_queue.put(n0)
    while not find_end(closed_queue):
        node = get_best_node(open_queue, "G")
        closed_queue.put(node)
        for x in ["L", "R", "U", "D"]:
            if valid_node(node, x, closed_queue, open_queue):
                aux = calc_node(node, x, id_gen)
                id_gen += 1
                open_queue.put(aux)
                register[aux.id] = node.id
    path = calc_traceback(closed_queue, register)
    print_result(maze, path)

def a_start_search():
    id_gen = 1
    n0 = Node(guide[0], guide[1], id_gen)
    closed_queue = queue.Queue()
    open_queue = queue.Queue()
    register = {n0.id: 0}
    open_queue.put(n0)
    while not find_end(closed_queue):
        node = get_best_node(open_queue, "A")
        closed_queue.put(node)
        for x in ["L", "R", "U", "D"]:
            if valid_node(node, x, closed_queue, open_queue):
                aux = calc_node(node, x, id_gen)
                id_gen += 1
                open_queue.put(aux)
                register[aux.id] = node.id
    path = calc_traceback(closed_queue, register)
    print_result(maze, path)

"""
maze = load_maze("dataset\\6.txt")
"""
maze = load_maze("testovaci_data\\1.txt")

maze = conver_maze(maze)
guide = coordenates(maze)
maze = normalize_maze(maze)
print("This is the maze in which we are going to search")
print_maze(maze)
print("Our starting point is: ",guide[0],",",guide[1])
print("And our ending point is: ",guide[2],",",guide[3])
print()
print("This is the result of Breadth First Search: ")
breadth_first_search()
print()
print("This is the result of Depth First Search: ")
depth_first_search()
print()
print("This is the result of Random Search: ")
random_search()
print()
print("This is the result of Greedy Search: ")
greedy_search()
print("This is the result of A* Search: ")
a_start_search()