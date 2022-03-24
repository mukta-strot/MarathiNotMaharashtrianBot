import os
from dotenv import load_dotenv
import re
import praw
import threading
import time as time

load_dotenv()

CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')
CLIENT_ID = os.getenv('CLIENT_ID')

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)

subreddit = reddit.subreddit("Marathi+testingground4bots+Pune+Indiaspeaks+Mumbai+Nagpur+Indiasocial+Indianews+Nashik+shahanpana+Maharashtra")
keyphrase = re.compile(
   r'^maharashtrian\b|\s\bmaharashtrian\b|\bmaharashtrians|^महाराष्ट्रीयन\s|\sमहाराष्ट्रीयन\s|\sमहाराष्ट्रीयन', re.IGNORECASE)
username = USERNAME
correction = 'Marathi (मराठी) not maharashtrian'


def commentReply():
    for comment in subreddit.stream.comments(skip_existing=True):
        m = keyphrase.search(comment.body.casefold())
        if m and correction.casefold() not in comment.body.casefold():
            author = comment.author.name
            if author != username:

                try:
                    print(
                        f"Replying to a comment made by {author} who said  : {comment.body}")
                    time.sleep(5)
                    comment.reply(f"""_\< English follows Marathi \>_  
                    नमस्कार __{author}__. आपल्या टिप्पणीत ~~महाराष्ट्रीयन~~ किंवा ~~Maharashtrian~~ असा शब्द आढळला आहे.  
                    मराठी लोकांचा उल्लेख करण्यासाठी योग्य शब्द हा __मराठी__ असा आहे.  
                    (बंगाली, पंजाबी, गुजराती वगैरे सारखे.)  
                    ही चूक बरेच जण करतात, त्यामुळे वाईट वाटून घेऊ नका. :)  
                    _हा संदेश एका स्वयंचलित बॉटने पाठवला आहे._  
                    ---  
                    Namaskar __{author}__. Your comment contains the word ~~महाराष्ट्रीयन~~ or ~~Maharashtrian~~.  
                    The correct demonym for Marathis is __Marathi__.  
                    (Similar to Bengali, Punjabi, Gujrati etc.)  
                    It's a common mistake so don't feel bad.  :)  
                    _This message was sent automatically by a bot._""")
                except:
                    print("too frequent")


def submissionReply():
    for submisison in subreddit.stream.submissions(skip_existing=True):
        author = submisison.author.name
        if re.search(keyphrase, submisison.title) or re.search(keyphrase, submisison.selftext.lower()):

            try:
                print("Replying to a post made by " + author +
                      " who posted:  " + submisison.title)
                time.sleep(5)
                submisison.reply(f"""_\< English follows Marathi \>_  
                नमस्कार __{author}__. आपल्या पत्रकात ~~महाराष्ट्रीयन~~ किंवा ~~Maharashtrian~~ असा शब्द आढळला आहे.  
                मराठी लोकांचा उल्लेख करण्यासाठी योग्य शब्द हा __मराठी__ असा आहे.  
                (बंगाली, पंजाबी, गुजराती वगैरे सारखे.)  
                ही चूक बरेच जण करतात, त्यामुळे वाईट वाटून घेऊ नका. :)  
                _हा संदेश एका स्वयंचलित बॉटने पाठवला आहे._  
                ---  
                Namaskar __{author}__. Your post contains the word ~~महाराष्ट्रीयन~~ or ~~Maharashtrian~~.  
                The correct demonym for Marathis is __Marathi__.  
                (Similar to Bengali, Punjabi, Gujrati etc.)  
                It's a common mistake so don't feel bad. :)  
                _This message was sent automatically by a bot._""")
            except:
                print("too frequent")

if __name__ == "__main__":
    t_commentReply = threading.Thread(target=commentReply)
    t_submissionReply = threading.Thread(target=submissionReply)

#    0324 - temporarily disable all functions
#    t_commentReply.start()
#    t_submissionReply.start()
#    t_submissionReply.join()
#    t_commentReply.join()
#    print("Done")
