from flask import Flask, request, jsonify

import forms
import models
import shortcuts

app = Flask(__name__)


@app.route("/api/notes/", methods=('GET',))
def note_list():
    """
    Notes list api endpoint. Returns a list of notes
    """

    qs = models.Note.query().order(-models.Note.created)

    return jsonify(items=qs.map(lambda n: n.to_data()))


@app.route("/api/notes/", methods=('POST',))
def note_create():
    """
    Note create api endpoint. Create a new note
    """

    form = forms.NoteForm(request.form)

    if form.validate():
        note = models.Note()
        form.populate_obj(note)
        note.put()

        return jsonify(note.to_data())

    return jsonify(errors=form.errors)


@app.route("/api/notes/<int:note_id>/", methods=('GET',))
def note_details(note_id):
    """
    Note details api endpoint. Returns a note instance
    """

    note = shortcuts.get_object_or_404(models.Note, note_id)

    return jsonify(note.to_data())


@app.route("/api/notes/<int:note_id>/", methods=('PUT',))
def note_update(note_id):
    """
    Note update api endpoint. Update a note
    """

    note = shortcuts.get_object_or_404(models.Note, note_id)
    form = forms.NoteForm(request.form, note)

    if form.validate():
        form.populate_obj(note)
        note.put()

        return jsonify(note.to_data())

    return jsonify(errors=form.errors)


@app.route("/api/notes/<int:note_id>/", methods=('DELETE',))
def note_delete(note_id):
    """
    Note delete api endpoint. Delete a note
    """

    note = shortcuts.get_object_or_404(models.Note, note_id)
    note.key.delete()

    return jsonify({})
