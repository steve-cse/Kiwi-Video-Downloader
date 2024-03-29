import youtube_dl
import requests
import time
import os
import getpass
import colorama
import sys
from colorama import Fore, Back, Style
# kiwi youtube video downloader
def check_conn (): # check internet connection
	try:
		response=requests.get ("https://www.google.com/")
		return True
	except requests.ConnectionError: pass
	return False

def get_video (url): #get video
	ydl_opts = {
				'writethumbnail': True,
				'format': 'bestvideo+bestaudio/best', #best stream
				'outtmpl': 'Downloads/%(title)s.%(ext)s', #set path to Downloads
				'postprocessors': [{
				'key': 'FFmpegVideoConvertor', # use ffmpeg to convert
				'preferedformat': 'mp4'}, # prefered format mp4
				{'key': 'EmbedThumbnail',},]} # embed thumbnails using atomic parsley
	with youtube_dl.YoutubeDL (ydl_opts) as ydl:
		ydl.download ([url]) #download

def mk_dir(): #make folder if it doesn't exists
	if not os.path.exists('Downloads'):
		os.makedirs('Downloads')

def get_title (url): # get the video title
	opts={
		"quiet":True} # quietly
	with youtube_dl.YoutubeDL (opts) as ydl:
		info_dict = ydl.extract_info(url, download=False)
		video_title = info_dict.get('title', None)
	return video_title

def get_name ():
	name=getpass.getuser()
	name=name[:1].upper()+name[1:]
	return name

def check_url(): #check for url as argument
	if len(sys.argv) > 1:
		return True
	else:
		return False


colorama.init()
mk_dir()
print(Fore.YELLOW+"Welcome "+get_name()+" to Kiwi Video Downloader"+ Style.RESET_ALL)
if not check_conn():
	print(Fore.RED+"No internet connection found. "+ Style.RESET_ALL)
	time.sleep(5)
else:
	if (check_url()):
		link=sys.argv[1]
	else:
		link=input("Enter video URL: ")

	print(Fore.CYAN+"Title: "+get_title(link)+Style.RESET_ALL)
	get_video(link) #test url: https://youtu.be/AOeY-nDp7hI
	print ("File(s) stored at:",os.getcwd()+"\\"+"Downloads")
	print (Fore.GREEN+"Complete."+Style.RESET_ALL)
