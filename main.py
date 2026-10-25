import pandas
import os
import datetime as dt
import random
import pathlib
from pathlib import Path
import smtplib

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
now_month = now.month
now_day = now.day
now_today = (now_month, now_day)
bdays = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bdays.iterrows()}
if (now_month, now_day) in birthdays_dict:
    what_file = random.randint(1,3)
    with open(f"letter_templates/letter_{what_file}.txt", "r") as file:
        content = file.read()
        objectin = birthdays_dict.get((now_month, now_day))
        upd_cont = content.replace("[NAME]",objectin.get("name"))
        # print(upd_cont)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{objectin.get("email")}",
                                msg=f"Subject:Happy Birthday!\n\n{upd_cont}")
            connection.close()


# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



