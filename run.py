# This program runs a markov chain through Philip K Dick's Second Variety
from time import sleep
from markov_python.cc_markov import MarkovChain
import tweepy
from keys import CKEY, CSECRET, AKEY, ASECRET

auth = tweepy.OAuthHandler(CKEY,CSECRET)
auth.secure = True
auth.set_access_token(AKEY,ASECRET)
api = tweepy.API(auth)

# Generates one text of 20 words 
mc = MarkovChain()
clean_text = ''
mc.add_file('second_variety.txt')	

run = True

while run == True:
	
	for word in mc.generate_text():
		clean_text += word + ' '
	
	length_of_tweet = len(clean_text)
	print 'Length of Tweet: ', length_of_tweet
	print 'Tweet: ', clean_text

	if length_of_tweet < 140:
		api.update_status(clean_text)
		sleep(30)

	clean_text = ''
