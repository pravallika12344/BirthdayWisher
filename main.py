##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas as pd
import random
import smtplib
today = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv("birthdays.csv")

my_email = "pravallikaramachandra46@gmail.com"
my_password = "mzadtpycisskwhbw"


birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}


if (today in birthdays_dict):
    birthday_person = birthdays_dict[today]
    file_path = f"C:/Users/pathi/OneDrive/Desktop/BirthdayWisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
print("email sent succesfully")
