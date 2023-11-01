from webpy import App

app = App(__name__, template_folder="html")

def webpy_setup(app: App):
	app.debug = True