import tkinter as tk


database = {}


def get_input():
    a = entry.get()
    if a == "1":
        
        rwindow = tk.Toplevel(root)
        rwindow.title("Register Window")
        rwindow.geometry("300x400")
        
        
        tk.Label(rwindow, text="Login").pack(pady=10)
        reentry = tk.Entry(rwindow)  
        reentry.pack(pady=10)
        
        
        tk.Label(rwindow, text="Password").pack(pady=10)
        reentry1 = tk.Entry(rwindow)
        reentry1.pack(pady=10)
        
        
        def register():
            login = reentry.get()  
            password = reentry1.get()  
            if login and password:
                database[login] = password   
                print(database)
                tk.Label(rwindow, text="registered successfully",fg="green").pack(pady=10)
                rwindow.after(3000,rwindow.destroy)
            else:
                print("Please enter both login and password.")  

       
        sbutton = tk.Button(rwindow, text="Register", command=register)
        sbutton.pack(pady=10)
    if a=="2":
        lwindow = tk.Toplevel(root)
        lwindow.title("Register Window")
        lwindow.geometry("300x400")
        
        
        tk.Label(lwindow, text="Login").pack(pady=10)
        lentry = tk.Entry(lwindow)  
        lentry.pack(pady=10)
        
        
        tk.Label(lwindow, text="Password").pack(pady=10)
        lentry1 = tk.Entry(lwindow)
        lentry1.pack(pady=10)
        def log():
            elogin=lentry.get()
            epassword=lentry1.get()
            if elogin in database and database[elogin]==epassword:
                tk.Label(lwindow, text="Login successful",fg="green").pack(pady=10)
                lwindow.after(10000,lwindow.destroy)
            else:
                tk.Label(lwindow, text="failed try again",fg="red").pack(pady=10)
        tk.Button(lwindow,text="submit",command=log).pack(pady=10)

    if a=="3":
        root.destroy()
root = tk.Tk()
root.title("Input Text Example")
root.geometry("500x500")

entry = tk.Entry(root)
entry.pack(pady=10)


button = tk.Button(root, text="Submit", command=get_input)
button.pack(pady=10)


label = tk.Label(root, text="1) Register\n2) Login\n3) Exit the website\n")
label.pack(pady=10)


root.mainloop()
