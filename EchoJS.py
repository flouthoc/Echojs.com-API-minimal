import httplib
import parser

class echojs():

	def __init__(self):
		self.url = "www.echojs.com"
		self.type = "GET"

	def get_topnews(self):
		conn = httplib.HTTPConnection(self.url)
		conn.request(self.type,"")
		r1 = conn.getresponse()
		data = r1.read()
		pr = parser.MyHTMLParser(data)

	def get_latest(self, upto = 0):
		page = 0
		loop_counter = 0
		link = "/latest/"
		while(loop_counter <= upto):
			f_link = link + str(page)
			conn = httplib.HTTPConnection(self.url)
                	conn.request(self.type,f_link)
                	r1 = conn.getresponse()
                	data = r1.read()
                	pr = parser.MyHTMLParser(data)
			page += 30
			loop_counter += 1
			

		

