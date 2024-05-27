# import requests
# from bs4 import BeautifulSoup
# import keyboard as keyboard
# import requests
# from Tools.scripts.dutree import display
# from bs4 import BeautifulSoup
# import time
# import smtplib
# from email.mime.text import MIMEText
# import pandas as pd
# import schedule
# import time
#
# website_urls = [
#     #'http://150.100.216.64:8080/scheduling/ajF?filtro=BC-MXCNHDIA-T02',
#     # 'http://150.100.216.64:8080/scheduling/ajF?filtro=BC-MXGKHDIA-T02'
#     'https://www.worldometers.info/'
# ]
#
# website_url = "http://150.100.216.64:8080/scheduling/ajF?filtro=BC-MXCNHDIA-T02"
# website_url2 = "http://150.100.216.64:8080/scheduling/ajF?filtro=BC-MXGKHDIA-T02"
#
#
# def scrape_website(url):
#     """This function will scrape a website indicated by the input URL.
#
#     This function will search for the website indicated by the ilnput URL and return the information from it.
#
#     Parameters:
#     param1 (string): Input URL. Currently, this function has no security for malicious incoming URLs.
#
#     Returns:
#     dataframe: Description of the return value
#
#     Raises:
#         ExceptionName: 'Invalid URL'.
#
#     Examples:
#         url = 'https://www.worldometers.info/world-population/'
#         >>> function_name(url)
#     result
#     """
#
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         # Extract specific data required
#         titles = [title.text for title in soup.findall('h1')]
#         return titles
#     else:
#         raise Exception('Invalid URL')
#
#
# def monitor_website(url, condition_function):
#     data = scrape_website()
#     if data:
#         return condition_function(data)
#     return False
#
#
# def sample_condition(data):
#     # Check if specific title is present
#     return "Current World Population" in data
#
#
# import smtplib
# from email.mime.text import MIMEText
#
#
# def send_email_alert(subject, body, to_email):
#     from_email = "your_email@example.com"
#     password = "your_password"
#
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = from_email
#     msg['To'] = to_email
#
#     server = smtplib.SMTP_SSL('smtp.example.com', 465)
#     server.login(from_email, password)
#     server.sendmail(from_email, to_email, msg.as_string())
#     server.quit()
#
#
# from twilio.rest import Client
#
#
# def send_sms_alert(body, to_number):
#     account_sid = 'your_account_sid'
#     auth_token = 'your_auth_token'
#     client = Client(account_sid, auth_token)
#
#     message = client.messages.create(
#         body=body,
#         from_='+1234567890',  # Your Twilio number
#         to=to_number
#     )
#
#
# def job():
#     url = 'http://example.com'
#     if monitor_website(url, sample_condition):
#         send_email_alert('Process Failed', 'The specific condition was met.', 'recipient@example.com')
#         send_sms_alert('The specific condition was met.', '+1234567890')
#
#
# schedule.every(10).minutes.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
#
# @app.route('/start', methods=['POST'])
# def start_bot():
#     url = request.json.get('url')
#     # Add logic to start monitoring the specified URL
#     return jsonify({"status": "Monitoring started"}), 200
#
#
# @app.route('/stop', methods=['POST'])
# def stop_bot():
#     # Add logic to stop monitoring
#     return jsonify({"status": "Monitoring stopped"}), 200
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from llm_axe import OnlineAgent, Pdfreader, OllamaChat
LLM = OllamaChat