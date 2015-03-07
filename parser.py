from HTMLParser import HTMLParser
import json


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	
	def __init__(self, datum):
		HTMLParser.__init__(self)        
		self.in_title = False
		self.title = ''
		self.tag_check = 'article'
		self.tag_flag = 0
		self.feed(datum)
    	def handle_starttag(self, tag, attrs):
        	if( tag == 'h2' ):
			self.tag_flag = 1
		elif( tag == 'a' and self.tag_flag == 1 ):
			link = attrs[1][1]
			print '{'
			print json.dumps({'Link': link})
			print ','
    	def handle_endtag(self, tag):
        	if( tag == 'h2' ):
			self.tag_flag = 0
                	print "}"
    	def handle_data(self, data):
		if( self.tag_flag == 1 ):
        		print json.dumps({'Title':data})			


