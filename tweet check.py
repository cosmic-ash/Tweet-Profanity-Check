import re

""" TOKENIZING THE TWEETS """

def tokenize(tweet):
    return(re.findall(r'\w+',tweet.lower()))

""" LIST OF RACIAL SLURS"""

racial_slurs=['nigga','beaner','gook','chink','wetback']

""" READING THE FILES CONTAING THE TWEETS IN TO A LIST"""

with open('tweets.txt') as f:
    lines=[line.rstrip() for line in f]

for i in lines:
    profanity_degree=0
    count=0
    tokenized_tweet=tokenize(i)
    for word in tokenized_tweet:
        if word.lower() in racial_slurs:
            count=count+1
    profanity_degree= profanity_degree + count/ len(tokenized_tweet)            #THE PROFANITY DEGREE IS CALCULATED AS NUMBER OF TOKENS THAT ARE PROFANITIES AMONG THE TOTAL TOKENS
    print("TWEET:"+i+"\n PROFANITY DEGREE: " + str(profanity_degree)+"\n")