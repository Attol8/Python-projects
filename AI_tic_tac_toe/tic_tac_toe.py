import random
class Game:
    def __init__(self):
        self.table_str = None
        self.active = False
        self.table_matrix = None
        self.valid_move = False
        self.state = None

    def convert_to_matrix(self, table_str):
        first_row = [cell if cell != '_' else ' ' for cell in table_str[0:3]]
        second_row = [cell if cell != '_' else ' ' for cell in table_str[3:6]]
        third_row = [cell if cell != '_' else ' ' for cell in table_str[6:9]]
        self.table_matrix = [first_row, second_row, third_row]
    
    def get_matrix_coordinates(self, move):
        try:
            y = int(move[0]) - 1
            if int(move[2]) == 3 : x = 0
            elif int(move[2]) == 2 : x = 1
            elif int(move[2]) == 1 : x = 2
            else : x = int(move[2])

            return x, y
        
        except ValueError:
            return None, None

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
        valid_condition_1 = type(x) == int and type(y) == int

        if valid_condition_1 == False:
            print('You should enter numbers!')

        else:
            try:
                valid_condition_2 = x <= 2 and y >= 0
                valid_condition_3 = x <= 2 and y >= 0
                valid_condition_4 = self.table_matrix[x][y] == ' '
                conditions = [valid_condition_2, valid_condition_3, valid_condition_4]
                if all(conditions):
                    self.valid_move = True
                    self.insert_move(x, y)
                elif all(conditions[0:1]) == True and conditions[2] == False:
                    print('This cell is occupied! Choose another one!')
            
            except IndexError:
                print('Coordinates should be from 1 to 3!')
        
    def get_symbol(self):
        self.table_str = "".join([cell for row in self.table_matrix for cell in row])
        X_len, O_len = (0, 0)
        for cell in self.table_str:
            if cell == 'X': X_len += 1
            elif cell == 'O': O_len += 1

        if X_len == O_len: return 'X'
        else: return 'O'

    def get_state(self):

        for i in range(0, 3):
            #check rows
            if self.table_matrix[i][0] == self.table_matrix[i][1] == self.table_matrix[i][2] and self.table_matrix[i][0] != ' ':
                self.state = '{0} wins'.format(self.table_matrix[i][0])
            #check columns
            elif self.table_matrix[0][i] == self.table_matrix[1][i] == self.table_matrix[2][i] and self.table_matrix[0][i] != ' ':
                self.state = '{0} wins'.format(self.table_matrix[0][i])
            #check diagonals
            elif self.table_matrix[0][0] == self.table_matrix[1][1] == self.table_matrix[2][2] and self.table_matrix[0][0] != ' ':
                self.state = '{0} wins'.format(self.table_matrix[0][0])

            elif self.table_matrix[0][2] == self.table_matrix[1][1] == self.table_matrix[2][0] and self.table_matrix[0][2] != ' ':
                self.state = '{0} wins'.format(self.table_matrix[0][2])
        
        cell_list = [cell for row in self.table_matrix for cell in row]
        if ' ' not in cell_list:
            self.state = 'Draw'
        
    def get_random_move(self):
        while True: 
            move = random.choices(range(0,3), k=3)
            x, y = (move[0], move[2])
            valid_condition = self.table_matrix[x][y] == ' '
            if valid_condition == True:
                return move
                break

def main():
    game = Game()
    game.table_str = '_________'
    game.convert_to_matrix(game.table_str) #fill self.table_matrix

    game.print_table()
    
    while True:
        while game.valid_move == False:
            player_move = input('Enter the coordinates:')
            game.check_move(player_move)
            game.print_table()
            
        game.get_state() 
        if game.state in ['X wins', 'O wins', 'Draw'] : break

        #AI move
        print('Making move level "easy"')
        AI_move = game.get_random_move()
        x, y = (AI_move[0], AI_move[2])
        game.insert_move(x, y)
        game.print_table()

        game.get_state()
        if game.state in ['X wins', 'O wins', 'Draw'] : break
        game.valid_move = False

    print(game.state)

if __name__ == "__main__":
    main()
