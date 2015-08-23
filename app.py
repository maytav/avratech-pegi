import re

from flask import Flask, render_template,request, session,redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



# Creates a Flask app and reads the settings from a
# configuration file. We then connect to the database specified
# in the settings file
from sqlalchemy import select

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

db = SQLAlchemy(app)


# We are defining a 'Comments' model to store the comments the user
# enters via the form.
class Comments(db.Model):
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'kosher app'
    id = db.Column('app_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    Description = db.Column(db.String(100))
    PEGI = db.Column(db.String(2))
    Img = db.Column(db.String)
    Link = db.Column(db.String)
    # pub_date = db.Column(db.DateTime)

    def __init__(self, name, Description, PEGI, Img, Link):
        # Initializes the fields with entered data
        # and sets the published date to the current time
        self.name = name
        self.Description = Description
        self.PEGI = PEGI
        self.Img = Img
        self.Link = Link
        # self.pub_date = datetime.now()


def is_email_address_valid(email):
    """Validate email address using regular expression."""
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
        return False
    return True


# The default route for the app.
# Displays the list of already entered comments
# We are getting all the comments ordered in
# descending order of pub_date and passing to the
# template via 'comments' variable
@app.route('/')
def show_all():
    # s=select([Comments])
    # a=Comments.query.filter_by(name="Facebook").all()
    # print(a)

    # return render_template('show_all.html', comments=Comments.query.order_by(Comments.name).all()  )
    return render_template('kosher.html', comments=Comments.query.order_by(Comments.name).all())


@app.route('/search',methods=['GET','POST'])
def search():
    if request.method== 'POST':
        if not request.form['search']:

            return redirect(url_for('show_all'))
        else:
            query=Comments.query.filter_by(name=request.form['search']).all()

            return render_template('search.html',comments=query)





    return render_template('kosher.html',comments=Comments.query.order_by(Comments.name).all())
    # return render_template('search.html',comments=Comments.query.order_by(Comments.name).all())


# This view method responds to the URL /new for the methods GET and POST
# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         # The request is POST with some data, get POST data and validate it.
#         # The form data is available in request.form dictionary.
#         # Check if all the fields are entered. If not, raise an error
#         if not request.form['name'] or not request.form['email'] or not request.form['comment']:
#             flash('Please enter all the fields', 'error')
#
#         # Check if the email address is valid. If not, raise an error
#         elif not is_email_address_valid(request.form['email']):
#             flash('Please enter a valid email address', 'error')
#
#         else:
#             # The data is valid. So create a new 'Comments' object
#             # to save to the database
#             comment = Comments(request.form['name'],
#                                request.form['email'],
#                                request.form['comment'],'0')
#
#             # Add it to the SQLAlchemy session and commit it to
#             # save it to the database
#             db.session.add(comment)
#             db.session.commit()
#
#             # Flash a success message
#             flash('Comment was successfully submitted')
#
#             # Redirect to the view showing all the comments
#             return redirect(url_for('show_all'))
#
#     # Render the form template if the request is a GET request or
#     # the form validation failed
#     return render_template('new.html')


# This is the code that gets executed when the current python file is
# executed.
if __name__ == '__main__':
    # Run the app on all available interfaces on port 80 which is the
    # standard port for HTTP
    app.run(
        host="localhost",
        port=int("80")
    )
    # c=Comments('rafi','1@gmail.com','qqq')
    # comments=Comments.query.order_by(Comments.pub_date.desc()).all()
    # for c in comments:
    #     print(c.comment)
