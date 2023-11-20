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

# Leaderboard GUI:

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import subprocess
import sqlite3
import getpass

# Copyright (C) 2023 Mohammad Dorri https://www.github.com/PG6AW

current_username = getpass.getuser()
event_by_admin = current_username
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
the_user = "*N-U-L-L*"
try:
    conn2 = sqlite3.connect("accounts.db")
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT id FROM login_logs WHERE event_by_admin=?", (event_by_admin,))
    Ids = cursor2.fetchall()
    if Ids is None:
        Ids = str(Ids)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    ids = max(Ids)
    for Id in ids:
        Id = int(Id)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor2.execute("SELECT username FROM login_logs WHERE id=?", (Id,))
    user_name = cursor2.fetchone()
    if user_name is None:
        user_name = str(user_name)
    else:
        for the_user in user_name:
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            the_user = str(the_user)
    conn2.close()
except (sqlite3.OperationalError , ValueError , sqlite3.ProgrammingError):
    pass

if the_user == "LOGGED->OUT" or the_user == "*N-U-L-L*":
    retry = True
    while retry:
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        retry = messagebox.askretrycancel("LOGGED OUT!", "You are currently Logged Out!\n\nYOU'D BE BETTER OFF CANCELLING THIS & LOG-IN FIRST BEFORE YOU COME BACK & RETRY!")
    subprocess.Popen(['python', 'login.py'])
    exit()
else:
    pass

conn5 = sqlite3.connect("leaderboard.db")
cursor5 = conn5.cursor()
window = tk.Tk()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
window.title("Real-Time Records LeaderBoard")
window.geometry("1600x880")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
window.configure(bg="#011042")
window.resizable(False,False)

image = Image.open("Additional/typewriter2.jpg")
background_image = ImageTk.PhotoImage(image)
# Copyright (C) [2023]  [Mohammad Dorri]
# https://www.github.com/PG6AW
background_label1 = tk.Label(window, image=background_image)
# Copyright  (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
background_label2 = tk.Label(window, image=background_image)
background_label1.place(relx=0.0, rely=0.0)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
background_label2.place(relx=0.5, rely=0.0)

records_frame = ttk.Frame(window, padding="10")
records_frame.pack(side="top", pady=140, padx=160)
# Copyright (C) [2023]  [Mohammad Dorri]
# https://www.github.com/PG6AW
records_label = ttk.Label(records_frame, text="L E A D E R B O A R D", font="impact 30 bold", foreground="darkblue", background="lightblue")
records_label.pack(side="top", pady=10)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_scrollbar2_frame = ttk.Frame(records_frame)
records_scrollbar2_frame.pack(side="bottom", fill="x")

records_scrollbar2 = ttk.Scrollbar(records_scrollbar2_frame, orient="horizontal")
records_scrollbar2.grid(row=0, column=0, sticky="ew", ipadx=600)

records_scrollbar = ttk.Scrollbar(records_frame)
records_scrollbar.pack(side="right", fill="y")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview = ttk.Treeview(records_frame, yscrollcommand=records_scrollbar.set, xscrollcommand=records_scrollbar2.set, height=20)
records_treeview.pack(side="left", fill="both", expand=True)

records_scrollbar.configure(command=records_treeview.yview)
records_scrollbar2.configure(command=records_treeview.xview)

records_treeview["columns"] = ("COMPETITIVE POSITION", "RECORD ID", "USERNAME", "TOTAL SCORE", "NET WPM", "GROSS WPM", "PURE WPM", "ACCURACY", "CORRECT CHARACTERS", "TOTAL KEYSTROKES", "CORRECT KEYSTROKES", "INCORRECT KEYSTROKES", "TIME IN MINUTES", "EXTENDED SECONDS", "TOTAL MINUTES", "TYPED WORDS", "CORRECT WORDS", "INCORRECT WORDS", "POSITIVE POINTS", "NEGATIVE POINTS", "ALL KEYS PRESSED", "INTERRUPTED", "IDLE", "CHALLENGE MODE", "TYPEWRITER MODE", "NET CPM", "KPM", "KPH", "KEYBOARD LAYOUT", "KEYBOARD KEYS USED", "KEYBOARD KEYS", "OS NAME", "OS ADMIN", "EVENT DATE")
records_treeview.column("#0", width=0, stretch="no")
records_treeview.column("COMPETITIVE POSITION", width=200, anchor="center")
records_treeview.column("RECORD ID", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("USERNAME", width=100, anchor="center")
records_treeview.column("TOTAL SCORE", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("NET WPM", width=100, anchor="center")
records_treeview.column("GROSS WPM", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("PURE WPM", width=100, anchor="center")
records_treeview.column("ACCURACY", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("CORRECT CHARACTERS", width=200, anchor="center")
records_treeview.column("TOTAL KEYSTROKES", width=200, anchor="center")
records_treeview.column("CORRECT KEYSTROKES", width=200, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("INCORRECT KEYSTROKES", width=200, anchor="center")
records_treeview.column("TIME IN MINUTES", width=200, anchor="center")
records_treeview.column("EXTENDED SECONDS", width=200, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("TOTAL MINUTES", width=100, anchor="center")
records_treeview.column("TYPED WORDS", width=100, anchor="center")
records_treeview.column("CORRECT WORDS", width=150, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("INCORRECT WORDS", width=150, anchor="center")
records_treeview.column("POSITIVE POINTS", width=200, anchor="center")
records_treeview.column("NEGATIVE POINTS", width=200, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("ALL KEYS PRESSED", width=200, anchor="center")
records_treeview.column("INTERRUPTED", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("IDLE", width=100, anchor="center")
records_treeview.column("CHALLENGE MODE", width=150, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("TYPEWRITER MODE", width=200, anchor="center")
records_treeview.column("NET CPM", width=100, anchor="center")
records_treeview.column("KPM", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("KPH", width=100, anchor="center")
records_treeview.column("KEYBOARD LAYOUT", width=200, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("KEYBOARD KEYS USED", width=200, anchor="center")
records_treeview.column("KEYBOARD KEYS", width=500, anchor="center")
records_treeview.column("OS NAME", width=100, anchor="center")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
records_treeview.column("OS ADMIN", width=200, anchor="center")
records_treeview.column("EVENT DATE", width=250, anchor="center")

for column in records_treeview["columns"]:
    records_treeview.heading(column, text=column, anchor="center")
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW

cursor5.execute("SELECT * FROM realtime_records")
data_record = cursor5.fetchall()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
for record in data_record:
    records_treeview.insert("", tk.END, values=record)

refresh = "0"
floor_counter = 0
ceiling_counter = 3600
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
conn5.close()
def timer():
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    global floor_counter, refresh , ceiling_counter
    floor_counter += 1
    hours = ceiling_counter // 3600
    hours = int(hours)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    minutes = ceiling_counter // 60
    minutes = int(minutes)
    seconds = ceiling_counter % 60
    seconds = int(seconds)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    if hours == 1:
        minutes = 0
        seconds = 0
    counter = tk.Label(window, bg="#00ff00", fg="darkblue", text="", font="arial 35 bold", width=42, height=1, relief="flat")
    counter.place(relx=0.5, rely=0.05, anchor=tk.N)
    counter.configure(text=f"Total Time Left to Refresh:      ---------->      {hours:02d}:{minutes:02d}:{seconds:02d}")
    ceiling_counter -= 1
    if floor_counter == 3600:
        refresh = "1"
        refresh_5_seconds()
        return
    window.after(1000, timer)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
def refresh_5_seconds():
    if refresh == "1":
        conn5.close()
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        window.destroy()
        subprocess.Popen(['python', 'leaderboard.py'])
        exit()
timer()

def quit():
    conn5.close()
    window.destroy()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    exit()

def refresher():
    conn5.close()
    messagebox.showinfo("Refreshing", "R E F R E S H I N G . . .")
    window.destroy()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    subprocess.Popen(['python', 'leaderboard.py'])
    exit()

exit_button = tk.Button(window, bg="red", fg="darkblue", font="arial 25 bold", text="E X I T", command=quit, relief="groove", cursor="hand2", width=15)
exit_button.place(relx=0.5, rely=0.9, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
refresh_button = tk.Button(window, bg="yellow", fg="purple", font="arial 20 bold", text="R  E  F  R  E  S  H!", command=refresher, relief="groove", cursor="hand2", width=60)
refresh_button.place(relx=0.5, rely=0.8, anchor=tk.N)

window.mainloop()
conn5.close()
exit()