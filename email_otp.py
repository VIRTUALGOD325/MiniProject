import os
import math, random
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from fpdf import FPDF


def otp():
    nums = "0123456789"
    OTP = ""

    for i in range(4):
        OTP += nums[math.floor(random.random() * 10)]

    return OTP

with open("user_name.txt", "r") as name:
    username = name.readlines()

for i in username:
    username = i
user_name = username

with open("email_id.txt", "r") as email:
    emailid = email.readlines()

for i in emailid:
    emailid = i
email_id = emailid

with open("carmodel.txt", "r") as carmodel:
    car_m = carmodel.readlines()

for i in car_m:
    car_m = i
car_model = car_m

with open("price.txt", "r") as price:
    p = price.readlines()

for i in p:
    p = i
price = int(p)
total_price = price + (price*0.18)


pdf = FPDF()
pdf.add_page()
pdf.set_font('courier', 'B', 30)
pdf.set_xy(5, 10)
pdf.cell(70, 20, '////// CAR RENTAL SYSTEM //////')
pdf.ln(15)
pdf.set_font('courier', 'BI', 21)
pdf.set_xy(65, 25)
pdf.cell(30, 10, 'RECEIPT GENERATED')
pdf.ln(25)
pdf.set_font('Helvetica', 'B', 40)
pdf.set_xy(90, 40)
pdf.cell(30, 20, f'{otp()}')
pdf.ln(30)
pdf.set_font('arial', 'B', 16)
pdf.set_xy(65, 65)
pdf.cell(30, 10, 'Thank You for riding with us!')
pdf.ln(10)
pdf.set_xy(63, 75)
pdf.cell(30, 10, 'Your bill details are as follows\n')
pdf.ln(10)
pdf.set_font('courier', 'B', 16)
name_d = f"NAME:  {user_name}"
email_d = f"EMAIL ID:  {email_id}"
pickloc = f"PICKUP LOCATION:  {loc1}"
destloc = f"DROP LOCATION:  {loc2}"
car_d = f"CAR:  {car_model}"
dist_d = f"DISTANCE:  {distance} kms"
cost_d = f"COST:  Rs.{price}"
total_cost_d = f"TOTAL COST[GST:18%]:  Rs.{total_price}"
pdf.cell(50, 20, name_d)
pdf.ln(10)
pdf.cell(50, 20, email_d)
pdf.ln(10)
pdf.cell(50, 20, pickloc)
pdf.ln(10)
pdf.cell(50, 20, destloc)
pdf.ln(10)
pdf.cell(50, 20, car_d)
pdf.ln(10)
pdf.cell(50, 20, dist_d)
pdf.ln(10)
pdf.cell(50, 20, cost_d)
pdf.ln(10)
pdf.cell(50, 20, total_cost_d)
pdf.ln(15)
pdf.cell(50, 20, '________________________________________________________')
pdf.ln(20)
pdf.set_font('courier', 'B', 46)
pdf.set_xy(60, 190)
pdf.cell(50, 20 , 'THANK YOU')
pdf.ln(10)
pdf.set_font('courier', 'B', 26)
pdf.set_xy(45, 210)
pdf.cell(50, 20 , 'Do ride with us again!')
pdf.set_font('courier', 'B', 30)
pdf.ln(20)
pdf.cell(70, 20, '//////////////////////////////')

pdf.output("RECEIPT.pdf", 'F') #

filename = "RECEIPT.pdf" 


att_name = os.path.basename(filename)
_f = open(filename, 'rb')
att = MIMEApplication(_f.read(), _subtype="pdf", Name="receipt.pdf")
_f.close()
att.add_header('Content-Disposition', 'attachment', filename=att_name)


subject = "Ride Confirmed"
body = f"**YOUR RECEIPT**\n\nYour OTP: {otp()}\n\n Dear {username},\nYour ride has been booked"
msg = MIMEMultipart(emailid)
msg['From'] = "shauryap71412@gmail.com"
msg['To'] = email_id
msg['Subject'] = subject
body = MIMEText(body, 'plain')
msg.attach(body)
msg.attach(att)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('shauryap71412@gmail.com', 'nxpcvprahshpaflm')
server.sendmail('shauryap71412#gmail.com', email_id, msg.as_string())
server.quit()