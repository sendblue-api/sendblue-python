import requests

class Sendblue:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.sendblue.co/api'

    def request(self, endpoint: str, data: dict = None) -> dict:
        url = self.base_url + endpoint
        headers = {
            'sb-api-key-id': self.api_key,
            'sb-api-secret-key': self.api_secret,
            'Content-Type': 'application/json'
        }

        if data:
            response = requests.post(url, headers=headers, json=data)
        else:
            response = requests.get(url, headers=headers)

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
        return self.request('/send-message', data)

    def send_group_message(self, numbers: list[str], content: str, group_id: str = None, send_style: str = None, media_url: str = None, status_callback: str = None):
        data = {
            'numbers': numbers,
            'group_id': group_id,
            'content': content,
            'send_style': send_style,
            'media_url': media_url,
            'status_callback': status_callback
        }
        return self.request('/send-group-message', data)

    def modify_group(self, group_id: str, modify_type: str, number: str):
        data = {
            "group_id": group_id,
            "modify_type": modify_type,
            "number": number
        }
        return self.request('/modify-group', data)

    def lookup(self, number: str):
        return self.request(f'/evaluate-service?number={number}')

    def send_typing_indicator(self, number: str):
        data = {
            'number': number
        }
        return self.request(f'/send-typing-indicator?number={number}', data)
