'''
'auth.py' sample.
Input your credential and make this file name 'auth.py'
'''

from requests_oauthlib import OAuth1Session
CLIENT = {
    'API_KEY': 'xxxxxxx',
    'API_KEY_SECRET': 'xxxxxxx',
    'ACCESS_TOKEN': 'xxxxxxx',
    'ACCESS_TOKEN_SECRET': 'xxxxxxx',
}

Uid = "xxxxxxx"  # 自分のUserID

# Not Used in this repository.
bearer_token = "xxxxxxxxxxxxxxxxxxxxx"


def define_client():
    # api接続の関数
    AK = CLIENT['API_KEY']
    AKS = CLIENT['API_KEY_SECRET']
    AT = CLIENT['ACCESS_TOKEN']
    ATS = CLIENT['ACCESS_TOKEN_SECRET']

    return OAuth1Session(AK, AKS, AT, ATS)
