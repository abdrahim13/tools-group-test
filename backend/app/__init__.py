
from flask import (
    Flask,
    abort,
    render_template,
)
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

import app.config as config


# init app
app = Flask(__name__,
            static_folder='public',
            template_folder='views')

app.config.from_object(config.DevelopmentConfig)

# init database
db = SQLAlchemy(app)

api_router = Api(app, prefix='/api')

# For testing add CORS
# (Because frontend is on different Port)
if app.config.get('DEVELOPMENT'):
    from flask_cors import CORS
    # config cores post
    CORS(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


""" @app.before_request
def before_request():
    # attach db session to request
    g.db = db.session
     """


# Vue app entry point
@app.route('/')
def index():
    return render_template("index.html")


# API resources
from app.api import todo_resources as resources

api_router.add_resource(resources.Todo, '/todo/<int:todo_id>')
api_router.add_resource(resources.TodoList, '/todos')
api_router.add_resource(resources.SearchTodoList, '/todos/search')

""" # PAGES Blueprints
app.register_blueprint(main.bp) """
