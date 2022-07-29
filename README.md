# StockDataAnalyzer
A python code that uses Stock API to create charts and send it as an email attachment

Here is what the email and the attached pdf looks like:

<img width="1440" alt="Screen Shot 2022-07-29 at 22 53 28" src="https://user-images.githubusercontent.com/100597716/181809891-a9842206-58fd-46d3-b488-fb76ed64380d.png">


<img width="1440" alt="Screen Shot 2022-07-29 at 22 53 38" src="https://user-images.githubusercontent.com/100597716/181809943-03d30fec-6439-4bea-a61e-a86ec45b7b45.png">

For this code, I've used Alpha Vantage's API to retrieve daily stock data for IBM. The data is in the form of a json file, which is then converted to a CSV file. After that, the CSV file is loaded as a dataframe and manipulated to enable plotting through Matplotlib library in Python. The plot is saved as a figure in a pdf file which is sent as an email attachment to the user's preferred email address along with the average stock value for the company for the past 10 days. 

Citations:
Sending emails with Python by Joska De Langen
https://realpython.com/python-send-email/
