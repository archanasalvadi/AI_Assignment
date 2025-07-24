class State:
    def __init__(self,init):
        self.init=init
        self.final = ['R', 'R', 'R', '_', 'L', 'L', 'L']
    def goalTest(self):
        return self.init == self.final
    def moveGen(self):
        children = []
        for i in range(len(self.init)):
            if self.init[i] == 'L':
                # Move right
                if i + 1 < len(self.init) and self.init[i + 1] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i + 1] = new_config[i + 1], new_config[i]
                    children.append(State(new_config))
                # Jump over R
                if i + 2 < len(self.init) and self.init[i + 1] == 'R' and self.init[i + 2] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i + 2] = new_config[i + 2], new_config[i]
                    children.append(State(new_config))
            elif self.init[i] == 'R':
                # Move left
                if i - 1 >= 0 and self.init[i - 1] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i - 1] = new_config[i - 1], new_config[i]
                    children.append(State(new_config))
                # Jump over L
                if i - 2 >= 0 and self.init[i - 1] == 'L' and self.init[i - 2] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i - 2] = new_config[i - 2], new_config[i]
                    children.append(State(new_config))
        return children
    def __eq__(self, other):
        return isinstance(other, State) and self.init == other.init

    def __hash__(self):
        return hash(tuple(self.init))

    def __repr__(self):
        return ''.join(self.init)
        
initial_state = ['L', 'L', 'L', '_', 'R', 'R', 'R']
start_state = State(initial_state)
def removeSeen(children, OPEN, CLOSED):
    open_nodes  = [node for node, parent in OPEN]
    closed_nodes = [node for node, parent in CLOSED]
    new_nodes = [node for node in children if node not in open_nodes and node not in closed_nodes]
    return new_nodes

def reconstructPath(node_pair, CLOSED):
    parent_map = {} 
    for node, parent in CLOSED:
        parent_map[node] = parent    
    N, parent = node_pair
    path = [N]
    
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    
    # path = path.reverse()
    print(" <- \n ".join([str(e) for e in path]))
    
    return path
              
def bfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        # print(N, parent)
        if N.goalTest():
            print("Goal is found")
            path = reconstructPath(node_pair, CLOSED)
            return
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN =  OPEN + new_pairs
         
    return []


def dfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        # print(N, parent)
        if N.goalTest():
            print("Goal is found")
            path = reconstructPath(node_pair, CLOSED)
            return
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = new_pairs + OPEN
         
    return []

initial_config = ['L', 'L', 'L', '_', 'R', 'R', 'R']
start_state = State(initial_config)
dfs(start_state)
