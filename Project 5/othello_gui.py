#othello_gui.py
#Udit Kaushik
#75825974

import othello_logic
import tkinter

class User_Input_Error(Exception):
    """
    Error raised when user's input doesn't match the criteria
    """
    pass

class Board:
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.configure(background = 'white')

        self._key = 0

        self._game_label = tkinter.Label(
            master = self._window,
            text = 'OTHELLO - FULL',
            font = ('Helvetica', 34))
        self._game_label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        self._canvas = tkinter.Canvas(
            master = self._window,
            width = 600,
            height = 600,
            background = 'green')
        self._canvas.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas2 = tkinter.Canvas(
            master = self._window,
            width = 600,
            height = 100,
            background = 'white')
        self._canvas2.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        cancel_frame = tkinter.Frame(master = self._canvas2)
        cancel_frame.grid(
            row = 0,
            column = 1,
            padx = 10,
            pady = 10)
        
        cancel_button = tkinter.Button(
            master = cancel_frame,
            text = 'CANCEL',
            font = ('Helvetica', 14),
            command = self.end)
        cancel_button.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        button_frame = tkinter.Frame(master = self._canvas2)
        button_frame.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 10)
        
        begin_button = tkinter.Button(
            master = button_frame,
            text = 'START GAME',
            font = ('Helvetica', 14),
            command = self.begin_button_pressed)
        begin_button.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        instruction_label = tkinter.Label(
            master = self._canvas2,
            text = 'PRESS START GAME TO ENTER PARAMETERS\nAND THEN CLICK ON THE BOARD TO PLACE INITIAL PIECES.',
            font = ('Helvetica', 14))
        instruction_label.grid(
            row = 0,
            column = 3,
            padx = 10,
            pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self.on_canvas_resized)
        self._canvas.bind('<Button-1>', self.on_canvas_clicked)

        self._window.rowconfigure(0, weight = 1)
        self._window.rowconfigure(1, weight = 3)
        self._window.columnconfigure(0, weight = 1)
        self._window.columnconfigure(1, weight = 1)
        self._window.columnconfigure(2, weight = 0)

    def on_canvas_resized(self, event: tkinter.Event) -> None:
        """
        Deals with the event of resizing.
        """
        self.create_board()
        
    def begin_button_pressed(self):
        """
        Brings up the parameter box for the game.
        """
        dialog = Dialog()
        dialog.show()
        self._column = dialog.get_column()
        self._row = dialog.get_row()
        self._player = dialog.get_player()
        self._win_condition = dialog.get_win_condition()

        self._parameter_list = []
        self._parameter_list.append(int(self._column))
        self._parameter_list.append(int(self._row))
        self._parameter_list.append(str(self._player))
        self._parameter_list.append(str(self._win_condition))
        self.user_check(self._parameter_list)
        self._move_list = []

        self._count = 0
        self.create_board()

    def create_board(self):
        """
        Creates the gui board.
        """
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_length = self._canvas.winfo_height()
        
        try:
            row = int(self._column)
            width_interval = canvas_width / row
            col = int(self._row)
            length_interval = canvas_length /col
            for i in range(row):
                temp_x1 = i * width_interval
                temp_x2 = temp_x1 + width_interval
                for j in range(col):
                    temp_y1 = j * length_interval
                    temp_y2 = temp_y1 + length_interval
                    self._canvas.create_rectangle(temp_x1, temp_y1, temp_x2, temp_y2)
                    
            if self._count == 0:
                pass
            else:
                for item in self._move_list:
                    self.draw_piece(item)
        except:
            pass

    def on_canvas_clicked(self, event: tkinter.Event) -> None:
        """
        Deals with the click point of the user.
        """
        canvas_width = self._canvas.winfo_width()
        canvas_length = self._canvas.winfo_height()
        
        try:
            row = int(self._column)
            width_interval = canvas_width / row
            col = int(self._row)
            length_interval = canvas_length /col

            click_x = int(event.x)
            click_y = int(event.y)

            cord_point_x = int(click_x/width_interval)
            cord_point_y = int(click_y/length_interval)

            temp = []
            temp_list = []
            temp.append(cord_point_x)
            temp.append(cord_point_y)
            temp.append(self._player)
            temp_list.append(temp)
            self._move_list.append(temp)

            self._count += 1

            if (self._key == 1) or (self._key == 2):
                u_in = []
                u_in.append(cord_point_y)
                u_in.append(cord_point_x)
                self._move_list = []
                
                self._move = self._b_struct.move(u_in)
                self._player = self._b_struct.current_player_move
                if self._move == 'VALID':
                    struct_list = []
                    for i in range(len(self._b_struct.current_board)):
                        for j in range(len(self._b_struct.current_board[i])):
                            if self._b_struct.current_board[i][j] == 'B' or self._b_struct.current_board[i][j] == 'W':
                                temp = []
                                temp.append(i)
                                temp.append(j)
                                temp.append(self._b_struct.current_board[i][j])
                                struct_list.append(temp)
                                self._move_list.append(temp)

                    for item in struct_list:
                        self.draw_piece(item)
                
                elif self._move == 'INVALID':
                    pass

                else:
                    struct_list = []
                    for i in range(len(self._b_struct.current_board)):
                        for j in range(len(self._b_struct.current_board[i])):
                            if self._b_struct.current_board[i][j] == 'B' or self._b_struct.current_board[i][j] == 'W':
                                temp = []
                                temp.append(i)
                                temp.append(j)
                                temp.append(self._b_struct.current_board[i][j])
                                struct_list.append(temp)
                                self._move_list.append(temp)

                    for item in struct_list:
                        self.draw_piece(item)
                

                self._board_list = self._b_struct.current_board
                self.update_canvas2()
                            
            elif self._key == 0:    
                self.draw_piece(temp)

        except:
            pass

    def draw_piece(self, temp_list: list):
        """
        Draws the actul pieces of the board
        """
        canvas_width = self._canvas.winfo_width()
        canvas_length = self._canvas.winfo_height()
        x = temp_list[0]
        y = temp_list[1]

        row = int(self._column)
        width_interval = canvas_width / row
        col = int(self._row)
        length_interval = canvas_length /col

        temp_x1 = (x) * width_interval
        temp_y1 = (y) * length_interval

        temp_x2 = (x+1) * width_interval
        temp_y2 = (y+1) * length_interval

        if temp_list[2] == 'B':
            color = 'black'
        elif temp_list[2] == 'W':
            color = 'white'

        self._canvas.create_oval(temp_x1, temp_y1,
                                 temp_x2, temp_y2,
                                 outline = 'black',
                                 fill = color)

        if self._key == 0:
            self.update_canvas2()
        

    def update_canvas2(self):
        """
        Updates the second canvas to properly display user's options during the game.
        """
        if self._count == 1:
            self._canvas2.delete(tkinter.ALL)
            self._player = self._parameter_list[2]
                        
            restart_button = tkinter.Button(
                master = self._canvas2,
                text = 'RESTART',
                font = ('Helvetica', 14),
                command = self.begin_button_pressed)
            restart_button.grid(
                row = 0,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
            black_button = tkinter.Button(
                master = self._canvas2,
                text = 'BLACK',
                font = ('Helvetica', 14),
                command = self.black_button_pressed)
            black_button.grid(
                row = 0,
                column = 1,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
            white_button = tkinter.Button(
                master = self._canvas2,
                text = 'WHITE',
                font = ('Helvetica', 14),
                command = self.white_button_pressed)
            white_button.grid(
                row = 0,
                column = 2,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
            ready_button = tkinter.Button(
                master = self._canvas2,
                text = 'READY',
                font = ('Helvetica', 14),
                command = self.ready_button_pressed)
            ready_button.grid(
                row = 0,
                column = 3,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        if self._key == 1:
            if self._player == 'B':
                player_turn = 'BLACK PLAYER TURN'
            elif self._player == 'W':
                player_turn = 'WHITE PLAYER TURN'
                
            self._canvas2.delete(tkinter.ALL)
            
            cancel_button = tkinter.Button(
                master = self._canvas2,
                text = 'END',
                font = ('Helvetica', 14),
                command = self.end)
            cancel_button.grid(
                row = 0,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
            player_label = tkinter.Label(
                master = self._canvas2,
                text = player_turn,
                font = ('Helvetica', 34))
            player_label.grid(
                row = 0,
                column = 1,
                columnspan = 3,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
            score = self._b_struct.score_counter(self._b_struct.current_board)
            score_str = 'W: {} B: {}'.format(score[0], score[1])
            score_label = tkinter.Label(
                master = self._canvas2,
                text = score_str,
                font = ('Helvetica', 34))
            score_label.grid(
                row = 0,
                column = 4,
                columnspan = 1,
                padx = 10,
                pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

            self._key = 2

        elif self._key == 2:
            self._canvas2.delete(tkinter.ALL)

            if self._move == 'WINNER: W':
                player_turn = 'WINNER: WHITE'
                cancel_button = tkinter.Button(
                    master = self._canvas2,
                    text = 'END',
                    font = ('Helvetica', 14),
                    command = self.end)
                cancel_button.grid(
                    row = 0,
                    column = 0,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                
                player_label = tkinter.Label(
                    master = self._canvas2,
                    text = player_turn,
                    font = ('Helvetica', 34))
                player_label.grid(
                    row = 0,
                    column = 1,
                    columnspan = 3,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

                score = self._b_struct.score_counter(self._b_struct.current_board)
                score_str = 'B: {} W: {}'.format(score[0], score[1])
                score_label = tkinter.Label(
                    master = self._canvas2,
                    text = score_str,
                    font = ('Helvetica', 34))
                score_label.grid(
                    row = 0,
                    column = 4,
                    columnspan = 1,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

            elif self._move == 'WINNER: B':
                player_turn = 'WINNER: BLACK'
                cancel_button = tkinter.Button(
                    master = self._canvas2,
                    text = 'END',
                    font = ('Helvetica', 14),
                    command = self.end)
                cancel_button.grid(
                    row = 0,
                    column = 0,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                
                player_label = tkinter.Label(
                    master = self._canvas2,
                    text = player_turn,
                    font = ('Helvetica', 34))
                player_label.grid(
                    row = 0,
                    column = 1,
                    columnspan = 3,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

                score = self._b_struct.score_counter(self._b_struct.current_board)
                score_str = 'B: {} W: {}'.format(score[0], score[1])
                score_label = tkinter.Label(
                    master = self._canvas2,
                    text = score_str,
                    font = ('Helvetica', 34))
                score_label.grid(
                    row = 0,
                    column = 4,
                    columnspan = 1,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

            elif self._move == 'WINNER: NONE':
                player_turn1 = 'WINNER: NONE'
                cancel_button = tkinter.Button(
                    master = self._canvas2,
                    text = 'END',
                    font = ('Helvetica', 14),
                    command = self.end)
                cancel_button.grid(
                    row = 0,
                    column = 0,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                
                player_label = tkinter.Label(
                    master = self._canvas2,
                    text = player_turn1,
                    font = ('Helvetica', 34))
                player_label.grid(
                    row = 0,
                    column = 1,
                    columnspan = 3,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

                score = self._b_struct.score_counter(self._b_struct.current_board)
                score_str = 'B: {} W: {}'.format(score[0], score[1])
                score_label = tkinter.Label(
                    master = self._canvas2,
                    text = score_str,
                    font = ('5', 34))
                score_label.grid(
                    row = 0,
                    column = 4,
                    columnspan = 1,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

            else:
                if self._player == 'B':
                    player_turn = 'BLACK PLAYER TURN'
                elif self._player == 'W':
                    player_turn = 'WHITE PLAYER TURN'

                player_turn = self._move + ', ' + player_turn
                
                cancel_button = tkinter.Button(
                    master = self._canvas2,
                    text = 'END',
                    font = ('Helvetica', 14),
                    command = self.end)
                cancel_button.grid(
                    row = 0,
                    column = 0,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                
                player_label = tkinter.Label(
                    master = self._canvas2,
                    text = player_turn,
                    font = ('Helvetica', 34))
                player_label.grid(
                    row = 0,
                    column = 1,
                    columnspan = 3,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

                score = self._b_struct.score_counter(self._b_struct.current_board)
                score_str = 'B: {} W: {}'.format(score[0], score[1])
                score_label = tkinter.Label(
                    master = self._canvas2,
                    text = score_str,
                    font = ('Helvetica', 34))
                score_label.grid(
                    row = 0,
                    column = 4,
                    columnspan = 1,
                    padx = 10,
                    pady = 10,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

    def black_button_pressed(self):
        """
        Switches the color for initial placement
        """
        self._player = 'B'

    def white_button_pressed(self):
        """
        Switches the color for initial placement
        """
        self._player = 'W'

    def create_logic_board(self):
        """
        Creates the logic board to ease the transition from gui to logic.
        """
        self._board_list = []
        for i in range(int(self._column)):
            temp = []
            for j in range(int(self._row)):
                temp.append('.')
            self._board_list.append(temp)

        for item in self._move_list:
            self._board_list[int(item[0])][int(item[1])] = item[2]
                
        self._parameter_list.append(self._board_list)
        self._b_struct = othello_logic.board_structure(self._parameter_list)

    def clean_list(self):
        """
        Removes extra points from the possible list.
        """
        temp = []
        for item in self._move_list:
            if item not in temp:
                temp.append(item)
                
        self._move_list = temp

    def ready_button_pressed(self):
        """
        Begins the game with the parameters.
        """
        self.clean_list()
        self.create_logic_board()
        self._key = 1

        self._player = self._parameter_list[2]

        self.update_canvas2()
        

    def user_check(self, u_in: list) -> None:
        """
        Checks whether user_defined entries are valid
        """

        if (u_in[0] % 2 == 0) and (4 <= u_in[0] <= 16):
            pass
        else:
            self.end()
            raise User_Input_Error()

        if (u_in[1] % 2 == 0) and (4 <= u_in[1] <= 16):
            pass
        else:
            self.end()
            raise User_Input_Error()

        if (u_in[2] == 'B') or (u_in[2] == 'W'):
            pass
        else:
            self.end()
            raise User_Input_Error()

        if (u_in[3] == '>') or (u_in[3] == '<'):
            pass
        else:
            self.end()
            raise User_Input_Error()

    def run(self):
        """
        Runs the game.
        """
        self._window.mainloop()

    def end(self):
        """
        Terminates the game.
        """
        self._window.destroy()

        


class Dialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        
        dialog_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Game Parameters',
            font = ('Helvetica', 16))
        dialog_label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10)
        
        column_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Enter Column (must be even number between 4 and 16): ',
            font = ('Helvetica', 16))
        column_label.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = 10,
            sticky = tkinter.W)
        self._column = tkinter.Entry(
            master = self._dialog_window,
            width = 20,
            font = ('Helvetica', 16))
        self._column.grid(
            row = 1,
            column = 1,
            padx = 10,
            pady = 5,
            sticky = tkinter.W + tkinter.E)

        row_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Enter Rows (must be even number between 4 and 16): ',
            font = ('Helvetica', 16))
        row_label.grid(
            row = 2,
            column = 0,
            padx = 10,
            pady = 10,
            sticky = tkinter.W)
        self._row = tkinter.Entry(
            master = self._dialog_window,
            width = 20,
            font = ('Helvetica', 16))
        self._row.grid(
            row = 2,
            column = 1,
            padx = 10,
            pady = 5,
            sticky = tkinter.W + tkinter.E)

        player_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Enter player who moves first (B or W): ',
            font = ('Helvetica', 16))
        player_label.grid(
            row = 3,
            column = 0,
            padx = 10,
            pady = 10,
            sticky = tkinter.W)
        self._player = tkinter.Entry(
            master = self._dialog_window,
            width = 20,
            font = ('Helvetica', 16))
        self._player.grid(
            row = 3,
            column = 1,
            padx = 10,
            pady = 5,
            sticky = tkinter.W + tkinter.E)

        win_condition_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Enter Win Condition (> or <): ',
            font = ('Helvetica', 16))
        win_condition_label.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 10,
            sticky = tkinter.W)
        self._win_condition = tkinter.Entry(
            master = self._dialog_window,
            width = 20,
            font = ('Helvetica', 16))
        self._win_condition.grid(
            row = 4,
            column = 1,
            padx = 10,
            pady = 5,
            sticky = tkinter.W + tkinter.E)

        enter_frame = tkinter.Frame(master = self._dialog_window)
        enter_frame.grid(
            row = 5,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = tkinter.E + tkinter.S)
        enter_button = tkinter.Button(
            master = enter_frame,
            text = 'ENTER!',
            font = ('Helvetica', 16),
            command = self.on_enter)
        enter_button.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 10)
    
    def on_enter(self) -> None:
        """
        Enters the dialog.
        """
        self._column = self._column.get()
        self._row = self._row.get()
        self._player = self._player.get()
        self._win_condition = self._win_condition.get()
        self._dialog_window.destroy()

    def show(self) -> None:
        """
        Displays the dialog window first.
        """
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def get_column(self) -> int:
        """
        Gets the column from parameter entries.
        """
        return self._column

    def get_row(self) -> int:
        """
        Gets rows from parameter entries.
        """
        return self._row
    
    def get_player(self) -> str:
        """
        Gets player move from parameter entries.
        """
        return self._player

    def get_win_condition(self) -> str:
        """
        Gets win condition from parameter entries.
        """
        return self._win_condition
        
def main():
    board = Board()
    board.run()

main()
    
