from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean)

@app.route('/')
def index():
    # show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

# route that is never shown
@app.route("/add", methods=["POST"])
def add():
    # add new item
    title = request.form.get('title')
    new_todo = Todo(title=title, completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


# @app.route('/about')
# def about():
#     return "About"




if __name__ == "__main__":
    with app.app_context():
        db.create_all()



    app.run(debug=True)