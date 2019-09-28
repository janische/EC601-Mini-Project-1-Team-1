# EC602-Mini-Project-1     

## How to build a our system        
### Environment   
Linux / Windows / Mac operating system that can run Python program works.      

### Packages needed   
<b> Twitter </b>     
You need to download searchtweets library through Pypi:    
pip install searchtweets               
Or you can install the development version locally via:   
git clone https://github.com/twitterdev/search-tweets-python   
cd search-tweets-python   
pip install -e .     

<b> Google </b>   
Install Google Natural language api for Python       
pip install --upgrade google-cloud-language        

<b> Tkinter </b>   
Package for Python GUI use.   
Just import tkinter or use "from tkinter import * " is fine.


### User story   
We, Popeyes (a multinational fast-food restaurant chain), want to know the sentiment (score and magnitude) of tweets about our new burger (chicken sandwich) in the time from when we introduced it until now so that we can determine whether to continue this menu item, and if so, whether it needs to be modified to be made better.

We, a small family-owned restaurant, want to know the sentiment of tweets about some of our menu items over the past several weeks so that we can get rid of the least-liked items as we try to streamline our menu.

We, a regional restaurant chain whose biggest competition is a national chain in our region, want to know the sentiment of tweets about some of our competitor's menu items so that we can add better versions of those items to our menu to become the dominant chain in our region.

### Architecture Flowsheet
Load data from popeyes twitter account through tweepy API    
Extract needed information (people's comments about popeyes' new burger) from result    
Import information to Google Natural Language API   
Get results of people's sentiment from Google NL API     
![Architecture Image](img/FlowChart.PNG )    
  

