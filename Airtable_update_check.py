import secrets
from pyairtable import Table

user_table = Table(secrets.airtable_Api_key, secrets.airtable_base, 'user')
subreddit_table = Table(secrets.airtable_Api_key, secrets.airtable_base, 'Subreddit')


#user table create update 
def checkIfusername_exists(user) : 
    for j in user_table.all():
        if (j['fields']['Username'] == user): 
            return j['id'],j['fields']['usage_count']
 
 
def update_existing_user(record_id,current_usage):
    return (user_table.update(record_id,{"usage_count" : current_usage + 1 }  ) )      

def Create_update_user(username):
    result = checkIfusername_exists(username)
    if ( result  == None):
       return ( user_table.create({'Username':username,'usage_count':1}) ) 
    else: 
        update_existing_user(record_id=result[0],current_usage=result[1])
        

#subreddit table create update 

def checkifSubredditExists(subreddit_name) : 
    for j in subreddit_table.all():
        if (j['fields']['Subreddit_name'] == subreddit_name): 
            return j['id'],j['fields']['usage_count']


def update_existing_subreddit(record_id,current_usage):
    return (subreddit_table.update(record_id,{"usage_count" : (current_usage) + 1 }  ) )      

def Create_update_subreddit(subreddit_name):
    result = checkifSubredditExists(subreddit_name)
    print("this is the result:  ", result)
    if ( result  == None):
       return ( subreddit_table.create({'Subreddit_name':subreddit_name,'usage_count':1}) ) 
    else: 
       return  update_existing_subreddit(record_id=result[0],current_usage=result[1])
        
           
          


if  __name__ == "__main__":
    
    print(Create_update_user(username= ''))
    print(Create_update_subreddit(subreddit_name = ''))
