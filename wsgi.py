from gevent import monkey
monkey.patch_all()

from werkzeug.wsgi import peek_path_info
from tearsheets import config
from tearsheets import App
from tearsheets import pdf
import logging

logging.basicConfig(level=config.LOG_LEVEL)

def create_app():
    logging.info("Initializing")
    _app = App()
    _app.register_blueprint(pdf)
    def app(env, start_response):
        #healthcheck(_app, env)
        return _app(env, start_response)

    logging.info("Running")
    return app

app = create_app()
