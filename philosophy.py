import urllib2
import sys
from BeautifulSoup import BeautifulSoup

#TODO: delete generating random link. Let it take a Wikipedia page name -> sys.argv[1]
class PhilosophyGame:
	def __init__(self):
		self.opener = urllib2.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		self.visited_URLs = []
		self.links_tried = []
		self.jump_counter = 0


	def get_next(self, new_URL):
	    in_file = self.opener.open(new_URL)
	    page = in_file.read()
	    soup = BeautifulSoup(page)
	    main_body = soup.find('div', id='mw-content-text').findAll({'p' : True})
	    for element in main_body:
	    	list_of_links = element.findAll('a')
	    	if list_of_links == []:
	    		return None
	    	else:
		    	link_title = self.find_next_page_link(list_of_links)
		    	if link_title != None:
		    		return link_title


	def find_next_page_link(self, list_of_links):
		next = None
		for a_link in list_of_links:
			if a_link not in self.links_tried:
				for attr, val in a_link.attrs:
					if attr == 'title':
						next = val
						self.links_tried.append(next)
						return next
				if next == None:
					continue
		

	def philosophy_game(self):
		new_URL = 'http://en.wikipedia.org/wiki/Puppy'
		self.visited_URLs.append(new_URL)
		new_page = self.get_next(new_URL)
		visited = set()
		if new_page == 'Philosophy':
		    print('You\'ve arrived at the Philosophy page! Whooo')
		    return self.visited_URLs, self.counter
		while new_page != 'Philosophy' and self.jump_counter < 100:
			if new_page == None:
				new_page = self.get_next(self.visited_URLs[-1])

			elif new_page in visited:
				new_page = self.get_next(self.visited_URLs[-1])
				print 'Oops already went there. Now jumping to the ' + new_page + ' page.'

			else:
				visited.add(new_page)
				new_URL = 'http://en.wikipedia.org/w/index.php?title=' + new_page
				self.visited_URLs.append(new_URL)
				new_page = self.get_next(new_URL)

				print 'Now jumping to the ' + str(new_page) + ' page.'
				self.jump_counter += 1
				print self.jump_counter
		return "Max jumps reached before reaching the Philosophy"

p = PhilosophyGame()
p.philosophy_game()
        