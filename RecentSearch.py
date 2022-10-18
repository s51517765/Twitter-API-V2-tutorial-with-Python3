import requests
import json
import auth

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {    'query': '(from:twitterdev -is:retweet) OR #twitterdev', 'tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Not Used in this rep.
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {auth.bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    #response = requests.get(url, auth=bearer_oauth, params=params)
    response = auth.define_client().get(url, params=params)
    print("【Response status code】", response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main(keyword):
    query_params = {'query': keyword}
    json_response = connect_to_endpoint(search_url, query_params)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    for d in json_response["data"]:
        print("【Tweet ID】", d["id"])
        print(d["text"])
        print("---------------------------------------------------")


if __name__ == "__main__":
    main("電子工作")
