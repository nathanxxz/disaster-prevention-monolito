from flask import *
from extension import login
from extension import db
from blueprints.bp_disaster import bp_disaster
from blueprints.bp_user_admin import bp_admin
from blueprints.bp_user_cliente import bp_cliente



app = Flask(__name__)

app.config['SECRET_KEY'] = 'KJHJH3w42#n!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:98087343@localhost:5432/disaster-prevention-b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

login.init_app(app)

app.register_blueprint(bp_admin)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_disaster)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)