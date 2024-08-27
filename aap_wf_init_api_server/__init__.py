from flask import Flask, jsonify
import random
from aap_wf_init_api_server.commons.configurator import flask_app
from aap_wf_init_api_server.webapp_components.test_comp1 import square_of

from aap_wf_init_api_server.aap_wf_init_services.srv1.srv1_ctrl1 import bp as srv1_bp
# from aap_wf_init_api_server.webapp_components.database.db_config import db

def create_app():

    #Configs
    # app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    #blueprint imports
    flask_app.register_blueprint(srv1_bp)

    #endpoints
    @flask_app.route('/init')
    def init_page():
        return jsonify({
            "message": "let's begin",
            "val": square_of(random.randint(100, 1000))
        })
    return flask_app