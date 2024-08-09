import requests
import json
import time

def get_tweets(username, cookie, csrf, cursor=None):
    # If no cursor is provided, create variables for the initial query
    if cursor is None:
        variables = {
            "rawQuery": f"{username}",
            "count": 20,
            "querySource": "typed_query",
            "product": "Top"
        }
    else:
        # If a cursor is provided, use it for pagination
        variables = {
            "rawQuery": f"{username}",
            "count": 20,
            "cursor": cursor,
            "querySource": "typed_query",
            "product": "Top"
        }

    # Define the features for the API request
    features = {
        "rweb_tipjar_consumption_enabled": True,
        "responsive_web_graphql_exclude_directive_enabled": True,
        "verified_phone_label_enabled": False,
        "creator_subscriptions_tweet_preview_api_enabled": True,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "communities_web_enable_tweet_community_results_fetch": True,
        "c9s_tweet_anatomy_moderator_badge_enabled": True,
        "articles_preview_enabled": True,
        "tweetypie_unmention_optimization_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "longform_notetweets_consumption_enabled": True,
        "responsive_web_twitter_article_tweet_consumption_enabled": True,
        "tweet_awards_web_tipping_enabled": False,
        "creator_subscriptions_quote_tweet_preview_enabled": False,
        "freedom_of_speech_not_reach_fetch_enabled": True,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
        "rweb_video_timestamps_enabled": True,
        "longform_notetweets_rich_text_read_enabled": True,
        "longform_notetweets_inline_media_enabled": True,
        "responsive_web_enhance_cards_enabled": False
    }

    # Define the URL for the API endpoint
    main_url = 'https://x.com/i/api/graphql/TQmyZ_haUqANuyBcFBLkUw/SearchTimeline'
    
    # Set up parameters by converting variables and features to JSON
    params = {
        "variables": json.dumps(variables),
        "features": json.dumps(features)
    }

    # Set up the headers including the necessary authorization and cookies
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "tr-TR,tr;q=0.9",
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "Content-Type": "application/json",
        "Cookie": cookie,
        "Referer": "https://x.com/search?q=Destek%20lang%3Atr%20-filter%3Areplies&src=typed_query&f=user",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
        "X-Csrf-Token": csrf,
        "X-Twitter-Active-User": "yes",
        "X-Twitter-Auth-Type": "OAuth2Session",
        "X-Twitter-Client-Language": "tr"
    }

    # Send the GET request to the API endpoint
    response = requests.get(main_url, params=params, headers=headers)

    if response.status_code == 200:
        # Parse the response to extract tweet data
        info = response.json()['data']['search_by_raw_query']['search_timeline']['timeline']['instructions']
        
        tweet_list = []
        
        try:
            entries = info[0]['entries']
        except KeyError:
            print('Key Error')
            return None
        
        # Iterate through entries to find tweets
        for i in entries:
            if 'tweet' in i['entryId']:
                try:
                    tweet = i['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
                    tweet_list.append(tweet.replace('\n', '') + '\n')
                except KeyError:
                    print('Damaged Data')
                    continue

            elif 'cursor-bottom' in i['entryId'] or 'entry_id_to_replace' in i['entryId']:
                cursor = i['content']['value']
                return tweet_list, cursor
            
        # Handle pagination cursor for the next batch of tweets
        cursor = info[2]['entry']['content']['value']
        
        return tweet_list, cursor

    else:
        # Handle rate limits and authentication errors
        if 'Rate limit exceeded.' in response.text or 'Could not authenticate you' in response.text:
            return 'rate'
        print(response.text)
        return None
    
# Load the list of Twitter accounts to be scraped. You can append via list.
with open(r'Twitter Support Accounts 100x.json', 'r', encoding='UTF-8') as read_file:
    userlist = json.load(read_file)

# Load the cookies and CSRF tokens for authentication
with open(r'materials.json', 'r', encoding='UTF-8') as load_material:
    coo_csrf = json.load(load_material)

account = 0
cursor = None

# Loop through each user in the userlist
for user in userlist:
    i = 0

    # Attempt to fetch up to 25 pages of tweets for each user
    while i <= 25:
        username = user['screen_name']
        cookie = coo_csrf['data'][account]['cookie']
        csrf = coo_csrf['data'][account]['csrf']

        result = get_tweets(username, cookie, csrf, cursor)
        print(f'{str(i)}. => {username}')
        
        if result:
            if 'rate' in result:
                # Switch accounts if rate limit is reached
                print('Account Changing. Remaining Account Count:', str(len(coo_csrf['data']) - account))
                account += 1
                continue

            tweet_list, cursor = result
            
            # Save the fetched tweets to a file
            with open('Tweets.txt', 'a', encoding='UTF-8') as save_file:
                save_file.writelines(tweet_list)
            
            i += 1
        else:
            print(result)
            # break if an error occurs
            #break
