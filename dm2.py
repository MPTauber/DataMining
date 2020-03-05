import keys
import tweepy

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True) ## there are limits on the amount of data you can get
## this command prevents from us getting banned from twitter for requesting too much data, and notifies us when that happens

'''tweets = api.search(q = "#coronavirus", count = 5) ## q arugment does query on the whole topic
print(tweets)
# this gets displayed as a JSON file and has tpoo much stuff ^

for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text) ## selects the username, then adds :, and thendisplays tweet text

trends_available = api.trends_available()

print(len(trends_available))
print(trends_available[:5])'''

world_trends = api.trends_place(id=2459115) ## id is woeidea which is yahoo's "where on earth" id
'''print(world_trends)'''

trends_list = world_trends[0]["trends"]

print(trends_list[0])

trends_list = [t for t in trends_list if t["tweet_volume"]] ## only values that meet the requirement

from operator import itemgetter
trends_list.sort(key= itemgetter("tweet_volume"), reverse=True) # highest ones first cause reverse

topics = {}

for trend in trends_list:
    topics[trend["name"]] = trend["tweet_volume"]  # makes "name" the key and adds the corresponsindg volume to it 
    
#pip install wordcloud
from wordcloud import WordCloud

wordcloud = WordCloud(
    width = 1600,
    height = 900,
    prefer_horizontal = 0.5,
    min_font_size = 10,
    colormap = "prism",
    background_color = "white"
)

wordcloud = wordcloud.fit_words(topics)
wordcloud = wordcloud.to_file("TrendingTwitter.png")