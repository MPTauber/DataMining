##py -3 -m venv dm_venv
## dm_venv/scripts/activate
## pip install tweepy
import keys ### imports keys file (txt files saved as py)
import tweepy

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True) ## there are limits on the amount of data you can get
## this command prevents from us getting banned from twitter for requesting too much data, and notifies us when that happens

user = api.get_user("CJTauber")

print(user.name)
print(user.status.text)

print(user.followers_count)
print(user.friends_count)

#me = api.me() ### shows all the info about my own (madetau_tweets)
#print(me)

followers = []
cursor = tweepy.Cursor(api.followers, screen_name = 'madetau_tweets')

for account in cursor.items(10):
    followers.append(account.screen_name)
#print(followers)

#print('Followers:',' '.join(followers))  ### this makes the output just look like a sentence (without [] and '' and ,)

print('Followers:', ' '.join(sorted(followers, key = lambda s: s.lower()))) 

friends = []
for account in cursor.items(10):
    friends.append(account.screen_name)

print('Friends:', ' '.join(sorted(friends, key = lambda s: s.lower()))) 



tweets = api.user_timeline(screen_name= 'ericakaze', count=3)

for tweet in tweets:
    print(tweet.text, '\n')

