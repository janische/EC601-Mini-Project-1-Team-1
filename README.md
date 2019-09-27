# EC602-Mini-Project-1    

## Build a system for running our application   
### Environment   

### Packages needed   

READM of how to build your system.


## Below parts should be in seperate file!  
### Target Users

### MVP 

### User interface (python GUI if possible)

### User story
#### Jonathan's part.   
We, Popeyes (a multinational fast-food restaurant chain), want to know the sentiment (score and magnitude) of tweets about our new burger (chicken sandwich) in the time from when we introduced it until now so that we can determine whether to continue this menu item, and if so, whether it needs to be modified to be made better.

We, a small family-owned restaurant, want to know the sentiment of tweets about some of our menu items over the past several weeks so that we can get rid of the least-liked items as we try to streamline our menu.

We, a regional restaurant chain whose biggest competition is a national chain in our region, want to know the sentiment of tweets about some of our competitor's menu items so that we can add better versions of those items to our menu to become the dominant chain in our region.

### Architecture Flowsheet
#### Zhou's part.
Load data from popeyes twitter account through tweepy API    
Extract needed information (people's comments about popeyes' new burger) from result    
Import information to Google Natural Language API   
Get results of people's sentiment from Google NL API     
![Architecture Image](img/FlowChart.PNG )    

### Write examples to use at least to get twitter feed and get results from one of the Google modules.
Please go to see tweepyTest1.py for our twitter feed, sentiment_analysis.py for Google API.        

