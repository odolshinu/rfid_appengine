

import os
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Store(db.Model):
    place = db.StringProperty()
    sequence = db.StringProperty()
#    date = db.DateTimeProperty()

class MainPage(webapp.RequestHandler):
    def post(self):
        store = Store()
	store.sequence = self.request.get('sequence')
	store.place = self.request.get('place')
#	store.date = self.request.get('time')
	store.put()

class Display(webapp.RequestHandler):
    def get(self):
        store_query = Store.all()
	store = store_query.fetch(10)

	template_values = {
		'store' : store
		}
        
        path = os.path.join(os.path.dirname(__file__), 'index.html')
	self.response.out.write(template.render(path,template_values))

application = webapp.WSGIApplication(
		                      [('/',MainPage),('/display', Display)],
				       debug = True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()

