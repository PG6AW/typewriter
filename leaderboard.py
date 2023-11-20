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

# Leaderboard CLI script:

from tkinter import messagebox
import getpass
import sqlite3
import shutil
import os
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
    if Ids is None:
        Ids = str(Ids)
    ids = max(Ids)
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
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
    exit()
else:
    pass

conn3 = sqlite3.connect("typewriter.db")
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
cursor3 = conn3.cursor()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
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
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
class leaderboard_app:

    def directory_mananager():
        directory = 'leaderboard_cache'
        # Copyright (C) [2023]  [Mohammad Dorri]
        # https://www.github.com/PG6AW
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            pass
        def delete_copy_rename_paste(source_dir, destination_dir, file_name, new_file_name):
            source_path = os.path.join(source_dir, file_name)
            # Copyright  (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            destination_path = os.path.join(destination_dir, new_file_name)
            try:
                os.remove(destination_path)
            except FileNotFoundError:
                pass
            try:
                shutil.copy2(source_path, destination_path)
            except FileNotFoundError:
                # Copyright (C)  [2023] [Mohammad Dorri]
                # https://www.github.com/PG6AW
                pass
        source_directory = ''
        destination_directory = 'leaderboard_cache'
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        file_to_copy = 'typewriter.db'
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        new_file_name = 'typewriter.db'
        delete_copy_rename_paste(source_directory, destination_directory, file_to_copy, new_file_name)

        def delete_record(destination_dir, new_file_name):
            destination_path = os.path.join(destination_dir, new_file_name)
            try:
                os.remove(destination_path)
            except FileNotFoundError:
                pass
        destination_directory = ''
        new_file_name = 'leaderboard.db'
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        delete_record(destination_directory, new_file_name)

    def db_manager():
        global conn4 , conn5
        conn4 = sqlite3.connect("leaderboard_cache/typewriter.db")
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        cursor4 = conn4.cursor()
        cursor4.execute("""CREATE TABLE IF NOT EXISTS records (
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
        conn4.commit()
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        conn5 = sqlite3.connect("leaderboard.db")
        cursor5 = conn5.cursor()
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        cursor5.execute("""CREATE TABLE IF NOT EXISTS realtime_records (
                        position INTEGER PRIMARY KEY AUTOINCREMENT,
                        record_id INTEGER,
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
        conn5.commit()
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        cursor5.execute("DELETE FROM realtime_records")
        conn5.commit()

    def db_slicer():
        conn4 = sqlite3.connect("leaderboard_cache/typewriter.db")
        cursor4 = conn4.cursor()
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        conn5 = sqlite3.connect("leaderboard.db")
        cursor5 = conn5.cursor()
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
        records_count = 1
        while records_count != 0:
            cursor4.execute("SELECT total_score FROM records")
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            total_scores = cursor4.fetchall()
            if total_scores is None:
                records_count = 0
                return
            else:
                records_count = len(total_scores)
                try:
                    total = max(total_scores)
                except ValueError:
                    return
                for scores in total:
                    score = int(scores)
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            cursor4.execute("SELECT username FROM records WHERE total_score=?", (score,))
            username = cursor4.fetchone()
            for user in username:
                the_username = str(user)
            cursor4.execute("SELECT record_id, total_score, net_wpm, gross_wpm, pure_wpm, accuracy, correct_chars, total_keystrokes, correct_keystrokes, incorrect_keystrokes, time_in_minutes, extended_seconds, total_minutes, typed_words, correct_words, incorrect_words, positive_points, negative_points, all_keypress, interrupted, idle, challenge_mode, typewriter_mode, net_cpm, kpm, kph, keyboard_layout, keyboard_keys_used, keyboard_keys, os_name, os_admin, event_date FROM records WHERE username=? and total_score=?", (the_username, score))
            record_set = cursor4.fetchall()
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            records_list = []
            for i in record_set[0]:
                records_list.append(i)
            record_set = []
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            record_set = records_list
            cursor5.execute("INSERT INTO realtime_records (record_id, username, total_score, net_wpm, gross_wpm, pure_wpm, accuracy, correct_chars, total_keystrokes, correct_keystrokes, incorrect_keystrokes, time_in_minutes, extended_seconds, total_minutes, typed_words, correct_words, incorrect_words, positive_points, negative_points, all_keypress, interrupted, idle, challenge_mode, typewriter_mode, net_cpm, kpm, kph, keyboard_layout, keyboard_keys_used, keyboard_keys, os_name, os_admin, event_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (record_set[0], the_username, record_set[1], record_set[2], record_set[3], record_set[4], record_set[5], record_set[6], record_set[7], record_set[8], record_set[9], record_set[10], record_set[11], record_set[12], record_set[13], record_set[14], record_set[15], record_set[16], record_set[17], record_set[18], record_set[19], record_set[20], record_set[21], record_set[22], record_set[23], record_set[24], record_set[25], record_set[26], record_set[27], record_set[28], record_set[29], record_set[30], str(record_set[31])))
            conn5.commit()
            # Copyright (C) [2023] [Mohammad Dorri]
            # https://www.github.com/PG6AW
            cursor4.execute("DELETE FROM records WHERE username=?", (the_username,))
            conn4.commit()

    def purger():
        subprocess.Popen(['python', 'helper/helper.py'])
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
leaderboard_app.directory_mananager()
leaderboard_app.db_manager()
leaderboard_app.db_slicer()
leaderboard_app.purger()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
conn3.close()
conn4.close()
conn5.close()
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
subprocess.Popen(['python', 'leaderboard_gui.py'])
exit()