import requests

class Sendblue:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.base_url = 'https://api.sendblue.co'
        self.session = requests.Session()
        self.session.headers = {
            'sb-api-key-id': api_key,
            'sb-api-secret-key': api_secret,
            'Content-Type': 'application/json'
        }
    
    def request(self, method: str, endpoint: str, data: dict = None):
        url = self.base_url + endpoint
        response = self.session.request(method, url, json=data)
        try:    
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e, response.text)
        return response.json()

    def send_message(self, number: str, content: str, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'number': number,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        return self.request('post', '/api/send-message', data)

    def send_group_message(self, numbers: list[str], content: str, group_id: str = None, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'numbers': numbers,
            'group_id': group_id,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        return self.request('post', '/api/send-group-message', data)

    def get_message(self, message_id: str):
        return self.request('get', f'/api/message/{message_id}')

    def modify_group(self, group_id: str, modify_type: str, number: str):
        data = {
            "group_id": group_id,
            "modify_type": modify_type,
            "number": number
        }
        return self.request('post', '/modify-group', data)

    def lookup(self, number: str):
        return self.request('get', f'/api/evaluate-service?number={number}')

    def send_typing_indicator(self, number: str):
        data = {
            'number': number
        }
        return self.request('post', f'/api/send-typing-indicator?number={number}', data)
    
    def get_contacts(self):
        return self.request('get', '/accounts/contacts')

    def create_contact(self, number: str, first_name: str = None, last_name: str = None, company_name: str = None):
        data = {
            'number': number,
            'firstName': first_name,
            'lastName': last_name,
            'companyName': company_name
        }
        return self.request('post', '/accounts/contacts', data)

    def delete_contact(self, contact_id: str):
        return self.request('delete', f'/accounts/contacts/{contact_id}')

    def get_messages(self, contact_id: str):
        return self.request('get', f'/accounts/messages?cid={contact_id}')