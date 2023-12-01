from flask import render_template, redirect
from ext import app, db
from forms import AddCommentForm, RegisterForm
from models import Comment

@app.route('/', methods=['POST', 'GET'])
def AddComment():
    form = AddCommentForm()
    if form.validate_on_submit():
        new_comment = Comment(name=form.name.data, comment=form.comment.data)
        db.session.add(new_comment)
        db.session.commit()
        comments = Comment.query.all()
        return render_template("index.html", form=form, comments=comments)
    return render_template("index.html", form=form)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.gender.data)
        print(form.country.data)
        print(form.birthday.data)
        return redirect('/register')  
    return render_template('registration.html', form=form)
