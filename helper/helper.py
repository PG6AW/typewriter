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

import shutil
import getpass
import sqlite3
from tkinter import messagebox
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
    ids = max(Ids)
    for Id in ids:
        Id = int(Id)
    cursor2.execute("SELECT username FROM login_logs WHERE id=?", (Id,))
    user_name = cursor2.fetchone()
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
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
    # Copyright (C) [2023] [Mohammad Dorri]
    # https://www.github.com/PG6AW
    while retry:
        retry = messagebox.askretrycancel("LOGGED OUT!", "You are currently Logged Out!\n\nYOU'D BE BETTER OFF CANCELLING THIS & LOG-IN FIRST BEFORE YOU COME BACK & RETRY!")
        # Copyright (C) [2023] [Mohammad Dorri]
        # https://www.github.com/PG6AW
    subprocess.Popen(['python', 'login.py'])
    exit()
else:
    pass

directory = 'leaderboard_cache'
# Copyright (C) [2023] [Mohammad Dorri]
# https://www.github.com/PG6AW
if shutil.rmtree(directory, ignore_errors=True):
    pass
else:
    pass

exit()