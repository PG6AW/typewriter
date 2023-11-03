# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import getpass

# Copyright (C) 2023 Mohammad Dorri https://www.github.com/PG6AW

conn = sqlite3.connect("accounts.db")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
cursor = conn.cursor()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
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

proceed = messagebox.askyesno("Confirmation", "The use of this mode is only granted to Managers or Supervisors!\nThis work must be limited in private access, only and only to the Managers and Supervisors in a local network as it can compromise user security.\n\nIF you are not a system Manager or not working as a supervisor, it's kindly requested to refrain from using this tool or even tampering with it!\n\n/Tap 'YES' if you are working as a Manager or a Supervisor /\n/Tap 'NO' if you are appointed as neither of the positions mentioned! /")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
if proceed:
    pass
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
else:
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    conn.close()
    exit()

def reset_password():
    username = username_entry.get()
    # Copyright (C) [2023]  [Mohammad Dorri]
    # https://www.github.com/PG6AW
    username = str(username)
    # Copyright  (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    if username == "":
        messagebox.showerror("Error", "Please input a username first!")
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        return
    else:
        pass
    query1 = "SELECT username FROM register"
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    query2 = "UPDATE register SET password=? WHERE username=?"
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    conn = sqlite3.connect("accounts.db")
    # Copyright (C)  [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor = conn.cursor()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor.execute(query1)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    usernames = cursor.fetchall()
    # Copyright  (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    if usernames is None:
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        usernames = str(usernames)
    else:
        usernames = list(usernames)
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
    if (f"('{username}',)") not in str(usernames):
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        messagebox.showerror("Error", "This username doesn't exist!\nPlease input a correct one that already exists in the local database.")
        return
    else:
        pass
    confirmation = messagebox.askyesno("Confirmation", "Do you confirm to reset user's password to '12345678'?")
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    if confirmation:
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        pass
    else:
        return
    cursor.execute(query2, ("12345678", username,))
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor.execute("""CREATE TABLE IF NOT EXISTS log_pass_reset_by_supervisors (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   password_reset TEXT,
                   event_by_admin TEXT,
                   event_date TEXT
    )               
    """)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    admins_account = getpass.getuser()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor.execute("INSERT INTO log_pass_reset_by_supervisors (username, password_reset, event_by_admin, event_date) VALUES (?, ?, ?, ?)", (username, "True", admins_account, datetime.datetime.now()))
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    messagebox.showinfo("Success!", f"User: {username}'s Password has been successfully reset to the literal value of '12345678'!\nMake sure to remind them to later change their password to something secure!")

def close_it():
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    confirm_close = messagebox.askyesno("Confirm", "Do you wish to close the current window?")
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    if confirm_close:
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        pass
    else:
        return
    conn.close()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    supervision.destroy()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    exit()

supervision = tk.Tk()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
supervision.configure(bg="#222222")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
supervision.geometry("1000x425")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
supervision.title("Password Reset Tool")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
supervision.resizable(False, False)

window_label = tk.Label(supervision, text="Reset Password  ", font="impact 25 italic", bg="orange")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
username_label = tk.Label(supervision, text="Enter a Username:", font="arial 24 italic", width=28, bg="yellow", fg="blue")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
username_entry = tk.Entry(supervision, font="lotus 20 bold", width=60, bg="lightblue", fg="darkgreen", justify="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
reset_button = tk.Button(supervision, text="Reset", font="arial 18 bold", width=15, height=2, bg="#00ff00", relief="groove", fg="darkblue", command=reset_password)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
exit_button = tk.Button(supervision, text="EXIT!", width=10, font="arial 10 italic", relief="ridge", bg="red", fg="yellow", command=close_it)

window_label.pack(pady=35)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
username_label.pack(pady=10)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
username_entry.pack(pady=5)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
reset_button.pack(pady=20)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
exit_button.pack(pady=20)

supervision.mainloop()
conn.close()