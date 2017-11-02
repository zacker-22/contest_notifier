import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import time
from hackerrank import hackerrank
from codeforces import codeforces
from codechef import codechef
class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("aboutus.html")
class UpcomingHandler(tornado.web.RequestHandler):
    def get(self):
        hackerrank_contests=hackerrank()
        codeforces_contests=codeforces()
        codechef_contests=codechef()
        self.render("upcoming.html",hackerrank_contests=hackerrank_contests,codeforces_contests=codeforces_contests,codechef_contests=codechef_contests)

 

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/upcoming", UpcomingHandler),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {'path': "./images"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {'path': "./css"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {'path': "./fonts"})
    
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
    
