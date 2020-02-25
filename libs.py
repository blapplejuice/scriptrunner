from tkinter import *;

def tk():

    root = Tk();
    frame = Frame(root);
    
    def close():
        root.destroy();
    
    frame.pack();
    root.title("scriptrunner");

    button = Button(frame,
                    width=20,
                    text="Exit",
                    command=close);
    button.pack(side=TOP);

    root.mainloop();
