""" 
Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
 """

# The initiative piece of the project, the first file that opens up in order for users to login and use the project (Login Tool):

import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import subprocess
import getpass
import random
import platform
os_name = platform.system()
if os_name == "Windows":
    import ctypes

# Copyright (C) 2023 Mohammad Dorri https://www.github.com/PG6AW

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
cursor.execute("""CREATE TABLE IF NOT EXISTS register (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               gender TEXT,
               birth_year INTEGER,
               birth_month TEXT,
               birth_day INTEGER,
               email TEXT,
               username TEXT UNIQUE,
               password TEXT,
               event_by_admin TEXT,
               register_date TEXT
)
""")
conn.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS login_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT,
            email TEXT,
            os_name TEXT,
            event_by_admin TEXT,
            login_date TEXT
)
""")
conn.commit()

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
cursor.execute("""CREATE TABLE IF NOT EXISTS captcha (captcha TEXT)""")
conn.commit()

try:
    cursor.execute("DELETE FROM captcha")
    conn.commit()
except sqlite3.OperationalError:
    pass

def recaptcha():
    c_entry1.delete(0, tk.END)
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    cursor.execute("""CREATE TABLE IF NOT EXISTS captcha (captcha TEXT)""")
    conn.commit()
    cursor.execute("DELETE FROM captcha")
    conn.commit()
    captcha_text = ""
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    for _ in range(12):
        captcha_text += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=|/><,.?':;~0123456789")
    cursor.execute("INSERT INTO captcha (captcha) VALUES (?)", (captcha_text,))
    conn.commit()
    try:
        captcha_label1.configure(text=captcha_text)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    except NameError:
        pass
    return

def login():
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    username = username_entry_2.get()
    password = password_entry_2.get()
    capt1 = c_entry1.get()

    if username == "" or password == "":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showerror("Error", "Both fields must be filled in!")
        recaptcha()
        return
    
    if capt1 == "":
        cursor.execute("DELETE FROM captcha")
        conn.commit()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showerror("Captcha", "You also have to click the captcha button!\nThen you can fill the captcha field and continue!")
        recaptcha()
        return

    capt = str(1)
    cursor.execute("SELECT captcha FROM captcha")
    captcha = cursor.fetchone()
    if captcha is None:
        captcha = str(captcha)
    else:
        captcha = list(captcha)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        for capt in captcha:
            capt = str(capt)
    c_entry1.delete(0, tk.END)

    def check_user():
        try:
            try:
                try:
                    conn = sqlite3.connect("accounts.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT id FROM login_logs WHERE username=?", (username,))
                    Ids = cursor.fetchall()
                    if Ids is None:
                        Ids = str(Ids)
                    ids = max(Ids)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for Id in ids:
                        Id = int(Id)
                    cursor.execute("SELECT login_date FROM login_logs WHERE username=? AND id=?", (username, Id))
                    login_date = cursor.fetchone()
                    if login_date is None:
                        login_date = str(login_date)
                    else:
                        for date in login_date:
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                            date = str(date)
                    date = date[:19]
                    datetime_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                    current_datetime = datetime.datetime.now()
                    time_delta = current_datetime - datetime_date
                    time_delta = str(time_delta)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if time_delta[0] == "-":
                        ask = messagebox.askyesno("Faulty Timezone", "We have detected that your system's datetime is not well-adjusted to your network timezone!\nAre you sure your timezone is adjusted accordingly to your network?\n\n<<Apart from answering to this, Please also note that we're asking this to urge you to check your system's timezone and adjust it as it deems it necessary | You may also want to ignore this as you wish!>>")
                        if ask:
                            pass
                        else:
                            return "0"
                    if "days" in time_delta:
                        return
                    if time_delta[1] != ":":
                        if time_delta[0:2] == "00":
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                            pass
                        else:
                            return
                    else:
                        if time_delta[0] == "0":
                            pass
                        else:
                            return
                    start_index = int(0)
                    dot_index_end = time_delta.index(".")
                    sliced_delta = time_delta[start_index:dot_index_end]
                    rest = sliced_delta[sliced_delta.index(":")+1:]
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    minutes = int(sliced_delta[sliced_delta.index(":")+1:rest.index(":")+sliced_delta.index(":")+1])
                    random_set = list(set([rand for rand in range(15,31)]))
                    rand = int(random.choice(random_set))

                    if minutes < rand:
                        messagebox.showerror("Flood Detected", f"Please wait for {rand-minutes} minute(s)!\nAlso note that the duration in which you must wait can vary in your next try.\n\nIt's best to wait an hour after each successful login attempt from the current network/system/OS/account!")
                        cursor.execute("DELETE FROM captcha")
                        conn.commit()
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        return "0"
                except(ValueError , TypeError):
                    pass
            except UnboundLocalError:
                pass
        except sqlite3.OperationalError:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            pass
    if check_user() == "0":
        recaptcha()
        return
    else:
        pass

    if capt == capt1:
        cursor.execute("DELETE FROM captcha")
        conn.commit()
    else:
        messagebox.showerror("Captcha Error", "Wrong answer inputted! Please press the captcha button and type it down in the appropriate entry field and try submitting again!\n\nPlease also note that the captcha could have been revoked too!\nHence, try regenerating another one using the button below!")
        recaptcha()
        return
    try:
        cursor.execute("SELECT password FROM register WHERE username=?", (username,))
        correct_password = cursor.fetchone()
        if correct_password is None:
            correct_password = str(correct_password)
        else:
            correct_password = list(correct_password)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            for i in correct_password:
                i = str(i)
        try:
            if i == str(password):
                # username_entry_2.delete(0, tk.END)
                password_entry_2.delete(0, tk.END)
                confirm = messagebox.askyesno("Success", "You have been successfully authenticated!\n\n__EXIT THE AUTHENTICATOR AND OPEN THE TYPEWRITER APP?__")
                if confirm:

                    cursor.execute("SELECT name FROM register WHERE username=?", (username,))
                    name = cursor.fetchone()
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if name is None:
                        name = str(name)
                    else:
                        name = list(name)
                        for j in name:
                            j = str(j)

                    cursor.execute("SELECT email FROM register WHERE username=?", (username,))
                    email = cursor.fetchone()
                    if email is None:
                        email = str(email)
                    else:
                        # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        email = list(email)
                        for mail in email:
                            mail = str(mail)

                    conn = sqlite3.connect("accounts.db")
                    cursor = conn.cursor()
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    cursor.execute("""CREATE TABLE IF NOT EXISTS login_logs (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                username TEXT,
                                email TEXT,
                                os_name TEXT,
                                event_by_admin TEXT,
                                login_date TEXT
                    )
                    """)
                    conn.commit()
                    current_username = getpass.getuser()
                    event_by_admin = current_username
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    cursor.execute("INSERT INTO login_logs (name, username, email, os_name, event_by_admin, login_date) VALUES (?, ?, ?, ?, ?, ?)", (j, username, mail, platform.system(), event_by_admin, datetime.datetime.now()))
                    conn.commit()
                    conn.close()

                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    
                    open_it = True

                    conn2 = sqlite3.connect("accounts.db")
                    cursor2 = conn2.cursor()
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    cursor2.execute("""CREATE TABLE IF NOT EXISTS retry_cache (cache TEXT)""")
                    conn2.commit()
                    cursor2.execute("SELECT cache FROM retry_cache")
                    cache = cursor2.fetchall()
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if cache is None:
                        cache = str(cache)
                    else:
                        for val in cache:
                            val = str(val)
                            if "retried" in val:
                                open_it = False
                    cursor2.execute("DELETE FROM retry_cache")
                    conn2.commit()
                    # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                    conn2.close()

                    conn.close()
                    messagebox.showinfo(f"Welcome Message", f"Congratulations on your favorite brand-new typewriter and welcome to your first typing game dear {username}!")
                    if open_it:
                        subprocess.Popen(['python', 'Leons_Typewriter.py']) #You can modify the address to which user will be redirected!

                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
                    
                    window.destroy()
                else:
                    recaptcha()
                    return
            else:
                messagebox.showerror("Authetnication Error", "Wrong Credentials provided including the username and password!")
                recaptcha()
        except UnboundLocalError:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            messagebox.showerror("Invalid Username", "User doesn't exist in the local database!\n\nPLEASE REGISTER IF YOU HAVE NOT TRIED YET or ARE LEFT WITH NO ACCOUNT!")
            recaptcha()
            return
    except sqlite3.OperationalError:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showinfo("Fresh/Empty", "The database is fresh and empty!\nNobody has registered themselves yet!\n\nYou can be the first one though by firing the REGISTER button on the left hand side!")
        recaptcha()
        return

show_it = "no"
def show_entry_text():
    global show_it
    if show_it != "yes":
        password_entry_2.configure(show="")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        show_pass_button.configure(text="Hide", bg="#333333", fg="white")
        show_it = "yes"
    elif show_it == "yes":
        password_entry_2.configure(show="*")
        show_pass_button.configure(text="Show", bg="red", fg="yellow")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        show_it = "no"

def go_to_register():
    confirm = messagebox.askyesno("Confirmation", "Go to the register window?")
    if confirm:
        subprocess.Popen(['python', 'register.py'])
        # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        conn.close()
        window.destroy()
    else:
        return

def exit_button():
    confirm = messagebox.askyesno("Confirmation", "SURE TO EXIT THE AUTHENTICATOR?")
    if confirm:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        conn.close()
        window.destroy()
        exit()
    else:
        return

lightness = "bright"
def dark_bright():
    global lightness
    if lightness == "bright":
        window.configure(bg="#333333")
        login_frame.configure(bg="#333333")
        # Copyright  (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        hyphen_label.configure(bg="#333333")
        username_entry_2.configure(bg="lightblue")
        password_entry_2.configure(bg="#bbbbbb")
        caps_lock_label_left.configure(bg="#333333")
        caps_lock_label_right.configure(bg="#333333")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        brightness_button_left.configure(bg="orange", fg="darkgreen", text="Light ", width=3, font="arial 7 bold")
        brightness_button_right.configure(bg="orange", fg="darkgreen", text="Light ", width=3, font="arial 7 bold")
        captcha_label1.configure(bg="#333333")
        brightness_button_left.place(relx=0.022, rely=0.97, anchor=tk.N)
        brightness_button_right.place(relx=0.975, rely=0.97, anchor=tk.N)
        # Copyright (C)   [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        lightness = "dark"
    elif lightness == "dark":
        window.configure(bg="green")
        login_frame.configure(bg="green")
        hyphen_label.configure(bg="green")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        username_entry_2.configure(bg="white")
        password_entry_2.configure(bg="#dddddd")
        caps_lock_label_left.configure(bg="green")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        caps_lock_label_right.configure(bg="green")
        brightness_button_left.configure(bg="#333333", fg="orange", text="Dark", width=3, font="arial 7 bold")
        brightness_button_right.configure(bg="#333333", fg="orange", text="Dark", width=3, font="arial 7 bold")
        captcha_label1.configure(bg="green")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        brightness_button_left.place(relx=0.022, rely=0.97, anchor=tk.N)
        brightness_button_right.place(relx=0.975, rely=0.97, anchor=tk.N)
        lightness = "bright"

def check_caps_lock():
    keyboard_state = ctypes.windll.user32.GetKeyState(0x14)
    caps_lock_state = keyboard_state & 0x0001 != 0
    # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
    if caps_lock_state:
        caps_lock_label_left.configure(fg="red", text="CapsLock On!")
        caps_lock_label_right.configure(fg="red", text="CapsLock On!")
    else:
        caps_lock_label_left.configure(fg="green", text="")
        caps_lock_label_right.configure(fg="green", text="")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    window.after(150, check_caps_lock)

def generate_captcha():
    c_entry1.delete(0, tk.END)
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    cursor.execute("""CREATE TABLE IF NOT EXISTS captcha (captcha TEXT)""")
    conn.commit()
    cursor.execute("DELETE FROM captcha")
    conn.commit()
    captcha_text = ""
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    for _ in range(12):
        captcha_text += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=|/><,.?':;~0123456789")
    cursor.execute("INSERT INTO captcha (captcha) VALUES (?)", (captcha_text,))
    conn.commit()
    try:
        captcha_label1.config(text=captcha_text)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    except NameError:
        pass

window = tk.Tk()
window.configure(bg="green")
window.geometry("570x640")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
window.resizable(False, False)
window.title("Login")

login_frame = tk.Frame(window)
login_frame.configure(bg="green")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
login_frame.place(relx=0.5, rely=0.004, anchor=tk.N)

main_label_2 = tk.Label(login_frame, text="Login ", bg="orange", font="impact 18 italic")
username_label_2 = tk.Label(login_frame, text="Enter your Username: ", font="arial 15 bold", bg="yellow")
username_entry_2 = tk.Entry(login_frame, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge")
password_label_2 = tk.Label(login_frame, text="Enter your Password: ", font="arial 15 bold", bg="yellow")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
password_entry_2 = tk.Entry(login_frame, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge", show="*", bg="#dddddd")
submit_button2 = tk.Button(window, cursor="hand1", text="Login! - >", command=login, font="arial 15 bold", bg="blue", fg="yellow", relief="raised")
quit_button = tk.Button(window, cursor="hand1", text="QUIT ", font="lotus 9 italic", bg="red", fg="darkblue", command=exit_button, relief="ridge")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
go_to_register_button = tk.Button(window, cursor="hand1", text="REGISTER", command=go_to_register, font="arial 15 italic", bg="darkblue", fg="yellow", relief="ridge")
hyphen_label = tk.Label(window, text="|  |", font="arial 15 bold", bg="green", fg="orange")
show_pass_button = tk.Button(window, cursor="hand1", text="Show", command=show_entry_text, font="arial 8 bold", bg="red", fg="yellow", width=4, relief="groove")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
show_pass_button.place(relx=0.92, rely=0.35, anchor=tk.N)

brightness_button_left = tk.Button(window, cursor="hand1", text="Dark", bg="#333333", fg="orange", font="arial 7 bold", width="3", relief="groove", command=dark_bright)
brightness_button_right = tk.Button(window, cursor="hand1", text="Dark", bg="#333333", fg="orange", font="arial 7 bold", width="3", relief="groove", command=dark_bright)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
brightness_button_left.place(relx=0.022, rely=0.97, anchor=tk.N)
brightness_button_right.place(relx=0.975, rely=0.97, anchor=tk.N)

caps_lock_label_left = tk.Label(window, text="", bg="green", fg="green", font="arial 10 bold", height=1, width=11)
caps_lock_label_right = tk.Label(window, text="", bg="green", fg="green", font="arial 10 bold", height=1, width=11)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
caps_lock_label_left.place(relx=0.18, rely=0.282, anchor=tk.N)
caps_lock_label_right.place(relx=0.82, rely=0.282, anchor=tk.N)
if os_name == "Windows":
    check_caps_lock()

c_label1 = tk.Label(login_frame, text="Solve the Captcha: ", bg="orange", fg="black", font="arial 15 bold", width=33)
c_entry1 = tk.Entry(login_frame, fg="blue", bg="lightblue", font="arial 18 italic", justify="center", width=23)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
captcha_label1 = tk.Label(login_frame, font=("segoe script", 23), width=16, relief="raised", bg="green", borderwidth=1, fg="#00ff00", height=1)
generate_button1 = tk.Button(login_frame, cursor="hand1", text="Generate Another!\n&\ninput below:", width=30, command=generate_captcha, bg="#00ff00", fg="blue", font="arial 10 bold", relief="groove")

recaptcha()

main_label_2.pack(pady=18)
username_label_2.pack(pady=10)
username_entry_2.pack(pady=5)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
password_label_2.pack(pady=10)
password_entry_2.pack(pady=5)
c_label1.pack(pady=20)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
captcha_label1.pack(pady=5)
generate_button1.pack(pady=15)
c_entry1.pack(pady=5)

submit_button2.place(relx=0.647, rely=0.85, anchor=tk.N)
quit_button.place(relx=0.5, rely=0.94, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
go_to_register_button.place(relx=0.343, rely=0.85, anchor=tk.N)
hyphen_label.place(relx=0.5, rely=0.86, anchor=tk.N)

window.mainloop()
conn.close()
exit()