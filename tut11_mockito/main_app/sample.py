import requests


def get_text(url):
    res = requests.get(url)
    if 200 <= res.status_code < 300:
        return res.text
    return None


class Dog:
    def bark(self):
        return 'Wuff'

    def action(self,action,command="sit"):
        return action + command