from flask import Flask, Blueprint, Response, render_template, jsonify, url_for
from flask.views import MethodView
import pdfkit
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
        options = {
            'disable-javascript':False,
        }
        goog = pdfkit.from_url("http://www.crtlabs.org/crt%20labs/smart%20devices/iot/2015/11/25/giftguide3.html", False, options=options)
        logging.info(goog)
        return Response(goog, mimetype="application/pdf")

class Link(MethodView):
    def get(self):
        return Response("<html><body><a href='http://tearsheets.local'>Link</a></body></html>", mimetype="text/html")

pdf.add_url_rule("/", view_func=PDF.as_view('index'))
pdf.add_url_rule("/link", view_func=Link.as_view('link'))
