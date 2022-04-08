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


@joke_posts.route('/<int:joke_post_id>')
def joke_post(joke_post_id):
    joke_post = JokePost.query.get_or_404(joke_post_id) 
    return render_template('joke_post.html', title=joke_post.title, date=joke_post.date, post=joke_post)

@joke_posts.route('/<int:joke_post_id>/update',methods=['GET','POST'])
@login_required
def update(joke_post_id):
    joke_post = JokePost.query.get_or_404(joke_post_id)

    if joke_post.author != current_user:
        abort(403)

    form = JokePostForm()

    if form.validate_on_submit():
        joke_post.title = form.title.data
        joke_post.text = form.text.data
        db.session.commit()
        flash('Joke was Updated')
        return redirect(url_for('joke_posts.joke_post',joke_post_id=joke_post.id))

    elif request.method == 'GET':
        form.title.data = joke_post.title
        form.text.data = joke_post.text

    return render_template('create_post.html',title='Updating',form=form)

@joke_posts.route('/<int:joke_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(joke_post_id):

    joke_post = JokePost.query.get_or_404(joke_post_id)
    if joke_post.author != current_user:
        abort(403)

    db.session.delete(joke_post)
    db.session.commit()
    flash('Joke was Deleted')
    return redirect(url_for('core.index'))