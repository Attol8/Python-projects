import random
import math
class Game:
    def __init__(self):
        self.table_str = '_________'
        self.active = False
        self.table_matrix = self.convert_to_matrix(self.table_str)
        self.valid_move = False
        self.state = None
        self.rec_state = None
        self.command = None

    def convert_to_matrix(self, table_str):
        first_row = [cell if cell != '_' else ' ' for cell in table_str[0:3]]
        second_row = [cell if cell != '_' else ' ' for cell in table_str[3:6]]
        third_row = [cell if cell != '_' else ' ' for cell in table_str[6:9]]
        return [first_row, second_row, third_row]
    
    def get_matrix_coordinates(self, move):
        trans = [[[2,0], [1,0], [0,0]],
                    [[2,1], [1,1], [0,1]],
                    [[2,2], [1,2], [0,2]]]

        try:
            x = trans[int(move[0])-1][int(move[1])-1][0]
            y = trans[int(move[0])-1][int(move[1])-1][1]
            return x, y
        except ValueError: return None, None
        except IndexError: return int(move[0]), int(move[1])
    
    def print_table(self):
        print('---------')
        print('| {0} {1} {2} |'.format(*self.table_matrix[0]))
        print('| {0} {1} {2} |'.format(*self.table_matrix[1]))
        print('| {0} {1} {2} |'.format(*self.table_matrix[2]))
        print('---------')
    
    def insert_move(self, x, y):
        symbol = self.get_symbol()
        self.table_matrix[x][y] = symbol

    def check_move(self, move):
        x, y = self.get_matrix_coordinates(move)
        if isinstance(x, int) and isinstance(y, int):
            if x in range(3) and y in range(3):
                if self.table_matrix[x][y] == ' ':
                    self.valid_move = True
                    self.insert_move(x, y)
                else: print('This cell is occupied! Choose another one!')
            else: print('Coordinates should be from 1 to 3!')
        else: print('You should enter numbers!')
        
    def get_symbol(self):
        table_list = "".join([cell for row in self.table_matrix for cell in row])

        X_len, O_len = (0, 0)
        for cell in table_list:
            if cell == 'X': X_len += 1
            elif cell == 'O': O_len += 1

        if X_len == O_len: return 'X'
        else: return 'O'

    def get_state(self, rec):

        for i in range(0, 3):
            #check rows
            if self.table_matrix[i][0] == self.table_matrix[i][1] == self.table_matrix[i][2] and self.table_matrix[i][0] != ' ':
                if rec == False: self.state = '{0} wins'.format(self.table_matrix[i][0])
                else: self.rec_state = '{0} wins'.format(self.table_matrix[i][0])
            #check columns
            elif self.table_matrix[0][i] == self.table_matrix[1][i] == self.table_matrix[2][i] and self.table_matrix[0][i] != ' ':
                if rec == False: self.state = '{0} wins'.format(self.table_matrix[0][i])
                else: self.rec_state = '{0} wins'.format(self.table_matrix[0][i])
            #check diagonals
            elif self.table_matrix[0][0] == self.table_matrix[1][1] == self.table_matrix[2][2] and self.table_matrix[0][0] != ' ':
                if rec == False: self.state = '{0} wins'.format(self.table_matrix[0][0])
                else: self.rec_state = '{0} wins'.format(self.table_matrix[0][0])
            elif self.table_matrix[0][2] == self.table_matrix[1][1] == self.table_matrix[2][0] and self.table_matrix[0][2] != ' ':
                if rec == False: self.state = '{0} wins'.format(self.table_matrix[0][2])
                else: self.rec_state = '{0} wins'.format(self.table_matrix[0][2])
        
        cell_list = [cell for row in self.table_matrix for cell in row]
        if ' ' not in cell_list:
            if rec == False: self.state = 'Draw'
            else: self.rec_state = 'Draw'
        
    def get_random_move(self):
        move = random.choices(range(0,3), k=2)
        x, y = (move[0], move[1])
        while self.table_matrix[x][y] is not ' ': 
            move = random.choices(range(0,3), k=2)
            x, y = (move[0], move[1])
        return move
    
    def get_medium_move(self):
        table_matrix_T = list(zip(*self.table_matrix))
        move = [None, None]
        diagonals_col = {0:2, 1:1, 2:0}
        player_symbol = self.get_symbol()
        if player_symbol == 'X': opponent_symbol = 'O'
        else: opponent_symbol = 'X'

        for symbol in [player_symbol, opponent_symbol]:
            for i in range(0,3):
                #check rows 
                if self.table_matrix[i].count(symbol) == 2 and ' ' in self.table_matrix[i]:
                    move = [i, self.table_matrix[i].index(' ')] #the medium move that gets returned 
                #check columns
                elif table_matrix_T[i].count(symbol) == 2 and ' ' in table_matrix_T[i]:
                    move = [table_matrix_T[i].index(' '), i]
                #check diagonals
                elif [self.table_matrix[0][2], self.table_matrix[1][1], self.table_matrix[2][0]].count(symbol) == 2 and ' ' in [self.table_matrix[0][2], self.table_matrix[1][1], self.table_matrix[2][0]]:
                    x = [self.table_matrix[0][2], self.table_matrix[1][1], self.table_matrix[2][0]].index(' ')
                    y = diagonals_col[x]
                    move = [x, y]
                elif [self.table_matrix[0][0], self.table_matrix[1][1], self.table_matrix[2][2]].count(symbol) == 2 and ' ' in [self.table_matrix[0][0], self.table_matrix[1][1], self.table_matrix[2][2]]:
                    x = [self.table_matrix[0][0], self.table_matrix[1][1], self.table_matrix[2][2]].index(' ')
                    y = x
                    move = [x, y]
            if isinstance(move[0], int) and isinstance(move[1], int): break #it means that AI can win 

        #Otherwise, it makes a random move.
        if isinstance(move[0], int) and isinstance(move[1], int): return move
        else: return self.get_random_move()

    def minimax(self, state, depth, player, AI_symbol): #1 = max # minimax

        if player == 1:
            best = [[None, None], -math.inf] #move and score
        else:
            best = [[None, None], math.inf]

        self.get_state(rec=True)
        if depth == 0 or self.rec_state != None:
            
            if self.rec_state == '{0} wins'.format(AI_symbol) : return [[None, None], +10]
            elif self.rec_state == 'Draw' : return [[None, None], 0]
            else: return [[None, None], -10]
        
        for empty_cell in self.empty_cells():
            x, y = (empty_cell[0], empty_cell[1])
            self.insert_move(x, y)
            score = self.minimax(self.table_matrix, len(self.empty_cells()), -player, AI_symbol)
            self.table_matrix[x][y] = ' '
            score[0][0], score[0][1]= x, y
            self.rec_state = None

            if player == 1:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
            
        return best
        
    def empty_cells(self):
        empty_cells = []
        for row_i in range (0,3): #row indices
            col_i_l = [i for i, x in enumerate(self.table_matrix[row_i]) if x == ' ']
            for col_i in col_i_l:
                empty_cells.append([row_i, col_i])
        return empty_cells


    def make_player_move(self, player_move):
        self.check_move(player_move)
        if self.valid_move == True:
            self.print_table()

    def make_AI_move(self, difficulty):
        if difficulty == 'easy':
            print('Making move level "easy"')
            AI_move = self.get_random_move()
            x, y = (AI_move[0], AI_move[1])
            self.insert_move(x, y)
            self.print_table()
        elif difficulty == 'medium':
            print('Making move level "medium"')
            AI_move = self.get_medium_move()
            x, y = (AI_move[0], AI_move[1])
            self.insert_move(x, y)
            self.print_table()
        elif difficulty == 'hard':
            print('Making move level "hard"')
            if len(self.empty_cells()) == 9 : 
                AI_move = self.get_random_move()
            else:
                AI_move = self.minimax(self.table_matrix, len(self.empty_cells()), 1, self.get_symbol())[0]
            x, y = (AI_move[0], AI_move[1])
            self.insert_move(x, y)
            self.print_table()

        #print(self.table_matrix[:][1])
    def check_command(self, command):
        if len(command) == 3 and command[0] == 'start' and command[1] in ['easy', 'medium', 'hard', 'user'] and command[2] in ['easy', 'medium', 'hard', 'user'] : self.command = command
        elif len(command) == 1 and command[0] == 'exit' : self.command = 'exit'
        else: print('Bad parameters!')

    def play_game(self, command):
        self.print_table()
        while self.state not in ['X wins', 'O wins', 'Draw']:
            for player in command: #loop through the players, it can be 'user' or 'easy'. each loop represents one move (either AI or user)
                if player == 'user':
                    while self.valid_move == False:
                        player_move = input('Enter the coordinates:').split()
                        self.make_player_move(player_move)
                    self.valid_move = False
                elif player in ['easy', 'medium', 'hard']:
                    self.make_AI_move(player)
                self.get_state(rec=False)
                if self.state in ['X wins', 'O wins', 'Draw']: break
        print(self.state)

def main():
    game = Game()

    while game.command != 'exit' :
        game= Game()
        command = input('Input command:').split()
        game.check_command(command)
    
        if game.command not in ['exit', None] : game.play_game(command)
        else: continue

if __name__ == "__main__":
    main()
