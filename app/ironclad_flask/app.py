from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import re
from datetime import datetime

app = Flask(__name__)

# Configure PostgreSQL database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ironclad:ironclad-is-copperbottom@pg.pg.svc.cluster.local:5432/ironclad'
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://ironclad:ironclad-is-copper-bottom@192.168.49.2:31352/ironclad"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Define the database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def is_valid_phone(phone):
    pattern = r"^\+1\d{10}$|^(\d{3}-\d{3}-\d{4})$|^\d{10}$"
    return re.match(pattern, phone)


def is_valid_date(date):
    try:
        datetime.strptime(date, "%m/%d/%Y")
        return True
    except ValueError:
        return False


@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route("/add", methods=["POST"])
def add_user():
    data = request.form

    first_name = data.get("first_name").strip()
    middle_name = data.get("middle_name", "").strip()
    last_name = data.get("last_name").strip()
    email = data.get("email").strip()
    phone_number = data.get("phone_number").strip()
    date_of_birth = data.get("date_of_birth").strip()

    if not first_name.isalpha() or not last_name.isalpha():
        return "Name fields should contain only alphabetic characters.", 400

    if not is_valid_email(email):
        return "Invalid email format.", 400

    if not is_valid_phone(phone_number):
        return "Invalid phone number format. Must be valid USA number.", 400

    if not is_valid_date(date_of_birth):
        return "Invalid date format. Use MM/DD/YYYY.", 400

    dob = datetime.strptime(date_of_birth, "%m/%d/%Y")

    new_user = User(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        date_of_birth=dob,
    )

    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found.", 404

    data = request.form

    user.first_name = data.get("first_name", user.first_name).strip()
    user.middle_name = data.get("middle_name", user.middle_name).strip()
    user.last_name = data.get("last_name", user.last_name).strip()
    user.email = data.get("email", user.email).strip()
    user.phone_number = data.get("phone_number", user.phone_number).strip()
    date_of_birth = data.get(
        "date_of_birth", user.date_of_birth.strftime("%m/%d/%Y")
    ).strip()

    if not user.first_name.isalpha() or not user.last_name.isalpha():
        return "Name fields should contain only alphabetic characters.", 400

    if not is_valid_email(user.email):
        return "Invalid email format.", 400

    if not is_valid_phone(user.phone_number):
        return "Invalid phone number format. Must be valid USA number.", 400

    if not is_valid_date(date_of_birth):
        return "Invalid date format. Use MM/DD/YYYY.", 400

    user.date_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y")

    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found.", 404

    db.session.delete(user)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)
