import smtplib
import datetime as dt
import pandas
import random

today = dt.datetime.now()

today_month = today.month
today_day = today.day
today_tuple = (today_month, today_day)
data = pandas.read_csv("birthdays.csv")
my_email = "<add email here. yahoo, gmail, etc>"
password = "<PASSWORD HERE>"

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file = f"letter_{random.randint(1, 3)}.txt"
    name = birthday_person["name"]

    with open(f"letter_templates/{file}", mode="r") as text_file:
        letter_file = text_file.read()
        bday_note = letter_file.replace("[NAME]", f"{name}")

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection: #SMTP to your provider
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="<to email address here>",
            msg=f"Subject:Happy Birthday {name}!\n\n{bday_note}"
        )



# HOW I DID IT THE FIRST TIME

# today_year = dt.datetime.now().year
# today_month = dt.datetime.now().month
# today_day = dt.datetime.now().day
# birthday_data = pandas.read_csv("birthdays.csv")
# my_email = "<add email here. yahoo, gmail, etc>"
# password = "<PASSWORD HERE>"
#
# birthday_month = birthday_data[birthday_data.month == today_month]
# birthday_day = birthday_month[birthday_month.day == today_day]
#
# if birthday_day.empty:
#     pass
# else:
#     template_num = random.randint(1, 3)
#     file = f"letter_{template_num}.txt"
#     name = birthday_day.name.to_string(index=False)
#
#     with open(f"letter_templates/{file}", mode="r") as text_file:
#         letter_file = text_file.read()
#         bday_note = letter_file.replace("[NAME]", f"{name}")
#
#     with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="<to email dress here>",
#             msg=f"Subject:Happy Birthday {name}!\n\n{bday_note}"
#         )




