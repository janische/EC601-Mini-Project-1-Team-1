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


def average(sentiments):
    num_Tweets = [0, 0, 0]
    total_score = [0, 0, 0]
    total_magnitude = [0, 0, 0]
    sentiment_avgs = [0, 0, 0]
    magnitude_avgs = [0, 0, 0]

    for index, sentence in enumerate(sentiments.sentences):
        sentence_sentiment = sentence.sentiment.score
        sentence_magnitude = sentence.sentiment.magnitude
        if (sentence_sentiment >= 0.25): # positive sentiment
            num_Tweets[0] = num_Tweets[0] + 1
            total_score[0] = total_score[0] + sentence_sentiment
            total_magnitude[0] = total_magnitude[0] + sentence_magnitude
        elif (sentence_sentiment <= -0.25): # negative sentiment
            num_Tweets[1] = num_Tweets[1] + 1
            total_score[1] = total_score[1] + sentence_sentiment
            total_magnitude[1] = total_magnitude[1] + sentence_magnitude
        else:                               # neutral sentiment
            num_Tweets[2]= num_Tweets[2] + 1
            total_score[2] = total_score[2] + sentence_sentiment
            total_magnitude[2] = total_magnitude[2] + sentence_magnitude
    for it in range(0,3):
        if (num_Tweets[it] != 0):
            sentiment_avgs[it] = total_score[it]/num_Tweets[it]
            magnitude_avgs[it] = total_magnitude[it]/num_Tweets[it]

    return sentiment_avgs,magnitude_avgs,num_Tweets


def print_result(results):
    sentiment_avgs,magnitude_avgs,num_Tweets = results
    percent_pos = 100.00*num_Tweets[0]/sum(num_Tweets)
    percent_neg = 100.00*num_Tweets[1]/sum(num_Tweets)
    percent_neu = 100.00*num_Tweets[2]/sum(num_Tweets)
    
    print('The results were {}% positive, {}% negative, and {}% neutral.'.format(
            percent_pos, percent_neg, percent_neu))

    print('Averages for Positive Results: \n Score of {:.2f} with magnitude of {:.2f}'.format(
        sentiment_avgs[0], magnitude_avgs[0]))
    print('Averages for Negative Results: \n Score of {:.2f} with magnitude of {:.2f}'.format(
        sentiment_avgs[1], magnitude_avgs[1]))
    print('Averages for Neutral Results: \n Score of {:.2f} with magnitude of {:.2f}'.format(
        sentiment_avgs[2], magnitude_avgs[2]))
    
    return 0


# [START language_sentiment_tutorial_analyze_sentiment]
def analyze(input_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(input_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    sentiments = client.analyze_sentiment(document=document)

    sentiment_results = average(sentiments)
    print_result(sentiment_results)
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