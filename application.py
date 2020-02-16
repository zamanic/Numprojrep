from flask import Flask, render_template
from wtform_fields import *
from models import *
app = Flask(__name__)
app.secret_key = 'replace later'
# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://haxnusriwibfjq:eacc7b9a8f248e91c7840059a4e31569bbaadc163125e934f926adb103ecff8d@ec2-23-21-13-88.compute-1.amazonaws.com:5432/dtkqb7hfh1sko'
db = SQLAlchemy(app)
@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        #return "Great Success!"
        username = reg_form.username.data
        password = reg_form.password.data
        #Check username exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username"
# Add user to DB
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB"
    return render_template("index.html", form=reg_form)
if __name__ == "__main__":
    app.run(debug=True)
