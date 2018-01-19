import tkinter

def show_gui() -> None:
    root_window = tkinter.Tk()
    button = tkinter.Button(
        master = root_window,
        text = 'Press me',
        font = ('Helvetica', 20),
        command = on_press)
    button.bind('<Enter>', on_mouse_enter)
    button.bind('<Leave>', on_mouse_exit)
    button.pack()
    root_window.mainloop()

def on_press() -> None:
    print('Button pressed')

def on_mouse_enter(event: tkinter.Event) -> None:
    event.widget['text'] = 'Mouse entered'

def on_mouse_exit(event: tkinter.Event) -> None:
    event.widget['text'] = 'MouseExit'

if __name__ == '__main__':
    show_gui()
