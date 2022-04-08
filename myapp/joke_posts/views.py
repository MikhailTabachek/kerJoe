from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import JokePost
from myapp.joke_posts.forms import JokePostForm

blog_posts = Blueprint('joke_posts', __name__)