class BlockWorld:
    def __init__(self):
        self.state = ['A', 'B', 'C'] #Initial state: Three blocks on table
    def move(self, source, destination):
        if source == destination or source not in self.state:
            return False #Invalid move
        
        block = self.state.pop(self.state.index(source)) #Remove block from source
        self.state.append(block) #place the block on destination
        return True

    def solve(self):
        #Move A to C
        self.move('A','C')
        #Move A to B
        self.move('A','B')
        #Move C to B
        self.move('C','B')
        #Move A to C
        self.move('A','C')
        #Move B to A
        self.move('B','A')
        #Move B to C
        self.move('B','C')
        #move A to C
        self.move('A','C')
        return self.state
        
# Create a Blockworld instance
block_world = BlockWorld()
#Solve the problem
final_state = block_world.solve()
print ("Final state:", final_state)
