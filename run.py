from aap_wf_init_api_server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=12000, debug=True)