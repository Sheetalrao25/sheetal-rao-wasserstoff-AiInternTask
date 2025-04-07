from authenticate import authenticate_gmail
import base64
import sqlite3
from email import message_from_bytes
from database import store_email_to_db

def get_message_details(service, msg_id):
    try:
        msg = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()
        raw_msg = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
        mime_msg = message_from_bytes(raw_msg)

        email_id = msg_id
        thread_id = msg.get('threadId', '')
        subject = mime_msg['subject']
        sender = mime_msg['from']
        recipient = mime_msg['to']
        date = mime_msg['date']
        body = msg.get('snippet', '')

        return email_id, thread_id, subject, sender, recipient, date, body
    except Exception as e:
        print(f"Failed to parse message {msg_id}: {e}")
        return None

def fetch_and_store_emails(service, label='INBOX', max_results=5):
    results = service.users().messages().list(userId='me', labelIds=[label], maxResults=max_results).execute()
    messages = results.get('messages', [])

    print(f"\nFound {len(messages)} messages.")
    
    for message in messages:
        details = get_message_details(service, message['id'])
        if details:
            store_email_to_db(*details)
            print(f"Stored email: {details[2]} from {details[3]}")

if __name__ == '__main__':
    service = authenticate_gmail()
    if service:
        fetch_and_store_emails(service)
    else:
        print("Failed to authenticate Gmail API.")
