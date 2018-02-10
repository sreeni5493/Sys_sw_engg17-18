from random import random, shuffle
from itertools import chain
from math import floor
import subprocess
import sudoku

class Sudoku:
    def __init__(self, difficulty, errors = 0, completion = 1, res_x = 1920, res_y = 1080, frontal_view = 1):
        self.cTex_hand = []
        self.cTex_font = []
        self.precreated_sudoku_dict = {"Easy" : [[1, 5, 2, 6, 4, 3, 7, 9, 8, 9, 3, 7, 1, 5, 8, 2, 6, 4, 8, 4, 6, 9, 7, 2, 5, 1, 3, 3, 9, 8, 5, 6, 4, 1, 2, 7, 4, 6, 5, 2, 1, 7, 3, 8, 9, 2, 7, 1, 3, 8, 9, 6, 4, 5, 5, 8, 9, 7, 2, 6, 4, 3, 1, 6, 1, 3, 4, 9, 5, 8, 7, 2, 7, 2, 4, 8, 3, 1, 9, 5, 6],\
                                           [6, 3, 4, 1, 8, 9, 7, 5, 2, 7, 9, 8, 5, 2, 6, 4, 1, 3, 1, 2, 5, 7, 4, 3, 8, 9, 6, 8, 4, 6, 9, 7, 2, 1, 3, 5, 9, 5, 7, 3, 1, 8, 6, 2, 4, 3, 1, 2, 6, 5, 4, 9, 7, 8, 2, 6, 1, 4, 3, 7, 5, 8, 9, 5, 8, 9, 2, 6, 1, 3, 4, 7, 4, 7, 3, 8, 9, 5, 2, 6, 1]],\
                                "Medium" : [[5, 1, 3, 8, 2, 7, 4, 9, 6, 4, 6, 7, 1, 9, 5, 8, 2, 3, 2, 8, 9, 6, 3, 4, 5, 7, 1, 7, 2, 1, 9, 5, 6, 3, 4, 8, 8, 9, 5, 3, 4, 1, 7, 6, 2, 6, 3, 4, 7, 8, 2, 9, 1, 5, 1, 4, 6, 5, 7, 3, 2, 8, 9, 9, 5, 2, 4, 6, 8, 1, 3, 7, 3, 7, 8, 2, 1, 9, 6, 5, 4],\
                                            [6, 1, 8, 3, 2, 7, 9, 4, 5, 5, 3, 9, 6, 4, 1, 8, 2, 7, 7, 2, 4, 9, 8, 5, 6, 3, 1, 3, 5, 1, 7, 6, 4, 2, 9, 8, 8, 6, 2, 1, 9, 3, 5, 7, 4, 9, 4, 7, 8, 5, 2, 3, 1, 6, 4, 8, 3, 2, 7, 6, 1, 5, 9, 1, 9, 5, 4, 3, 8, 7, 6, 2, 2, 7, 6, 5, 1, 9, 4, 8, 3]],\
                                "Hard" : [[8, 5, 2, 6, 1, 7, 9, 4, 3, 4, 3, 9, 2, 8, 5, 7, 6, 1, 6, 7, 1, 3, 9, 4, 5, 2, 8, 9, 1, 3, 7, 6, 2, 4, 8, 5, 7, 6, 5, 8, 4, 3, 2, 1, 9, 2, 8, 4, 9, 5, 1, 6, 3, 7, 5, 4, 6, 1, 3, 9, 8, 7, 2, 3, 2, 8, 5, 7, 6, 1, 9, 4, 1, 9, 7, 4, 2, 8, 3, 5, 6],\
                                       [2, 1, 4, 7, 8, 3, 9, 6, 5, 5, 3, 6, 4, 2, 9, 7, 1, 8, 8, 9, 7, 1, 6, 5, 2, 4, 3, 7, 2, 8, 6, 5, 1, 3, 9, 4, 3, 6, 9, 2, 7, 4, 8, 5, 1, 4, 5, 1, 9, 3, 8, 6, 2, 7, 6, 4, 2, 8, 1, 7, 5, 3, 9, 9, 7, 3, 5, 4, 2, 1, 8, 6, 1, 8, 5, 3, 9, 6, 4, 7, 2]],\
                               "Insane" : [[8, 9, 4, 7, 3, 1, 5, 6, 2, 7, 2, 1, 4, 6, 5, 8, 9, 3, 6, 5, 3, 9, 8, 2, 1, 7, 4, 3, 6, 2, 5, 7, 8, 9, 4, 1, 5, 4, 8, 1, 2, 9, 6, 3, 7, 1, 7, 9, 6, 4, 3, 2, 5, 8, 2, 1, 5, 3, 9, 4, 7, 8, 6, 9, 3, 7, 8, 1, 6, 4, 2, 5, 4, 8, 6, 2, 5, 7, 3, 1, 9],\
                                            [6, 3, 7, 9, 1, 4, 8, 2, 5, 2, 4, 9, 8, 7, 5, 1, 3, 6, 5, 1, 8, 2, 6, 3, 4, 7, 9, 4, 5, 1, 7, 9, 8, 3, 6, 2, 9, 8, 6, 3, 5, 2, 7, 4, 1, 7, 2, 3, 1, 4, 6, 9, 5, 8, 8, 9, 5, 6, 3, 7, 2, 1, 4, 3, 6, 2, 4, 8, 1, 5, 9, 7, 1, 7, 4, 5, 2, 9, 6, 8, 3]]}
        self.precreated_unsolved_sudoku_dict =  {"Easy" : [[0, 0, 0, 0, 4, 0, 7, 0, 0, 9, 0, 0, 0, 0, 8, 0, 0, 4, 8, 4, 0, 9, 0, 0, 0, 1, 0, 3, 9, 0, 5, 0, 0, 0, 2, 0, 4, 0, 5, 0, 1, 7, 3, 8, 0, 2, 7, 0, 0, 8, 0, 6, 4, 5, 5, 0, 0, 0, 2, 6, 0, 3, 0, 6, 1, 0, 4, 9, 5, 8, 7, 2, 7, 2, 4, 0, 0, 0, 0, 5, 0],
                                           [6, 0, 0, 1, 8, 9, 7, 0, 0, 0, 0, 8, 0, 0, 6, 4, 0, 3, 0, 2, 5, 7, 4, 3, 0, 9, 0, 8, 4, 0, 9, 7, 2, 1, 3, 5, 9, 5, 0, 0, 1, 0, 0, 2, 0, 3, 1, 2, 6, 5, 0, 9, 7, 8, 2, 6, 1, 4, 3, 0, 5, 8, 9, 5, 8, 9, 2, 0, 0, 3, 0, 0, 4, 7, 0, 8, 9, 0, 0, 6, 1]],
                                 "Medium" : [[0, 0, 3, 8, 0, 0, 0, 0, 6, 4, 0, 0, 0, 9, 0, 0, 0, 0, 2, 0, 9, 6, 3, 0, 0, 7, 0, 7, 2, 0, 9, 5, 6, 0, 4, 8, 0, 0, 5, 0, 4, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 3, 2, 0, 0, 9, 0, 0, 4, 6, 0, 0, 0, 7, 0, 0, 8, 0, 0, 0, 6, 5, 0],
                                            [6, 0, 0, 0, 2, 7, 9, 0, 5, 5, 0, 9, 6, 0, 1, 0, 2, 7, 0, 0, 0, 9, 8, 0, 6, 3, 1, 0, 5, 0, 7, 0, 0, 0, 9, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 4, 0, 8, 5, 0, 0, 1, 0, 4, 8, 0, 2, 0, 6, 1, 5, 0, 0, 9, 5, 4, 0, 8, 7, 6, 0, 0, 0, 6, 5, 1, 9, 4, 8, 0]],
                                "Hard" : [[0, 0, 0, 0, 0, 7, 9, 0, 3, 0, 0, 9, 0, 0, 5, 7, 0, 0, 6, 7, 0, 3, 0, 4, 5, 0, 0, 0, 1, 0, 7, 0, 0, 0, 0, 0, 0, 6, 0, 8, 0, 3, 0, 1, 9, 0, 0, 4, 9, 0, 0, 6, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 8, 3, 0, 6],
                                       [0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 3, 0, 4, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 2, 0, 0, 7, 0, 8, 6, 0, 1, 3, 9, 0, 0, 6, 9, 0, 7, 0, 8, 5, 0, 4, 0, 0, 9, 3, 8, 6, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 9, 0, 7, 3, 0, 4, 2, 0, 8, 6, 0, 8, 0, 0, 0, 6, 0, 7, 0]],
                                "Insane" : [[0, 9, 0, 7, 3, 0, 5, 0, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 6, 2, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 9, 0, 0, 7, 0, 0, 0, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 8, 0, 6, 0, 0, 0, 0, 8, 0, 2, 5, 0, 3, 0, 9],
                                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 8, 7, 0, 0, 0, 6, 0, 1, 8, 2, 0, 3, 4, 7, 0, 0, 0, 0, 0, 9, 8, 0, 0, 2, 0, 0, 0, 3, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 5, 0, 8, 0, 0, 0, 0, 7, 2, 1, 0, 0, 6, 0, 4, 0, 0, 0, 0, 7, 0, 0, 4, 0, 2, 0, 0, 0, 3]]}
        r = floor(random()*len(self.precreated_sudoku_dict[difficulty]))
        self.complete_sudoku = self.precreated_sudoku_dict[difficulty][int(r)]
        self.unsolved_sudoku = self.precreated_unsolved_sudoku_dict[difficulty][int(r)]
        self.completion = completion
        self.difficulty = difficulty
        self.errors = errors
        self.r_x = res_x
        self.r_y = res_y
        self.frontal_view = frontal_view

    def randomize_sudoku(self):
        r = floor(random()*len(self.precreated_sudoku_dict[self.difficulty]))
        self.complete_sudoku = self.precreated_sudoku_dict[self.difficulty][r]
        self.unsolved_sudoku = self.precreated_unsolved_sudoku_dict[self.difficulty][r]
        blocksize = 9
        r = random()
        permutation_list = [i for i in range(0,81)]
        for i in range(0,3):
            blocks = [permutation_list[i:i+blocksize] for i in range(i*3*blocksize,(i+1)*3*blocksize,blocksize)]
            print(blocks)
            shuffle(blocks)
            permutation_list[i*3*blocksize:(i+1)*3*blocksize] = [b for bs in blocks for b in bs]
        # Flip sudoku to shuffle former lines
        blocks = [permutation_list[i:i+blocksize] for i in range(0,len(permutation_list),blocksize)]
        blocks = zip(*blocks)
        permutation_list = list(chain(*blocks))
        for i in range(0,3):
            print(permutation_list)
            print(blocksize)
            blocks = [permutation_list[i:i+blocksize] for i in range(i*3*blocksize,(i+1)*3*blocksize,blocksize)]
            print("blocks" + str(blocks))
            shuffle(blocks)
            permutation_list[i*3*blocksize:(i+1)*3*blocksize] = [b for bs in blocks for b in bs]
        # Maybe flip back
        if (random() < 0.5):
            blocks = [permutation_list[i:i+blocksize] for i in range(0,len(permutation_list),blocksize)]
            blocks = zip(*blocks)
            permutation_list[0:len(permutation_list)] = [b for bs in blocks for b in bs]
        # Reorder sudokus
        tmp_complete_sudoku = []
        tmp_unsolved_sudoku = []
        for i in range(0,81):
            tmp_complete_sudoku.append(self.complete_sudoku[permutation_list[i]])
            tmp_unsolved_sudoku.append(self.unsolved_sudoku[permutation_list[i]])
        self.complete_sudoku = tmp_complete_sudoku
        self.unsolved_sudoku = tmp_unsolved_sudoku
        del tmp_complete_sudoku,tmp_unsolved_sudokus
    
    def create_new_sudoku(self):
        start = time.time()

        # Create sudoku data
        # Create a solved and an unsolved sudoku, the different is the handwritten input.
        condition = False   # The sudokus are created and the difficulty is checked afterwards. So we create sudokus (which is rather fast) until we have a sudoku of given difficulty.
        while (condition == False):
            new_complete_sudoku = sudoku.perfectSudoku()
            unsolved_sudoku_result = sudoku.puzzleGen(copy.deepcopy(new_complete_sudoku))
            print(unsolved_sudoku_result[2])
            if unsolved_sudoku_result[2] == self.difficulty:
                condition = True

        for i in range(0,81,1):
            self.complete_sudoku[i] = new_complete_sudoku[i].returnPossible()[0]
            if len(unsolved_sudoku_result[0][i].returnPossible())<2:
                self.unsolved_sudoku[i] = unsolved_sudoku_result[0][i].returnPossible()[0]
            else:
                self.unsolved_sudoku[i] = 0
                
        end = time.time()
        print("sudoku generation took ",end - start," seconds")
        
    def set_errors(self,val):
        self.errors = val
    
    def set_difficulty(self,val):
        if (val == "Easy" or val == "Medium" or val == "Hard" or val == "Insane"):
            self.difficulty = val
        else:
            raise ValueError('Difficulty can\'t be set to %s.'%val)
    
    def set_errors(self,val):
        self.errors = val        
    
    def set_resolution(self,val1,val2):
        self.r_x = val1
        self.r_y = val2
    
    def set_frontal_view(self,val):
        if val:
            self.frontal_view = 1
        else:
            self.frontal_view = 0
    
if __name__ == '__main__':
    s = Sudoku("Hard", 0, 1)
    string_call = '/home/sreenivas/Downloads/blender-2.79-linux-glibc219-x86_64/blender'
    #arguments = []
    #string_call.append(arguments)
    print(string_call)
    subprocess.call([string_call,"-b","--python",'./generate_sudoku_scene.py',"--","--difficulty","%s"%s.difficulty,"--errors","%d"%s.errors,"--completion","%d"%s.completion,"--resolution","%d"%s.r_x,"%d"%s.r_y,"--solved","%s"%s.complete_sudoku,"--unsolved","%s"%s.unsolved_sudoku,"--frontal_view","%s"%s.frontal_view])