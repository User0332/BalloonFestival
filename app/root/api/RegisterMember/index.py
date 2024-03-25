from volunteer import Volunteer
import os
import webpy
import dill

def handler(app: webpy.App, *args):
	from flask import request, redirect

	blocks_committed = [int(block) for block in request.form.getlist("blocks_committed")]

	volunteer = Volunteer(
		int(request.form["CAPID"]),
		request.form["fname"],
		request.form["lname"],
		request.form["squadron"],
		request.form["grade"],
		int(request.form["age"]),
		int(request.form["member_type"]),
		blocks_committed,
		int(request.form["food_pref"]),
		request.form["med_hist"],
		bool(request.form.get("icut_cert")),
		bool(request.form.get("driver")),
		(bool(request.form.get("camping_fri")), bool(request.form.get("camping_sat"))),
		int(request.form["experience_level"])
	)

	with open(os.path.join(app.config['VOLUNTEER_DIR'], str(volunteer.CAPID)), "wb") as f:
		dill.dump(volunteer, f)

	return redirect("/CadetActionsPage")