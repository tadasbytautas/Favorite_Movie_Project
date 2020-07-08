from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from forms import PostForm

app = Flask(__name__)


app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Title: ' + self.title + '\n'
                'Name: ' + self.userID + '\n'
                'Content: ' + self.content
            ]
        )


@app.route('/')
@app.route('/home')
def home():
    post_data = Posts.query.all()
    return render_template('homepage.html', title='Homepage', posts=post_data)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        post_data = Posts(
            userID=form.userID.data,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('post.html', title='Add a post', form=form)

@app.route('/create')
def create():
    db.create_all()
    post = Posts(userID='Tadas', title='The Shawshank Redemption (1994)', content="Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red. Written by J-S-Golden")
    post2 = Posts(userID='Marija', title='The Dark Knight (2008)', content="Set within a year after the events of Batman Begins (2005), Batman, Lieutenant James Gordon, and new District Attorney Harvey Dent successfully begin to round up the criminals that plague Gotham City, until a mysterious and sadistic criminal mastermind known only as \"The Joker\" appears in Gotham, creating a new wave of chaos. Batman's struggle against The Joker becomes deeply personal, forcing him to \"confront everything he believes\" and improve his technology to stop him. A love triangle develops between Bruce Wayne, Dent, and Rachel Dawes. Written by Leon Lombardi")
    db.session.add(post)
    db.session.add(post2)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    # db.drop_all()  # drops all the schemas
    db.session.query(Posts).delete()  # deletes the contents of the table
    db.session.commit()
    return redirect(url_for('home'))
    # return "everything is gone woops soz"


if __name__ == '__main__':
    app.run()
