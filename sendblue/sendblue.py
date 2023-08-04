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

    def send_message(self, number: str, content: str, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'number': number,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        url = self.base_url + '/api/send-message'
        response = self.session.post(url, data)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()

    def send_group_message(self, numbers: list[str], content: str, group_id: str = None, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'numbers': numbers,
            'group_id': group_id,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        url = self.base_url + '/api/send-group-message'
        response = self.session.post(url, data)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()

    def modify_group(self, group_id: str, modify_type: str, number: str):
        data = {
            "group_id": group_id,
            "modify_type": modify_type,
            "number": number
        }
        url = self.base_url + '/modify-group'
        response = self.session.post(url, data)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()

    def lookup(self, number: str):
        url = self.base_url + f'/api/evaluate-service?number={number}'
        response = self.session.get(url)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()

    def send_typing_indicator(self, number: str):
        data = {
            'number': number
        }
        url = self.base_url + f'/api/send-typing-indicator?number={number}'
        response = self.session.post(url, data)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()
    
    def get_contacts(self):
        url = self.base_url + '/accounts/contacts'
        response = self.session.get(url)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()

    def create_contact(self, number: str, first_name: str = None, last_name: str = None, company_name: str = None):
        data = {
            'number': number,
            'first_name': first_name,
            'last_name': last_name,
            'company_name': company_name
        }
        url = self.base_url + '/accounts/contacts'
        response = self.session.post(url, data)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()

    def delete_contact(self, contact_id: str):
        url = self.base_url + '/accounts/contacts/{contact_id}'
        response = self.session.delete(url)
        if not response.ok:
            raise Exception("Error: " + response.text)
        else:
            return response.json()