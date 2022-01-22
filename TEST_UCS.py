from dauphinetDS import PQmin

class Point (object):

    def __init__ (self, pos, cost=0, path=[]):
        
        self.pos = pos
        self.path = path + [self.pos] 
        self.acc_cost = cost

    def __eq__ (self, other):
        return self.pos == other.pos

    def __str__ (self):
        (i,j) = self.pos
        return "Posicao: ({},{}) , g(self) = {} , Path: {}".format(i,j,self.acc_cost, self.path)
        

class MapProblem (object):
    

    def __init__ (self, width, height, obstacles, goal):

        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.goal = Point(goal)
        self.move_list = "UP DOWN LEFT RIGHT UP-LEFT UP-RIGHT DOWN-LEFT DOWN-RIGHT".split()

    def cost (self, point, move):
        if move in self.move_list[0:4]:
            return 10 # Se for para lados ou norte/sul
        else:
            return 14 # Se for na diagonal

    def convert (self, pos, move):
        (i,j) = pos
        
        if move == "UP":
            return (i-1,j)
        if move == "DOWN":
            return (i+1,j)
        if move == "LEFT":
            return (i,j-1)
        if move == "RIGHT":
            return (i,j+1)
        if move == "UP-LEFT":
            return (i-1,j-1)
        if move == "UP-RIGHT":
            return (i-1,j+1)
        if move == "DOWN-LEFT":
            return (i+1,j-1)
        if move == "DOWN-RIGHT":
            return (i+1,j+1)

    def moves (self, point):
        (i,j) = point.pos
        possible_moves = []
        
        if i > 0:
            if (i-1,j) not in self.obstacles:
                possible_moves.append("UP")
            if j > 0 and (i-1,j-1) not in self.obstacles:
                possible_moves.append("UP-LEFT")
            if j < self.width - 1 and (i-1,j+1) not in self.obstacles:
                possible_moves.append("UP-RIGHT")
                
        if i < self.height - 1:
            if (i+1,j) not in self.obstacles:
                possible_moves.append("DOWN")
            if j > 0 and (i+1,j-1) not in self.obstacles:
                possible_moves.append("DOWN-LEFT")
            if j < self.width - 1 and (i+1,j+1) not in self.obstacles:
                possible_moves.append("DOWN-RIGHT")
                
        if j > 0:
            if (i,j-1) not in self.obstacles:
                possible_moves.append("LEFT")
                
        if j < self.width - 1:
            if (i,j+1) not in self.obstacles:
                possible_moves.append("RIGHT")
                

        return possible_moves

    def expand(self, point):
        p_moves = self.moves(point)
        p_points = []
        for move in p_moves:
            p_points.append( Point (self.convert(point.pos, move), point.acc_cost + self.cost(point, move), point.path))
        return p_points

    def start (self, s_pos):
        s_point = Point(s_pos)

        self.frontier = PQmin()
        self.frontier.add(s_point)
        self.visited = []

    def next_iteration (self):
        print("next iteration")

        if self.frontier.elements != []:
            smallest = self.frontier.pop_smallest()
            if smallest.pos not in self.visited:
                
                self.visited.append(smallest.pos)
            
                if smallest == self.goal:
                    return smallest
            
                children = self.expand(smallest)
                
                for child in children:
                    can_add = True
                    for ele in self.frontier.elements:
                        if child == ele:
                            if child.acc_cost < ele.acc_cost:
                                self.frontier.remove(ele)
                                self.frontier.add(child)
                            can_add = False
                    if can_add and child.pos not in self.visited:
                        self.frontier.add(child)
            return Point((-1,-1)) # signals it's still searching for the goal
        else:
            print("oops")
            return None # signals it has no solution.
          
