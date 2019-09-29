# Copyright 2016, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START language_sentiment_tutorial]
"""Demonstrates how to make a simple call to the Natural Language API."""

# [START language_sentiment_tutorial_imports]
import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# [END language_sentiment_tutorial_imports]


def average(sentiments,num_Tweets,total_score,total_magnitude,sentiment_avgs,magnitude_avgs):
    score = sentiments.document_sentiment.score
    magnitude = sentiments.document_sentiment.magnitude
    if (score >= 0.25): # positive sentiment
        num_Tweets[0] = num_Tweets[0] + 1
        total_score[0] = total_score[0] + score
        total_magnitude[0] = total_magnitude[0] + magnitude
    elif (score <= -0.25): # negative sentiment
        num_Tweets[1] = num_Tweets[1] + 1
        total_score[1] = total_score[1] + score
        total_magnitude[1] = total_magnitude[1] + magnitude
    else:                               # neutral sentiment
        num_Tweets[2]= num_Tweets[2] + 1
        total_score[2] = total_score[2] + score
        total_magnitude[2] = total_magnitude[2] + magnitude

def print_result(sentiment_avgs,magnitude_avgs,num_Tweets):
    percent_pos = 100.00*num_Tweets[0]/sum(num_Tweets)
    percent_neg = 100.00*num_Tweets[1]/sum(num_Tweets)
    percent_neu = 100.00*num_Tweets[2]/sum(num_Tweets)
    
    print("\n\n\n")
    print("Out of {} tweets in supported languages, the results were:".format(sum(num_Tweets)))
    print(' {:.2f}% positive, {:.2f}% negative, and {:.2f}% neutral.'.format(
            percent_pos, percent_neg, percent_neu))

    print('\nAverages for Positive Results: \n  Score of {:.2f} with magnitude of {:.2f}'.format(
        sentiment_avgs[0], magnitude_avgs[0]))
    print('Averages for Negative Results: \n  Score of {:.2f} with magnitude of {:.2f}'.format(
        sentiment_avgs[1], magnitude_avgs[1]))
    print('Averages for Neutral Results: \n  Score of {:.2f} with magnitude of {:.2f}'.format(
        sentiment_avgs[2], magnitude_avgs[2]))
    
    return 0


# [START language_sentiment_tutorial_analyze_sentiment]
def analyze(input_filename):
    num_Tweets = [0, 0, 0]
    total_score = [0, 0, 0]
    total_magnitude = [0, 0, 0]
    sentiment_avgs = [0, 0, 0]
    magnitude_avgs = [0, 0, 0]
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(input_filename, 'r') as tweets_file:
        # Instantiates a plain text document.
        content = tweets_file.read()
    start_index = 0
    end_index = 0
    while (True):
        end_index = content.find("This tweet ends.",start_index)
        if end_index == -1:
            break
        tweet = content[start_index:end_index]
        start_index = end_index + len("This tweet ends.")
        document = types.Document(
            content=tweet,
            type=enums.Document.Type.PLAIN_TEXT)
        try:
            sentiments = client.analyze_sentiment(document=document)
        except:
            continue
        average(sentiments,num_Tweets,total_score,total_magnitude,sentiment_avgs,magnitude_avgs)
    for it in range(0,3):
        if (num_Tweets[it] != 0):
            sentiment_avgs[it] = total_score[it]/num_Tweets[it]
            magnitude_avgs[it] = total_magnitude[it]/num_Tweets[it]
    if (sum(num_Tweets) == 0):
        print("\n\n\nThere were no results.")
    else:
        print_result(sentiment_avgs,magnitude_avgs,num_Tweets)
# [END language_sentiment_tutorial_analyze_sentiment]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'input_filename')
    args = parser.parse_args()

    analyze(args.input_filename)
# [END language_sentiment_tutorial]