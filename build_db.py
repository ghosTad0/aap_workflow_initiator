from aap_wf_init_api_server.webapp_components.database.db_config import db
from aap_wf_init_api_server.commons.configurator import flask_app
from aap_wf_init_api_server.webapp_components.database.db_models import *


with flask_app.app_context():
    db.create_all()