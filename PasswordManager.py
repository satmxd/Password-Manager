import tkinter as tk
from tkinter.font import BOLD
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import simpledialog


from ast import Pass
from cryptography.fernet import Fernet


password = {
    "email": "qwerty",
    "youtube": "qwerty"
}


class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self):
        path = filedialog.askopenfile(initialdir= (".//"))
        print(path.name)
        print("path recognised")
        self.key = Fernet.generate_key()
        with open(path.name, 'wb') as f:
            f.write(self.key)

    def load_key(self):
        path = filedialog.askopenfile(initialdir= (".//"))
        print(path.name)
        print("key recognised")
        with open(path.name, 'rb') as f:
            self.key = f.read()

    def create_password_file(self):
        path = filedialog.askopenfile(initialdir= (".//"))
        print(path.name)
        print("pw created")
        self.password_file = path.name
        initial_values = password
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
        
    def load_password_file(self):
        path = filedialog.askopenfile(initialdir= (".//"))
        print(path.name)
        print("pw loaded")
        self.password_file = path.name

        with open(path.name, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()


    def add_password(self, site = None, pw = None):
        if site != None and pw != None:
            print(site)
            print(pw)
            self.password_dict[site] = password
            print(password)
            if self.password_file is not None:
                with open(self.password_file, 'a+') as f:
                    encrypted = Fernet(self.key).encrypt(pw.encode())
                    f.write(site + ":" + encrypted.decode() + "\n")
        # else:
        #     site = simpledialog.askstring("Site", "Enter Site name: ")
        #     print(site)
        #     pw = simpledialog.askstring("Password", "Enter Password: ")
        #     print(pw)
            # self.password_dict[site] = pw
            # if self.password_file is not None:
            #     with open(self.password_file, 'a+') as f:
            #         encrypted = Fernet(self.key).encrypt(pw.encode())
            #         f.write(site + ":" + encrypted.decode() + "\n")


    def get_password(self):
        site = simpledialog.askstring("Site", "Which Site do you want the password for: ")
        print(site)
        return self.password_dict[site]


pm = PasswordManager()

class ManagerUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Password Manager")
         
        self.label = tk.Label(self.root, text = "Password Manager", font = ('Arial', 18, BOLD))
        self.label.pack(pady = 20)   

        self.entry_txt = tk.Entry(self.root)
        entry = self.entry_txt
        self.entry_txt.pack()


        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.pack()



    
        self.create_key = tk.Button(self.buttonframe, text = "Create Key", font = ('Arial', 14), command= pm.create_key)
        self.create_key.grid(row=0, column=0, padx = 20, pady = 15,  sticky = tk.W+tk.E)

        self.load_key = tk.Button(self.buttonframe, text = "Load Key", font = ('Arial', 14), command= pm.load_key)
        self.load_key.grid(row =0, column = 1, pady = 15, sticky = tk.W+tk.E)

        self.create_pw = tk.Button(self.buttonframe, text = "Create new Password", font = ('Arial', 14), command= pm.create_password_file)
        self.create_pw.grid(row =1, column = 0, padx = 20, pady = 15, sticky = tk.W+tk.E)

        self.load_pw = tk.Button(self.buttonframe, text = "Load existing Password", font = ('Arial', 14), command= pm.load_password_file)
        self.load_pw.grid(row =1, column = 1, pady = 15, sticky = tk.W+tk.E)

        self.add_pw = tk.Button(self.buttonframe, text = "Add new Password", font = ('Arial', 14), command= pm.add_password)
        self.add_pw.grid(row =2, column = 0, padx = 20, pady = 15, sticky = tk.W+tk.E)

        self.get_pw = tk.Button(self.buttonframe, text = "Get Password", font = ('Arial', 14), command=pm.get_password)
        self.get_pw.grid(row =2, column = 1, pady = 15, sticky = tk.W+tk.E)

        self.quit = tk.Button(self.buttonframe, text = "Quit", font = ('Arial', 14))
        self.quit.grid(row =3, column = 0, padx = 20, pady = 15, sticky = tk.W+tk.E)







        self.root.mainloop()

ui = ManagerUI()



# def main():
#     password = {
#         "email": "12345",
#         "ig": "12345"
#     }
    
#     pm = PasswordManager()

