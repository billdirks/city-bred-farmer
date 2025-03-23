import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import sys

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    """Authenticate using data in token.json, generating if necessary.
    
    Token is generated from credentials in credentials.json.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_message_id(service, user_id='me', subject=''):
    """Return id of the first email matching the subject."""
    try:
        response = service.users().messages().list(userId=user_id,
                                                   q=f'subject:"{subject}"').execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        for message in messages[:1]:  # Limit to first email
            return message['id']
    except HttpError as error:
        print(f'An error occurred: {error}')

def download_attachments(service, user_id='me', msg_id=''):
    """Download attachments from a specified message."""
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        for part in message['payload']['parts']:
            if 'filename' in part and part['filename'] != '':
                # Check if the attachmentId is present
                if 'attachmentId' in part['body']:
                    attachment_id = part['body']['attachmentId']
                    filename = part['filename']
                    print(f"Downloading {filename}...")
                    attachment = service.users().messages().attachments().get(
                        userId=user_id, messageId=msg_id, id=attachment_id).execute()
                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                    with open(filename, 'wb') as f:
                        f.write(file_data)
                elif part['body'].get('data'):
                    # Handle inline attachments or parts with data
                    file_data = base64.urlsafe_b64decode(part['body']['data'].encode('UTF-8'))
                    filename = part['filename']
                    print(f"Downloading {filename}...")
                    with open(filename, 'wb') as f:
                        f.write(file_data)
            elif 'parts' in part:
                for sub_part in part['parts']:
                    if 'filename' in sub_part and sub_part['filename'] != '':
                        # Check if the attachmentId is present
                        if 'attachmentId' in sub_part['body']:
                            attachment_id = sub_part['body']['attachmentId']
                            filename = sub_part['filename']
                            print(f"Downloading {filename}...")
                            attachment = service.users().messages().attachments().get(
                                userId=user_id, messageId=msg_id, id=attachment_id).execute()
                            file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                            with open(filename, 'wb') as f:
                                f.write(file_data)
                        elif sub_part['body'].get('data'):
                            # Handle inline attachments or parts with data
                            file_data = base64.urlsafe_b64decode(sub_part['body']['data'].encode('UTF-8'))
                            filename = sub_part['filename']
                            print(f"Downloading {filename}...")
                            with open(filename, 'wb') as f:
                                f.write(file_data)

    except HttpError as error:
        print(f'An error occurred: {error}')

def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    
    subject = sys.argv[1]
    #subject = input("Enter the email subject to search for attachments: ")
    msg_id = get_message_id(service, subject=subject)
    
    if msg_id:
        download_attachments(service, msg_id=msg_id)
    else:
        print(f"No email found with subject: {subject}")

if __name__ == '__main__':
    main()