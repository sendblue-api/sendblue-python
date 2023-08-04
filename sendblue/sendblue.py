import requests

class Sendblue:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.sendblue.co'

    def request(self, endpoint: str, method: str, data: dict = None) -> dict:
        url = self.base_url + endpoint
        headers = {
            'sb-api-key-id': self.api_key,
            'sb-api-secret-key': self.api_secret,
            'Content-Type': 'application/json'
        }

        if method == 'get':
            response = requests.get(url, headers=headers, json=data)
        elif method == 'post':
            response = requests.post(url, headers=headers, json=data)
        elif method == 'put':
            response = requests.put(url, headers=headers, json=data)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, json=data)

        if not response.ok:
            raise Exception("Error: " + response.text)

        return response.json()

    def send_message(self, number: str, content: str, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'number': number,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        return self.request('/api/send-message', 'post', data)

    def send_group_message(self, numbers: list[str], content: str, group_id: str = None, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'numbers': numbers,
            'group_id': group_id,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        return self.request('/api/send-group-message', 'post', data)

    def modify_group(self, group_id: str, modify_type: str, number: str):
        data = {
            "group_id": group_id,
            "modify_type": modify_type,
            "number": number
        }
        return self.request('/modify-group', 'post', data)

    def lookup(self, number: str):
        return self.request(f'/api/evaluate-service?number={number}', 'get')

    def send_typing_indicator(self, number: str):
        data = {
            'number': number
        }
        return self.request(f'/api/send-typing-indicator?number={number}', 'post', data)
    
    def get_contacts(self):
        return self.request('/accounts/contacts', 'get')

    def create_contact(self, number: str, first_name: str = None, last_name: str = None, company_name: str = None):
        data = {
            'number': number,
            'first_name': first_name,
            'last_name': last_name,
            'company_name': company_name
        }
        return self.request(f'/accounts/contacts', 'post', data)

    def delete_contact(self, contact_id: str):
        return self.request(f'/accounts/contacts/{contact_id}')