import requests
import time

def send_message(api_url, message, api_number):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print(f"API {api_number} = Success {response.status_code} OK")
            return True, response.json()
        else:
            print(f"API {api_number} = {response.status_code} {response.reason}")
            return False, response.json()
    except Exception as e:
        print(f"Error sending message to API {api_number}: {str(e)}")
        return False, None

def main():
    api_urls = [
        "https://api.telegram.org/bot7073742992:AAF3fBCHGAcvpPeHdt-xyfLC15xn8X-k02o/sendMessage?parse_mode=markdown&chat_id=6050538291&text=Bang-ada-Undangan-dari-mantan-nih",
        "https://api.telegram.org/bot6928730988:AAHKy88YEVBSX3Ne9AEExbJ7BwViDleRMqo/sendMessage?parse_mode=markdown&chat_id=6973831185&text=Bang-ada-Undangan-dari-mantan-nih"
    ]

    while True:
        for i, api_url in enumerate(api_urls, start=1):
            success, response = send_message(api_url, "  ", i)
            if response:
                # Log the response
                with open("message_log.txt", "a") as f:
                    f.write(f"API {i} : {response}\n")

        time.sleep(0.001)

if __name__ == "__main__":
    main()
