from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import logging

logging.basicConfig(level=logging.INFO)

# Create the Flask app
app = Flask(__name__)
# Set the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
# Create the SQLAlchemy database object
db = SQLAlchemy(app)


class User(db.Model):
    """Model for storing Users."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False, unique=True)


def insert_users():
    """Insert Users"""
    try:
        leonardo = User(name="Leonardo Caballero", address="Av. 16 de Septiembre, Edif. 23, Merida")
        ana = User(name="Ana Poleo", address="Urb. Monte Mario, C. Trevi, 6001, Anzoátegui")
        manuel = User(name="Manuel Matos", address="Av. 03 de Septiembre, Edif. 56, Merida")
        # New objects are added to the database
        db.session.add_all([leonardo, ana, manuel])
        # Save changes to the database
        db.session.commit()
        logging.info(f"Successful insertion users!\n")
        # Return a info message with JSON format
    except exc.IntegrityError as e:
        logging.error(f"Integrity data error when try to insert new users: {str(e)}\n")
        # Return a error message with JSON format
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500


@app.route("/create", methods=["POST"])
def create_user():
    """Create a User"""
    try:
        # Gets the data from the request body in JSON format
        data = request.get_json(force=True)
        if not data or "name" not in data or "address" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        user = User(name=data["name"], address=data["address"])
        # Add to database and commit changes
        db.session.add(user)
        # Save changes to the database
        db.session.commit()
        logging.info("The record was entered correctly in the table!")
        # Return a info message with JSON format
        return jsonify(
            {"message": "User created", "user": {"id": user.id, "name": user.name, "address": user.address}}
        ), 201  # Code 201, indicates that the User was successfully created
    except Exception as e:
        logging.error(f"Error creating user: {str(e)}")
        # Return a error message with JSON format
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500


@app.route("/update/<int:id>", methods=["PUT"])
def update_user(id):
    """Update a User"""
    try:
        # Get User by ID or return 404 does not exist
        user = User.query.get_or_404(id)
        # Get data from the body of the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        # Update the fields if they exist in the application
        if "name" in data:
            user.name = data["name"]
        if "address" in data:
            user.address = data["address"]
        # Save changes to the database
        db.session.commit()
        # Return a info message with JSON format
        return jsonify(
            {"message": "User updated", "user": {"id": user.id, "name": user.name, "address": user.address}}
        ), 200  # Code 200 Ok, indicates that the User was successfully updated
    except Exception as e:
        logging.error(f"Error updating user: {str(e)}")
        # Return a error message with JSON format
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500



@app.route("/")
def get_users():
    """Get all the Users"""
    # Get all User order by ID
    users = db.session.execute(db.select(User).order_by(User.id)).scalars()
    data = []
    for user in users:
        data.append({"user": {"id": user.id, "name": user.name, "address": user.address}})
    logging.info("Users list was shows correctly!")
    # Return a info message with JSON format
    return jsonify({"data": data})


@app.route("/detail/<int:id>", methods=["GET", "POST"])
def detail_user(id):
    """Get details of a User"""
    # Get User by ID
    user = db.get_or_404(User, id)
    logging.info("User ID was found correctly!")
    # Return a info message with JSON format
    return jsonify(
        {"message": "User details", "user": {"id": user.id, "name": user.name, "address": user.address}}
    )


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    """Delete a User"""
    try:
        # Get User by ID or return 404 does not exist
        user = User.query.get_or_404(id)
        # Delete User
        db.session.delete(user)
        # Save changes to the database
        db.session.commit()
        logging.info("The record in the table was deleted correctly!")
        # Return a info message with JSON format
        return jsonify(
            {"message": "User deleted", "user": {"id": user.id, "name": user.name, "address": user.address}}
        ), 200  # Code 200 Ok, indicates that the User was successfully deleted
    except Exception as e:
        logging.error(f"Error deleting user: {str(e)}")
        # Return a error message with JSON format
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500


with app.app_context():
    try:
        # Create the database tables
        db.create_all()
        logging.info(f"The table was created correctly in the database!\n")
    except exc as error:
        logging.error(f"Failed to create table(s) in the database: {error}")
    # Insert users data default
    insert_users()
