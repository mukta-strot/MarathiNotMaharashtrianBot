import re
import praw
import secrets
import threading
import time as time

reddit = praw.Reddit(client_id=secrets.client_id,
                     client_secret=secrets.client_secret,
                     username=secrets.username,
                     password=secrets.password,
                     user_agent=secrets.user_agent)
# \let's set the subreddit
#subreddit = reddit.subreddit("Somalia")
subreddit = reddit.subreddit("Testmybots_2020+Somalia+all+popular")
keyphrase = re.compile(r'^somalian\b|\s\bsomalian\b|\bsomalians',re.IGNORECASE)
username = secrets.username
correction = 'Somali not Somalian'
def commentReply():
    for comment in subreddit.stream.comments(skip_existing=True):
        m = keyphrase.search(comment.body.casefold())
        if m and correction.casefold() not in comment.body.casefold():
            author = comment.author.name
            if author != username:

                try:
                    #updateDatabase(author, 'post')
                    print("Replying to a comment made by " +  author + " who said  :" + comment.body )
                    time.sleep(3)
                    comment.reply(
                        "Hi, __" + author + "__. Your comment contains the word ~~Somalian~~.\n\n" +
                        "The correct nationality/ethnic demonym(s) for Somalis is __Somali__.\n\n" +
                        "It's a common mistake so don't feel bad.\n\n" +
                        "For other nationality demonym(s) check out this website [Here](https://www.nationmaster.com/country-info/stats/People/Nationality/Adjective)\n\n" +
                        "___This action was performed automatically by a bot.___")
                except:
                    print("too frequent")

def submissionReply():

    for submisison in subreddit.stream.submissions(skip_existing=True):



        author = submisison.author.name
        if re.search(keyphrase, submisison.title) or re.search(keyphrase, submisison.selftext.lower()):



            try:
                print("Replying to a post made by " + author + " who posted:  " + submisison.title)
                time.sleep(3)
                submisison.reply(
                    "Hi, __" + author + "__. Your post contains the word ~~Somalian~~.\n\n" +
                    "The correct nationality/ethnic demonym(s) for Somalis is __Somali__.\n\n" +
                    "It's a common mistake so don't feel bad.\n\n" +
                    "For other nationality demonym(s) check out this website [Here](https://www.nationmaster.com/country-info/stats/People/Nationality/Adjective)\n\n" +
                    "___This action was performed automatically by a bot.___")
            except:
                print("too frequent")

def getOldComments(author):
    redittor = reddit.get_redditor(author)



t_commentReply = threading.Thread(target=commentReply)
t_submissionReply = threading.Thread(target=submissionReply)

t_commentReply.start()
t_submissionReply.start()
t_submissionReply.join()
t_commentReply.join()
