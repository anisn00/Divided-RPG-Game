import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
from subprocess import call
import tkinter as tk
from tkinter import PhotoImage
import ctypes

app = customtkinter.CTk()
app.title('Game Account')
app.geometry('800x600')
app.config(bg='#001220')


try:
    app.iconbitmap("logo_task.ico")
except Exception as e:
    print("Error:", e)
    
    
def app_intro():
    call(["python", "app_intro.py"])

app_intro()

def set_taskbar_icon(window_handle, icon_path):
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        ctypes.windll.user32.SendMessageW(window_handle, 0x80, 0, icon_path)
    except Exception as e:
        print("Error setting taskbar icon:", e)

window_handle = app.winfo_id()

set_taskbar_icon(window_handle, "logo_task.ico")


font1 = ('Helvitica', 25,'bold')
font2 = ('Arial', 17,'bold')
font3 = ('Arial', 13,'bold')
font4 = ('Arial', 13,'bold','underline')

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username Already Exists.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username, hashed_password])
            connect.commit()
            messagebox.showinfo('Success', 'Account has been created')
    else:
        messagebox.showerror('Error', 'Enter All Data')

def open_game_file():
    app.withdraw()
    call(["python", "game_intro.py"])
    app.destroy()
        
def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            stored_password_bytes = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_bytes):
                messagebox.showinfo('Success', 'Logged in successfully.')
                open_game_file() 
            else:
                messagebox.showerror('Error', 'Invalid password.')
        else:
            messagebox.showerror('Error', 'Invalid username.')
    else:
        messagebox.showerror('Error','Enter all data.')



def login():
    global frame1
    frame1.destroy()
    global frame2
    frame2 = customtkinter.CTkFrame(app,bg_color='#001220',fg_color='#001220',width=1000,height=810)
    frame2.place(x=0,y=0)
    
    image1 = PhotoImage(file = "l.png")
    image1_label = Label(frame2,image=image1,bg='#001220')
    image1_label.place(x=4,y=60)
    frame2.image1 = image1
    
    login_label2 = customtkinter.CTkLabel(frame2,font=font1,text='Log in',text_color='#fff',bg_color='#001220')
    login_label2.place(x=550,y=20)
    
    global username_entry2
    global password_entry2
    
    username_entry2 = customtkinter.CTkEntry(frame2,font=font2,text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Username',placeholder_text_color='#a3a3a3',width=200,height=50)
    username_entry2.place(x=550,y=120)
    
    password_entry2 = customtkinter.CTkEntry(frame2,font=font2,show = '*',text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Password',placeholder_text_color='#a3a3a3',width=200,height=50)
    password_entry2.place(x=550,y=200)
    
    login_button2 = customtkinter.CTkButton(frame2,command=login_account,font=font2,text_color='#fff',text='Log In',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor ='hand2',corner_radius=5,width=120)
    login_button2.place(x=550,y=280)
    
    # Add a back button
    back_button = customtkinter.CTkButton(frame2, command=show_frame1, font=font4, text_color='#fff', text='Back', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
    back_button.place(x=20, y=20)


def show_frame1():
    global frame2
    frame2.destroy()
    global frame1
    frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=1000, height=810)
    frame1.place(x=0, y=0)

    image1 = PhotoImage(file="l.png")
    image1_label = Label(frame1, image=image1, bg='#001220')
    image1_label.place(x=4, y=60)
    frame1.image1 = image1

    signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up', text_color='#fff', bg_color='#001220')
    signup_label.place(x=550, y=20)

    global username_entry
    global password_entry

    username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',border_color='#004780', border_width=3, placeholder_text='Username',placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry.place(x=550, y=120)

    password_entry = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e',bg_color='#121111', border_color='#004780', border_width=3,placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200,height=50)
    password_entry.place(x=550, y=190)

    signup_button = customtkinter.CTkButton(frame1, command=sign_up, font=font2, text_color='#fff', text='Sing up',fg_color='#00965d', hover_color='#006e44', bg_color='#121111',cursor='hand2', corner_radius=5, width=120)
    signup_button.place(x=550, y=280)

    login_label = customtkinter.CTkLabel(frame1, font=font3, text='Already have an account ?', text_color='#fff',bg_color='#001220')
    login_label.place(x=530, y=340)

    login_button = customtkinter.CTkButton(frame1, command=login, font=font4, text_color='#fff', text='Login',fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
    login_button.place(x=700, y=340)

frame1 = customtkinter.CTkFrame(app, bg_color='#001220',fg_color='#001220', width=1000, height=810)
frame1.place(x=0,y=0)

image1 = PhotoImage(file = "l.png")
image1_label = Label(frame1, image = image1, bg='#001220')
image1_label.place(x=4,y=60)

signup_label = customtkinter.CTkLabel(frame1, font = font1, text = 'Sign up',text_color='#fff', bg_color= '#001220')
signup_label.place(x=550,y=20)

username_entry = customtkinter.CTkEntry(frame1, font = font2, text_color = '#fff',fg_color = '#001a2e' ,bg_color = '#121111',border_color = '#004780',border_width=3, placeholder_text= 'Username', placeholder_text_color= '#a3a3a3', width = 200, height=50)
username_entry.place(x=550,y=120)

password_entry = customtkinter.CTkEntry(frame1, font = font2,show = '*' ,text_color = '#fff',fg_color = '#001a2e' ,bg_color = '#121111',border_color = '#004780',border_width=3, placeholder_text= 'Password', placeholder_text_color= '#a3a3a3', width = 200, height=50)
password_entry.place(x=550,y=190)


signup_button = customtkinter.CTkButton(frame1,command=sign_up ,font = font2, text_color = '#fff', text= 'Sing up', fg_color= '#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
signup_button.place(x=550,y=280)

login_label = customtkinter.CTkLabel(frame1, font = font3, text = 'Already have an account ?',text_color='#fff', bg_color= '#001220')
login_label.place(x=550,y=340)

login_button = customtkinter.CTkButton(frame1 ,command=login,font = font4, text_color = '#fff',text ='Login' ,fg_color = '#001220', hover_color='#001220', cursor = 'hand2', width=40)
login_button.place(x=700,y=340)


app.mainloop()
