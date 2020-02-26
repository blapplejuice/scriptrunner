import tkinter as tk;
import libs as scriptrunner;

# put a 1 in the bool() to auto fill in password
autopassword = bool(1);



password = '';

root = tk.Tk();
root.title("unlocker");
frame = tk.Frame(root);
frame.pack();

def validate():
    password = "hackerman";  #password
    inputpassword = passbox.get();
    if(inputpassword == password):
        root.destroy();
        scriptrunner.tk();

def valid(event):
    validate();
    
root.bind('<Return>', valid)

disclaimertxt = "password";
if(autopassword):
    disclaimer = tk.Label(frame, text="autofilled, debug mode");
else:
    disclaimer = tk.Label(frame, text="password");
    
disclaimer.pack(side=tk.TOP);


passbox = tk.Entry(frame,
                       width=20,
                        show="★");
passbox.pack(side=tk.TOP);

validbtn = tk.Button(frame,
                     width=20,
                     text="unlock",
                     command=validate);
validbtn.pack(side=tk.BOTTOM);
if(autopassword):
    passbox.insert(0, "hackerman");
    print("auto password mode is on");
root.mainloop();
