from flask import Blueprint, render_template, request, flash, redirect, url_for

from flask_login import current_user, login_required

from app.models import Music, db

from app.forms import newMusicForm

site = Blueprint('site', __name__, template_folder='site_templates')


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
    form = newMusicForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            namedata = form.name.data
            genredata = form.genre.data
            banddata = form.band.data
            playlistdata = form.playlist.data
            print(namedata, banddata)

            new_Music = Music(namedata, genredata, banddata, playlistdata)

            db.session.add(new_Music)
            db.session.commit()

            flash(
                f'You have successfully added the Music {namedata} to your database.')

            return redirect(url_for('site.profile'))
    except:
        flash(f'Invaild form input try again')
        return redirect(url_for('site.profile'))
    return render_template('profile.html', form=form)


@site.route('/flappybird')
def flappy():
    return render_template('flappybird.html')


@site.route('/Dino')
def Dino():
    return render_template('Dino.html')


@site.route('/pacman')
def pacman():
    return render_template('pacman.html')


@site.route('/snake')
def snake():
    return render_template('snake.html')