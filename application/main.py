import bottle
from bottle import request

import shortcuts
import models

app = bottle.Bottle()


@app.get("/api/notes/")
def note_list():
    qs = models.Note.query().order(-models.Note.created)
    return {
        "items": qs.map(lambda n: n.to_data())
    }


@app.post("/api/notes/")
def note_create():
    return {}


@app.get("/api/notes/<note_id:int>/")
def note_details(note_id):
    note = shortcuts.get_object_or_404(models.Note, note_id)
    return note.to_data()


@app.put("/api/notes/<note_id:int>/")
def note_update(note_id):
    note = shortcuts.get_object_or_404(models.Note, note_id)
    return {}


@app.delete("/api/notes/<note_id:int>/")
def note_delete(note_id):
    note = shortcuts.get_object_or_404(models.Note, note_id)
    return {}
