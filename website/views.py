from flask import Blueprint, render_template, flash , request
from flask_login import login_required, current_user
from .models import News, User
from . import db
views = Blueprint('views', __name__)



@views.route("/", methods = ["GET", "POST"])
@login_required
def home():
  if request.method == "POST":
    news = request.form.get('news')

    if len(news) < 1:
      flash("Post is too short", category='error')
    else:
      new_post = News(data = news, user_id = current_user.id)
      flash("Post added succesfully", category='success')
      db.session.add(new_post)

      db.session.commit()
  return render_template("home.html", user = current_user)