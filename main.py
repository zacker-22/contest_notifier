import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import time
import datetime
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

class OngoingHandler(tornado.web.RequestHandler):
    def get(self):
        hackerrank_contests=hackerrank()
        codeforces_contests=codeforces()
        codechef_contests=codechef()
        cur=datetime.datetime.now()
        ongoing_hackerrank=[]
        ongoing_codeforces=[]
        ongoing_codechef=[]
        for contest in hackerrank_contests:
            if datetime.datetime.strptime(contest[1],"%Y-%m-%d %H:%M:%S")<=cur<=datetime.datetime.strptime(contest[2],"%Y-%m-%d %H:%M:%S"):
                ongoing_hackerrank.append(contest)
        for contest in codeforces_contests:
            if datetime.datetime.strptime(contest[1],"%Y-%m-%d %H:%M:%S")<=cur<=datetime.datetime.strptime(contest[2],"%Y-%m-%d %H:%M:%S"):
                ongoing_codeforces.append(contest)
        for contest in codechef_contests:
            if datetime.datetime.strptime(contest[1],"%Y-%m-%d %H:%M:%S")<=cur<=datetime.datetime.strptime(contest[2],"%Y-%m-%d %H:%M:%S"):
                ongoing_codechef.append(contest)
        #print ongoing_codechef,ongoing_hackerrank,ongoing_codeforces
        self.render("ongoing.html",hackerrank_contests=ongoing_hackerrank,codeforces_contests=ongoing_codeforces,codechef_contests=ongoing_codechef)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/upcoming", UpcomingHandler),
        (r"/ongoing", OngoingHandler),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {'path': "./images"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {'path': "./css"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {'path': "./fonts"})
    
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
    
