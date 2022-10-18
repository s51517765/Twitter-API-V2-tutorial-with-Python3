from requests_oauthlib import OAuth1Session
import json
import auth


def main(tweet_id):
    payload = {"tweet_id": str(tweet_id)}

    oauth = auth.define_client()
    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/users/{}/retweets".format(auth.Uid), json=payload
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == '__main__':
    main(1582265720284774401)
