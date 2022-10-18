
# https: // exactsolutions.co.jp/column/rpa/python-twitterapi-tweet/ Tweet
# https: // penguinchord.com/blog/python/twitter-api-v2-get-sample 自分のTweet
import datetime
from time import sleep
from requests_oauthlib import OAuth1Session
import json
import auth


def post_tweet(param_text: str):
    # ツイート処理の関数
    today = datetime.datetime.now()
    edited_text = str(today)

    api = auth.define_client()
    resource_url = r'https://api.twitter.com/2/tweets'  # エンドポイントURL

    params = {
        "text": edited_text + param_text
    }

    res = api.post(resource_url, json=params)
    dict_results = {'code': res.status_code,
                    'response': res.json()}

    return dict_results


def UserTweet(Uid):
    url = f"https://api.twitter.com/2/users/{Uid}/tweets"

    params = {
        'expansions': 'author_id',
        'tweet.fields': 'created_at,public_metrics',
        'user.fields': 'name',
        'max_results': 15,
    }

    res = auth.define_client().get(url, params=params)
    data = json.loads(res.text)
    # print(data["data"])
    for d in data["data"]:
        print(d["text"])


if __name__ == '__main__':
    post_tweet("テスト")
    UserTweet(auth.Uid)
