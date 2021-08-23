from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models import Game, db
from app.forms import newGameForm

import mimetypes
mimetypes.add_type('application/javascript', '.js')

site = Blueprint('site', __name__,
                 template_folder='site_templates', static_folder='../static')


@site.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = "Please sign in."

    return render_template('index.html', user=username)


@site.route('/profile')
@login_required
def profile():
    form = newGameForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            namedata = form.name.data

            print(namedata)
            new_Game = Game(name=namedata)

            db.session.add(new_Game)
            db.session.commit()

            flash(
                f'You have successfully added the Game {namedata} to your database.')

            return redirect(url_for('site.profile'))
    except:
        flash(f'Invaild form input try again')
        return redirect(url_for('site.profile'))
    return render_template('profile.html', form=form)


@login_required
@site.route('/flappybird')
def flappy():
    return render_template('flappybird.html')


@login_required
@site.route('/Dino')
def Dino():
    return render_template('Dino.html')


@login_required
@site.route('/pacman')
def pacman():
    return render_template('pacman.html')


@login_required
@site.route('/snake')
def snake():
    return render_template('snake.html')
