import webapp2
import os
import jinja2
import json
import sys
from google.appengine.ext import ndb
from google.appengine.api import images

from models import Usuarios


##usuarios ################
class ModelClass(object):
 pass

def ObjectClass(obj):
 return obj.__dict__

###Image
class Image(webapp2.RequestHandler):
    def get(self):
        greeting_key = ndb.Key(urlsafe=self.request.get('img_id'))
        greeting = greeting_key.get()
        if greeting.avatar:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(greeting.avatar)
        else:
            self.response.out.write('No image')

#### Create
class CreateUserHandler(webapp2.RequestHandler):
    def post(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        c = ModelClass()

        try:

            myEmail = self.request.get('email')
            myPasswd = self.request.get('password')

            myNuevoUsuario = Usuarios ( email = myEmail , password = myPasswd)
            myUsuarioKey = myNuevoUsuario.put()

            c.message = "inserted"
            c.key = myUsuarioKey.urlsafe()

        except:

            c.message = "Exception ..."

        json_string = json.dumps(c, default=ObjectClass)
        self.response.write(json_string)


#### ReadAll
class ReadAllUserHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        myList = []

        try:

            lstUsers = Usuarios.query().fetch()
            for i in lstUsers:
                c = ModelClass()
                c.id = i.key.urlsafe()
                c.email = i.email
                c.passwd = i.password
                myList.append(c)

        except:

            c = ModelClass()
            c.message = "Exception ..."
            myList.append(c)
        json_string = json.dumps(myList, default=ObjectClass)
        self.response.write(json_string)

#### ReadOne
class ReadOneUserHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        c = ModelClass()
        try:

            userkey = self.request.get('key')
            id_userkey = ndb.Key(urlsafe=userkey)
            myUser = Usuarios.query(Usuarios.key == id_userkey).get()
            c.key = userkey
            if myUser is not None:
                c.email = myUser.email
                c.passwd = myUser.password
            else:
                c.message = "error: not found"
        except:
            c.message = "Exception ..."
        json_string = json.dumps(c, default=ObjectClass)
        self.response.write(json_string)


#### Update
class UpdateUserHandler(webapp2.RequestHandler):
    def post(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        c = ModelClass ()
        try:
            userkey = self.request.get('key')
            myEmail = self.request.get('email')
            myPasswd = self.request.get('password')
            id_userkey = ndb.Key(urlsafe=userkey)
            myUser = Usuarios.query(Usuarios.key == id_userkey).get()
            c.key = userkey
            if myUser is not None:
                myUser.email = myEmail
                myUser.password = myPasswd
                myUser.put()
                c.message = "updated"
            else:
                c.message = "error: not found"
        except:
            c.message = "Exception ..."
        json_string = json.dumps(c, default=ObjectClass)
        self.response.write(json_string)


#### Delete
class DeleteUserHandler(webapp2.RequestHandler):
    def post(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        c = ModelClass()
        try:
            userkey = self.request.get('key')
            id_userkey = ndb.Key(urlsafe=userkey)
            myUser = Usuarios.query(Usuarios.key == id_userkey).get()
            c.key = userkey

            if myUser is not None:
                myUser.key.delete()
                c.message = "deleted"
            else:
                c.message = "error: not found"
        except:
            c.message = "Exception ..."
        json_string = json.dumps(c, default=ObjectClass)
        self.response.write(json_string)


jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('index.html')
    template_context = {}
    self.response.out.write(template.render(template_context))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/createUser', CreateUserHandler),
  ('/readAllUser', ReadAllUserHandler),
  ('/readOneUser', ReadOneUserHandler),
  ('/updateUser', UpdateUserHandler),
  ('/deleteUser', DeleteUserHandler)
], debug=True)
