import tornado.ioloop
import tornado.web
import os
import time
from hackerrank import hackerrank
from codeforces import codeforces
class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("C:/Users/HP 15 AB032TX/Desktop/study/Project_WM/aboutus.html")
class UpcomingHandler(tornado.web.RequestHandler):
    def get(self):
        hackerrank_contests=hackerrank()
        codeforces_contests=codeforces()
        self.render("C:/Users/HP 15 AB032TX/Desktop/study/Project_WM/upcoming.html",hackerrank_contests=hackerrank_contests,codeforces_contests=codeforces_contests)
cwd = os.getcwd()
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/upcoming", UpcomingHandler),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {'path': "./images"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {'path': "./css"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {'path': "./fonts"})
    	
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    