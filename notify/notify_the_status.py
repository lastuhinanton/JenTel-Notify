"""
    Python module provides an easy and comfortable way
    to create notifications for Jenkins pipeline status in a Telegram bot.
"""

import sys
import requests
from datetime import datetime

def send_message_to_bot(token_id, chat_id, message):
    url = f"https://api.telegram.org/bot{token_id}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

def start_pipeline(arguments):
    id_pipeline = arguments[2]
    token_id = arguments[3]
    chat_id = arguments[4]
    now = datetime.now()
    message = f"""
====== ⏩ Pipeline {id_pipeline} started ⏪ ======
Time: {now.strftime("%H:%M:%S")}
Date: {now.strftime("%m/%d/%Y")}
"""
    send_message_to_bot(token_id, chat_id, message)

def notify_status_stage_to_bot(arguments):
    token_id = arguments[2]
    chat_id = arguments[3]
    status = arguments[4]
    url = arguments[5]
    name = arguments[6]
    smile = "✅" if status == "SUCCESS" else "🚫"
    message = f"""
=====
Stage: {name}
Status: {smile}{status}{smile}
Link: {url}
=====
"""
    send_message_to_bot(token_id, chat_id, message)

def finish_pipeline(arguments):
    id_pipeline = arguments[2]
    token_id = arguments[3]
    chat_id = arguments[4]
    status = arguments[5]
    now = datetime.now()
    message = f"""
Time: {now.strftime("%H:%M:%S")}
Date: {now.strftime("%m/%d/%Y")}
====== ⏩ Pipeline {id_pipeline} finished ⏪ ======
"""
    send_message_to_bot(token_id, chat_id, message)

if __name__ == "__main__":
    arguments = sys.argv
    if arguments[1] == 'start':
        start_pipeline(arguments)
    elif arguments[1] == 'stage':
        notify_status_stage_to_bot(arguments)
    elif arguments[1] == 'finish':
        finish_pipeline(arguments)
