from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CRIAÇÃO DO BANCO DE DADOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///favorite-movies.db'  

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

class RateMovie(FlaskForm):
    rating = StringField('Sua nota')
    review = StringField('Seu review')
    submit = SubmitField('Enviar')

def reposicionar_filmes():
    lista = Movie.query.all()
    count = 1
    for filme in lista:
        filme.id = count
        count+=1

@app.route("/delete/<int:movie_id>")
def deleteMovie(movie_id):
    movie = Movie.query.get(movie_id)
    print(movie)
    db.session.delete(movie)
    db.session.commit()
    print("deletado!")
    return redirect((url_for("home")))

@app.route("/update/<int:movie_id>", methods=['GET', 'POST'])
def updateMovie(movie_id):
    form = RateMovie()
    movie = db.get_or_404(Movie, movie_id) 
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home')) 

    return render_template('edit.html', movie=movie, form= form)  


@app.route("/")
def home():
    movies = Movie.query.all()
    reposicionar_filmes()
    return render_template("index.html", movies = movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        movie_title = request.form['movie_title']
        movie_year = request.form['movie_year']  # New field
        movie_description = request.form['movie_description']  # New field
        movie_rating = request.form['movie_rating']  # New field
        movie_ranking = request.form['movie_ranking']  # New field
        movie_review = request.form['movie_review']  # New field
        movie_img_url = request.form['movie_img_url']  # New field
        
        new_movie = Movie(
            title=movie_title,
            year=movie_year,
            description=movie_description,
            rating=movie_rating,
            ranking=movie_ranking,
            review=movie_review,
            img_url=movie_img_url
        )
        
        db.session.add(new_movie)
        db.session.commit()
        return redirect('/')

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
