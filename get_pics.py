""""
The simplest tool ever to grab images from a reddit subreddit.
I've seen alternatives to this, and I've also seen tools get the job done more nicely
but this is created for simplicity and minimalism, I wanted to create the simplest image download I can.

Baha - meddbeibia@gmail.com - @meddbeibia
JULY 12, 2015
"""
import praw
import urllib
import gallery_get


USERAGENT = 'Image downloader by /u/medtn'
SUBREDDIT = raw_input("Please enter the name of the subreddit: ")


def get_pics():
    """
    Added a a get_pics function based on a suggestion form /u/schleifer
    """
r = praw.Reddit(USERAGENT)
submissions = r.get_subreddit(SUBREDDIT).get_hot(limit=25)

print'Starting download for subreddit :', SUBREDDIT, '\n'

for submission in submissions:
	try:
		if "imgur.com/a/" in submission.url: # launch the gallery_get module if this condition is true (if the link is an album)
				print ("> " + submission.url)
				gallery_get.run(submission.url)

		elif "http://imgur.com/" in submission.url: # if the link is not a direct link (as in http://imgur.com/picture.jpg) a direct one will be appended to it
			url = submission.url + ".jpg"
			print ('> * ' + url)
			urllib.urlretrieve(url, "Picture - "+submission.id+".jpg")

		else: 
			urllib.urlretrieve(submission.url, "Picture - "+submission.id+".jpg")
			print ("> " + submission.url)
	except:
			pass



if __name__ == '__main__':
    if not USERAGENT:
        print('Missing useragent')
    elif not SUBREDDIT:
        print('Missing subreddit')
    else:
        get_pics()