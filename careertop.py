import praw 
r = praw.Reddit(user_agent='crawlr')
usub = input('Enter the name of subreddit: ')
sub = r.get_subreddit(usub)
posts = sub.get_top(limit=5)
for x in posts:
	print(x)