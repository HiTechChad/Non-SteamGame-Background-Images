from os import listdir
from os.path import isfile, join
import os, sys
from PIL import Image
import json
from distutils.dir_util import copy_tree
import shutil
rsize = (1920, 1080)
tsize = (200, 112)

with open('config.json') as config_file:
    data = json.load(config_file)

def main():
	#check if id is valid
	if firstRun():
		print "please enter your steamid in config.json then run the program again"
		return
	#get path location of files
	ssf_path = getPath()
	tnf_path = ssf_path + '\\thumbnails'
	
	#get file names from path location
	ssf = [f for f in listdir(ssf_path) if isfile(join(ssf_path, f))]
	tnf = [f for f in listdir(tnf_path) if isfile(join(tnf_path, f))]
	
	#get folder of new images that will replace screenshots
	itmp = os.getcwd() + '\\' + getNewImageFolder()
	mimp = itmp + '-tmp'
	mtnp = mimp + '\\thumbnails'
	
	#get all image names that will need to be modified
	rssf = [f for f in listdir(itmp) if isfile(join(itmp, f))]
	createDir(mimp)
	createDir(mtnp)
	print "\nCreating your images now"
	if resizeScreenShots(rssf, itmp, mimp, ssf) and resizeThumbnails(rssf, itmp, mtnp, tnf):
		print "\nAll images whre sucsefully created"
	else:
		print "\nAn error has occured"
	
	print "\nCopying files to steam directory"
	copy_tree(mimp, ssf_path)
	
	print "\nRemoving Temporary files"
	shutil.rmtree(mimp)
def firstRun():
	if data['steamid'] == "":
		return True
	else:
		return False
def getPath():
	print " "
	path = 'C:\\Program Files (x86)\\Steam\\userdata\\' + data['steamid'] + '\\760\\remote\\'
	gameid = str(input('Please enter the game id : '))
	path = path + gameid + '\\screenshots'
	return path
def getNewImageFolder():
	print " "
	while True:
		print "---Please create a new folder in the directory of this program and place all your images in it---"
		if(str(raw_input('Have you created a folder (y/n)? : ')) == 'y'):
			break
	print " "
	tmp = str(raw_input('Enter the name of the created folder: '))
	return tmp
	
def createDir(dir_name):
    try:    
        os.mkdir(dir_name)
        return True;
    except:
        return False

def resizeScreenShots(rssf, itmp, mimp, ssf):
	for index,item in enumerate(rssf):
		try:
			im = Image.open(itmp + '\\' + item)
			im.thumbnail(rsize, Image.ANTIALIAS)
			im.save(mimp + '\\' + ssf[index])
		except:
			print 'here'
			return False
	return True
def resizeThumbnails(rssf, itmp, mimp, ssf):
	for index,item in enumerate(rssf):
		try:
			im = Image.open(itmp + '\\' + item)
			im.thumbnail(tsize, Image.ANTIALIAS)
			im.save(mimp + '\\' + ssf[index])
		except:
			print 'here'
			return False
	return True

if __name__.endswith('__main__'):
	main()