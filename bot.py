import requests
from time import sleep

url = "https://api.telegram.org/bot621357860:AAF1nFmirZ4Q9hhUfxX_1onNl298KQz7L0k/"
proxies = {'https': "socks5://telegram:telegram@nixbg.telegramproxy.today:1080"}
# 'socks5://user:pass@host:port'


def get_updates_json(request):
    response = requests.get(request + 'getUpdates', proxies=proxies)
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params, proxies=proxies)
    return response


def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
