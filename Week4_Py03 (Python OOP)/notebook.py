import datetime


class Note:

    def __init__(self, note_id, memo, tags):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.note_id = note_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, note_id, memo, tags):
        self.notes.append(Note(note_id, memo, tags))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note_id == note_id:
                note.memo = memo
                break

    def search(self, filter):
        for note in self.notes:
            return note.match(filter)


# n1 = Note(1, "hello", tags="greeting")
# n2 = Note(2, "grocery list", tags="shopping")
# print(f"note_id: {n1.note_id}\nnote_name: {n1.memo}\ncreation_date: {n1.creation_date}")

nb = Notebook()
nb.new_note(1, "nom nom", tags="eating")
nb.new_note(2, "i like ice cream", tags="favorites")

for note in nb.notes:
    print(note.memo)

print(nb.search("hello"))
