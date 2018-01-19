import tkinter

class Scribble:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500,
            height = 400,
            background = 'orange')
        self._canvas.bind('<Button-1>', self._button_down)
        self._canvas.bind('<ButtonRElease-1>', self._button_up)
        self._canvas.bind('<Motion>', self._mouse_moved)
        self._canvas.pack()

        self._button_is_down = False
        self._last_x = 0
        self._last_y = 0

    def run(self):
        self._root_window.mainloop()

    def button_down(self, event):
        self.button_is_down = True
        self.last_x = event.x
        self.last_y = event.y
        

        


