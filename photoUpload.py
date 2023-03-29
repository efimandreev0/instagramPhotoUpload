from instabot import Bot
import sys

def info():
	print ("Usage: python toolName.py username password photo caption")

def uploadPost():
	bot = Bot()

	bot.login(username = sys.argv[0],
		password = sys.argv[1])
	
	bot.upload_photo(sys.argv[2], 
		caption = sys.argv[3])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        info()
	else:
		uploadPhoto()