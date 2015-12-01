
import re

STOP_WORDS=None

def load():
    STOP_WORDS=loadStopwords()
    tl=open('data/training.1600000.processed.noemoticon.csv','r')
    # tl=open('testdata.manual.2009.06.14.csv','r')
    line=tl.readline()
    proc_tweets=[]
    while line:
        temp=line.split(',')
        proc_tweets.append({int(re.sub('"','',temp[0])):processTweet(temp[-1])})
        line=tl.readline()
    tl.close()
    return proc_tweets

def loadStopwords():
    stopwords = set(["URL","USER"])
    fp = open('data/stopwords_en.txt', 'r')
    line = fp.readline()
    while line:
        line = line.strip('\n')
        stopwords.add(line)
        line = fp.readline()
    fp.close()
    return stopwords

# start process_tweet
# **taken from internet
def processTweet(tweet):
    # Convert to lower case
    tweet = tweet.lower()
    # Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    # Convert @username to USER
    tweet = re.sub('@[^\s]+', 'USER', tweet)
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # trim
    tweet = tweet.strip('\'"')

    #delete not letter chars
    tweet=re.sub('[=|+|,|.|?|!|*|;|:|(|)|&|-|\|[|\]]','', tweet)

    #delete consecutive chars with the same value
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    tweet=pattern.sub(r"\1",tweet)

    return removeStopWords(tweet)

# end



#remove the stopwords and set it to a dict
def removeStopWords(tweet):
    stop_words=loadStopwords()
    tweet=tweet.split()
    output=[word for word in tweet if word not in stop_words and len(word)>2]
    return output






# tweets=load()
# wf=open('proc_tweets.txt', 'w')
# for line in tweets:
#     sent, tweet=line.keys()[0], line.values()[0]
#     f_t=''
#     for w in tweet:
#         f_t+=' '+w
#     wf.write(str(sent)+','+f_t+'\n')
# wf.close()
# a=1+2