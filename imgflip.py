import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

class ImgFlipCreator:
    def __init__(self):
        super().__init__()
        self.username = os.getenv('IMGFLIP_USERNAME')
        self.password = os.getenv('IMGFLIP_PASSWORD')
        self.memes = {
            'distracted_bf': {'template_id' : 112126428},
            'confused_cat': {'template_id' : 188390779},
            'drakepost' : {'template_id' : 181913649},
            'modern_problems' : {'template_id' : 161887818},
            'two_buttons' : {'template_id' : 87743020},
            'smile' : {'template_id' : 27813981},
        }
    def create(self, meme, top, bottom, extra=None):
        url = "https://api.imgflip.com/caption_image"
        data = {
            'template_id':self.memes[meme]['template_id'],
            'username':self.username,
            'password':self.password,
            'boxes[0][text]':top,
            'boxes[1][text]':bottom,
            'boxes[2][text]':extra,
        }
        try:
            r = requests.post(url = url, data = data)
        except Exception as e:
            raise Exception('Error requesting the service.')
        try:
            result = json.loads(r.text)
        except:
            msg = 'Unexpected response format: (%s)' % r.text
            raise Exception(msg)
        if not result['success']:
            msg = 'Unexpected response: (%s)' % r.text
            raise Exception(msg)
        result_url = result["data"]["url"]
        return result_url