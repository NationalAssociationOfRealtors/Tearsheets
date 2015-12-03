from flask import Flask, Blueprint, Response, render_template, jsonify, url_for
from flask.views import MethodView
import logging

class App(Flask):

    def __init__(self):
        super(App, self).__init__(__name__)
        self.config.from_object('tearsheets.config')
        logging.info("SERVER_NAME: {}".format(self.config['SERVER_NAME']))

pdf = Blueprint(
    'pdf',
    __name__,
)

class PDF(MethodView):

    def get(self):
        logging.info("Create PDF!")
        return Response('woot!', mimetype="text/html")

pdf.add_url_rule("/", view_func=PDF.as_view('index'))
