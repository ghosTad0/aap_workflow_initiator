#/bin/bash

python build_db.py
if [[ $? != 0 ]]; then
    exit
fi
export FLASK_APP=run
flask run --host 0.0.0.0 --port 12000