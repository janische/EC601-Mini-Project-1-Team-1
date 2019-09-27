from TwitterSearch import *
import sys

# which account would like to search
accountName = input("Please type account name you would like to search for \n")

# keywords for search
key1 = input("Please type 3 keywords would like to search for in Twitter, first one \n")
key2 = input("Please type 3 keywords would like to search for in Twitter, second one \n")
key3 = input("Please type 3 keywords would like to search for in Twitter, third one \n")

# how many tweets needed
numberTweets = input("Please type how many tweets needed, recommend: less than 100 will be appreciated! \n")

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tuo = TwitterUserOrder(accountName) # create a TwitterUserOrder
    # use parameters instead of fixed string
    tso.set_keywords([key1,key2, key3]) # let's define all words we would like to have a look for
    #tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # optional: limit the range of time, no need here
    # most recent tweets 
    # 8/27/2019 is the date burgers come out


    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        #Twitter API credentials
        #warning!!!!
        #Before upload to GIthub, replace them!!!
        consumer_key = "Mine",
        consumer_secret = "Mine",
        access_token = "Mine",
        access_token_secret = "Mine"
     )

    #write tweet objects to txt/Json file
    file = open('searchTweetOutput.txt', 'w+') 
    print ("Writing tweet objects to txt, please wait...")
    num = 0; #record for number of tweets we have
    numberTweet = int (numberTweets)
    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        if num <= numberTweet:
            # exclude the retweet
            if (not tweet['retweeted']) and ('RT @' not in tweet['text']):
                #file.write('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
                file.write('%s tweeted: %s . This tweet ends. \n' % ( tweet['user']['screen_name'], tweet['text'] ))
                num += 1
        else:
            result = numberTweets + " tweets we have now."
            file.write(result)
            print(numberTweets, " tweets we have now")
            break

    
    #close the file
    print ("Done")
    file.close()
    
    """
    num = 0; #record for number of tweets we have
    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        if num <= 100:
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            num += 1
        else:
            print("100 tweets we have now")
            break
    """

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
