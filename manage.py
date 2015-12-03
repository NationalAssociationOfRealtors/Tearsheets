from flask.ext.script import Manager, Command, Option
from tearsheets import App
import logging

logging.basicConfig(level=logging.INFO)
app = App()
manager = Manager(app)

class CreatePDF(Command):

    def run(self):
        logging.info("creating PDF")


manager.add_command('create_pdf', CreatePDF())

if __name__ == "__main__":
    manager.run()
