# Heroku Demo | Deploying a Twitter Bot

##### Description 

In mid-2016 I built at Twitter bot, @findmyatm. Through that process I learned how to deploy a web-based application running continuously on a remote server via Heroku. I wanted to share that knowledge, so I helped a few keen friends with the basics. I created this repository to help demostrate the fundamentals for deploying a program on Heroku using a simple Twitter bot. I hope it will also help anyone looking to quickly learn how to remotely deploy a program.


##### Fundamentals 

* run.py - This is the main file in this directory. It will connect to a Twitter account and every 30 seconds generate a tweet based on Philip K. Dick's Second Variety. It uses a Markov Chain generator to create the tweets. 
* Procfile - This file tells Heroku what kind of program is being executed ('web' or 'worker') and what command to starts the program.
* runtime.txt - This file tells Heroku what program language it needs to use. 
* requirements.txt - This file tells Heroku what dependancies (i.e. non-standard python libraries) are required. 


##### Directions

* Sign up to [Herkou's free-tier](https://signup.heroku.com/dc)
* Create a new Twitter account or be ready to use your current account
* Create a [Twitter 'app'](https://apps.twitter.com/) and obtain Twitter API authentication keys - both consumer keys and access token keys
* Clone this directory and update the keys.py file with Twitter API authentication keys
* Don't forget to commit changes to your git repository!
* Download [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
* Navigate to the cloned directory in command line, log into Heroku and create a dyno with the 'create heroku' command
* Push files to Heroku with the command 'git push herokku master'
* Heroku will then initialize Python along with dependant libraries
* Turn the program on using the 'heroku ps:scale worker=1' command
* Heroku will then initiate the program based on the Procfile
* Enjoy the Twitter bot that spews jibberish every 30 seconds! :)
* Turn it off with the 'heroku ps:scale worker=0' command (you'll want to do this so it  doesn't chew through all your dyno hours)
* For more detail, reference Heroku's ['Getting Started on Heroku with Python'](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
