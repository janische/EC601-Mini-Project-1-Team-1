## System Design      
In out thoughts, major components we will use are searching contents with Twitter search API and analysing the contents of tweets with Google Natural Language API.      

For Python GUI part, we would like an easy-using method. Tkinter is a standard Python interface that shipped with Python, moreover, it outputs the fastest and easiest way to create the GUI applications.     

For Twitter search part, we first found the core thing, “search contents of tweets from desired Twitter account”, we need to adjust our user stories. Comparing with several APIs in Twitter, TwitterSearch API is obviously the most convenient one. It avoids us to parse the search url every time we want to search, also it is pretty easy to use in Python and will give us all the available information we need.     

For Google NL API, since it analysis the feelings and strength of them from the contents of Tweets, it is exactly what we want.      

We made a bunch of unit test for Twitter search and Google NL API during programming. What’s more, we wrote test programs to test the code and changed several test inputs to check whether the result is what we want.     
