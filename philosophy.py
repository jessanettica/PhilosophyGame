import urllib2
import sys
from BeautifulSoup import BeautifulSoup

#TODO: delete generating random link. Let it take a Wikipedia page name -> sys.argv[1]

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def getNext(newURL):
    infile = opener.open(newURL)
    page = infile.read()
    soup = BeautifulSoup(page)
    main_body = soup.find('div',id="bodyContent").findAll({'ul' : True, 'p' : True})
    for i in main_body:
    	for a_link in i.findAll('a'):
    		k = 0
    		for val, att in a_link.attrs:
    			if val == "href":
    				nexturl = att
    			if val == "title":
    				next = att
    				k = 1
    		if k ==0:
    			continue
    		return next

def PhilosophyGame():
	newURL = 'http://en.wikipedia.org/w/index.php?title=Special:Random' #URL for a random article
	newPage = getNext(newURL)
	visited = set()
	counter = 0 #Keeps track of the jumps
	if newPage == 'Philosophy':
	    print("You've arrived at the Philosophy page! Whooo")
	    #TODO: loop through visited, appeding wikiperdia prefix and adding to a list
	    #RETURN: List of links in visited and counter
	while newPage != 'Philosophy':
		if newPage in visited:
			newPage = getNext(newURL)
			print 'Oops already went there. Now jumping to the ' + newPage + ' page.'
		else:
			visited.add(newPage)
			newURL = 'http://en.wikipedia.org/w/index.php?title=' + newPage
			newPage = getNext(newURL)
			print 'Now jumping to the ' + newPage + ' page.'
			counter +=1
			print counter

PhilosophyGame()
        