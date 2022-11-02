

import requests
import json

class Sendblue:
    def __init__(self, api_key, api_secret, opts={}):
        self.api_key = api_key
        self.api_secret = api_secret
        self.log_level = opts.get('log_level', 'info')
        self.base_url = "https://api.sendblue.co/api"

    def request(self, endpoint, method, data={}):
        url = self.base_url + endpoint
        headers = {
            'sb-api-key-id': self.api_key,
            'sb-api-secret-key': self.api_secret,
            'Content-Type': 'application/json'
        }

        if (self.log_level == 'debug'):
            print('Sending request to ' + url)
            print('Headers: ' + json.dumps(headers))
            print('Data: ' + json.dumps(data))

        if method == 'get':
            r = requests.get(url, headers=headers)
        elif method == 'post':
            r = requests.post(url, headers=headers, data=json.dumps(data))
        else:
            raise Exception("Invalid method: " + method)
        
        if r.status_code < 200 and r.status_code > 299:
            raise Exception("Error: " + r.text)
        return r.json()

    def send_message(self, number, opts={}):
        data = {
            'number': number,
        }
        if (opts.get('content')):
            data['content'] = opts.get('content')
        if (opts.get('media_url')):
            data['media_url'] = opts.get('media_url')
        if (opts.get('status_callback')):
            data['status_callback'] = opts.get('status_callback')
        if (opts.get('send_style')):
            data['send_style'] = opts.get('send_style')

        data.update(opts)
        return self.request('/send-message', 'post', data)

    def send_group_message(self, opts={}):
        data = {}

        if (opts.get('numbers')):
            data['numbers'] = opts.get('numbers')
        if (opts.get('group_id')):
            data['group_id'] = opts.get('group_id')
        if (opts.get('content')):
            data['content'] = opts.get('content')
        if (opts.get('media_url')):
            data['media_url'] = opts.get('media_url')
        if (opts.get('status_callback')):
            data['status_callback'] = opts.get('status_callback')
        if (opts.get('send_style')):
            data['send_style'] = opts.get('send_style')

        data.update(opts)
        return self.request('/send-group-message', 'post', data)
