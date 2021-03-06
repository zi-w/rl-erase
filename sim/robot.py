import random
import pdb

#a 1D grid world where a robot is moving toward a cake
#s = 2 leads to a reward, s = 4 as well.
class Robot:
    def __init__(self, board):
        self.state = [0,0]
        self.xlimit = board.board.shape[0]
        self.ylimit = board.board.shape[1]
        self.pressure = 1
        self.board = board
        self.width = 6
        self.wipe_length = 8
        self.board.erase(self)

    def copy(self):
        r = Robot(self.board.copy())
        r.state = self.state[:]
        return r

    #does move, but in a smooth wiping motion, as a robot would
    def wipe(self, direction, board):
        for i in range(self.wipe_length):
            self.move(direction, board)
        
    #-1 for backward, +1 for forward
    #direction is a tuple (-1,-1) for example
    def move(self,direction, board):
        for i in [1,0]:
            potential_next = self.state[i] + direction[i]
            if potential_next < 0:
                return
            if i == 0 and potential_next + self.width > self.xlimit:
                return
            if i == 1 and potential_next + self.width > self.ylimit:
                return
            else:
                self.state[i] = potential_next
        board.erase(self)
       
    def reward(self,board):
        return board.reward()
        


