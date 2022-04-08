from flask import render_template, request, Blueprint
from myapp.models import JokePost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    joke_posts = JokePost.query.order_by(JokePost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', joke_posts=joke_posts)

@core.route('/info')
def info():
    return render_template('info.html')
