# -*- coding: utf-8 -*-
from base64 import encode
import requests
import json
import auth

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = auth.bearer_token


def create_url(user_id):
    # Replace with user ID below
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Not Used in this rep.
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    #response = requests.request("GET", url, auth=bearer_oauth, params=params)
    response = auth.define_client().get(url, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    print(response.encoding)
    return response.json()


def main(user_id):
    url = create_url(user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    for d in json_response["data"]:
        print("【Tweet ID】", d["id"])
        print(d["text"])
        print("---------------------------------------------------")


if __name__ == "__main__":
    main(auth.Uid)
