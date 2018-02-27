import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import time
import datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        if self.get_argument("name")=="dev":
            self.write("bad boy")
            print "bad"
        elif self.get_argument("name")=="yash":
            self.write("good boy")
            print "good"
        else:
            print "noth"
            pass
class About(tornado.web.RequestHandler):
    def get(self):
        self.render("aboutus.html")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ab", About)
    
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
    
