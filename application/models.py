from google.appengine.ext import ndb


class Note(ndb.Model):

    title = ndb.StringProperty()
    content = ndb.TextProperty()
    tags = ndb.StringProperty(repeated=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    def to_data(self):
        return dict(self.to_dict(include=("title", "content")),
            id=self.key.id()
        )
