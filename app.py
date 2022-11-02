from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Initialize app
app = Flask(__name__)

# configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String)


# home route
@app.route('/')
def index():
    journals = Journal.query.all()
    print(journals)
    return render_template("index.html", journals=journals)

# add a new journal content
@app.route('/add', methods=['POST'])
def add():
    # add a journal
    title = request.form.get("title")
    print(title)
    content = request.form.get("content")
    print(content)
    new_journal = Journal(title=title, content=content)
    db.session.add(new_journal)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:journal_id>')
def update(journal_id):
    # update a journal
    journal = Journal.query.filter_by(id=journal_id).first()
    journal.content = request.form.get("content")
    new_journal = Journal(title=title, content=content)
    db.session.add(new_journal)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:journal_id>')
def delete(journal_id):
    journal = Journal.query.filter_by(id=journal_id).first()
    db.session.delete(journal)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        new_journal = Journal(title="journal1", content="I am testing")
        db.session.add(new_journal)
        db.session.commit()
        app.run(debug=True)