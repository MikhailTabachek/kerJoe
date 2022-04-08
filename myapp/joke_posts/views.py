from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import JokePost
from myapp.joke_posts.forms import JokePostForm

joke_posts = Blueprint('joke_posts', __name__)

@joke_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = JokePostForm()
    if form.validate_on_submit():
        joke_post = JokePost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(joke_post)
        db.session.commit()
        flash('Joke Created')
        print('Joke was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)