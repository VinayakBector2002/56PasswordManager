from tkinter import *
import os
from PIL import ImageTk, Image
import pickle

def deleteMAIN ():
  screen.destroy()
def delete1():
  screen1.destroy()
def DeleteScreen2():
  screen2.destroy()

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
def Addpass():
  file=open(username1, "ab")
  a = AccDet.get()
  b = Accpass.get()
  d1 = {a:b}
  d= {}
  pickle.dump(d1, file)
  pickle.dump(d,file)
  file.close()
  Label(screen3, text = "Sucessfully stored the password for  "+a, fg = "white", bg="black").pack()

def Showpass():
  file=open(username1, "rb")
  while True:
    try:
      rec =pickle.load(file)
      Label(screen3, text = rec,fg = "white", bg="black" ).pack()
    except EOFError:
      break
    except pickle.UnpicklingError:
      continue
    
  file.close()
      

def NewAcc():
  global AccDet
  global Accpass
  AccDet = StringVar()
  Accpass = StringVar()

  Label(screen3, text = "Enter Account Details").pack()
  Acc_entry = Entry(screen3, textvariable = AccDet)
  Acc_entry.pack()
  Label(screen3, text = "", bg = "black").pack()
  
  Label(screen3, text = "Password").pack()
  Pass_entry = Entry(screen3, textvariable = Accpass)
  Pass_entry.pack()
  Label(screen3, text = "", bg = "black").pack()
  Button(screen3, text = "Add", command =Addpass).pack()
  Label(screen3, text = "", bg = "black").pack()
  


  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("500x500")
  screen3.configure(bg='black')
  Label(screen3, text = "", bg = "black" ).pack()
  Label(screen3, text = "", bg = "black" ).pack()
  Label(screen3, text = "Login Sucess").pack()
  Label(screen3, text = "", bg = "black" ).pack()
  Button(screen3, text = "Add New Password", command =NewAcc).pack()
  Label(screen3, text = "", bg = "black" ).pack()
  Button(screen3, text = "Show Password(s)", command =Showpass).pack()
  Label(screen3, text = "", bg = "black" ).pack()
  Button(screen3, text = "EXIT", command =delete2).pack()
  Label(screen3, text = "", bg = "black" ).pack()
  
  

  
def password_not_recognised():
  global screen4
  screen4.configure(bg='black')
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("300x300")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("user_not_found")
  screen5.geometry("150x100")
  screen5.configure(bg='black')
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info+"\n")
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green", bg="black" ,font = ("calibri", 11)).pack()

def login_verify():
  global username1
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    
    if password1 == verify[1]:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("500x500")
  screen1.configure(bg="black")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
  Label(screen1, text = "", bg ="black").pack()
  Label(screen1, text = "", bg ="black").pack()
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "", bg ="black").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "", bg ="black").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
  Label(screen1, text = "", bg ="black").pack()
  Label(screen1, text = "", bg ="black").pack()
  Label(screen1, text = "", bg ="black").pack()
  Button(screen1, text = "Go Back!", width = 10, height = 1, command = delete1).pack()  

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("500x500")
  screen2.configure(bg='black')
  Label(screen2, text = "", bg = "black").pack()
  Label(screen2, text = "", bg = "black").pack()
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "", bg = "black").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "", bg ="black").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "", bg = "black").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  Label(screen2, text = "", bg = "black").pack()
  Label(screen2, text = "", bg = "black").pack()
  Label(screen2, text = "", bg = "black").pack()
  Button(screen2, text = "Go Back!", width = 10, height = 1, command = DeleteScreen2).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.configure(bg='black')
  screen.geometry("1200x800")
  screen.title("PASSWORD MANAGER :P ")
  photo = ImageTk.PhotoImage(Image.open("PassBan3.jpg"))
  panel = Label(screen, image = photo)
  panel.pack()
  Label(text = "Welcome! Please select any one of the following options", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "",bg = "black").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "",bg = "black").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
  Label(text = "",bg = "black").pack()
  Button(text = "EXIT",height = "2", width = "30", command = deleteMAIN).pack()
  

  screen.mainloop()

main_screen()
  
