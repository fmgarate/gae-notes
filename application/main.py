import bottle
from bottle import request

import forms
import models
import shortcuts

app = bottle.Bottle()


@app.get("/api/notes/")
def note_list():
    """
    Notes list api endpoint. Returns a list of notes
    """

    qs = models.Note.query().order(-models.Note.created)

    return {
        "items": qs.map(lambda n: n.to_data())
    }


@app.post("/api/notes/")
def note_create():
    """
    Note create api endpoint. Create a new note
    """

    form = forms.NoteForm(request.POST)

    if form.validate():
        note = models.Note()
        form.populate_obj(note)
        note.put()

        return note.to_data()

    return {"errors": form.errors}


@app.get("/api/notes/<note_id:int>/")
def note_details(note_id):
    """
    Note details api endpoint. Returns a note instance
    """
    return shortcuts.get_object_or_404(models.Note, note_id).to_data()


@app.put("/api/notes/<note_id:int>/")
def note_update(note_id):
    """
    Note update api endpoint. Update a note
    """

    note = shortcuts.get_object_or_404(models.Note, note_id)
    form = forms.NoteForm(request.POST, note)

    if form.validate():
        form.populate_obj(note)
        note.put()

        return note.to_data()

    return {"errors": form.errors}


@app.delete("/api/notes/<note_id:int>/")
def note_delete(note_id):
    """
    Note delete api endpoint. Delete a note
    """

    note = shortcuts.get_object_or_404(models.Note, note_id)
    note.key.delete()

    return {}
