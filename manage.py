from flask.ext.script import Manager, Command, Option
from tearsheets import App
import logging
import pdfkit

logging.basicConfig(level=logging.INFO)
app = App()
manager = Manager(app)

class CreatePDF(Command):

    def run(self):
        options = {
            'disable-javascript':False
        }
        goog = pdfkit.from_url("http://www.crtlabs.org/crt%20labs/smart%20devices/iot/2015/11/25/giftguide3.html", './output.pdf', options=options)


manager.add_command('create_pdf', CreatePDF())

if __name__ == "__main__":
    manager.run()
