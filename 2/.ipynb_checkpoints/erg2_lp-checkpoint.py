from scipy import optimize as lp
import numpy as np 


class bonus2:
    def __init__(self, n_players:int):
        self.n = n_players 
    

    def create_game_matrix(self):
        n = self.n_players 
        A = np.zeros((n, n), dtype=int)

        rows, cols = np.indices((n, n))
        delta = cols - rows

        A[delta == 1] = -1
        A[delta > 1]  = 2
        A[delta == -1] = 1
        A[delta < -1] = -2

        return self.A 

    def solve_game(self):


