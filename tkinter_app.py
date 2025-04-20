import tkinter as tk

database = {}

def register():
    rwindow = tk.Toplevel(root)
    rwindow.title("Register")
    rwindow.geometry("300x300")
    
    tk.Label(rwindow, text="Register",bg="green",fg="white", font=("Arial", 14,"bold")).pack(pady=10)
    tk.Label(rwindow, text="Login",font=("Arial", 12)).pack(pady=5)
    reentry = tk.Entry(rwindow)
    reentry.pack(pady=5)
    
    tk.Label(rwindow, text="Password",font=("Arial", 12)).pack(pady=5)
    reentry1 = tk.Entry(rwindow, show="*")
    reentry1.pack(pady=5)

    def handle_register():
        login = reentry.get()
        password = reentry1.get()
        if login and password:
            if login in database:
                tk.Label(rwindow, text="User already exists", fg="red").pack(pady=5)
            else:
                database[login] = password
                tk.Label(rwindow, text="Registered successfully", fg="green").pack(pady=5)
                rwindow.after(2000, rwindow.destroy)
        else:
            tk.Label(rwindow, text="Please enter login and password", fg="red").pack(pady=5)

    tk.Button(rwindow, text="Register", command=handle_register).pack(pady=10)

def login():
    lwindow = tk.Toplevel(root)
    lwindow.title("Login")
    lwindow.geometry("300x300")
    
    tk.Label(lwindow, text="Login",bg="blue",fg="white", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(lwindow, text="Login",font=("Arial", 12)).pack(pady=5)
    leentry = tk.Entry(lwindow)
    leentry.pack(pady=5)
    
    tk.Label(lwindow, text="Password",font=("Arial", 12)).pack(pady=5)
    leentry1 = tk.Entry(lwindow, show="*")
    leentry1.pack(pady=5)

    def handle_login():
        login = leentry.get()
        password = leentry1.get()
        if login and password:
            if login in database and database[login] == password:
                tk.Label(lwindow, text="Login successful", fg="green").pack(pady=5)
                lwindow.after(2000, lwindow.destroy)
            else:
                tk.Label(lwindow, text="Invalid credentials", fg="red").pack(pady=5)
        else:
            tk.Label(lwindow, text="Please enter login and password", fg="red").pack(pady=5)

    tk.Button(lwindow, text="Submit", command=handle_login).pack(pady=10)

def exit1():
    exwindow = tk.Toplevel(root)
    exwindow.title("Exit")
    exwindow.geometry("300x200")
    
    tk.Label(exwindow, text="Are you sure you want to exit?", font=("Arial", 12)).pack(pady=10)
    tk.Button(exwindow, text="Yes",bg="red",font=("Arial", 12),fg="white", command=root.destroy).pack(pady=5)
    tk.Button(exwindow, text="No",bg="green",font=("Arial", 12),fg="white", command=exwindow.destroy).pack(pady=5)


root = tk.Tk()
root.title("User Management")
root.geometry("300x300")

tk.Label(root, text="Welcome", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Register",bg="blue",fg="white",command=register).pack(pady=10)
tk.Button(root, text="Login",bg="green",fg="white", command=login).pack(pady=10)
tk.Button(root, text="Exit",bg="red",fg="white", command=exit1).pack(pady=10)

root.mainloop()