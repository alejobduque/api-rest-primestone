from flask import Flask

from models.Models import db
from services.routes import services
from validations import page_not_found, method_not_allowed


app = Flask(__name__)
app.register_blueprint(services)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/object-json'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.run(debug=True, port=5000)
