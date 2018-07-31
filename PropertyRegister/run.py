from sqlalchemy.event import listens_for

from PropertyRegister.app import app

# init Flask
# app = Flask(__name__)
#
# # Basic config with security for forms and session cookie
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://marsyu:123456@localhost:3306/propertyregister'
# app.config['CSRF_ENABLED'] = True
# app.config['SECRET_KEY'] = 'thisismyscretkey'
#
# # Init SQLAlchemy
# db = SQLA(app)
# # Init F.A.B.
# appbuilder = AppBuilder(app, db.session)

# Run the development server
# from PropertyRegister.app.models import Property

app.run(host='127.0.0.1', port=8080, debug=True)

