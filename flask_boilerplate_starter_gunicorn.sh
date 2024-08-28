#/bin/bash

# ACCESS_LOG_FORMAT='%(h)s %(l)s %(u)s %(t)s PID: [%(p)s] "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" - %(M)s ms'

# gunicorn --access-logfile logs/gunicorn_access.log --error-logfile logs/gunicorn_error.log --log-level ${LOG_LEVEL} \
#     --access-logformat "${ACCESS_LOG_FORMAT}" --timeout ${TIMEOUT} --worker-class sync --threads ${THREADS} --workers ${WORKERS} --max-requests ${MAX_REQUESTS} \
#     --max-requests-jitter ${MAX_REQUESTS_JITTER} --preload --name vimadp_api_server --bind 0.0.0.0:5036 --config gunicorn_config.py vimadp_api:app

python build_db.py

if [ ! -d logs ]; then
    echo "Created 'logs' directory!"
    mkdir logs
fi


gunicorn \
--access-logfile logs/gunicorn_access.log \
--error-logfile logs/gunicorn_error.log \
--log-level INFO  \
--worker-class sync \
--name flask_boilerplate1 \
--bind 0.0.0.0:12000 \
"run:app"
