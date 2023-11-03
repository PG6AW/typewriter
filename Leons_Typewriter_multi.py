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

from words import english_words_full , english_words_essential , english_words_advanced
import tkinter as tk
from tkinter import messagebox , ttk
from PIL import Image, ImageTk
import random
import getpass
import webbrowser
import sqlite3
import platform
import subprocess
import datetime
os_name = platform.system()
if os_name == "Windows":
    import ctypes

# Copyright (C) 2023 Mohammad Dorri https://www.github.com/PG6AW

positive_points = 0
negative_points = 0
total_keystrokes = 0
all_keypress = 0
correct_keystrokes = 0
number_of_words = 0
correct_words = 0
incorrect_words = 0
realtime_stroke_aggregator = 0
meter_timer = 0
wpm_calc = 0
keyboard_keys_used = []
total_stat = "On"
random_state = "0"
color_reset = "yes"
typewriter_mode = "Multi-Words"
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
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
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
event_by_admin = getpass.getuser()
the_user = "*N-U-L-L*"
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
try:
    conn2 = sqlite3.connect("accounts.db")
    cursor2 = conn2.cursor()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    cursor2.execute("SELECT id FROM login_logs WHERE event_by_admin=?", (event_by_admin,))
    Ids = cursor2.fetchall()
    if Ids is None:
        Ids = str(Ids)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    ids = max(Ids)
    for Id in ids:
        Id = int(Id)
    cursor2.execute("SELECT username FROM login_logs WHERE id=?", (Id,))
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    user_name = cursor2.fetchone()
    if user_name is None:
        user_name = str(user_name)
    else:
        for the_user in user_name:
            the_user = str(the_user)
    conn2.close()
except (sqlite3.OperationalError , ValueError , sqlite3.ProgrammingError):
    pass

if the_user == "LOGGED->OUT" or the_user == "*N-U-L-L*":
    conn.close()
    subprocess.Popen(['python', 'login.py'])
    retry = True
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    while retry:
        retry = messagebox.askretrycancel("LOGGED OUT!", "You are currently Logged Out!\n\nYOU MUST LOG-IN FIRST BEFORE YOU COME BACK & RETRY!")
        if retry:
            conn2 = sqlite3.connect("accounts.db")
            cursor2 = conn2.cursor()
            cursor2.execute("""CREATE TABLE IF NOT EXISTS retry_cache (cache TEXT)""")
            conn2.commit()
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            cursor2.execute("INSERT INTO retry_cache (cache) VALUES(?)", ("retried",))
            conn2.commit()
            conn2.close()
            try:
                conn2 = sqlite3.connect("accounts.db")
                cursor2 = conn2.cursor()
                cursor2.execute("SELECT id FROM login_logs WHERE event_by_admin=?", (event_by_admin,))
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                Ids = cursor2.fetchall()
                if Ids is None:
                    Ids = str(Ids)
                ids = max(Ids)
                for Id in ids:
                    Id = int(Id)
                cursor2.execute("SELECT username FROM login_logs WHERE id=?", (Id,))
                user_name = cursor2.fetchone()
                if user_name is None:
                    user_name = str(user_name)
                else:
                    for the_user in user_name:
                        the_user = str(the_user)
                conn2.close()
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            except (sqlite3.OperationalError , ValueError , sqlite3.ProgrammingError):
                pass
            if the_user != "LOGGED->OUT" and the_user != "*N-U-L-L*":
                retry = False
                subprocess.Popen(['python', 'Leons_Typewriter_multi.py'])
        else:
            conn2 = sqlite3.connect("accounts.db")
            cursor2 = conn2.cursor()
            cursor2.execute("""CREATE TABLE IF NOT EXISTS retry_cache (cache TEXT)""")
            conn2.commit()
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            cursor2.execute("DELETE FROM retry_cache")
            conn2.commit()
            conn2.close()
    exit()
else:
    pass

conn3 = sqlite3.connect("typewriter.db")
cursor3 = conn3.cursor()
cursor3.execute("""CREATE TABLE IF NOT EXISTS records (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                total_score INTEGER,
                net_wpm TEXT,
                gross_wpm TEXT,
                pure_wpm TEXT,
                accuracy TEXT,
                correct_chars INTEGER,
                total_keystrokes INTEGER,
                correct_keystrokes INTEGER,
                incorrect_keystrokes INTEGER,
                time_in_minutes INTEGER,
                extended_seconds INTEGER,
                total_minutes TEXT,
                typed_words INTEGER,
                correct_words INTEGER,
                incorrect_words INTEGER,
                positive_points INTEGER,
                negative_points INTEGER,
                all_keypress INTEGER,
                interrupted TEXT,
                idle TEXT,
                challenge_mode TEXT,
                typewriter_mode TEXT,
                net_cpm TEXT,
                kpm TEXT,
                kph INTEGER,
                keyboard_layout TEXT,
                keyboard_keys_used INTEGER,
                keyboard_keys TEXT,
                os_name TEXT,
                os_admin TEXT,
                event_date TEXT
)""")
conn3.commit()

conn3 = sqlite3.connect("typewriter.db")
cursor3 = conn3.cursor()
cursor3.execute("""CREATE TABLE IF NOT EXISTS layout (layout)""")
conn3.commit()
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
cursor3.execute("DELETE FROM layout")
conn3.commit()

update_uptimer = True
uptimer = 0
def uptime():
    global update_uptimer , uptimer
    if update_uptimer:
        hours = uptimer // 3600
        hours = int(hours)
        uptimer_residual = uptimer % 3600
        minutes = uptimer_residual // 60
        minutes = int(minutes)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        seconds = uptimer % 60
        seconds = int(seconds)
        uptime_label.configure(text=f"Uptime: {hours:02d}:{minutes:02d}:{seconds:02d}")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        uptimer += 1
    if total_stat == "On":
        uptime_label.after(1000, uptime)

go = False
typewriter_stat = "Off"
def activate_typewriter():
    global typewriter_stat , time_remaining , selected_mode , go , time_interval , what_color
    if typewriter_stat == "Off":
        what_color = ""
        time_remaining = typewriter_duration_entry.get()
        time_interval = time_remaining
        selected_mode = selected_button.get()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        if selected_mode is None or selected_mode == "":
            messagebox.showerror("Error", "Please choose session's difficulty mode first!")
            return
        if time_remaining == "":
            messagebox.showerror("Error", "Please Don't Leave the field empty!")
            return
        if time_remaining == "0":
            messagebox.showerror("Error", "Please set the duration from at least 1 minute, to any number as you wish!")
            return
        try:
            time_remaining = int(time_remaining)
        except (ValueError , TypeError):
            messagebox.showerror("Error", "Please input only numbers representing minutes!")
            return
        typewriter_duration_entry.delete(0, tk.END)
        words_entry.delete(0, tk.END)
        selected_button.set("")
        minutes_word = "minute"
        if time_remaining > 1:
            minutes_word = "minutes"
        ask = messagebox.askyesno("Begin?", f"In this typing session, you're about to start in the {selected_mode} typing mode for a maximum of {time_remaining} {minutes_word}.\n\n___PROCEED___?")
        if ask:
            pass
        else:
            return
        typewriter_stat = "On"
        typewriter_button.configure(text="_Toggle_OFF_", bg="red")
        typewriter_duration_label.configure(bg="#000000", fg="#000000")
        typewriter_duration_entry.configure(bg="#000000", fg="#000000")
        typewriter_options_frame.place(relx=0.88, rely=0.15, anchor=tk.N)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        blank_label.configure(bg="#000000", text="", width=35, height=5)
        blank_label2.configure(bg="#000000", text="", width=25, height=3)
        blank_label.place(relx=0.88, rely=0.15, anchor=tk.N)
        blank_label2.place(relx=0.88, rely=0.25, anchor=tk.N)
        start_timer()
    elif typewriter_stat == "On":
        ask = messagebox.askyesno("End?", "You're about to End the current typing session.\n\nDo you confirm?")
        if ask:
            pass
        else:
            return
        typewriter_stat = "Off"
        go = False
        typewriter_button.configure(text="__RESTART__", bg="#00ff00")
        typewriter_duration_label.configure(bg="#000000", fg="#00ff00")
        typewriter_duration_entry.configure(bg="lightgreen", fg="#000000")
        words_label.configure(text="____RESTART_THE_ENGINE!____", fg="#00ff00", font="arial 55 bold")
        timer_label.configure(text="", fg="#000000")
        typewriter_options_frame.place(relx=0.88, rely=0.25, anchor=tk.N)
        timer_label.place(relx=0.88, rely=0.51, anchor=tk.N)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        blank_label.configure(bg="#000000", text="", width=1, height=1)
        blank_label2.configure(bg="#000000", text="", width=1, height=1)
        blank_label.place(relx=0.88, rely=0.95, anchor=tk.N)
        blank_label2.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_entry.delete(0, tk.END)
        words_entry.configure(fg="#333333", bg="turquoise")

def start_timer():
    global time_remaining , indice , saved1 , challenge
    indice = 0
    try:
        time_remaining = (60 * int(time_remaining)) + int(((int(time_remaining)) * (0/100)) * 60) + 4
        challenge = False
    except (ValueError , TypeError):
        return
    saved1 = time_remaining
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if typewriter_stat == "On":
        update_timer()
        preparation()
    else:
        return

def update_timer():
    global time_remaining , typewriter_stat , stopwatch , go , saved1 , the_user , total_keystrokes , correct_keystrokes , correct_words , incorrect_words , positive_points , negative_points , all_keypress , interrupted , idle , number_of_words , time_interval , color_reset , typewriter_mode
    time_remaining = int(time_remaining)
    if time_remaining > 0 and typewriter_stat == "On":
        words_label.configure(text="")
        hours = time_remaining // 3600
        time_remaining_residual = time_remaining % 3600
        minutes = time_remaining_residual // 60
        seconds = time_remaining % 60
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        stopwatch = int(hours) + int(minutes) + int(seconds)
        timer_label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        timer_label.place(relx=0.88, rely=0.42, anchor=tk.N)
        words_entry.focus_set()
        time_remaining -= 1
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        saved2 = time_remaining
        if saved1 - saved2 < 5:
            if seconds % 2 == 0:
                timer_label.configure(fg="yellow")
            else:
                timer_label.configure(fg="red")
        else:
            timer_label.configure(fg="#00ff00")
        if hours == 0 and minutes == 0 and seconds < 15:
            if seconds % 2 == 0:
                timer_label.configure(fg="#00ff00")
            else:
                timer_label.configure(fg="red")
        timer_label.after(1000, update_timer)
    else:
        typewriter_button.configure(text="__RESTART__", bg="#00ff00")
        words_label.configure(text="____RESTART_THE_ENGINE!____", fg="#00ff00", font="arial 55 bold")
        typewriter_duration_label.configure(bg="#000000", fg="#00ff00")
        typewriter_duration_entry.configure(bg="lightgreen", fg="#000000")
        typewriter_options_frame.place(relx=0.88, rely=0.25, anchor=tk.N)
        timer_label.place(relx=0.88, rely=0.51, anchor=tk.N)
        wpm_meter_label.configure(fg="#000000", text="")
        blank_label.configure(bg="#000000", text="", width=1, height=1)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        blank_label2.configure(bg="#000000", text="", width=1, height=1)
        total_stat_label.configure(bg="lightgreen", fg="blue", text="STATE:  AFK")
        uptime_label.configure(bg="lightgreen", fg="blue")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        system_label.configure(fg="blue", bg="lightgreen")
        top_frame_label.configure(bg="lightgreen")
        blank_label.place(relx=0.88, rely=0.95, anchor=tk.N)
        blank_label2.place(relx=0.88, rely=0.95, anchor=tk.N)
        typewriter_duration_entry.delete(0, tk.END)
        words_entry.delete(0, tk.END)

        words_label2.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label3.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label4.place(relx=0.88, rely=0.95, anchor=tk.N)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_label5.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label6.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label7.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label8.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label9.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label10.place(relx=0.88, rely=0.95, anchor=tk.N)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_label11.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label12.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label13.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label14.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label15.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label16.place(relx=0.88, rely=0.95, anchor=tk.N)
        words_label17.place(relx=0.88, rely=0.95, anchor=tk.N)

        words_label2.configure(bg="#000000", fg="#000000", text="")
        words_label3.configure(bg="#000000", fg="#000000", text="")
        words_label4.configure(bg="#000000", fg="#000000", text="")
        words_label5.configure(bg="#000000", fg="#000000", text="")
        words_label6.configure(bg="#000000", fg="#000000", text="")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_label7.configure(bg="#000000", fg="#000000", text="")
        words_label8.configure(bg="#000000", fg="#000000", text="")
        words_label9.configure(bg="#000000", fg="#000000", text="")
        words_label10.configure(bg="#000000", fg="#000000", text="")
        words_label11.configure(bg="#000000", fg="#000000", text="")
        words_label12.configure(bg="#000000", fg="#000000", text="")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_label13.configure(bg="#000000", fg="#000000", text="")
        words_label14.configure(bg="#000000", fg="#000000", text="")
        words_label15.configure(bg="#000000", fg="#000000", text="")
        words_label16.configure(bg="#000000", fg="#000000", text="")
        words_label17.configure(bg="#000000", fg="#000000", text="")
        color_reset = "yes"
        radiobutton_entry_focus()
        # Some arithmetic paperworks:
        typewriter_mode = typewriter_mode
        difficulty = selected_mode
        username = the_user
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        extended_seconds = int((int(time_interval)*60) * (0/100))
        total_score = positive_points - negative_points
        keyboard_layout = "QWERTY"
        conn3 = sqlite3.connect("typewriter.db")
        cursor3 = conn3.cursor()
        cursor3.execute("""CREATE TABLE IF NOT EXISTS layout (layout)""")
        conn3.commit()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        cursor3.execute("SELECT layout FROM layout")
        k_layout = cursor3.fetchone()
        if k_layout == None:
            k_layout = str(k_layout)
        else:
            for layout in k_layout:
                keyboard_layout = str(layout)
        try:
            gross_wpm = int((total_keystrokes/5)/(float(time_interval)))
            net_wpm = ((correct_keystrokes + (number_of_words-1))/5)/(float(time_interval))
            pure_wpm = (correct_keystrokes/5)/(float(time_interval))
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            accuracy = int((correct_keystrokes+(number_of_words-1))*100/total_keystrokes)
            correct_chars = correct_keystrokes
            total_keystrokes = total_keystrokes
            if correct_keystrokes > 0:
                correct_keystrokes += (number_of_words-1)
            else:
                correct_keystrokes = correct_keystrokes
            incorrect_keystrokes = total_keystrokes - correct_keystrokes
            time_in_minutes = float(time_interval)
            total_minutes = int(time_interval) + (extended_seconds/60)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            correct_words = correct_words
            incorrect_words = incorrect_words
            positive_points = positive_points
            negative_points = negative_points
            all_keypress = all_keypress
            idle = "False"
            challenge_mode = str(challenge)
            net_cpm = (correct_keystrokes/float(time_interval))
            kpm = (total_keystrokes/float(time_interval))
            kph = int(total_keystrokes/(float(time_interval)/60))
            typed_words = number_of_words
            os_name = platform.system()
            os_admin = getpass.getuser()
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            event_date = str(datetime.datetime.now())
        except ZeroDivisionError:
            gross_wpm = "N/A"
            net_wpm = "N/A"
            pure_wpm = "N/A"
            accuracy = "N/A"
            correct_chars = correct_keystrokes
            total_keystrokes = total_keystrokes
            if correct_keystrokes > 0:
                correct_keystrokes += (number_of_words-1)
            else:
                correct_keystrokes = correct_keystrokes
            incorrect_keystrokes = total_keystrokes - correct_keystrokes
            time_in_minutes = int(time_interval)
            total_minutes = int(time_interval) + (extended_seconds/60)
            correct_words = correct_words
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            incorrect_words = incorrect_words
            positive_points = positive_points
            negative_points = negative_points
            all_keypress = all_keypress
            idle = "False"
            challenge_mode = str(challenge)
            net_cpm = "N/A"
            kpm = "N/A"
            kph = "N/A"
            typed_words = number_of_words
            os_name = platform.system()
            os_admin = getpass.getuser()
            event_date = str(datetime.datetime.now())
        if correct_words == 0:
            net_wpm = "N/A"
            gross_wpm = "N/A"
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            pure_wpm = "N/A"
            accuracy = "N/A"
            correct_chars = "N/A"
            correct_keystrokes = "N/A"
            incorrect_keystrokes = "N/A"
            net_cpm = "N/A"
            kpm = "N/A"
            kph = "N/A"
        if challenge:
            total_score += int(0.15*total_score)
            extended_seconds = 0
            total_minutes = int(time_interval) + (extended_seconds/60)
        if typewriter_stat == "Off":
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            timer_label.configure(text="Process Stopped Manually!", fg="#00ff00")
            interrupted = "True"
            messagebox.showinfo(f"{username}'s RESULTS:", f"YOU CAN'T SAVE YOUR PROGRESS BECAUSE YOU HAVE ENDED THE SESSION MANUALLY! HOWEVER, THE INCOMPLETE RESULTS WOULD BE AS FOLLOWS:\n\n\t--------- S C O R E ---------                         \n\n\t   1. Score: {total_score} PTS\n\n\t--------- W P M ---------                         \n\n\t   2. Net WPM:   {net_wpm} WPM\n\t   3. Gross WPM:   {gross_wpm} WPM\n\t   4. Pure WPM:   {pure_wpm} WPM\n\n\t--------- A C C U R A C Y ---------                         \n\n\t   5. Accuracy: {accuracy}%\n\n\t--------- C H A R A C T E R S ---------                         \n\n\t   6. Correct Characters: {correct_chars} Char(s)\n\n\t--------- K E Y . S T R O K E S ---------                         \n\n\t   7. Total Keystrokes: {total_keystrokes} Stroke(s)\n\t   8. Correct Keystrokes: {correct_keystrokes} Stroke(s)\n\t   9. Incorrect Keystrokes: {incorrect_keystrokes} Stroke(s)\n\n\t--------- T I M E ---------                         \n\n\t   10. Time In Minutes: {time_in_minutes} Minute(s)\n\t   11. Extended Seconds: {extended_seconds} Second(s)\n\t   12. Total Minutes: {total_minutes} Minute(s)\n\n\t--------- W O R D S ---------                         \n\n\t   13. All Typed Words: {typed_words} Word(s)\n\t   14. Correct Words: {correct_words} Word(s)\n\t   15. Incorrect Words: {incorrect_words} Word(s)\n\n\t--------- P O I N T S ---------                         \n\n\t   16. Positive Points: {positive_points} PTS\n\t   17. Negative Points: -{negative_points} PTS\n\n\t--------- S T A T S ---------                         \n\n\t   18. All Keys Pressed: {all_keypress} Key(s)\n\t   19. Stopped by User?  {interrupted}\n\t   20. Idle?  {idle}\n\t   21. Session On Challenge Mode?  {challenge_mode}\n\n\t--------- N O N - W P M ---------                         \n\n\t   22. Net CPM:   {net_cpm} CPM\n\t   23. KPM:   {kpm} KPM\n\t   24. KPH:   {kph} KPH")
            radiobutton_entry_focus()
        else:
            timer_label.configure(text="Time's up!", fg="#00ff00")
            words_entry.configure(bg="turquoise", fg="#333333")
            typewriter_stat = "Off"
            interrupted = "False"
            go = False
            wpm_measure = 15
            try:
                wpm_measure = int(net_wpm)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            except (ValueError , TypeError):
                pass
            if wpm_measure < 15 or net_wpm == "N/A":
                idle = "True"
                messagebox.showinfo("Idle_True", "Apologies, Sounds like you were AFK or completely idle for sometime. Hence, your progress cannot be saved nor will it be represented to you by any means or by any possible way, only & only because you went AFK during an ongoing session!")
                return
            else:
                messagebox.showinfo("Time's Over!", "Successfully carried out the test and completed a session!\nTherefore, you are being redirected to your results shortly ...")
                store_message = messagebox.askyesno(f"{username}'s RESULTS:", f"\t--------- S C O R E ---------                         \n\n\t   1. Score: {total_score} PTS\n\n\t--------- W P M ---------                         \n\n\t   2. Net WPM:   {net_wpm} WPM\n\t   3. Gross WPM:   {gross_wpm} WPM\n\t   4. Pure WPM:   {pure_wpm} WPM\n\n\t--------- A C C U R A C Y ---------                         \n\n\t   5. Accuracy: {accuracy}%\n\n\t--------- C H A R A C T E R S ---------                         \n\n\t   6. Correct Characters: {correct_chars} Char(s)\n\n\t--------- K E Y . S T R O K E S ---------                         \n\n\t   7. Total Keystrokes: {total_keystrokes} Stroke(s)\n\t   8. Correct Keystrokes: {correct_keystrokes} Stroke(s)\n\t   9. Incorrect Keystrokes: {incorrect_keystrokes} Stroke(s)\n\n\t--------- T I M E ---------                         \n\n\t   10. Time In Minutes: {time_in_minutes} Minute(s)\n\t   11. Extended Seconds: {extended_seconds} Second(s)\n\t   12. Total Minutes: {total_minutes} Minute(s)\n\n\t--------- W O R D S ---------                         \n\n\t   13. All Typed Words: {typed_words} Word(s)\n\t   14. Correct Words: {correct_words} Word(s)\n\t   15. Incorrect Words: {incorrect_words} Word(s)\n\n\t--------- P O I N T S ---------                         \n\n\t   16. Positive Points: {positive_points} PTS\n\t   17. Negative Points: -{negative_points} PTS\n\n\t--------- S T A T S ---------                         \n\n\t   18. All Keys Pressed: {all_keypress} Key(s)\n\t   19. Stopped by User?  {interrupted}\n\t   20. Idle?  {idle}\n\t   21. Session On Challenge Mode?  {challenge_mode}\n\n\t--------- N O N - W P M ---------                         \n\n\t   22. Net CPM:   {net_cpm} CPM\n\t   23. KPM:   {kpm} KPM\n\t   24. KPH:   {kph} KPH\n\n\n\t********* ___SAVE STATS?___ *********           ")
                radiobutton_entry_focus()
                if store_message:
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    conn3 = sqlite3.connect("typewriter.db")
                    cursor3 = conn3.cursor()
                    cursor3.execute("INSERT INTO records (username, total_score, net_wpm, gross_wpm, pure_wpm, accuracy, correct_chars, total_keystrokes, correct_keystrokes, incorrect_keystrokes, time_in_minutes, extended_seconds, total_minutes, typed_words, correct_words, incorrect_words, positive_points, negative_points, all_keypress, interrupted, idle, challenge_mode, typewriter_mode, net_cpm, kpm, kph, keyboard_layout, keyboard_keys_used, keyboard_keys, os_name, os_admin, event_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (username, total_score, f"{net_wpm} WPM", gross_wpm, pure_wpm, f"{accuracy}%", correct_chars, total_keystrokes, correct_keystrokes, incorrect_keystrokes, f"{time_in_minutes} m", f"{extended_seconds} s", f"{total_minutes} m", typed_words, correct_words, incorrect_words, positive_points, -negative_points, all_keypress, interrupted, idle, challenge_mode, f"{typewriter_mode}, {difficulty}", net_cpm, kpm, kph, keyboard_layout, len(keyboard_keys_used), f"{tuple(keyboard_keys_used)}", os_name, os_admin, event_date))
                    conn3.commit()
                    lb_check = messagebox.askyesno("STORED!", "Results sucessfully transferred and saved into the database!\n\nAnd additionally ... **___ONE FINAL THING:___\nWould you like to check out the Leaderboard?")
                    if lb_check:
                        subprocess.Popen(['python', 'leaderboard.py'])
                    else:
                        return
                else:
                    return

def preparation():
    global indice , go , preparation_count , positive_points , negative_points , total_keystrokes , correct_keystrokes , random_word , number_of_words , correct_words , incorrect_words , all_keypress , realtime_stroke_aggregator , meter_timer , wpm_calc , keyboard_keys_used , color_reset , random_state , start
    go = False
    if typewriter_stat == "On":
        preparation_count_list = ["WAIT ... <-----Three----->", "WAIT ... <-----Two----->", "WAIT ... <-----One----->", "<-----Go!----->"]
        if indice < 4:
            preparation_count = preparation_count_list[indice]
            indice += 1
            if indice < 4:
                words_label.configure(text=preparation_count, fg="red", font="arial 45 italic")
            elif indice == 4:
                words_label.configure(text=preparation_count, fg="yellow", font="arial 45 italic")
            words_label.after(1000, preparation)
        elif indice == 4:
            random_word = ""
            positive_points = 0
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            negative_points = 0
            total_keystrokes = 0
            all_keypress = 0
            correct_keystrokes = 0
            number_of_words = 0
            correct_words = 0
            incorrect_words = 0
            realtime_stroke_aggregator = 0
            meter_timer = 0
            wpm_calc = 0
            random_state = "0"
            keyboard_keys_used = []
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            color_reset = "yes"
            start = "1"
            go = True
            words_entry.delete(0, tk.END)
            words()
            realtime_wpm_meter_timer()
            realtime_wpm_meter()
            idle_timeout_check()
            words_label.configure(text="")
            return
    else:
        return

def idle_timeout_check():
    global stopwatch , go , typewriter_stat
    if stopwatch == 0:
        go = False
        typewriter_stat = "Off"
    words_label.after(1000, idle_timeout_check)

def words():
    global typewriter_stat , stopwatch , english_words_essential , english_words_advanced , english_words_full , selected_mode , go , preparation_count , positive_points , negative_points , correct_keystrokes , random_word , time_interval , number_of_words , correct_words , incorrect_words , all_keypress , realtime_stroke_aggregator , keyboard_keys_used , random_state , color_reset , start , random_word1 , random_word2 , random_word3 , random_word4 , random_word5 , random_word6 , random_word8, random_word9 , random_word10 , random_word11 , random_word12 , random_word13 , random_word14 , random_word15 , random_word16 , random_word17 , total_keystrokes
    if go:
        pass
    else:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_entry.delete(0, tk.END)
        return
    words_label.configure(fg="#00ff00", font="arial 55 bold")
    if typewriter_stat == "On":
        if stopwatch == 0:
            return
        else:
            pass
        if selected_mode == "'Essential'":
            total_stat_label.configure(bg="darkblue", fg="yellow", text=f"STATE:  During a {time_interval}-Minute Essential Words Typing Session")
            top_frame_label.configure(bg="darkblue")
            uptime_label.configure(fg="yellow", bg="darkblue")
            system_label.configure(fg="yellow", bg="darkblue")
            
            words_label2.place(relx=0.11, rely=0.055, anchor=tk.N)
            words_label3.place(relx=0.22, rely=0.055, anchor=tk.N)
            words_label4.place(relx=0.33, rely=0.055, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label5.place(relx=0.44, rely=0.055, anchor=tk.N)
            words_label6.place(relx=0.55, rely=0.055, anchor=tk.N)
            words_label7.place(relx=0.66, rely=0.055, anchor=tk.N)
            words_label8.place(relx=0.77, rely=0.055, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label9.place(relx=0.88, rely=0.055, anchor=tk.N)
            words_label10.place(relx=0.11, rely=0.11, anchor=tk.N)
            words_label11.place(relx=0.22, rely=0.11, anchor=tk.N)
            words_label12.place(relx=0.33, rely=0.11, anchor=tk.N)
            words_label13.place(relx=0.44, rely=0.11, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label14.place(relx=0.55, rely=0.11, anchor=tk.N)
            words_label15.place(relx=0.66, rely=0.11, anchor=tk.N)
            words_label16.place(relx=0.77, rely=0.11, anchor=tk.N)
            words_label17.place(relx=0.88, rely=0.11, anchor=tk.N)

            preparation_count = ""
            typewriter_word = words_entry.get()

            if start == "1":
                random_word1 = random.choice(english_words_essential)
                words_label2.configure(text=f"{random_word1}")
                random_word2 = random.choice(english_words_essential)
                words_label3.configure(text=f"{random_word2}")
                random_word3 = random.choice(english_words_essential)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label4.configure(text=f"{random_word3}")
                random_word4 = random.choice(english_words_essential)
                words_label5.configure(text=f"{random_word4}")
                random_word5 = random.choice(english_words_essential)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label6.configure(text=f"{random_word5}")
                random_word6 = random.choice(english_words_essential)
                words_label7.configure(text=f"{random_word6}")
                random_word8 = random.choice(english_words_essential)
                words_label8.configure(text=f"{random_word8}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word9 = random.choice(english_words_essential)
                words_label9.configure(text=f"{random_word9}")
                random_word10 = random.choice(english_words_essential)
                words_label10.configure(text=f"{random_word10}")
                random_word11 = random.choice(english_words_essential)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label11.configure(text=f"{random_word11}")
                random_word12 = random.choice(english_words_essential)
                words_label12.configure(text=f"{random_word12}")
                random_word13 = random.choice(english_words_essential)
                words_label13.configure(text=f"{random_word13}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word14 = random.choice(english_words_essential)
                words_label14.configure(text=f"{random_word14}")
                random_word15 = random.choice(english_words_essential)
                words_label15.configure(text=f"{random_word15}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word16 = random.choice(english_words_essential)
                words_label16.configure(text=f"{random_word16}")
                random_word17 = random.choice(english_words_essential)
                words_label17.configure(text=f"{random_word17}")
                start = "0"

            if color_reset == "yes":
                words_label2.configure(fg="#00ff00")
                words_label3.configure(fg="#00ff00")
                words_label4.configure(fg="#00ff00")
                words_label5.configure(fg="#00ff00")
                words_label6.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label7.configure(fg="#00ff00")
                words_label8.configure(fg="#00ff00")
                words_label9.configure(fg="#00ff00")
                words_label10.configure(fg="#00ff00")
                words_label11.configure(fg="#00ff00")
                words_label12.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label13.configure(fg="#00ff00")
                words_label14.configure(fg="#00ff00")
                words_label15.configure(fg="#00ff00")
                words_label16.configure(fg="#00ff00")
                words_label17.configure(fg="#00ff00")

            if typewriter_word.count(" ") == len(typewriter_word):
                words_entry.delete(0, tk.END)
            
            if random_state != "1" and random_state != "2" and random_state != "3" and random_state != "4" and random_state != "5" and random_state != "6" and random_state != "7" and random_state != "8" and random_state != "9" and random_state != "10" and random_state != "11" and random_state != "12" and random_state != "13" and random_state != "14" and random_state != "15" and random_state != "16":
                words_entry.delete(0, tk.END)
                random_word = random_word1
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_state = "1"
                color_reset = "no"
                #words_label(s) are configured to pose as cursors to the word being typed:
                words_label2.configure(bg="#555555")

            allowed_space_count = random_word.count(" ") + 1
            random_state = str(random_state)

            if ((typewriter_word.count(" ") >= allowed_space_count) and (typewriter_word[len(typewriter_word)-1] == " ") and (typewriter_word[len(typewriter_word)-2:len(typewriter_word)] != "  ")) and (len(typewriter_word) >= len(random_word) or (len(random_word) - len(typewriter_word)) < 3) and "  " not in typewriter_word:
                tks = len(typewriter_word)
                number_of_words += 1
                if random_word17 == typewriter_word[:len(typewriter_word)-1] and random_state == "16":
                    words_entry.delete(0, tk.END)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    typewriter_word = ""
                    random_state = "0"
                    color_reset = "yes"
                    words_label17.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word17)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word17 != typewriter_word[:len(typewriter_word)-1] and random_state == "16":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_state = "0"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    color_reset = "yes"
                    words_label17.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word17:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word16 == typewriter_word[:len(typewriter_word)-1] and random_state == "15":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word17
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "16"
                    words_label17.configure(bg="#555555")
                    words_label16.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word16)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word16 != typewriter_word[:len(typewriter_word)-1] and random_state == "15":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word17
                    random_state = "16"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label17.configure(bg="#555555")
                    words_label16.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word16:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word15 == typewriter_word[:len(typewriter_word)-1] and random_state == "14":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word16
                    random_state = "15"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#555555")
                    words_label15.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word15)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word15 != typewriter_word[:len(typewriter_word)-1] and random_state == "14":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word16
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "15"
                    words_label16.configure(bg="#555555")
                    words_label15.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word15:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word14 == typewriter_word[:len(typewriter_word)-1] and random_state == "13":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word15
                    random_state = "14"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label15.configure(bg="#555555")
                    words_label14.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word14)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word14 != typewriter_word[:len(typewriter_word)-1] and random_state == "13":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word15
                    random_state = "14"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label15.configure(bg="#555555")
                    words_label14.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 1
                    for char in random_word14:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word13 == typewriter_word[:len(typewriter_word)-1] and random_state == "12":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word14
                    random_state = "13"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label14.configure(bg="#555555")
                    words_label13.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word13)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word13 != typewriter_word[:len(typewriter_word)-1] and random_state == "12":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word14
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "13"
                    words_label14.configure(bg="#555555")
                    words_label13.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word13:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word12 == typewriter_word[:len(typewriter_word)-1] and random_state == "11":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_word = random_word13
                    random_state = "12"
                    words_label13.configure(bg="#555555")
                    words_label12.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word12)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word12 != typewriter_word[:len(typewriter_word)-1] and random_state == "11":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word13
                    random_state = "12"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label13.configure(bg="#555555")
                    words_label12.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 1
                    for char in random_word12:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word11 == typewriter_word[:len(typewriter_word)-1] and random_state == "10":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word12
                    random_state = "11"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label12.configure(bg="#555555")
                    words_label11.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word11)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word11 != typewriter_word[:len(typewriter_word)-1] and random_state == "10":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word12
                    random_state = "11"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label12.configure(bg="#555555")
                    words_label11.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word11:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word10 == typewriter_word[:len(typewriter_word)-1] and random_state == "9":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word11
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "10"
                    words_label11.configure(bg="#555555")
                    words_label10.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word10)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word10 != typewriter_word[:len(typewriter_word)-1] and random_state == "9":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word11
                    random_state = "10"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label11.configure(bg="#555555")
                    words_label10.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 1
                    for char in random_word10:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word9 == typewriter_word[:len(typewriter_word)-1] and random_state == "8":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word10
                    random_state = "9"
                    words_label10.configure(bg="#555555")
                    words_label9.configure(bg="#000000")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word9)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word9 != typewriter_word[:len(typewriter_word)-1] and random_state == "8":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word10
                    random_state = "9"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label10.configure(bg="#555555")
                    words_label9.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word9:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word8 == typewriter_word[:len(typewriter_word)-1] and random_state == "7":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word9
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "8"
                    words_label9.configure(bg="#555555")
                    words_label8.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word8)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word8 != typewriter_word[:len(typewriter_word)-1] and random_state == "7":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word9
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "8"
                    words_label9.configure(bg="#555555")
                    words_label8.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word8:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word6 == typewriter_word[:len(typewriter_word)-1] and random_state == "6":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word8
                    random_state = "7"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label8.configure(bg="#555555")
                    words_label7.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word6)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word6 != typewriter_word[:len(typewriter_word)-1] and random_state == "6":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word8
                    random_state = "7"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label8.configure(bg="#555555")
                    words_label7.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word6:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word5 == typewriter_word[:len(typewriter_word)-1] and random_state == "5":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word6
                    random_state = "6"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label7.configure(bg="#555555")
                    words_label6.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word5)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word5 != typewriter_word[:len(typewriter_word)-1] and random_state == "5":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word6
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "6"
                    words_label7.configure(bg="#555555")
                    words_label6.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word5:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word4 == typewriter_word[:len(typewriter_word)-1] and random_state == "4":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word5
                    random_state = "5"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label6.configure(bg="#555555")
                    words_label5.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word4)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word4 != typewriter_word[:len(typewriter_word)-1] and random_state == "4":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word5
                    random_state = "5"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label6.configure(bg="#555555")
                    words_label5.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word4:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word3 == typewriter_word[:len(typewriter_word)-1] and random_state == "3":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word4
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "4"
                    words_label5.configure(bg="#555555")
                    words_label4.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word3)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word3 != typewriter_word[:len(typewriter_word)-1] and random_state == "3":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word4
                    random_state = "4"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label5.configure(bg="#555555")
                    words_label4.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 1
                    for char in random_word3:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word2 == typewriter_word[:len(typewriter_word)-1] and random_state == "2":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word3
                    random_state = "3"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label4.configure(bg="#555555")
                    words_label3.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word2)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word2 != typewriter_word[:len(typewriter_word)-1] and random_state == "2":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word3
                    random_state = "3"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label4.configure(bg="#555555")
                    words_label3.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 1
                    for char in random_word2:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word1 == typewriter_word[:len(typewriter_word)-1] and random_state == "1":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "2"
                    words_label3.configure(bg="#555555")
                    words_label2.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word1)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word1 != typewriter_word[:len(typewriter_word)-1] and random_state == "1":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word2
                    random_state = "2"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label3.configure(bg="#555555")
                    words_label2.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 10
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 1
                    for char in random_word1:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

            if random_state == "0":
                random_word1 = random.choice(english_words_essential)
                words_label2.configure(text=f"{random_word1}")
                random_word2 = random.choice(english_words_essential)
                words_label3.configure(text=f"{random_word2}")
                random_word3 = random.choice(english_words_essential)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label4.configure(text=f"{random_word3}")
                random_word4 = random.choice(english_words_essential)
                words_label5.configure(text=f"{random_word4}")
                random_word5 = random.choice(english_words_essential)
                words_label6.configure(text=f"{random_word5}")
                random_word6 = random.choice(english_words_essential)
                words_label7.configure(text=f"{random_word6}")
                random_word8 = random.choice(english_words_essential)
                words_label8.configure(text=f"{random_word8}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word9 = random.choice(english_words_essential)
                words_label9.configure(text=f"{random_word9}")
                random_word10 = random.choice(english_words_essential)
                words_label10.configure(text=f"{random_word10}")
                random_word11 = random.choice(english_words_essential)
                words_label11.configure(text=f"{random_word11}")
                random_word12 = random.choice(english_words_essential)
                words_label12.configure(text=f"{random_word12}")
                random_word13 = random.choice(english_words_essential)
                words_label13.configure(text=f"{random_word13}")
                random_word14 = random.choice(english_words_essential)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label14.configure(text=f"{random_word14}")
                random_word15 = random.choice(english_words_essential)
                words_label15.configure(text=f"{random_word15}")
                random_word16 = random.choice(english_words_essential)
                words_label16.configure(text=f"{random_word16}")
                random_word17 = random.choice(english_words_essential)
                words_label17.configure(text=f"{random_word17}")

            if typewriter_word not in random_word and random_state == "1":
                words_label2.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "1":
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label2.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label2.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "2":
                words_label3.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "2":
                words_label3.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label3.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "3":
                words_label4.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "3":
                words_label4.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label4.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "4":
                words_label5.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "4":
                words_label5.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label5.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "5":
                words_label6.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "5":
                words_label6.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label6.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "6":
                words_label7.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "6":
                words_label7.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label7.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "7":
                words_label8.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "7":
                words_label8.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C)    [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label8.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "8":
                words_label9.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "8":
                words_label9.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label9.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "9":
                words_label10.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "9":
                words_label10.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label10.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "10":
                words_label11.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "10":
                words_label11.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label11.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "11":
                words_label12.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "11":
                words_label12.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label12.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "12":
                words_label13.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "12":
                words_label13.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label13.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "13":
                words_label14.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "13":
                words_label14.configure(fg="#00ff00")
                # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label14.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "14":
                words_label15.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "14":
                words_label15.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label15.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "15":
                words_label16.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "15":
                words_label16.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label16.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "16":
                words_label17.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "16":
                words_label17.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label17.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            all_keypress += 1
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            for key in typewriter_word:
                keyboard_keys_used.append(key)
                keyboard_keys_used = list(set(keyboard_keys_used))

            if color_reset == "yes":
                words_label2.configure(fg="#00ff00")
                words_label3.configure(fg="#00ff00")
                words_label4.configure(fg="#00ff00")
                words_label5.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label6.configure(fg="#00ff00")
                words_label7.configure(fg="#00ff00")
                words_label8.configure(fg="#00ff00")
                words_label9.configure(fg="#00ff00")
                words_label10.configure(fg="#00ff00")
                words_label11.configure(fg="#00ff00")
                words_label12.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label13.configure(fg="#00ff00")
                words_label14.configure(fg="#00ff00")
                words_label15.configure(fg="#00ff00")
                words_label16.configure(fg="#00ff00")
                words_label17.configure(fg="#00ff00")
                words_label2.configure(bg="#555555")

        elif selected_mode == "'Advanced'":
            total_stat_label.configure(bg="darkblue", fg="yellow", text=f"STATE:  During a {time_interval}-Minute Advanced Words Typing Session")
            top_frame_label.configure(bg="darkblue")
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            uptime_label.configure(fg="yellow", bg="darkblue")
            system_label.configure(fg="yellow", bg="darkblue")
            
            words_label2.place(relx=0.11, rely=0.055, anchor=tk.N)
            words_label3.place(relx=0.22, rely=0.055, anchor=tk.N)
            words_label4.place(relx=0.33, rely=0.055, anchor=tk.N)
            words_label5.place(relx=0.44, rely=0.055, anchor=tk.N)
            words_label6.place(relx=0.55, rely=0.055, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label7.place(relx=0.66, rely=0.055, anchor=tk.N)
            words_label8.place(relx=0.77, rely=0.055, anchor=tk.N)
            words_label9.place(relx=0.88, rely=0.055, anchor=tk.N)
            words_label10.place(relx=0.11, rely=0.11, anchor=tk.N)
            words_label11.place(relx=0.22, rely=0.11, anchor=tk.N)
            words_label12.place(relx=0.33, rely=0.11, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label13.place(relx=0.44, rely=0.11, anchor=tk.N)
            words_label14.place(relx=0.55, rely=0.11, anchor=tk.N)
            words_label15.place(relx=0.66, rely=0.11, anchor=tk.N)
            words_label16.place(relx=0.77, rely=0.11, anchor=tk.N)
            words_label17.place(relx=0.88, rely=0.11, anchor=tk.N)

            preparation_count = ""
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            typewriter_word = words_entry.get()

            if start == "1":
                random_word1 = random.choice(english_words_advanced)
                words_label2.configure(text=f"{random_word1}")
                random_word2 = random.choice(english_words_advanced)
                words_label3.configure(text=f"{random_word2}")
                random_word3 = random.choice(english_words_advanced)
                words_label4.configure(text=f"{random_word3}")
                random_word4 = random.choice(english_words_advanced)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label5.configure(text=f"{random_word4}")
                random_word5 = random.choice(english_words_advanced)
                words_label6.configure(text=f"{random_word5}")
                random_word6 = random.choice(english_words_advanced)
                words_label7.configure(text=f"{random_word6}")
                random_word8 = random.choice(english_words_advanced)
                words_label8.configure(text=f"{random_word8}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word9 = random.choice(english_words_advanced)
                words_label9.configure(text=f"{random_word9}")
                random_word10 = random.choice(english_words_advanced)
                words_label10.configure(text=f"{random_word10}")
                random_word11 = random.choice(english_words_advanced)
                words_label11.configure(text=f"{random_word11}")
                random_word12 = random.choice(english_words_advanced)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label12.configure(text=f"{random_word12}")
                random_word13 = random.choice(english_words_advanced)
                words_label13.configure(text=f"{random_word13}")
                random_word14 = random.choice(english_words_advanced)
                words_label14.configure(text=f"{random_word14}")
                random_word15 = random.choice(english_words_advanced)
                words_label15.configure(text=f"{random_word15}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word16 = random.choice(english_words_advanced)
                words_label16.configure(text=f"{random_word16}")
                random_word17 = random.choice(english_words_advanced)
                words_label17.configure(text=f"{random_word17}")
                start = "0"

            if color_reset == "yes":
                words_label2.configure(fg="#00ff00")
                words_label3.configure(fg="#00ff00")
                words_label4.configure(fg="#00ff00")
                words_label5.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label6.configure(fg="#00ff00")
                words_label7.configure(fg="#00ff00")
                words_label8.configure(fg="#00ff00")
                words_label9.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label10.configure(fg="#00ff00")
                words_label11.configure(fg="#00ff00")
                words_label12.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label13.configure(fg="#00ff00")
                words_label14.configure(fg="#00ff00")
                words_label15.configure(fg="#00ff00")
                words_label16.configure(fg="#00ff00")
                words_label17.configure(fg="#00ff00")

            if typewriter_word.count(" ") == len(typewriter_word):
                words_entry.delete(0, tk.END)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            
            if random_state != "1" and random_state != "2" and random_state != "3" and random_state != "4" and random_state != "5" and random_state != "6" and random_state != "7" and random_state != "8" and random_state != "9" and random_state != "10" and random_state != "11" and random_state != "12" and random_state != "13" and random_state != "14" and random_state != "15" and random_state != "16":
                words_entry.delete(0, tk.END)
                random_word = random_word1
                random_state = "1"
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                color_reset = "no"
                #words_label(s) are configured to pose as cursors to the word being typed:
                words_label2.configure(bg="#555555")

            allowed_space_count = random_word.count(" ") + 1
            random_state = str(random_state)

            if ((typewriter_word.count(" ") >= allowed_space_count) and (typewriter_word[len(typewriter_word)-1] == " ") and (typewriter_word[len(typewriter_word)-2:len(typewriter_word)] != "  ")) and (len(typewriter_word) >= len(random_word) or (len(random_word) - len(typewriter_word)) < 3) and "  " not in typewriter_word:
                tks = len(typewriter_word)
                number_of_words += 1
                if random_word17 == typewriter_word[:len(typewriter_word)-1] and random_state == "16":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_state = "0"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    color_reset = "yes"
                    words_label17.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word17)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word17 != typewriter_word[:len(typewriter_word)-1] and random_state == "16":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_state = "0"
                    color_reset = "yes"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label17.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word17:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word16 == typewriter_word[:len(typewriter_word)-1] and random_state == "15":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word17
                    random_state = "16"
                    words_label17.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word16)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word16 != typewriter_word[:len(typewriter_word)-1] and random_state == "15":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word17
                    random_state = "16"
                    words_label17.configure(bg="#555555")
                    # Copyright  (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word16:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word15 == typewriter_word[:len(typewriter_word)-1] and random_state == "14":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word16
                    random_state = "15"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#555555")
                    words_label15.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word15)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word15 != typewriter_word[:len(typewriter_word)-1] and random_state == "14":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word16
                    random_state = "15"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#555555")
                    words_label15.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word15:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word14 == typewriter_word[:len(typewriter_word)-1] and random_state == "13":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word15
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "14"
                    words_label15.configure(bg="#555555")
                    words_label14.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word14)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word14 != typewriter_word[:len(typewriter_word)-1] and random_state == "13":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word15
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "14"
                    words_label15.configure(bg="#555555")
                    words_label14.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word14:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word13 == typewriter_word[:len(typewriter_word)-1] and random_state == "12":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word14
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "13"
                    words_label14.configure(bg="#555555")
                    words_label13.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word13)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word13 != typewriter_word[:len(typewriter_word)-1] and random_state == "12":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word14
                    random_state = "13"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label14.configure(bg="#555555")
                    words_label13.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word13:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>

                if random_word12 == typewriter_word[:len(typewriter_word)-1] and random_state == "11":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word13
                    # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                    random_state = "12"
                    words_label13.configure(bg="#555555")
                    words_label12.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word12)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word12 != typewriter_word[:len(typewriter_word)-1] and random_state == "11":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word13
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "12"
                    words_label13.configure(bg="#555555")
                    words_label12.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word12:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word11 == typewriter_word[:len(typewriter_word)-1] and random_state == "10":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word12
                    random_state = "11"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label12.configure(bg="#555555")
                    words_label11.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word11)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word11 != typewriter_word[:len(typewriter_word)-1] and random_state == "10":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word12
                    random_state = "11"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label12.configure(bg="#555555")
                    words_label11.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word11:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word10 == typewriter_word[:len(typewriter_word)-1] and random_state == "9":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word11
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "10"
                    words_label11.configure(bg="#555555")
                    words_label10.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word10)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word10 != typewriter_word[:len(typewriter_word)-1] and random_state == "9":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word11
                    random_state = "10"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label11.configure(bg="#555555")
                    words_label10.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word10:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word9 == typewriter_word[:len(typewriter_word)-1] and random_state == "8":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word10
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "9"
                    words_label10.configure(bg="#555555")
                    words_label9.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word9)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word9 != typewriter_word[:len(typewriter_word)-1] and random_state == "8":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word10
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "9"
                    words_label10.configure(bg="#555555")
                    words_label9.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 2
                    for char in random_word9:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word8 == typewriter_word[:len(typewriter_word)-1] and random_state == "7":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_word = random_word9
                    random_state = "8"
                    words_label9.configure(bg="#555555")
                    words_label8.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word8)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word8 != typewriter_word[:len(typewriter_word)-1] and random_state == "7":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word9
                    random_state = "8"
                    words_label9.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label8.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word8:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word6 == typewriter_word[:len(typewriter_word)-1] and random_state == "6":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word8
                    random_state = "7"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label8.configure(bg="#555555")
                    words_label7.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word6)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word6 != typewriter_word[:len(typewriter_word)-1] and random_state == "6":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word8
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "7"
                    words_label8.configure(bg="#555555")
                    words_label7.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word6:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word5 == typewriter_word[:len(typewriter_word)-1] and random_state == "5":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word6
                    random_state = "6"
                    words_label7.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label6.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word5)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word5 != typewriter_word[:len(typewriter_word)-1] and random_state == "5":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word6
                    random_state = "6"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label7.configure(bg="#555555")
                    words_label6.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word5:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word4 == typewriter_word[:len(typewriter_word)-1] and random_state == "4":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word5
                    random_state = "5"
                    words_label6.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label5.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word4)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word4 != typewriter_word[:len(typewriter_word)-1] and random_state == "4":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word5
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "5"
                    words_label6.configure(bg="#555555")
                    words_label5.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C)   [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word4:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word3 == typewriter_word[:len(typewriter_word)-1] and random_state == "3":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word4
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "4"
                    words_label5.configure(bg="#555555")
                    words_label4.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word3)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word3 != typewriter_word[:len(typewriter_word)-1] and random_state == "3":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word4
                    random_state = "4"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label5.configure(bg="#555555")
                    words_label4.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 2
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word3:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word2 == typewriter_word[:len(typewriter_word)-1] and random_state == "2":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word3
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "3"
                    words_label4.configure(bg="#555555")
                    words_label3.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word2)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word2 != typewriter_word[:len(typewriter_word)-1] and random_state == "2":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word3
                    random_state = "3"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label4.configure(bg="#555555")
                    words_label3.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 2
                    for char in random_word2:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word1 == typewriter_word[:len(typewriter_word)-1] and random_state == "1":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word2
                    random_state = "2"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label3.configure(bg="#555555")
                    words_label2.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 8
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word1)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word1 != typewriter_word[:len(typewriter_word)-1] and random_state == "1":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word2
                    random_state = "2"
                    words_label3.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label2.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 16
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 2
                    for char in random_word1:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

            if random_state == "0":
                random_word1 = random.choice(english_words_advanced)
                words_label2.configure(text=f"{random_word1}")
                random_word2 = random.choice(english_words_advanced)
                words_label3.configure(text=f"{random_word2}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word3 = random.choice(english_words_advanced)
                words_label4.configure(text=f"{random_word3}")
                random_word4 = random.choice(english_words_advanced)
                words_label5.configure(text=f"{random_word4}")
                random_word5 = random.choice(english_words_advanced)
                words_label6.configure(text=f"{random_word5}")
                random_word6 = random.choice(english_words_advanced)
                words_label7.configure(text=f"{random_word6}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word8 = random.choice(english_words_advanced)
                words_label8.configure(text=f"{random_word8}")
                random_word9 = random.choice(english_words_advanced)
                words_label9.configure(text=f"{random_word9}")
                random_word10 = random.choice(english_words_advanced)
                words_label10.configure(text=f"{random_word10}")
                # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word11 = random.choice(english_words_advanced)
                words_label11.configure(text=f"{random_word11}")
                random_word12 = random.choice(english_words_advanced)
                words_label12.configure(text=f"{random_word12}")
                random_word13 = random.choice(english_words_advanced)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label13.configure(text=f"{random_word13}")
                random_word14 = random.choice(english_words_advanced)
                words_label14.configure(text=f"{random_word14}")
                random_word15 = random.choice(english_words_advanced)
                words_label15.configure(text=f"{random_word15}")
                random_word16 = random.choice(english_words_advanced)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label16.configure(text=f"{random_word16}")
                random_word17 = random.choice(english_words_advanced)
                words_label17.configure(text=f"{random_word17}")

            if typewriter_word not in random_word and random_state == "1":
                words_label2.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            elif random_state == "1":
                words_label2.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label2.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "2":
                words_label3.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "2":
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label3.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label3.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "3":
                words_label4.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "3":
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label4.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label4.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "4":
                words_label5.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "4":
                words_label5.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label5.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "5":
                words_label6.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "5":
                words_label6.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label6.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "6":
                words_label7.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "6":
                words_label7.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label7.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "7":
                words_label8.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "7":
                words_label8.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label8.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "8":
                words_label9.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "8":
                words_label9.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label9.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "9":
                words_label10.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "9":
                words_label10.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label10.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "10":
                words_label11.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "10":
                words_label11.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label11.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "11":
                words_label12.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "11":
                words_label12.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label12.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "12":
                words_label13.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "12":
                words_label13.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label13.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "13":
                words_label14.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "13":
                words_label14.configure(fg="#00ff00")
                # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label14.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "14":
                words_label15.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "14":
                words_label15.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label15.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "15":
                words_label16.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
                # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            elif random_state == "15":
                words_label16.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label16.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "16":
                words_label17.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "16":
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label17.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label17.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            all_keypress += 1
            for key in typewriter_word:
                keyboard_keys_used.append(key)
                keyboard_keys_used = list(set(keyboard_keys_used))

            if color_reset == "yes":
                words_label2.configure(fg="#00ff00")
                words_label3.configure(fg="#00ff00")
                words_label4.configure(fg="#00ff00")
                words_label5.configure(fg="#00ff00")
                words_label6.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label7.configure(fg="#00ff00")
                words_label8.configure(fg="#00ff00")
                words_label9.configure(fg="#00ff00")
                words_label10.configure(fg="#00ff00")
                words_label11.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label12.configure(fg="#00ff00")
                words_label13.configure(fg="#00ff00")
                words_label14.configure(fg="#00ff00")
                words_label15.configure(fg="#00ff00")
                words_label16.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label17.configure(fg="#00ff00")
                words_label2.configure(bg="#555555")

        elif selected_mode == "'Full'":
            total_stat_label.configure(bg="darkblue", fg="yellow", text=f"STATE:  During a {time_interval}-Minute Dictionary-Full Grade typing Session! Godspeed;D")
            top_frame_label.configure(bg="darkblue")
            uptime_label.configure(fg="yellow", bg="darkblue")
            system_label.configure(fg="yellow", bg="darkblue")
            
            words_label2.place(relx=0.11, rely=0.055, anchor=tk.N)
            words_label3.place(relx=0.22, rely=0.055, anchor=tk.N)
            words_label4.place(relx=0.33, rely=0.055, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label5.place(relx=0.44, rely=0.055, anchor=tk.N)
            words_label6.place(relx=0.55, rely=0.055, anchor=tk.N)
            words_label7.place(relx=0.66, rely=0.055, anchor=tk.N)
            words_label8.place(relx=0.77, rely=0.055, anchor=tk.N)
            words_label9.place(relx=0.88, rely=0.055, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label10.place(relx=0.11, rely=0.11, anchor=tk.N)
            words_label11.place(relx=0.22, rely=0.11, anchor=tk.N)
            words_label12.place(relx=0.33, rely=0.11, anchor=tk.N)
            words_label13.place(relx=0.44, rely=0.11, anchor=tk.N)
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            words_label14.place(relx=0.55, rely=0.11, anchor=tk.N)
            words_label15.place(relx=0.66, rely=0.11, anchor=tk.N)
            words_label16.place(relx=0.77, rely=0.11, anchor=tk.N)
            words_label17.place(relx=0.88, rely=0.11, anchor=tk.N)

            preparation_count = ""
            typewriter_word = words_entry.get()

            if start == "1":
                random_word1 = random.choice(english_words_full)
                words_label2.configure(text=f"{random_word1}")
                random_word2 = random.choice(english_words_full)
                words_label3.configure(text=f"{random_word2}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word3 = random.choice(english_words_full)
                words_label4.configure(text=f"{random_word3}")
                random_word4 = random.choice(english_words_full)
                words_label5.configure(text=f"{random_word4}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word5 = random.choice(english_words_full)
                words_label6.configure(text=f"{random_word5}")
                random_word6 = random.choice(english_words_full)
                words_label7.configure(text=f"{random_word6}")
                random_word8 = random.choice(english_words_full)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label8.configure(text=f"{random_word8}")
                random_word9 = random.choice(english_words_full)
                words_label9.configure(text=f"{random_word9}")
                random_word10 = random.choice(english_words_full)
                words_label10.configure(text=f"{random_word10}")
                # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                random_word11 = random.choice(english_words_full)
                words_label11.configure(text=f"{random_word11}")
                random_word12 = random.choice(english_words_full)
                words_label12.configure(text=f"{random_word12}")
                random_word13 = random.choice(english_words_full)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label13.configure(text=f"{random_word13}")
                random_word14 = random.choice(english_words_full)
                words_label14.configure(text=f"{random_word14}")
                random_word15 = random.choice(english_words_full)
                words_label15.configure(text=f"{random_word15}")
                random_word16 = random.choice(english_words_full)
                # Copyright  (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label16.configure(text=f"{random_word16}")
                random_word17 = random.choice(english_words_full)
                words_label17.configure(text=f"{random_word17}")
                start = "0"

            if color_reset == "yes":
                words_label2.configure(fg="#00ff00")
                words_label3.configure(fg="#00ff00")
                words_label4.configure(fg="#00ff00")
                words_label5.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label6.configure(fg="#00ff00")
                words_label7.configure(fg="#00ff00")
                words_label8.configure(fg="#00ff00")
                words_label9.configure(fg="#00ff00")
                words_label10.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label11.configure(fg="#00ff00")
                words_label12.configure(fg="#00ff00")
                words_label13.configure(fg="#00ff00")
                words_label14.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label15.configure(fg="#00ff00")
                words_label16.configure(fg="#00ff00")
                words_label17.configure(fg="#00ff00")

            if typewriter_word.count(" ") == len(typewriter_word):
                words_entry.delete(0, tk.END)
            
            if random_state != "1" and random_state != "2" and random_state != "3" and random_state != "4" and random_state != "5" and random_state != "6" and random_state != "7" and random_state != "8" and random_state != "9" and random_state != "10" and random_state != "11" and random_state != "12" and random_state != "13" and random_state != "14" and random_state != "15" and random_state != "16":
                words_entry.delete(0, tk.END)
                random_word = random_word1
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_state = "1"
                color_reset = "no"
                #words_label(s) are configured to pose as cursors to the word being typed:
                words_label2.configure(bg="#555555")

            allowed_space_count = random_word.count(" ") + 1
            random_state = str(random_state)

            if ((typewriter_word.count(" ") >= allowed_space_count) and (typewriter_word[len(typewriter_word)-1] == " ") and (typewriter_word[len(typewriter_word)-2:len(typewriter_word)] != "  ")) and (len(typewriter_word) >= len(random_word) or (len(random_word) - len(typewriter_word)) < 3) and "  " not in typewriter_word:
                tks = len(typewriter_word)
                number_of_words += 1
                if random_word17 == typewriter_word[:len(typewriter_word)-1] and random_state == "16":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_state = "0"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    color_reset = "yes"
                    words_label17.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word17)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word17 != typewriter_word[:len(typewriter_word)-1] and random_state == "16":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_state = "0"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    color_reset = "yes"
                    words_label17.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word17:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word16 == typewriter_word[:len(typewriter_word)-1] and random_state == "15":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word17
                    # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "16"
                    words_label17.configure(bg="#555555")
                    words_label16.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word16)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word16 != typewriter_word[:len(typewriter_word)-1] and random_state == "15":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word17
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "16"
                    words_label17.configure(bg="#555555")
                    words_label16.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word16:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word15 == typewriter_word[:len(typewriter_word)-1] and random_state == "14":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word16
                    random_state = "15"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#555555")
                    words_label15.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word15)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word15 != typewriter_word[:len(typewriter_word)-1] and random_state == "14":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word16
                    random_state = "15"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label16.configure(bg="#555555")
                    words_label15.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 3
                    # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word15:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word14 == typewriter_word[:len(typewriter_word)-1] and random_state == "13":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word15
                    random_state = "14"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label15.configure(bg="#555555")
                    words_label14.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word14)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word14 != typewriter_word[:len(typewriter_word)-1] and random_state == "13":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word15
                    # Copyright (C) [2023]   [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "14"
                    words_label15.configure(bg="#555555")
                    words_label14.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 3
                    for char in random_word14:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word13 == typewriter_word[:len(typewriter_word)-1] and random_state == "12":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word14
                    random_state = "13"
                    words_label14.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label13.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word13)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word13 != typewriter_word[:len(typewriter_word)-1] and random_state == "12":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word14
                    random_state = "13"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label14.configure(bg="#555555")
                    words_label13.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word13:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word12 == typewriter_word[:len(typewriter_word)-1] and random_state == "11":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_word = random_word13
                    random_state = "12"
                    words_label13.configure(bg="#555555")
                    words_label12.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word12)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word12 != typewriter_word[:len(typewriter_word)-1] and random_state == "11":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word13
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "12"
                    words_label13.configure(bg="#555555")
                    words_label12.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023]  [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word12:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word11 == typewriter_word[:len(typewriter_word)-1] and random_state == "10":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word12
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "11"
                    words_label12.configure(bg="#555555")
                    words_label11.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word11)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word11 != typewriter_word[:len(typewriter_word)-1] and random_state == "10":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_word = random_word12
                    random_state = "11"
                    words_label12.configure(bg="#555555")
                    words_label11.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 3
                    for char in random_word11:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word10 == typewriter_word[:len(typewriter_word)-1] and random_state == "9":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word11
                    random_state = "10"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label11.configure(bg="#555555")
                    words_label10.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word10)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word10 != typewriter_word[:len(typewriter_word)-1] and random_state == "9":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word11
                    random_state = "10"
                    words_label11.configure(bg="#555555")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label10.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word10:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word9 == typewriter_word[:len(typewriter_word)-1] and random_state == "8":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word10
                    random_state = "9"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label10.configure(bg="#555555")
                    words_label9.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    correct_keystrokes += len(random_word9)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word9 != typewriter_word[:len(typewriter_word)-1] and random_state == "8":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word10
                    random_state = "9"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label10.configure(bg="#555555")
                    words_label9.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word9:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word8 == typewriter_word[:len(typewriter_word)-1] and random_state == "7":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word9
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "8"
                    words_label9.configure(bg="#555555")
                    words_label8.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word8)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word8 != typewriter_word[:len(typewriter_word)-1] and random_state == "7":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word9
                    # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "8"
                    words_label9.configure(bg="#555555")
                    words_label8.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 3
                    for char in random_word8:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word6 == typewriter_word[:len(typewriter_word)-1] and random_state == "6":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word8
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "7"
                    words_label8.configure(bg="#555555")
                    words_label7.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word6)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word6 != typewriter_word[:len(typewriter_word)-1] and random_state == "6":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word8
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "7"
                    words_label8.configure(bg="#555555")
                    words_label7.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 3
                    for char in random_word6:
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word5 == typewriter_word[:len(typewriter_word)-1] and random_state == "5":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word6
                    random_state = "6"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label7.configure(bg="#555555")
                    words_label6.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word5)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word5 != typewriter_word[:len(typewriter_word)-1] and random_state == "5":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word6
                    random_state = "6"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label7.configure(bg="#555555")
                    words_label6.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 3
                    for char in random_word5:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word4 == typewriter_word[:len(typewriter_word)-1] and random_state == "4":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word5
                    random_state = "5"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label6.configure(bg="#555555")
                    words_label5.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word4)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word4 != typewriter_word[:len(typewriter_word)-1] and random_state == "4":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word5
                    random_state = "5"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label6.configure(bg="#555555")
                    words_label5.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word4:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word3 == typewriter_word[:len(typewriter_word)-1] and random_state == "3":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_word = random_word4
                    random_state = "4"
                    words_label5.configure(bg="#555555")
                    words_label4.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word3)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word3 != typewriter_word[:len(typewriter_word)-1] and random_state == "3":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word4
                    random_state = "4"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label5.configure(bg="#555555")
                    words_label4.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    penalty = 3
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for char in random_word3:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word2 == typewriter_word[:len(typewriter_word)-1] and random_state == "2":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word3
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "3"
                    words_label4.configure(bg="#555555")
                    words_label3.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word2)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word2 != typewriter_word[:len(typewriter_word)-1] and random_state == "2":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word3
                    random_state = "3"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    words_label4.configure(bg="#555555")
                    words_label3.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    correct_keystroke_aggregator = []
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    penalty = 3
                    for char in random_word2:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

                if random_word1 == typewriter_word[:len(typewriter_word)-1] and random_state == "1":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_word = random_word2
                    random_state = "2"
                    words_label3.configure(bg="#555555")
                    words_label2.configure(bg="#000000")

                    correct_words += 1
                    positive_points += 20
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystrokes += len(random_word1)
                    words_entry.configure(fg="#333333", bg="turquoise")

                elif random_word1 != typewriter_word[:len(typewriter_word)-1] and random_state == "1":
                    words_entry.delete(0, tk.END)
                    typewriter_word = ""
                    random_word = random_word2
                    # Copyright  (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    random_state = "2"
                    words_label3.configure(bg="#555555")
                    words_label2.configure(bg="#000000")

                    incorrect_words += 1
                    negative_points += 40
                    total_keystrokes += tks
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    correct_keystroke_aggregator = []
                    penalty = 3
                    for char in random_word1:
                        if char in typewriter_word:
                            correct_keystroke_aggregator.append(char)
                    correct_keystrokes += (len(correct_keystroke_aggregator) - int(penalty))
                    words_entry.configure(fg="#333333", bg="turquoise")

            if random_state == "0":
                random_word1 = random.choice(english_words_full)
                words_label2.configure(text=f"{random_word1}")
                random_word2 = random.choice(english_words_full)
                words_label3.configure(text=f"{random_word2}")
                random_word3 = random.choice(english_words_full)
                words_label4.configure(text=f"{random_word3}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word4 = random.choice(english_words_full)
                words_label5.configure(text=f"{random_word4}")
                random_word5 = random.choice(english_words_full)
                words_label6.configure(text=f"{random_word5}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word6 = random.choice(english_words_full)
                words_label7.configure(text=f"{random_word6}")
                random_word8 = random.choice(english_words_full)
                words_label8.configure(text=f"{random_word8}")
                random_word9 = random.choice(english_words_full)
                words_label9.configure(text=f"{random_word9}")
                random_word10 = random.choice(english_words_full)
                words_label10.configure(text=f"{random_word10}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word11 = random.choice(english_words_full)
                words_label11.configure(text=f"{random_word11}")
                random_word12 = random.choice(english_words_full)
                words_label12.configure(text=f"{random_word12}")
                random_word13 = random.choice(english_words_full)
                words_label13.configure(text=f"{random_word13}")
                random_word14 = random.choice(english_words_full)
                words_label14.configure(text=f"{random_word14}")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                random_word15 = random.choice(english_words_full)
                words_label15.configure(text=f"{random_word15}")
                random_word16 = random.choice(english_words_full)
                words_label16.configure(text=f"{random_word16}")
                random_word17 = random.choice(english_words_full)
                words_label17.configure(text=f"{random_word17}")

            if typewriter_word not in random_word and random_state == "1":
                words_label2.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "1":
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label2.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label2.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "2":
                words_label3.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "2":
                words_label3.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label3.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "3":
                words_label4.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "3":
                words_label4.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label4.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "4":
                words_label5.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "4":
                words_label5.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label5.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "5":
                words_label6.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "5":
                words_label6.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label6.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "6":
                words_label7.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "6":
                words_label7.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label7.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "7":
                words_label8.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "7":
                words_label8.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label8.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "8":
                words_label9.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "8":
                words_label9.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri]    <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label9.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "9":
                words_label10.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "9":
                words_label10.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label10.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "10":
                words_label11.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "10":
                words_label11.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label11.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "11":
                words_label12.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "11":
                words_label12.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label12.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "12":
                words_label13.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "12":
                words_label13.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label13.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "13":
                words_label14.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "13":
                words_label14.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label14.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "14":
                words_label15.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "14":
                words_label15.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label15.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "15":
                words_label16.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "15":
                words_label16.configure(fg="#00ff00")
                words_entry.configure(fg="#333333", bg="turquoise")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label16.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            if typewriter_word not in random_word and random_state == "16":
                words_label17.configure(fg="red")
                words_entry.configure(fg="darkblue", bg="yellow")
            elif random_state == "16":
                words_label17.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_entry.configure(fg="#333333", bg="turquoise")
                if typewriter_word != "" and (len(typewriter_word) <= len(random_word)):
                    realtime_stroke_aggregator += 1
                    if typewriter_word[:len(typewriter_word)] != random_word[:len(typewriter_word)]:
                        words_label17.configure(fg="red")
                        words_entry.configure(fg="darkblue", bg="yellow")
                        realtime_stroke_aggregator -= 1

            all_keypress += 1
            for key in typewriter_word:
                keyboard_keys_used.append(key)
                keyboard_keys_used = list(set(keyboard_keys_used))

            if color_reset == "yes":
                words_label2.configure(fg="#00ff00")
                words_label3.configure(fg="#00ff00")
                words_label4.configure(fg="#00ff00")
                words_label5.configure(fg="#00ff00")
                words_label6.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label7.configure(fg="#00ff00")
                words_label8.configure(fg="#00ff00")
                words_label9.configure(fg="#00ff00")
                words_label10.configure(fg="#00ff00")
                words_label11.configure(fg="#00ff00")
                words_label12.configure(fg="#00ff00")
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                words_label13.configure(fg="#00ff00")
                words_label14.configure(fg="#00ff00")
                words_label15.configure(fg="#00ff00")
                words_label16.configure(fg="#00ff00")
                words_label17.configure(fg="#00ff00")
                words_label2.configure(bg="#555555")
    else:
        keyboard_keys_used = []
        return

def realtime_wpm_meter_timer():
    global meter_timer
    if typewriter_stat == "On":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        window.after(1100, realtime_wpm_meter_timer)
        meter_timer += 1
    elif typewriter_stat == "Off":
        meter_timer = 0
        return

def realtime_wpm_meter():
    global wpm_calc
    if typewriter_stat == "On" and total_stat == "On":
        wpm_calc = int((realtime_stroke_aggregator/5)/(meter_timer/60))
        if wpm_calc < 20:
            wpm_meter_label.configure(fg="#ff0000")
        elif wpm_calc < 40:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            wpm_meter_label.configure(fg="violet")
        elif wpm_calc < 60:
            wpm_meter_label.configure(fg="yellow")
        else:
            wpm_meter_label.configure(fg="#00ff00")
        wpm_meter_label.configure(text=f"Real-Time Speed: {wpm_calc} WPM")
        wpm_meter_label.after(50, realtime_wpm_meter)
    else:
        wpm_calc = 0
        return

hide_text = "no"
def hide_entry_text():
    global hide_text
    if hide_text != "yes":
        words_entry.configure(show="$")
        hide_words_button.configure(text="S   H   O   W", bg="yellow", fg="blue")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_entry.configure(fg="#333333")
        hide_text = "yes"
    elif hide_text == "yes":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        words_entry.configure(show="")
        hide_words_button.configure(text="H   I   D   E", bg="blue", fg="yellow")
        words_entry.configure(fg="#333333")
        hide_text = "no"

def my_github():
    url = "https://www.github.com/PG6AW"
    # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    webbrowser.open(url)

def hide_github():
    github_label.configure(bg="#000000", fg="#000000", relief="flat", height=1, width=1, font="arial 7", text="", cursor="arrow")
    hide_github_label.configure(bg="#000000", fg="#000000", relief="flat", height=1, width=1, font="arial 1", text="", cursor="arrow")
    hide_github_label.place(relx=0.88, rely=0.95, anchor=tk.N)
    github_label.place(relx=0.88, rely=0.95, anchor=tk.N)
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    github_label.unbind(lambda e: my_github(), handler)
    hide_github_label.config(state=tk.DISABLED)
    # It was all just for fun as the following two would do the whole trick alone when are invoked together lol:
    github_label.destroy()
    hide_github_label.destroy()

def check_caps_lock():
    keyboard_state = ctypes.windll.user32.GetKeyState(0x14)
    caps_lock_state = keyboard_state & 0x0001 != 0
    if caps_lock_state:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        caps_lock_label.configure(fg="red", text="CapsLock On!", font="arial 35 bold", width=25, height=5, bg="yellow")
        caps_lock_label.place(relx=0.3, rely=0.43, anchor=tk.N)
    else:
        caps_lock_label.configure(bg="#000000", fg="#000000", text="", height=1, width=1, font="arial 1")
        caps_lock_label.place(relx=0.88, rely=0.95, anchor=tk.N)
    if total_stat == "On":
        window.after(100, check_caps_lock)

def switch_on_spray():
    global what_color
    if what_color != "":
        what_color = ""
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    elif what_color == "":
        what_color = "Green"
        color_spray()

what_color = "Green"
def color_spray():
    global what_color
    if what_color != "" and total_stat == "On":
        if what_color == "Green":
            words_label.configure(fg="yellow")
            what_color = "Yellow"
        elif what_color == "Yellow":
            words_label.configure(fg="red")
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            what_color = "Red"
        elif what_color == "Red":
            words_label.configure(fg="#0000ff")
            what_color = "Blue"
        elif what_color == "Blue":
            words_label.configure(fg="purple")
            what_color = "Purple"
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        elif what_color == "Purple":
            words_label.configure(fg="orange")
            what_color = "Orange"
        elif what_color == "Orange":
            words_label.configure(fg="violet")
            what_color = "Violet"
        elif what_color == "Violet":
            words_label.configure(fg="pink")
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            what_color = "Pink"
        elif what_color == "Pink":
            words_label.configure(fg="darkblue")
            what_color = "blue"
        elif what_color == "blue":
            words_label.configure(fg="#ffffff")
            what_color = "White"
        elif what_color == "White":
            words_label.configure(fg="lightgreen")
            # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
            what_color = "LightGreen"
        elif what_color == "LightGreen":
            words_label.configure(fg="#00ff00")
            what_color = "Green"
        words_label.after(100, color_spray)
    else:
        return

def radiobutton_entry_focus():
    if typewriter_stat == "Off" and total_stat == "On":
        typewriter_duration_entry.focus_set()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        typewriter_duration_entry.after(300, radiobutton_entry_focus)
    elif typewriter_stat == "On":
        return

def quit_button():
    global total_stat , the_user
    ask_ = messagebox.askyesno("QUIT", "Are you sure you're going to log out of your account and Quit the program now and subsequently go back to login window?")
    if ask_ and typewriter_stat == "Off":
        conn.close()
        conn3.close()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        current_username = getpass.getuser()
        event_by_admin = current_username
        the_user = "*N-U-L-L*"
        try:
            conn2 = sqlite3.connect("accounts.db")
            cursor2 = conn2.cursor()
            cursor2.execute("SELECT id FROM login_logs WHERE event_by_admin=?", (event_by_admin,))
            Ids = cursor2.fetchall()
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            if Ids is None:
                Ids = str(Ids)
            ids = max(Ids)
            for Id in ids:
                Id = int(Id)
            cursor2.execute("SELECT username FROM login_logs WHERE id=?", (Id,))
            user_name = cursor2.fetchone()
            if user_name is None:
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                user_name = str(user_name)
            else:
                for the_user in user_name:
                    the_user = str(the_user)
            cursor2.execute("INSERT INTO login_logs (name, username, email, os_name, event_by_admin, login_date) VALUES(?, ?, ?, ?, ?, ?)", (f"@ {the_user}", "LOGGED->OUT", "@@@", os_name, event_by_admin, f"LOGOUT {datetime.datetime.now()}"))
            conn2.commit()
            conn2.close()
        except (sqlite3.OperationalError , ValueError , sqlite3.ProgrammingError):
            pass
        total_stat = "Off"
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showinfo("Success!", f"Successfully logged out as <{the_user}>!")
        subprocess.Popen(['python', 'login.py'])
        window.destroy()
        exit()
    elif ask_ and typewriter_stat == "On":
        messagebox.showwarning("Request failed!" ,"Sorry, you cannot Quit the program while in an ongoing active session! However, if your request is urgent, please first end the session manually, and only then, try again later!")
        return
    else:
        return

def leaderboard():
    ask__ = messagebox.askyesno("LeaderBoard", "OPEN THE LEADERBOARD?")
    if ask__ and typewriter_stat == "Off":
        messagebox.showinfo("LeaderBoard Introduction", "This is the leaderboard that shows each user's best results and progress in a single record, in respect to their position by an ordinal number representing their status in a competitive theme, like their typing speed along with more details worth mentioning about them!\n\n** It's also worth noting that this leaderboard keeps refreshing on its own, in a realtime manner and once every hour, while you can also refresh it anytime by yourself, & of course! through a button!")
        subprocess.Popen(['python', 'leaderboard.py'])
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    elif ask__ and typewriter_stat == "On":
        messagebox.showerror("Request failed!" ,"Sorry, you cannot launch the leaderboard while in an ongoing active session! However, if your request is urgent, please first end the session manually, and only then, try again later!")
        return
    else:
        return

def keyboard_layout_config():
    ask__ = messagebox.askyesno("Layout Config", "Are you sure you're going to configure your keyboard layout?")
    if ask__ and typewriter_stat == "Off":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        subprocess.Popen(['python', 'layout_config/layout_config.py'])
    elif ask__ and typewriter_stat == "On":
        messagebox.showerror("Request failed!" ,"Sorry, you cannot configure your keyboard layout while in an ongoing active session! However, if your request is urgent, please first end the session manually, and only then, try again later!")
        return
    else:
        return

def switch_to_solo():
    ask__ = messagebox.askyesno("SOLO_WORD_VIEW?", "You are switching to solo typewriter mode, which means you'll be typing words one by one, rather than the current chain view mode representing multiple words all at once.\n\n___PROCEED TO SOLO MODE?___")
    if ask__ and typewriter_stat == "Off":
        conn3 = sqlite3.connect("typewriter.db")
        cursor3 = conn3.cursor()
        cursor3.execute("""CREATE TABLE IF NOT EXISTS switch (switch)""")
        conn3.commit()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        cursor3.execute("DELETE FROM switch")
        conn3.commit()
        cursor3.execute("INSERT INTO switch (switch) VALUES (?)", ("Switched",))
        conn3.commit()
        conn3.close()
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        window.destroy()
        subprocess.Popen(['python', 'Leons_Typewriter.py'])
        exit()
    elif ask__ and typewriter_stat == "On":
        messagebox.showerror("Request failed!" ,"Sorry, you cannot switch to SOLO-Word typewriter mode while in an ongoing active session! However, if your request is urgent, please first end the session manually, and only then, try again later!")
        return
    else:
        return

window = tk.Tk()
window.geometry("1600x900")
window.configure(bg="#333333", cursor="crosshair")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
window.title("Leon's Typewriter _ Multi")
window.resizable(False, False)

image = Image.open("Additional/RE2_Capcom.jpg")
background_image = ImageTk.PhotoImage(image)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
background_label = tk.Label(window, image=background_image)

words_label = tk.Label(window, bg="#000000", text="____START_THE_ENGINE!____", font="arial 55 bold", fg="#00ff00", width=34, height=2, cursor="spraycan")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_entry = tk.Entry(window, justify="center", font="arial 25 bold", width=31, bg="turquoise", fg="#333333", cursor="pencil")
words_entry.bind('<KeyRelease>', lambda event: words())

hide_words_button = tk.Button(window, text="H   I   D   E", command=hide_entry_text, cursor="hand1", font="arial 11 bold", bg="blue", fg="yellow", width=32, height=1, relief="groove")

typewriter_options_frame = tk.Frame(window, bg="#000000")
typewriter_duration_label = tk.Label(typewriter_options_frame, text="Type down an *Optional*\ntime duration in minutes:", bg="#000000", fg="#00ff00", font="arial 10 bold", cursor="based_arrow_down")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
typewriter_button = tk.Button(typewriter_options_frame, text="__START__", cursor="hand2", command=activate_typewriter, font="arial 15 bold", bg="#00ff00", fg="darkblue", width=15, height=2, relief="groove")
typewriter_duration_entry = tk.Entry(typewriter_options_frame, width=14, bg="lightgreen", justify="center", font="arial 11 bold", relief="flat", fg="darkblue")
timer_label = tk.Label(window, bg="#000000", fg="#00ff00", text="", font="arial 12 bold", height=2, cursor="exchange")
blank_label = tk.Label(window, bg="#000000", text="", width=1, height=1)
# Copyright (C) [2023]    [Mohammad Dorri] <[https://www.github.com/PG6AW]>
blank_label2 = tk.Label(window, bg="#000000", text="", width=1, height=1)
exit_button = tk.Button(window, text="____QUIT____", cursor="hand2", command=quit_button, font="arial 15 bold", bg="red", fg="darkblue", width=17, height=3, relief="groove")
to_solo_button = tk.Button(window, text="Switch_To_Solo", bg="darkblue", fg="orange", command=switch_to_solo, height=2, width=14, font="arial 14 bold", relief="groove", cursor="hand2")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
github_label = tk.Label(window, bg="orange", fg="blue", height=6, width=120, font="arial 15 bold", cursor="hand1", text='CLICK HERE TO VISIT "PG6AW" GITHUB PAGE & SUPPORT US BY RATING THIS PROJECT!\n&\nALSO, CONSIDER CHECKING OUT OUR OTHER NOTABLE PORJECTS WHICH ARE WORTH GIVING A TRY!')
hide_github_label = tk.Button(window, bg="blue", fg="yellow", font="arial 19 bold", text="Hide!", relief="groove", command=hide_github, cursor="hand2")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
leaderboard_button = tk.Button(window, text="_LEADERBOARD_", cursor="hand2", command=leaderboard, font="arial 15 bold", bg="yellow", fg="darkgreen", width=17, height=3, relief="groove")
divisor_label = tk.Label(window, text="_______OR_______", cursor="based_arrow_down", bg="#000000", fg="#ff00ff", font="arial 15 bold")
layout_config_button = tk.Button(window, text="KB Layout", bg="lightblue", fg="darkblue", command=keyboard_layout_config, height=2, width=11, font="impact 25 bold", relief="sunken", cursor="hand2")
caps_lock_label = tk.Label(window, bg="#000000", fg="#000000", text="")

words_label2 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label3 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label4 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label5 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label6 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label7 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label8 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label9 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label10 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label11 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label12 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label13 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label14 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label15 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label16 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")
words_label17 = tk.Label(window, bg="#000000", fg="#000000", font="arial 14 bold")

handler = github_label.bind("<Button-1>", lambda e: my_github())
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label.bind("<Button-1>", lambda e: switch_on_spray())

top_frame_label = tk.Label(window, bg="lightgreen", width=250, height=1, font="arial 14 bold", cursor="fleur")

total_stat_label = tk.Label(window, bg="lightgreen", fg="blue", font="arial 13 bold", text="STATE:  AFK", cursor="exchange")
uptime_label = tk.Label(window, bg="lightgreen", fg="blue", font="arial 13 bold", text="- - : - -", cursor="exchange")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
system_label = tk.Label(window, bg="lightgreen", fg="blue", font="arial 13 bold", text=f"Node ({getpass.getuser()}) -:;:-> User ({the_user})", cursor="exchange")
uptime()
radiobutton_entry_focus()
if os_name == "Windows":
    check_caps_lock()

style = ttk.Style()
style.configure("Graphical.TRadiobutton", indicatorsize=10, background="#000000", foreground="#00ff00", font="arial 8 bold")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
radiobutton_frame = tk.LabelFrame(typewriter_options_frame, text="Choose Difficulty:", bg="#000000", fg="#00ff00", bd=2, highlightbackground="#00ff00", highlightthickness=0, font="arial 12 bold", width=30, pady=2, labelanchor="n", relief="sunken", cursor="based_arrow_down")
selected_button = tk.StringVar()
radio_button1 = ttk.Radiobutton(radiobutton_frame, cursor="hand2", text="Essential", variable=selected_button, value="'Essential'", style="Graphical.TRadiobutton")
radio_button1.pack(side="left", padx=2)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
radio_button2 = ttk.Radiobutton(radiobutton_frame, cursor="hand2", text="Advanced", variable=selected_button, value="'Advanced'", style="Graphical.TRadiobutton")
radio_button2.pack(side="left", padx=2)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
radio_button3 = ttk.Radiobutton(radiobutton_frame, cursor="hand2", text="FULL", variable=selected_button, value="'Full'", style="Graphical.TRadiobutton")
radio_button3.pack(side="left", padx=2)

wpm_meter_label = tk.Label(window, bg="#000000", fg="#000000", font=("segoe script", 11), text="", cursor="watch")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
wpm_meter_label.bind('<KeyRelease>', lambda event: realtime_wpm_meter())

top_frame_label.pack()
radiobutton_frame.pack(pady=9)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
typewriter_duration_label.pack(pady=5)
typewriter_duration_entry.pack(pady=5)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
typewriter_button.pack(pady=15)

words_label.place(relx=0.5, rely=0, anchor=tk.N)
words_entry.place(relx=0.2, rely=0.22, anchor=tk.N)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
hide_words_button.place(relx=0.2, rely=0.29, anchor=tk.N)
typewriter_options_frame.place(relx=0.88, rely=0.25, anchor=tk.N)
timer_label.place(relx=0.88, rely=0.51, anchor=tk.N)
blank_label.place(relx=0.88, rely=0.95, anchor=tk.N)
blank_label2.place(relx=0.88, rely=0.95, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
total_stat_label.place(relx=0.5, rely=0.002, anchor=tk.N)
uptime_label.place(relx=0.83, rely=0.002, anchor=tk.N)
system_label.place(relx=0.17, rely=0.002, anchor=tk.N)
exit_button.place(relx=0.88, rely=0.79, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
github_label.place(relx=0.5, rely=0.75, anchor=tk.N)
hide_github_label.place(relx=0.885, rely=0.804, anchor=tk.N)
caps_lock_label.place(relx=0.88, rely=0.95, anchor=tk.N)
wpm_meter_label.place(relx=0.5, rely=0.165, anchor=tk.N)
leaderboard_button.place(relx=0.88, rely=0.62, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
divisor_label.place(relx=0.88, rely=0.56, anchor=tk.N)
layout_config_button.place(relx=0.15, rely=0.525, anchor=tk.N)
to_solo_button.place(relx=0.12, rely=0.82, anchor=tk.N)
words_label2.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label3.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label4.place(relx=0.88, rely=0.95, anchor=tk.N)
# Copyright  (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label5.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label6.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label7.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label8.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label9.place(relx=0.88, rely=0.95, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label10.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label11.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label12.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label13.place(relx=0.88, rely=0.95, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
words_label14.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label15.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label16.place(relx=0.88, rely=0.95, anchor=tk.N)
words_label17.place(relx=0.88, rely=0.95, anchor=tk.N)

conn3 = sqlite3.connect("typewriter.db")
cursor3 = conn3.cursor()
cursor3.execute("""CREATE TABLE IF NOT EXISTS switch (switch)""")
conn3.commit()
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
cursor3.execute("SELECT switch FROM switch")
is_switched = cursor3.fetchone()
is_switched = str(is_switched)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
if "Switched" in is_switched:
    messagebox.showinfo("Success Message", "The program has successfully transitioned into MULTI_WORDS_VIEW typewriter mode!")
    cursor3.execute("DELETE FROM switch")
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    conn3.commit()
else:
    cursor3.execute("DELETE FROM switch")
    conn3.commit()

window.mainloop()
conn.close()
conn2.close()
conn3.close()