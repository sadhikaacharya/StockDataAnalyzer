import csv
import requests
import pandas as pd
import matplotlib.pyplot as plt
import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Use the request library to connect to the API
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey=API_KEY'
r = requests.get(url)
result = r.json()

# Put the json file in a csv file
header = ['Company', 'Date', 'Price']
with open('IBMStockPrice.csv', 'a+', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

dataForAllDays = result['Time Series (Daily)']
for date in result['Time Series (Daily)']:
    dataForSingleDate = dataForAllDays[date]

    data = ['IBM', date, dataForSingleDate['4. close']]
    with open('IBMStockPrice.csv', 'a+', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Load the contents of csv file into dataframe
df = pd.read_csv('IBMStockPrice.csv')


# Put the last 10 days of data in arrays
stock_prices = []
stock_date = []
sum = 0
for i in range (10):
    stock_date.insert(i, df.iat[i,1][5:10])
    stock_prices.insert(i, float(df.iat[i,2]))
    sum += df.iat[i,2]

mean_value = round(sum / 10, 2)

# Use matplotlib to make a line graph
stock_date.reverse()
stock_prices.reverse()
fig = plt.figure()
plt.plot(stock_date, stock_prices)
plt.title("IBM Stock Data")
plt.xlabel("Date")
plt.ylabel("Stock Prices")
fig.savefig('stock_summary.pdf', dpi=fig.dpi)

# Set the data for your email
subject = "Stock Data Summary"
body = "Attached below is the stock data for IBM for the past 10 days. The average value for stock was: " + str(mean_value)
sender_email = "sadhisophi@gmail.com"
receiver_email = "acharyasadhika@gmail.com"
password = "sender_password"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "stock_summary.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
