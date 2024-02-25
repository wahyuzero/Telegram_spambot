import requests
import time

def send_telegram_message(bot_token, chat_id, stringExtra, stringExtra2, stringExtra3):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {'Content-Type': 'application/json'}
    message = f"*{stringExtra}*%0A%0A*From:* _{stringExtra2}_%0A*Message:* _{stringExtra3}_"
    payload = {
        'parse_mode': 'markdown',
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)
    return response

def log_response(response, filename="response_log.txt"):
    with open(filename, "a") as file:
        file.write("Timestamp: " + time.strftime('%Y-%m-%d %H:%M:%S') + "\n")
        file.write(str(response.json()) + "\n\n")
# Api Token
bot_token = "6928730988:AAHKy88YEVBSX3Ne9AEExbJ7BwViDleRMqo"
chat_id = "6973831185"
# Message
stringExtra = "Pakyu"
stringExtra2 = "Bitchhh"
stringExtra3 = "Loremipsummmmmmm"

while True:
    response = send_telegram_message(bot_token, chat_id, stringExtra, stringExtra2, stringExtra3)
    if response:
        log_response(response)
        print("Response from Telegram API logged.")
    time.sleep(0.01)
