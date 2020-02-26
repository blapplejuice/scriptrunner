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
    
    def showchoice():
        choice = v.get();
        print("Method: ")
        if(choice == 1):
            print("Windows");
        elif(choice == 2):
            print("Linux")

    def close():
        root.destroy();

    def linuxrun(script):
        name = "a";
        print("Running script in Linux mode.");
        f= open(name + ".txt","w+");

    def process():
        script = pad.get("1.0",'end-1c');
        print('Script:\n\n')
        print(script + '\n\n');
        showchoice();



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
