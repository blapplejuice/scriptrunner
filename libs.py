from tkinter import *;
import random;
import string;
import os;

def tk():

    root = Tk();
    frame = Frame(root);
    v = IntVar();
    v.set(1);
    oses= [
        ("Windows", 1),
        ("Linux", 2)
    ]
    
    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase;
        return ''.join(random.choice(letters) for i in range(stringLength));

    def showchoice(script):
        choice = v.get();
        print("Method: ")
        if(choice == 1):
            print("Windows");
            windowsrun(script);
        elif(choice == 2):
            print("Linux")
            linuxrun(script);

    def close():
        root.destroy();

    def windowsrun(script):
        name = randomString(64);
        print("Running script in Linux mode.\n");
        print("generated file: " + name + ".bat")
        f= open(name + ".bat","x");
        f.write(script);
        f.close();
        log = os.popen(name + ".bat").read();
        pad.delete('1.0', END);
        pad.insert(1.0, log);
        os.remove(name + ".bat");

    def linuxrun(script):
        name = randomString(64);
        print("Running script in Linux mode.\n");
        print("generated file: " + name + ".sh")
        f= open(name + ".sh","x");
        f.write(script);
        f.close();

    def process():
        script = pad.get("1.0",'end-1c');
        print('Script:\n\n')
        print(script + '\n\n');
        showchoice(script);



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
