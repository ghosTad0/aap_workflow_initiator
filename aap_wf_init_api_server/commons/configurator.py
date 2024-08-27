from flask import Flask
from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('/hms/apps/aap_workflow_initiator/conf/aap_wf_init.ini')

base_dir = config.get('default', 'base_directory')


# flask app object
flask_app = Flask(__name__)