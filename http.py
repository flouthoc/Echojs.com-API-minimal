import httplib
import parser

def get_latest(upto = 0):
                page = 0
		loop_counter = 0
                link = "/latest/"
                while(loop_counter <= upto):
                        f_link = link + str(page)
                        conn = httplib.HTTPConnection("www.echojs.com")
                        conn.request("GET",f_link)
			print f_link
			r1 = conn.getresponse()
                        data = r1.read()
                        pr = parser.MyHTMLParser(data)
                        page += 30
			loop_counter += 1
get_latest(1)

