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
from llm_axe import OllamaChat, OnlineAgent, FunctionCaller, make_prompt

# Insert the websites that you want to monitor. For each website make a prompt indicating what you want to do with 
# that information.
websites_to_monitor = {
    'https://www.worldometers.info/': 'Return the current world population value.'
}


def get_information():
    """
    Choose if there is information on the website.
    """
    return ""


def main():
    print(
        '''
        ----------------------------------------------------------------
        Welcome to SMART-AI! A little bot to help monitor all your important sites.
        Every 5 minutes the bot will search the indicated website for the information you programmed in your prompts.
        Type 'exit' to exit the program.
        ----------------------------------------------------------------
        '''
    )
    # Determine what large language model you want to use to monitor
    llm = OllamaChat(model="llama3:latest")
    # Declare what agents we need
    online_agent = OnlineAgent(llm)
    # function_caller = FunctionCaller(llm, functions=[get_information])

    chat_history = []
    agent_response = online_agent.search(websites_to_monitor.get('https://www.worldometers.info/'))
    print(agent_response)
    chat_history.append(agent_response)
    # chat_history.append(online_agent.search(websites_to_monitor.get('https://www.worldometers.info/')))


if __name__ == '__main__':
    main()
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
