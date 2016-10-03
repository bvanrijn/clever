import requests
import json


class CleverBot(object):
    """
    >>> import clever
    >>> client = clever.CleverBot(user='...', key='...')
    >>> client.query("Hi")
    """
    def __init__(self, user, key, nick=None):
        self.user = user
        self.key = key
        self.nick = nick
        
        body = {
            'user': user,
            'key': key,
            'nick': nick
        }

        requests.post('https://cleverbot.io/1.0/create', json=body)
        
    def query(self, text=''):
        body = {
            'user': self.user,
            'key': self.key,
            'nick': self.nick,
            'text': text
        }

        r = requests.post('https://cleverbot.io/1.0/ask', json=body)
        r = json.loads(r.text)

        if r['status'] == 'success':
            return r['response']
        else:
            return r['status']
