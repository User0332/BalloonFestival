from webpy import App
import os
import sys

sys.path.append(os.path.abspath('.'))


app = App(__name__, template_folder="html")

def webpy_setup(app: App):
	app.debug = True

	app.config["APP_DIR"] = os.path.abspath(".")
	app.config["VOLUNTEER_DIR"] = os.path.join(os.path.abspath("."), "../data/volunteers")
