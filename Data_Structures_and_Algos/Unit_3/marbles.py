'''
Week 3
by: Joseph Roberts robertsj32@gmail.com

This marble games works out to be rouhgly a quadratic equation as we have nested loops.  
The approximate equation is (n**2) - 6.  If we remove the constant, then O(n**2). 
'''
import sys

class MarblesBoard:
    
    def __init__(self, marbles):
        
        self._marbles = list(marbles)
       
    def __str__(self):
        str_list = [str(x) for x in self._marbles]
        str_list = ' '.join(str_list)
        return str_list
    
    def __repr__ (self):
        str_list = [str(x) for x in self._marbles]
        str_list = ' '.join(str_list)
        return str_list
    
    def switch(self):
        self._marbles[1], self._marbles[0] = self._marbles[0], self._marbles[1]
        print(self)
        return self
    
    def rotate(self):
        self._marbles.append(self._marbles.pop(0))
        print(self)
        return self
    
    def solved(self):
        flag = False
        if(all(self._marbles[i] <= self._marbles[i + 1] for i in range(len(self._marbles)-1))):
            return True
        else:
            return False
        
class Solver(MarblesBoard):

    
    def __init__(self, marbles):
        self.Marbles = marbles
        self._marbles = self.Marbles._marbles
        
    def solve(self):
        print(self)
        count = 0
        while not self.Marbles.solved():
            count+=1
            if self.Marbles._marbles[0] < self.Marbles._marbles[1]:
                self.Marbles.rotate()
            else:
                if (self.Marbles._marbles[0] != 0) and (self.Marbles._marbles[1] != 0):
                    self.Marbles.switch()
                else:
                    self.Marbles.rotate()
                    
        if self.Marbles.solved():
            print(f'total steps: {count}')
            
if __name__ == '__main__': 
    user_input = sys.argv[1:][0].split(',')
    cleaned_list = [int(x) for x in user_input]
    
    board = MarblesBoard(cleaned_list)
    solve_it = Solver(board)
    solve_it.solve()