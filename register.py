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

# Registration Tool:

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import datetime
import subprocess
import getpass
import random
import unicodedata
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
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
cursor.execute("""CREATE TABLE IF NOT EXISTS register_logs (
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
)""")
conn.commit()

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
cursor.execute("""CREATE TABLE IF NOT EXISTS captcha (captcha TEXT)""")
conn.commit()

try:
    cursor.execute("DELETE FROM captcha")
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
except sqlite3.OperationalError:
    pass

def is_english(string):
    for char in string:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        if not (unicodedata.name(char).startswith('LATIN') or char.isdigit()):
            return False
    return True

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

def register():
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()
    name = name_entry.get()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    gender = selected_button.get()
    birth_year = year_menu.get()
    birth_month = month_menu.get()
    birth_day = day_menu.get()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    confirm_password = confirm_password_entry.get()
    capt1 = c_entry1.get()

    if name == "" or username == "" or password == "" or email == "" or confirm_password == "":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showerror("Error", "All fields must be filled in!")
        recaptcha()
        return

    if gender == "" or str(gender) == "None" or gender == None:
        messagebox.showerror("Error", "Please choose your gender pronoun!")
        recaptcha()
        return

    if birth_year == "YEAR":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showerror("Error", "Please select your Year of Birth!")
        recaptcha()
        return

    if birth_month == "MONTH":
        messagebox.showerror("Error", "Please select your Month of Birth!")
        recaptcha()
        return

    if birth_day == "DAY":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showerror("Error", "Please select your Day of Birth!")
        recaptcha()
        return

    invalid_username_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "|", "\\", "{", "}", "[", "]", ":", ";", '"', "'", ">", "<", "/", "?", ",", " "]
    for char in invalid_username_chars:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        if char in username:
            messagebox.showerror("Invalid_Char", "Ambiguous Characters like '#', '@', '!' or even a 'space' & ... except for underscore, are not allowed for use in the Username field!\n\nTry a mix of numbers and regular characters instead.")
            recaptcha()
            return
        else:
            pass

    users_char = username
    if "_" in username:
        users_char = username.split("_")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        users_char = str("".join(users_char))
    if is_english(users_char) == False:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        messagebox.showerror("Invalid_Char", "Please use only english characters in your username!")
        recaptcha()
        return
    else:
        pass

    valid_email = True
    if "@" in email:
        if email.count("@") > 1 or len(email[email.index("@")+1:]) < 4 or email[len(email)-1] == "." or "." not in email[email.index("@")+1:] or len(email[:email.index("@")]) < 1 or len(email[:email.index("@")]) > 64 or len(email[email.index("@")+1:]) > 255:
            valid_email = False
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if "." in email:
        if len(email[:email.index("."):-1]) < 2 or email[len(email)-2] == "." or ".." in email:
            valid_email = False
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if "-" in email and "@" in email and "." in email:
        if "-" in email[:email.index("@")] or "-" not in email[email.index("@"):email.index(".")] or "--" in email:
            valid_email = False
    if "_" in email and "@" in email and "." in email:
        if "_" in email[email.index("@"):] or "__" in email:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            valid_email = False
    if "_" in email or "-" in email or "." in email or "@" in email:
        if "-_" in email or "_-" in email or ".@" in email or "@." in email or "_@" in email or "@-" in email or "._" in email or "_." in email or "-." in email or ".-" in email:
            valid_email = False
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if "gmail.com" in email.lower() and "@" in email and ("-" in email or "_" in email or len(email[:email.index("@")]) > 30 or len(email[:email.index("@")]) < 6):
        valid_email = False
    if len(email) > 0:
        if email[0] == "." or email[0] == "@" or email[0] == "_":
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            valid_email = False
    for e in email:
        if e in ['~', '`', '!', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '\\', '|', '[', ']', '{', '}', "'", '"', ';', ':', '/', '?', '<', '>', ',', ' ']:
            valid_email = False
    list_e_char = email
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if "@" in email or "." in email or "_" in email or "-" in email:
        list_e_char = email.split("@")
        list_e_char = "".join(list_e_char)
        list_e_char = list_e_char.split(".")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        list_e_char = "".join(list_e_char)
        list_e_char = list_e_char.split("-")
        list_e_char = "".join(list_e_char)
        list_e_char = list_e_char.split("_")
        list_e_char = "".join(list_e_char)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        list_e_char = str(list_e_char)
    if is_english(list_e_char) == False:
        valid_email = False
    if "@" not in email or "." not in email or valid_email == False:
        messagebox.showerror("Invalid Email", "Your email address is not valid!\nPlease enter a valid email address and try again!")
        recaptcha()
        return
    else:
        email = email.lower()

    try:
        birth_year = int(birth_year)
    except(ValueError , TypeError):
        pass

    try:
        birth_day = int(birth_day)
    except(ValueError , TypeError):
        pass

    if capt1 == "":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        cursor.execute("DELETE FROM captcha")
        conn.commit()
        messagebox.showerror("Captcha", "You also have to click the captcha button!\nThen you can fill the captcha field and continue!")
        recaptcha()
        return

    capt = str(1)
    cursor.execute("SELECT captcha FROM captcha")
    captcha = cursor.fetchone()
    if captcha is None:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        captcha = str(captcha)
    else:
        captcha = list(captcha)
        for capt in captcha:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            capt = str(capt)
    c_entry1.delete(0, tk.END)

    def check_user():
        try:
            try:
                try:
                    conn = sqlite3.connect("accounts.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT id FROM register_logs WHERE event_by_admin=?", (str(getpass.getuser()),))
                    Ids = cursor.fetchall()
                    if Ids is None:
                        Ids = str(Ids)
                    ids = max(Ids)
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    for Id in ids:
                        Id = int(Id)
                    cursor.execute("SELECT register_date FROM register_logs WHERE event_by_admin=? AND id=?", (str(getpass.getuser()), Id))
                    register_date = cursor.fetchone()
                    if register_date is None:
                        register_date = str(register_date)
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    else:
                        for date in register_date:
                            date = str(date)
                    date = date[:19]
                    datetime_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                    current_datetime = datetime.datetime.now()
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    time_delta = current_datetime - datetime_date
                    time_delta = str(time_delta)
                    if time_delta[0] == "-":
                        ask = messagebox.askyesno("Faulty Timezone", "We have detected that your system's datetime is not well-adjusted to your network timezone!\nAre you sure your timezone is adjusted accordingly to your network?\n\n<<Apart from answering to this, Please also note that we're asking this to urge you to check your system's timezone and adjust it as it deems it necessary | You may also want to ignore this as you wish!>>")
                        if ask:
                            pass
                        else:
                            return "0"
                    if "days" in time_delta:
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        return
                    if time_delta[1] != ":":
                        if time_delta[0:2] == "00":
                            pass
                        else:
                            return
                    else:
                        if time_delta[0] == "0":
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
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
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if minutes < rand:
                        messagebox.showerror("Flood Detected", f"Please wait for {rand-minutes} minute(s)!\nAlso note that the duration in which you must wait can vary in your next try.\n\nIt's best to wait an hour after every successful register attempt from the current network/system/OS/account!")
                        cursor.execute("DELETE FROM captcha")
                        conn.commit()
                        return "0"
                except(ValueError , TypeError):
                    # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    pass
            except UnboundLocalError:
                pass
        except sqlite3.OperationalError:
            pass
    if check_user() == "0":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        recaptcha()
        return
    else:
        pass

    if capt == capt1:
        cursor.execute("DELETE FROM captcha")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        conn.commit()
    else:
        messagebox.showerror("Captcha Error", "Wrong answer inputted! Please press the captcha button and type it down in the appropriate entry field and try submitting again!\n\nPlease also note that the captcha could have been revoked too!\nHence, try regenerating another one using the button below!")
        recaptcha()
        return

    ambiguous_char = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", '"', "'", "|", "{", "}", "[", "]", ":", ";", "/", "?", ",", ".", ">", "<", "\\"]
    num_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    lower_case_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_case_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ambiguous_check = []
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    num_check = []
    lower_case_char_check = []
    upper_case_char_check = []

    if len(password) < 8:
        messagebox.showerror("error", "Password is too short!\nPassphrase must be at least 8 characters long!")
        recaptcha()
        return
    else:
        for amb in ambiguous_char:
            if amb in password:
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                ambiguous_check.append("1")
            else:
                pass
        if len(ambiguous_check) > 0:
            for num in num_char:
                if num in password:
                    num_check.append("1")
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                else:
                    pass
            if len(num_check) > 2:
                for lower in lower_case_char:
                    if lower in password:
                        lower_case_char_check.append("1")
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    else:
                        pass
                if len(lower_case_char_check) > 2:
                    for upper in upper_case_char:
                        if upper in password:
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                            upper_case_char_check.append("1")
                        else:
                            pass
                    if len(upper_case_char_check) > 0:
                        pass
                    else:
                        messagebox.showerror("error", "You should at least include 1 upper-case letter in your password!")
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        recaptcha()
                        return
                else:
                    messagebox.showerror("error", "You should at least include 3 different lower-case letters in your password!")
                    recaptcha()
                    return
            else:
                messagebox.showerror("error", "You should at least include 3 different numbers in your password!")
                recaptcha()
                return
        else:
            messagebox.showerror("error", "You should at least include 1 ambiguous character in your password!")
            recaptcha()
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            return

        if password != confirm_password:
            messagebox.showerror("Cfrm-P-N-M Error!", "PASSWORDS DO NOT MATCH! PLEASE CONFIRM YOUR PASSWORD FIRST!")
            recaptcha()
            return
        else:
            pass

    confirm_registration = messagebox.askyesno("Register Confirmation", "Have you double-checked the details before you register?\n\n__COMMIT & PROCEED?__")
    if confirm_registration:
        pass
    else:
        recaptcha()
        return

    cursor.execute("SELECT username FROM register")
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    usernames = cursor.fetchall()
    if usernames is None:
        usernames = str(usernames)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    else:
        usernames = list(usernames)
    if (f"('{username}',)") in str(usernames):
        update = messagebox.askyesno("EXISTS!", "Usernames are unique & the provided username already exists in the local database!\n\nWant to update your details or even your password?")
        if update:
            conn = sqlite3.connect("accounts.db")
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS cache (username TEXT)""")
            conn.commit()
            cursor.execute("INSERT INTO cache (username) VALUES (?)", (username,))
            conn.commit()
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            subprocess.Popen(['python', 'update_login_info.py'])
            window.destroy()
            recaptcha()
            conn.close()
            return
        else:
            recaptcha()
            return
    else:
        recaptcha()
        pass

    current_username = getpass.getuser()
    event_by_admin = current_username
    cursor.execute("INSERT INTO register (name, gender, birth_year, birth_month, birth_day, email, username, password, event_by_admin, register_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, gender, birth_year, birth_month, birth_day, email, username, password, event_by_admin, datetime.datetime.now()))
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
    messagebox.showinfo("Success", "User successfully registered!")
    cursor.execute("""CREATE TABLE IF NOT EXISTS register_logs (
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
    )""")
    conn.commit()
    cursor.execute("INSERT INTO register_logs (name, gender, birth_year, birth_month, birth_day, email, username, password, event_by_admin, register_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, gender, birth_year, birth_month, birth_day, email, username, password, event_by_admin, datetime.datetime.now()))
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    conn.close()

    name_entry.delete(0, tk.END)
    # username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    day_menu.set("DAY")
    month_menu.set("MONTH")
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    year_menu.set("YEAR")
    selected_button.set(None)
    subprocess.Popen(['python', 'login.py'])
    window.destroy()
    exit()

def real_time_password_status_label():
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    ambiguous_char = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", '"', "'", "|", "{", "}", "[", "]", ":", ";", "/", "?", ",", ".", ">", "<", "\\"]
    num_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    lower_case_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_case_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ambiguous_check = []
    num_check = []
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    lower_case_char_check = []
    upper_case_char_check = []
    ambiguous_perplexity = []
    num_perplexity = []
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    lower_case_perplexity = []
    upper_case_perplexity = []
    for char in password:
        if char in ambiguous_char:
            if len(num_perplexity) == 0 and len(upper_case_perplexity) == 0:
                ambiguous_perplexity.append(1)
            elif len(num_perplexity) > 0 or len(upper_case_perplexity) > 0:
                ambiguous_perplexity.append(2)
                num_perplexity.clear()
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        if char in num_char:
            if len(ambiguous_perplexity) == 0 and len(lower_case_perplexity) == 0:
                num_perplexity.append(1)
            elif len(ambiguous_perplexity) > 0 or len(lower_case_perplexity) > 0:
                num_perplexity.append(2)
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                lower_case_perplexity.clear()
        if char in lower_case_char:
            if len(num_perplexity) == 0 and len(upper_case_perplexity) == 0:
                lower_case_perplexity.append(1)
            elif len(num_perplexity) > 0 or len(upper_case_perplexity) > 0:
                lower_case_perplexity.append(2)
                upper_case_perplexity.clear()
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        if char in upper_case_char:
            if len(ambiguous_perplexity) == 0 and len(lower_case_perplexity) == 0:
                upper_case_perplexity.append(1)
            elif len(ambiguous_perplexity) > 0 or len(lower_case_perplexity) > 0:
                # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                upper_case_perplexity.append(2)
                ambiguous_perplexity.clear()

    perplexity_level = "low"
    if 2 in ambiguous_perplexity:
        perplexity_level = "medium"
    if 2 in upper_case_perplexity:
        perplexity_level = "medium"
    if 2 in lower_case_perplexity:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        perplexity_level = "medium"
    if 2 in num_perplexity:
        perplexity_level = "medium"
    if (2 in ambiguous_perplexity) and (2 in lower_case_perplexity):
        perplexity_level = "high"
    if (2 in upper_case_perplexity) and (2 in num_perplexity):
        perplexity_level = "high"
    if (2 in ambiguous_perplexity) and (2 in num_perplexity):
        # Copyright (C) [2023]  [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        perplexity_level = "high"
    if (2 in upper_case_perplexity) and (2 in lower_case_perplexity):
        perplexity_level = "high"
    if (2 in lower_case_perplexity) and (2 in num_perplexity):
        perplexity_level = "high"
    if (2 in ambiguous_perplexity) and (2 in upper_case_perplexity):
        perplexity_level = "high"

    if len(password) == 0:
        stat = "Waiting for you ..."
        stat_label.configure(fg="#00ff00")
    elif len(password) < 4:
        stat = "Weakest Passphrase ever!"
        stat_label.configure(fg="red")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    elif len(password) < 8:
        stat = "Passphrase is quite Poor!"
        stat_label.configure(fg="red")
    else:
        for amb in ambiguous_char:
            if amb in password:
                ambiguous_check.append("1")
            else:
                pass
        if len(ambiguous_check) > 0:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            for num in num_char:
                if num in password:
                    num_check.append("1")
                else:
                    pass
            if len(num_check) > 2:
                for lower in lower_case_char:
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    if lower in password:
                        lower_case_char_check.append("1")
                    else:
                        pass
                if len(lower_case_char_check) > 2:
                    for upper in upper_case_char:
                        if upper in password:
                            upper_case_char_check.append("1")
                        else:
                            pass
                    if len(upper_case_char_check) > 0:
                        stat = "Passphrase strength is Fair!"
                        stat_label.configure(fg="#00ff00")
                        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        if len(password) > 15 and len(num_check) > 4 and len(lower_case_char_check) > 6 and len(upper_case_char_check) > 1 and len(ambiguous_check) > 1:
                            stat = "Passphrase strength is Average!"
                            stat_label.configure(fg="#00ff00")
                        if len(password) > 21 and len(upper_case_char_check) > 2 and len(num_check) > 7 and len(lower_case_char_check) > 8 and len(ambiguous_check) > 1 and (perplexity_level == "medium" or perplexity_level == "high"):
                            stat = "Passphrase strength is Good!"
                            stat_label.configure(fg="#00ff00")
                        if len(password) > 35 and len(ambiguous_check) > 4 and len(upper_case_char_check) > 7 and len(lower_case_char_check) > 12 and len(num_check) > 8 and (perplexity_level == "medium" or perplexity_level == "high"):
                            stat = "Noice! Passphrase strength is now Great!"
                            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                            stat_label.configure(fg="#00ff00")
                        if len(password) > 45 and len(ambiguous_check) > 7 and len(upper_case_char_check) > 9 and len(lower_case_char_check) > 15 and len(num_check) > 9 and (perplexity_level == "high"):
                            stat = "Great Job! The Passphrase is now Consolidated!"
                            stat_label.configure(fg="#00ff00")
                            # Copyright (C)  [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                        if len(password) > 50 and len(ambiguous_check) > 9 and len(upper_case_char_check) > 11 and len(num_check) > 9 and len(lower_case_char_check) > 17 and (perplexity_level == "high"):
                            stat = "Excellent! This Passphrase is Fortified!"
                            stat_label.configure(fg="#00ff00")
                    else:
                        stat = "Passphrase is still Weak!"
                        stat_label.configure(fg="red")
                else:
                    stat = "Passphrase is still Weak!"
                    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
                    stat_label.configure(fg="red")
            else:
                stat = "Passphrase is still Weak!"
                stat_label.configure(fg="red")
        else:
            stat = "Passphrase is still Weak!"
            stat_label.configure(fg="red")
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if password != confirm_password and (stat == "Passphrase strength is Average!" or stat == "Passphrase strength is Fair!" or stat == "Passphrase strength is Good!" or stat == "Noice! Passphrase strength is now Great!" or stat == "Excellent! This Passphrase is Fortified!" or stat == "Great Job! The Passphrase is now Consolidated!"):
        stat_label.place(relx=0.5, rely=0.945, anchor=tk.N)
        stat = "PASSWORDS DO NOT MATCH!\nEventhough you may have almost passed some strict security measures,\nBUT PLEASE CONFIRM YOUR PASSWORD FIRST!"
        stat_label.configure(fg="yellow")
    else:
        stat_label.place(relx=0.5, rely=0.958, anchor=tk.N)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        pass
    status_label.set(stat)

show_it = "no"
def show_entry_text():
    global show_it
    if show_it != "yes":
        password_entry.configure(show="")
        show_pass_button.configure(text="Hide", bg="#333333", fg="white")
        show_it = "yes"
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    elif show_it == "yes":
        password_entry.configure(show="*")
        show_pass_button.configure(text="Show", bg="red", fg="yellow")
        show_it = "no"

show_it_2 = "no"
def show_entry_text_2():
    global show_it_2
    if show_it_2 != "yes":
        confirm_password_entry.configure(show="")
        show_pass_button_2.configure(text="Hide", bg="#333333", fg="white")
        show_it_2 = "yes"
    elif show_it_2 == "yes":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        confirm_password_entry.configure(show="*")
        show_pass_button_2.configure(text="Show", bg="red", fg="yellow")
        show_it_2 = "no"

def update_login():
    username = username_entry.get()
    if username == "":
        messagebox.showerror("E-F Error", "To get redirected to the credentials modification window, please fill at least the username field!")
        return
    else:
        pass
    conn = sqlite3.connect("accounts.db")
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM register")
    usernames = cursor.fetchall()
    if usernames is None:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        usernames = str(usernames)
    else:
        usernames = list(usernames)
    if (f"('{username}',)") in str(usernames):
        confirm = messagebox.askyesno("Confirmation", "Update login info?")
        if confirm:
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            conn = sqlite3.connect("accounts.db")
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS cache (username TEXT)""")
            conn.commit()
            cursor.execute("INSERT INTO cache (username) VALUES (?)", (username,))
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
            conn.commit()
            subprocess.Popen(['python', 'update_login_info.py'])
            window.destroy()
            conn.close()
        else:
            return
    else:
        messagebox.showerror("Invalid User", "Sounds like this username doesn't exist in the local database!\n\nHowever, you need to first signup with this username here on the current window!")

def back_to_login():
    confirm = messagebox.askyesno("Confirmation", "Back to login window?")
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if confirm:
        subprocess.Popen(['python', 'login.py'])
        window.destroy()
        conn.close()
    else:
        return

def check_caps_lock():
    keyboard_state = ctypes.windll.user32.GetKeyState(0x14)
    caps_lock_state = keyboard_state & 0x0001 != 0
    if caps_lock_state:
        caps_lock_label_left.configure(fg="red", text="CapsLock On!")
        caps_lock_label_right.configure(fg="red", text="CapsLock On!")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        caps_lock_label_left_2.configure(fg="red", text="CapsLock On!")
        caps_lock_label_right_2.configure(fg="red", text="CapsLock On!")
    else:
        caps_lock_label_left.configure(fg="green", text="")
        caps_lock_label_right.configure(fg="green", text="")
        caps_lock_label_left_2.configure(fg="green", text="")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        caps_lock_label_right_2.configure(fg="green", text="")
    window.after(150, check_caps_lock)

lightness = "bright"
def dark_bright():
    global lightness
    if lightness == "bright":
        window.configure(bg="#333333")
        radiobutton_frame.configure(bg="#333333")
        style1.configure("Graphical.TRadiobutton", background = "#333333")
        stat_label.configure(bg="#333333")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        dropdowns_frame.configure(bg="#333333")
        caps_lock_label_left.configure(bg="#333333")
        caps_lock_label_right.configure(bg="#333333")
        caps_lock_label_left_2.configure(bg="#333333")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        caps_lock_label_right_2.configure(bg="#333333")
        username_entry.configure(bg="lightblue")
        name_entry.configure(bg="lightblue")
        email_entry.configure(bg="lightblue")
        email_check_label.configure(bg="#333333")
        email_check_label2.configure(bg="#333333")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        username_check_label.configure(bg="#333333")
        username_check_label2.configure(bg="#333333")
        brightness_button_left.configure(bg="orange", fg="darkgreen", text="Light", width=4, font="arial 8 bold")
        brightness_button_right.configure(bg="orange", fg="darkgreen", text="Light", width=4, font="arial 8 bold")
        brightness_button_left.place(relx=0.033, rely=0.975, anchor=tk.N)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        brightness_button_right.place(relx=0.969, rely=0.975, anchor=tk.N)
        lightness = "dark"
    elif lightness == "dark":
        window.configure(bg="green")
        # Copyright (C) [2023]   [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        radiobutton_frame.configure(bg="green")
        style1.configure("Graphical.TRadiobutton", background = "green")
        stat_label.configure(bg="green")
        dropdowns_frame.configure(bg="green")
        caps_lock_label_left.configure(bg="green")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        caps_lock_label_right.configure(bg="green")
        caps_lock_label_left_2.configure(bg="green")
        caps_lock_label_right_2.configure(bg="green")
        username_entry.configure(bg="white")
        name_entry.configure(bg="white")
        email_entry.configure(bg="white")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        email_check_label.configure(bg="green")
        email_check_label2.configure(bg="green")
        username_check_label.configure(bg="green")
        username_check_label2.configure(bg="green")
        brightness_button_left.configure(bg="#333333", fg="orange", text="Dark", width=3, font="arial 7 bold")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        brightness_button_right.configure(bg="#333333", fg="orange", text="Dark", width=3, font="arial 7 bold")
        brightness_button_left.place(relx=0.022, rely=0.984, anchor=tk.N)
        brightness_button_right.place(relx=0.975, rely=0.984, anchor=tk.N)
        lightness = "bright"

def generate_captcha():
    c_entry1.delete(0, tk.END)
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    cursor.execute("""CREATE TABLE IF NOT EXISTS captcha (captcha TEXT)""")
    conn.commit()
    cursor.execute("DELETE FROM captcha")
    conn.commit()
    # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    captcha_text = ""
    for _ in range(12):
        captcha_text += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=|/><,.?':;~0123456789")
    cursor.execute("INSERT INTO captcha (captcha) VALUES (?)", (captcha_text,))
    conn.commit()
    try:
        captcha_label1.config(text=captcha_text)
    except NameError:
        pass

def realtime_email_check():
    email = email_entry.get()
    valid_email = True
    if "@" in email:
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        if email.count("@") > 1 or len(email[email.index("@")+1:]) < 4 or email[len(email)-1] == "." or "." not in email[email.index("@")+1:] or len(email[:email.index("@")]) < 1 or len(email[:email.index("@")]) > 64 or len(email[email.index("@")+1:]) > 255:
            valid_email = False
    if "." in email:
        if len(email[:email.index("."):-1]) < 2 or email[len(email)-2] == "." or ".." in email:
            valid_email = False
    if "-" in email and "@" in email and "." in email:
        if "-" in email[:email.index("@")] or "-" not in email[email.index("@"):email.index(".")] or "--" in email:
            valid_email = False
            # Copyright (C)   [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if "_" in email and "@" in email and "." in email:
        if "_" in email[email.index("@"):] or "__" in email:
            valid_email = False
    if "_" in email or "-" in email or "." in email or "@" in email:
        if "-_" in email or "_-" in email or ".@" in email or "@." in email or "_@" in email or "@-" in email or "._" in email or "_." in email or "-." in email or ".-" in email:
            valid_email = False
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if "gmail.com" in email.lower() and "@" in email and ("-" in email or "_" in email or len(email[:email.index("@")]) > 30 or len(email[:email.index("@")]) < 6):
        valid_email = False
    if len(email) > 0:
        if email[0] == "." or email[0] == "@" or email[0] == "_":
            valid_email = False
            # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    for e in email:
        if e in ['~', '`', '!', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '\\', '|', '[', ']', '{', '}', "'", '"', ';', ':', '/', '?', '<', '>', ',', ' ']:
            valid_email = False
    list_e_char = email
    if "@" in email or "." in email or "_" in email or "-" in email:
        list_e_char = email.split("@")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        list_e_char = "".join(list_e_char)
        list_e_char = list_e_char.split(".")
        list_e_char = "".join(list_e_char)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        list_e_char = list_e_char.split("-")
        list_e_char = "".join(list_e_char)
        list_e_char = list_e_char.split("_")
        list_e_char = "".join(list_e_char)
        list_e_char = str(list_e_char)
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    if is_english(list_e_char) == False:
        valid_email = False
    if "@" not in email or "." not in email or valid_email == False:
        email_check_label.configure(fg="orange", text="::Invalid Syntax::")
        email_check_label2.configure(fg="orange", text="::Invalid Syntax::")
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
    else:
        email_check_label.configure(fg="green", text="")
        email_check_label2.configure(fg="green", text="")
    if email == "":
        # Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        email_check_label.configure(fg="green", text="")
        email_check_label2.configure(fg="green", text="")

def realtime_username_check():
    username = username_entry.get()
    invalid_username = False
    users_char = username
    if "_" in username:
        # Copyright (C) [2023]     [Mohammad Dorri] <[https://www.github.com/PG6AW]>
        users_char = username.split("_")
        users_char = str("".join(users_char))
    if is_english(users_char) == False:
        invalid_username = True
    invalid_username_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "|", "\\", "{", "}", "[", "]", ":", ";", '"', "'", ">", "<", "/", "?", ",", " "]
    for char in invalid_username_chars:
        if char in username:
            # Copyright (C) [2023] [Mohammad Dorri]  <[https://www.github.com/PG6AW]>
            invalid_username = True
    if invalid_username:
        username_check_label.configure(fg="orange", text="::Invalid Syntax::")
        username_check_label2.configure(fg="orange", text="::Invalid Syntax::")
    else:
        username_check_label.configure(fg="green", text="")
        username_check_label2.configure(fg="green", text="")

window = tk.Tk()
window.configure(bg="green")
window.geometry("570x1048")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
window.resizable(False, False)
window.title("Register")

main_label = tk.Label(window, text="Register ", font="impact 17 italic", bg="orange")
name_label = tk.Label(window, text="Enter your Name & Last Name: ", font="arial 15 bold", bg="yellow")
name_entry = tk.Entry(window, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
email_label = tk.Label(window, text="Enter your Email: ", font="arial 15 bold", bg="yellow")
email_entry = tk.Entry(window, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge")
username_label = tk.Label(window, text="Enter your Username: ", font="arial 15 bold", bg="yellow")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
username_entry = tk.Entry(window, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge")
password_label = tk.Label(window, text="Enter your Password: ", font="arial 15 bold", bg="yellow")
password_entry = tk.Entry(window, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge", show="*", bg="#dddddd")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
confirm_password_label = tk.Label(window, text="Confirm your Password: ", font="arial 15 bold", bg="yellow")
confirm_password_entry = tk.Entry(window, font="arial 18 italic", justify="center", width=40, fg="purple", relief="ridge", show="*", bg="#dddddd")
dropdowns_frame = tk.LabelFrame(window, text="Choose your Date of Birth:", bg="green", fg="yellow", bd=3, highlightbackground="#00ff00", highlightthickness=1, font="arial 14 bold", width=230, pady=12, labelanchor="n")

email_check_label = tk.Label(window, text="", font="arial 10 bold", bg="green", fg="green")
email_check_label2 = tk.Label(window, text="", font="arial 10 bold", bg="green", fg="green")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
username_check_label = tk.Label(window, text="", font="arial 10 bold", bg="green", fg="green")
username_check_label2 = tk.Label(window, text="", font="arial 10 bold", bg="green", fg="green")
email_entry.bind('<KeyRelease>', lambda event: realtime_email_check())
username_entry.bind('<KeyRelease>', lambda event: realtime_username_check())

month_menu = ttk.Combobox(dropdowns_frame, width=6, justify="center")
style2 = ttk.Style(dropdowns_frame)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
style2.configure('TMenubutton', background='lightgreen')
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_menu['values'] = (months)
month_menu.set("MONTH")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
month_menu.configure(style='TMenubutton', cursor="hand2", font="arial 12 bold", foreground="darkgreen")
month_menu.state(['readonly'])
month_menu.pack(side="left", padx=44)

day_menu = ttk.Combobox(dropdowns_frame, width=4, justify="center")
style2 = ttk.Style(dropdowns_frame)
style2.configure('TMenubutton', background='lightgreen')
days = [int(day) for day in range(1, 32)]
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
day_menu['values'] = (days)
day_menu.set("DAY")
day_menu.configure(style='TMenubutton', cursor="hand2", font="arial 12 bold", foreground="darkgreen")
day_menu.state(['readonly'])
day_menu.pack(side="left", padx=44)

year_menu = ttk.Combobox(dropdowns_frame, width=4, justify="center")
style2 = ttk.Style(dropdowns_frame)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
style2.configure('TMenubutton', background='lightgreen')
years = [int(year) for year in range(1870, 2024)]
year_menu['values'] = (years)
year_menu.set("YEAR")
year_menu.configure(style='TMenubutton', cursor="hand2", font="arial 12 bold", foreground="darkgreen")
year_menu.state(['readonly'])
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
year_menu.pack(side="left", padx=44)

style1 = ttk.Style()
style1.configure("Graphical.TRadiobutton", indicatorsize=25, background="green", foreground="orange", font="impact 15 italic")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
radiobutton_frame = tk.LabelFrame(window, text="You'd rather be referred to as:", bg="green", fg="yellow", bd=3, highlightbackground="#00ff00", highlightthickness=1, font="arial 18 bold", width=230, pady=2, labelanchor="n")
selected_button = tk.StringVar()
radio_button1 = ttk.Radiobutton(radiobutton_frame, cursor="hand2", text="He", variable=selected_button, value="Male", style="Graphical.TRadiobutton")
radio_button1.pack(side="left", padx=55)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
radio_button2 = ttk.Radiobutton(radiobutton_frame, cursor="hand2", text="She", variable=selected_button, value="Female", style="Graphical.TRadiobutton")
radio_button2.pack(side="left", padx=55)
radio_button3 = ttk.Radiobutton(radiobutton_frame, cursor="hand2", text="They", variable=selected_button, value="N/A", style="Graphical.TRadiobutton")
radio_button3.pack(side="left", padx=55)

brightness_button_left = tk.Button(window, cursor="hand2", text="Dark", bg="#333333", fg="orange", font="arial 7 bold", width="3", relief="groove", command=dark_bright)
brightness_button_right = tk.Button(window, cursor="hand2", text="Dark", bg="#333333", fg="orange", font="arial 7 bold", width="3", relief="groove", command=dark_bright)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
brightness_button_left.place(relx=0.022, rely=0.984, anchor=tk.N)
brightness_button_right.place(relx=0.975, rely=0.984, anchor=tk.N)

caps_lock_label_left = tk.Label(window, text="", bg="green", fg="green", font="arial 11 bold", height=1, width=11)
caps_lock_label_right = tk.Label(window, text="", bg="green", fg="green", font="arial 11 bold", height=1, width=11)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
caps_lock_label_left_2 = tk.Label(window, text="", bg="green", fg="green", font="arial 11 bold", height=1, width=11)
caps_lock_label_right_2 = tk.Label(window, text="", bg="green", fg="green", font="arial 11 bold", height=1, width=11)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
caps_lock_label_left.place(relx=0.17, rely=0.343, anchor=tk.N)
caps_lock_label_right.place(relx=0.83, rely=0.343, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
caps_lock_label_left_2.place(relx=0.15, rely=0.43, anchor=tk.N)
caps_lock_label_right_2.place(relx=0.85, rely=0.43, anchor=tk.N)
if os_name == "Windows":
    check_caps_lock()

show_pass_button = tk.Button(window, cursor="hand2", text="Show", command=show_entry_text, font="arial 8 bold", bg="red", fg="yellow", width=4, relief="groove")
show_pass_button.place(relx=0.92, rely=0.3855, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
show_pass_button_2 = tk.Button(window, cursor="hand2", text="Show", command=show_entry_text_2, font="arial 8 bold", bg="red", fg="yellow", width=4, relief="groove")
show_pass_button_2.place(relx=0.92, rely=0.478, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
submit_button = tk.Button(window, cursor="hand2", text="Register!", command=register, font="arial 15 bold", bg="blue", fg="yellow", relief="raised")
update_login_info_button = tk.Button(window, cursor="hand2", text="Update info", command=update_login, font="arial 15 bold", bg="blue", fg="yellow", relief="ridge")
back_to_login_button = tk.Button(window, cursor="hand2", text="< - Back To Login", command=back_to_login, font="arial 15 bold", bg="darkblue", fg="yellow", relief="ridge")

c_label1 = tk.Label(window, text="Solve the Captcha: ", bg="orange", fg="black", font="arial 15 bold", width=38)
c_entry1 = tk.Entry(window, fg="blue", bg="lightblue", font="arial 18 italic", justify="center", width=30)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
captcha_label1 = tk.Label(window, font=("segoe script", 15), width=15, relief="raised", bg="green", borderwidth=1, fg="#00ff00", height=1)
generate_button1 = tk.Button(window, cursor="hand2", text="Generate New Captcha!", width=35, command=generate_captcha, bg="#00ff00", fg="blue", font="arial 10 bold", relief="groove")

recaptcha()

main_label.pack(pady=18)
name_label.pack(pady=10)
name_entry.pack(pady=5)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
email_label.pack(pady=10)
email_entry.pack(pady=5)
username_label.pack(pady=10)
username_entry.pack(pady=5)
password_label.pack(pady=10)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
password_entry.pack(pady=5)
confirm_password_label.pack(pady=10)
confirm_password_entry.pack(pady=10)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
radiobutton_frame.pack(padx=20, pady=16)
dropdowns_frame.pack(padx=20, pady=7)
c_label1.pack(pady=18)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
captcha_label1.pack(pady=3)
generate_button1.pack(pady=3)
c_entry1.pack(pady=8)
submit_button.place(relx=0.8, rely=0.9, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
update_login_info_button.place(relx=0.2, rely=0.9, anchor=tk.N)
back_to_login_button.place(relx=0.51, rely=0.9, anchor=tk.N)
email_check_label.place(relx=0.79, rely=0.167, anchor=tk.N)
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
email_check_label2.place(relx=0.202, rely=0.167, anchor=tk.N)
username_check_label.place(relx=0.83, rely=0.255, anchor=tk.N)
username_check_label2.place(relx=0.162, rely=0.255, anchor=tk.N)

status_label = tk.StringVar()
stat_label = tk.Label(window, textvariable=status_label, bg="green", fg="#00ff00", font="lotus 10 italic")
# Copyright (C) [2023] [Mohammad Dorri] <[https://www.github.com/PG6AW]>
password_entry.bind('<KeyRelease>', lambda event: real_time_password_status_label())
confirm_password_entry.bind('<KeyRelease>', lambda event: real_time_password_status_label())
stat_label.place(relx=0.5, rely=0.958, anchor=tk.N)

window.mainloop()
conn.close()
exit()