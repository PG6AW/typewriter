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

# Layout_Config for Keyboard Layout:

import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3
import getpass
import subprocess

# Copyright (C) 2023 Mohammad Dorri https://www.github.com/PG6AW

current_username = getpass.getuser()
event_by_admin = current_username
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
the_user = "*N-U-L-L*"
try:
    conn2 = sqlite3.connect("accounts.db")
    cursor2 = conn2.cursor()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor2.execute("SELECT id FROM login_logs WHERE event_by_admin=?", (event_by_admin,))
    Ids = cursor2.fetchall()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
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
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
    else:
        for the_user in user_name:
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            the_user = str(the_user)
    conn2.close()
except (sqlite3.OperationalError , ValueError , sqlite3.ProgrammingError):
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    pass

if the_user == "LOGGED->OUT" or the_user == "*N-U-L-L*":
    retry = True
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    while retry:
        retry = messagebox.askretrycancel("LOGGED OUT!", "You are currently Logged Out!\n\nYOU'D BE BETTER OFF CANCELLING THIS & LOG-IN FIRST BEFORE YOU COME BACK & RETRY!")
    subprocess.Popen(['python', 'login.py'])
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    exit()
else:
    pass

def config_layout():
    layout = combo.get()
    # Copyright  (C)   [2023]  [Mohammad Dorri]
    # https://www.github.com/PG6AW
    if len(layout) > 0 and layout != "QWERTY":
        if len(layout[:layout.index(".")]) == 1:
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            layout = layout[12:]
        elif len(layout[:layout.index(".")]) == 2:
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            layout = layout[13:]
        elif len(layout[:layout.index(".")]) == 3:
            layout = layout[14:]
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
    elif layout == "":
        layout = "QWERTY"
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
    saved = str(layout)
    conn3 = sqlite3.connect("typewriter.db")
    cursor3 = conn3.cursor()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor3.execute("""CREATE TABLE IF NOT EXISTS layout (layout)""")
    conn3.commit()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor3.execute("DELETE FROM layout")
    conn3.commit()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    cursor3.execute("INSERT INTO layout (layout) VALUES(?)", (saved,))
    conn3.commit()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    conn3.close()
    root_window.destroy()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    messagebox.showinfo("Configuration Success!", f'Successfully configured your keyboard layout to ("{saved}") !')
    exit()

root_window = tk.Tk()
root_window.configure(bg="#333333")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
root_window.geometry("728x800")
root_window.title("Layout Config")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
root_window.resizable(False, False)

image = Image.open("Additional/typewriter1.jpg")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
background_image = ImageTk.PhotoImage(image)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
background_label = tk.Label(root_window, image=background_image)

overall_label = tk.Label(root_window, font="impact 40 bold", text="Select your Keyboard Layout:", height=2, width=28)

combo = ttk.Combobox(root_window, width=28, justify="center", height=10)
style2 = ttk.Style(root_window)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
style2.configure('TMenubutton', foreground='darkblue', background='orange')
combo['values'] = (
    "1.          QWERTY",
    "2.          AZERTY",
    "3.          QWERTZ",
    "4.          Dvorak",
    "5.          Colemak",
    "6.          Workman",
    "7.          BÉPO",
    "8.          COLEMAK-DH",
    "9.          Programmer Dvorak",
    "10.          Norman",
    "11.          Asset",
    "12.          Capewell-Dvorak",
    "13.          CarpalX QGMLWB",
    "14.          Colemak Mod-DH",
    "15.          Colemak Mod-DHm",
    "16.          Colemak Mod-DV",
    "17.          Colemak Mod-DVb",
    "18.          Colemak Mod-DHb",
    "19.          Dvorak-PT",
    "20.          Dvorak-SE",
    "21.          Dvorak-Colemak",
    "22.          Dvorak-IE",
    "23.          Dvorak-IE2",
    "24.          Dvorak-IE3",
    "25.          Dvorak-IE4",
    "26.          Dvorak-IE5",
    "27.          Dvorak-IE6",
    "28.          Dvorak-IE7",
    "29.          Dvorak-IE8",
    "30.          Dvorak-IE9",
    "31.          Dvorak-IE10",
    "32.          Dvorak-IE11",
    "33.          Dvorak-PL",
    "34.          Dvorak-PL2",
    "35.          Dvorak-NO",
    "36.          Dvorak-NO2",
    "37.          Dvorak-NO3",
    "38.          Dvorak-NO4",
    "39.          Dvorak-NO5",
    "40.          Dvorak-NO6",
    "41.          Dvorak-NO7",
    "42.          Dvorak-NO8",
    "43.          Dvorak-NO9",
    "44.          Dvorak-NO10",
    "45.          Dvorak-NO11",
    "46.          Dvorak-NO12",
    "47.          Dvorak-JP",
    "48.          Dvorak-JK",
    "49.          Dvorak-JK2",
    "50.          Dvorak-JK3",
    "51.          Dvorak-JK4",
    "52.          Dvorak-JK5",
    "53.          Dvorak-JK6",
    "54.          Dvorak-JK7",
    "55.          Dvorak-JK8",
    "56.          Dvorak-JK9",
    "57.          Dvorak-JK10",
    "58.          Dvorak-JK11",
    "59.          Dvorak-JK12",
    "60.          Dvorak-JK13",
    "61.          Asset-QGMLWY",
    "62.          Asset-QGMLWY-Ext",
    "63.          Asset-QGMLWY-Fun",
    "64.          Asset-QGMLWY-OS",
    "65.          Asset-QGMLWY-Web",
    "66.          Asset-QGMLWY-Work",
    "67.          Asset-QGMLWY-Work2",
    "68.          Asset-QGMLWY-Work3",
    "69.          Asset-QGMLWY-Work4",
    "70.          Asset-QGMLWY-Work5",
    "71.          Asset-QGMLWY-Work6",
    "72.          Asset-QGMLWY-Work7",
    "73.          Asset-QGMLWY-Work8",
    "74.          Asset-QGMLWY-Work9",
    "75.          Asset-QGMLWY-Work10",
    "76.          Asset-QGMLWY-Work11",
    "77.          Asset-QGMLWY-Work12",
    "78.          Asset-QGMLWY-Work13",
    "79.          Asset-QGMLWY-Work14",
    "80.          Asset-QGMLWY-Work15",
    "81.          NEO",
    "82.          Colemak Wide",
    "83.          Kinesis Advantage",
    "84.          Maltron",
    "85.          Colemak-DH Wide",
    "86.          QGMLWB",
    "87.          Minimak-8",
    "88.          Minimak-4",
    "89.          Minimak-12",
    "90.          Minimak-16",
    "91.          Asset-QGMLWY-Mirror",
    "92.          Arensito",
    "93.          Colemak-DHm Wide",
    "94.          Asset-QGFLBY",
    "95.          Workman-P",
    "96.          QFMLWY",
    "97.          Arensito Wide",
    "98.          Asset-QGFPLM",
    "99.          Colemak-ModDH Wide",
    "100.          Capewell-Plumbley"
)
combo.set("QWERTY")
combo.configure(style='TMenubutton', font="arial 30 bold")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
combo.state(['readonly'])

config_button = tk.Button(root_window, font="arial 18 bold", bg="darkblue", fg="yellow", command=config_layout, text="SAVE CONFIG", height=2, width=15)

combo.place(relx=0.5, rely=0.3, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
overall_label.place(relx=0.5, rely=0.0, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
config_button.place(relx=0.5, rely=0.6, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
background_label.pack()

root_window.mainloop()
exit()