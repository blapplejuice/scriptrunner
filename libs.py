from tkinter import *;

def tk():

    root = Tk();
    frame = Frame(root);
    v = IntVar();
    v.set(1);
    os= [
        ("Windows", 1),
        ("Linux", 2)
    ]
    
    def close():
        root.destroy();
    
    def process():
        script = pad.get();


    frame.pack();
    root.title("scriptrunner");

    exitbtn = Button(frame,
                    width=50,
                    text="Exit",
                    command=close);
    exitbtn.pack(side=TOP);
    
    pad = Text(frame,
                width=50);
    pad.pack();

    windowsradio = Radiobutton(frame,
                            text="Windows",
                            variable=v,
                            value=1);
    windowsradio.pack(side=BOTTOM);

    linuxradio = Radiobutton(frame,
                            text="Linux",
                            variable=v,
                            value=2);
    linuxradio.pack(side=BOTTOM);

    osinfo = Label(frame,
                    text="Operating System",
                    justify=LEFT)
    osinfo.pack(side=BOTTOM)

    processbtn = Button(frame,
                        width=50,
                        text="Process",
                        command=process);
    processbtn.pack(side=BOTTOM)


    root.mainloop();
