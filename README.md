# IBMHC20
**Sentiment Analysis of COVID-19 Tweets – Visualization Dashboard**

![1_vp1M37AGMOFwCvLxVm62IA](https://user-images.githubusercontent.com/52466713/87548081-a0663380-c6c9-11ea-858c-20246ca1c6b5.jpeg)

**Background**

The severe outbreak of Covid-19 pandemic has affected many countries across the world, and disrupted the day to day activities of many people. During such outbreaks, understanding the emotional state of citizens of a country could be of interest to various organizations to carry out tasks and to take necessary measures. Several studies have been performed on data available on various social media platforms and websites to understand the emotions of people against many events, inclusive of Covid-19, across the world. Twitter and other social media platforms have been bridging the gap between the citizens and government in various countries and areof more prominence in India. 
The sentiment analysis of Indians after the extension of lockdown announcements to be analyzed with the relevant #tags on twitter and build a predictive analytics model to understand the behavior of people if the lockdown is further extended.Also develop a dashboard with visualization of people reaction to the govt announcements on lockdown extension.

**Aim of the Project**

The aim of this project is to create an ineractive web based COVID-19 Sentiment Analyser. The primary goal is to develop a space where everyone can visualize the impact of COVID-19 on human society in easy and simpler way.This helps to realize how the sentiment of people changes during this time of COVID-19.It will enable visitors to learn impact of COVID-19 by interacting with graphs,maps,charts and other interactive elements as they proceed through the web.
To develop a twitter sentiment analysis model to understand the following:

_1. Get to know people’s sentiment towards the epidemic_

_2. Understand the sentiments of people on govt. decision to extend the lockdown_

Twitter and other social media platforms have been bridging the gap between the citizens and government in various countries and are of more prominence in India. Sentiment Analysis of posts on twitter is observed to accurately reveal the sentiments. Analysing real time posts on twitter in India during Covid-19, could help in identifying the mood of the nation.

**Idea General Description**

It is live dashboard of streamed twitter tweets, filtered by your own key words with applying sentiment analysis of tweets. Sentiment analysis is for classifying on positve and negative tweets. Store them in local database, and then creates a dashbord with live charts.

Twitter is a micro blogging and social networking service on which users post and interact with messages known as "tweets". It’s a great platform to exchange such great Ideas. 
As now the World is struggling to deal with pandemic disease called Novel Coronavirus (COVID-19). During this lockdown period, people have taken social networks as the medium to express their feelings and find a way to calm themselves down.
In our proposed idea a country wise sentiment analysis of the tweets related to COVID-19 will be done by using python algorithms which is running as at backend server. In this, tweets from all countries will be gathered at a particular time duration , and which are related to COVID19 in some or the other way. It will analyse how the citizens of different countries are dealing with this situation. The tweets will be collected, pre-processed, and then used for text mining and sentiment analysis with the help of python libraries like tweepy, nltk, pandas data frame, textblob and some more.
The output will be represented in the form of Visual Dashboard on a proposed webpage that’ll display how the people throughout the world are taking this COVID-19.Positive , negative and Neutral approaches ,also the instances of fear, sadness and disgust all will be represented in it.

This website was built using React and also uses mapbox to show maps layered by the the markers having tooltips showing the current status due to COVID-19. Website uses ChartJS to represent data fetched using axios form NovelCOVID API. Apart from just representing data fetched from API in charts, this Website also done Sentiment Analysis over the tweets of people for span of 30 days to learn more about imapct of COVID-19 on us. The sentiment analysis is done over 300,000 tweets globaly and has been represented interactively using line graphs and Pie Chart.

->Historical scatter moving average chart. With dynamic historical window size.

->Pie chart, which shows positive/negative partition by count. Also availble to control historical period.

->Live table with tweets.

->Possible to change list of 'key words', in Config.py

**Novelty**

In our proposed solution we are developing a user friendly webpage which has the feature of time –flexibilty i.e. it take the users desired time period for the sentiment analysis on COVID19 ,duration during which the user wants to know the reaction of public.This’ll help to analyse and monitor the public reaction during any particular case period. For eg. If the government wants to know the opinion of opening of schools from the parents in a week , if the government is imposing any new policies what is the reaction of its citizens ,it can be detected after a two or three week of its implementation etc.
The website is user friendly easy to handle and has Well Planned Information Architecture that will provide a detailed overall responses of the people towards the defined topics.

![2](https://user-images.githubusercontent.com/52466713/87548246-da373a00-c6c9-11ea-9cfb-34598ec50e28.jpg)

**Business / Social Impact**

Sentiment analysis dashboard represents the overall responses of the people towards any defined topics. It will help the government and organizations for better implementation of any new policy by knowing the responses about the existing policies from their citizens responses.
It will help the government to know their citizen’s opinion about any their particular decisions, any case or any situation. Like during this pandemic situation it would be a best tool for knowing how the people of a country are dealing with this contagious virus and what their views toward the extension of lockdown according to the received data i.e. whether they are satisfied or not and also in any other subjects.
This will lead to increase the mutual understanding and harmony between government and their people. Also helps the other agencies and citizens to know opinions and views on any topic as it reach a large number of people quickly through tweets and retweets.

**Technology Stack**

_Frontend_:  A simple user friendly webpage will be created by using HTML, CSS and JavaScript for the convenience of the user. The user has to put their desired time period for the sentiment analysis on COVID19 or for the sentiments of LOCKDOWN extension tweets and after that just click on given START button.

_Backend_:  After clicking on START button the command has been transferred to the to the localhost server i.e our python algorithms. It will fetch the tweets related to COVID19 for this we use twitter API configuration .Now after fetching, Tokenization, filtration/Cleaning, removing stop words and Classification of tweets proceeded by using the python algorithm which is applied at the backend and then it generates the output sentiments with the help of three variables positive, negative and neutral then return these values to the webpage.

**Technologies & Tools**	

Python 3.6,pandas,threading,sqlite3,textblob,tweepy,plotly,dash,dash-html-components,dash-core-componentsIBM Watson Studio, Herokuapp  Deployment, Any Web frameworks.


**Scope of Work**

The proposed idea has implemented on the local host by using FLASK web framework so it can be accessible in that particular system only. But doing further some more research it could work on live cloud servers like IBM cloud and would make it easily accessible across the globe through world wide web services in any platform and devices. 
Also we can add options like to perform sentiment analysis on any other topics just by typing the keyword of it. Also more effective types of dashboard visualization can be plotted.
Also it’s essential to identify fake tweets as well to stop the spreading of false information among people.

**Youtube Video Link** : 

![1_vp1M37AGMOFwCvLxVm62IA](https://user-images.githubusercontent.com/52466713/87548081-a0663380-c6c9-11ea-858c-20246ca1c6b5.jpeg)
