from flask import blueprints, jsonify, request
import random

from aap_wf_init_api_server.aap_wf_init_services.srv2.srv2_utils import srv2_number_of_fields
from aap_wf_init_api_server.webapp_components.database.db_models import User
from aap_wf_init_api_server.webapp_components.database.db_config import db

bp = blueprints.Blueprint(name="bp_srv1", import_name="__name__", url_prefix="/srv1")

@bp.route("/init")
def srv1_init():
    srv1_init_data = {
        "message": "srv1 initiated!!",
        "status": "ACTIVE",
        "value": random.randint(1, 100),
        "__name__": __name__
    }
    srv1_init_data['number_of_fields'] = srv2_number_of_fields(srv1_init_data) + 1
    return jsonify(srv1_init_data)

@bp.route("/user", methods=["POST"])
def user_add():
    user_create_req = request.json
    try:
        user_object = User(username=user_create_req['username'], email=user_create_req['email'])
        db.session.add(user_object)
        db.session.commit()
        user_add_resp = {'status': 'created'}
        return jsonify(user_add_resp), 200
    except Exception as e:
        error_resp = {'status': 'failed', 'err_msg': str(e)}
        return jsonify(error_resp), 500
