from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb
#import endpoints

class CustomBaseModel(EndpointsModel):
    def populate(self, data):
        super(self.__class__, self).__init__()
        for attr in self._message_fields_schema:
            if hasattr(data, attr):
                setattr(self, attr, getattr(data, attr))

#####USUARIOS#########
class Usuarios(CustomBaseModel):
    _message_fields_schema = ('email', 'password')
    email = ndb.StringProperty()
    password = ndb.StringProperty()
   

