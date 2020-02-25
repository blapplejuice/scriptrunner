import tkinter as tk;

# put a 1 in the bool() to auto fill in password
autopassword = bool();



password = '12345!"£$%';

root = tk.Tk();
root.title("unlocker");
frame = tk.Frame(root);
frame.pack();

def validate(event):
    password = "hackerman";
    inputpassword = passbox.get();
    if(inputpassword == password):
        import two;
        root.destroy();
    
root.bind('<Return>', validate)

disclaimertxt = "password";
if(autopassword):
    disclaimer = tk.Label(frame, text="autofilled, debug mode");
else:
    disclaimer = tk.Label(frame, text="password");
    
disclaimer.pack(side=tk.TOP);


passbox = tk.Entry(frame,
                       width=20,
                        show="•");
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
