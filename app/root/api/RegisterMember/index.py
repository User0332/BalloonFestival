from dataclasses import dataclass
import os
import webpy
import dill

TimeSlot = int
FoodPreference: str

SENIOR_MEMBER = 0
CADET_MEMBER = 1

NO_FOOD_PREF = 0
VEGETARIAN = 1
NO_BEEF = 2
NO_PORK = 3
VEGAN = 4

FOOD_PREF_MAP = {
	NO_FOOD_PREF: "anything",
	VEGETARIAN: "vegetarian",
	NO_BEEF: "no beef",
	NO_PORK: "no pork",
	VEGAN: "vegan"
}

CAMPING_MAP = {
	(True, True): "both days",
	(True, False): "Friday-Saturday only",
	(False, True): "Saturday-Sunday only",
	(False, False): "neither day."
}

MemberType = int
FoodPreference = int

NOT_A_CAP_MEMBER = 0

class Volunteer:
	def __init__(
		self,
		CAPID: int,
		fname: str,
		lname: str,
		squadron: str,
		grade: str,
		age: str,
		member_type: MemberType,
		blocks_committed: list[TimeSlot],
		food_pref: FoodPreference,
		med_hist: str,
		icut_cert: bool,
		driver: bool,
		camping: tuple[bool, bool],
		experience_level: int,
		weighted_exp: int = None,
	):
		self.CAPID = CAPID
		self.fname = fname
		self.lname = lname
		self.squadron = squadron
		self.grade = grade
		self.age = age
		self.member_type = member_type
		self.blocks_committed = blocks_committed
		self.food_pref = food_pref
		self.med_hist = med_hist
		self.icut_cert = icut_cert
		self.driver = driver
		self.camping = camping
		self.experience_level = experience_level
		self.weighted_exp = weighted_exp



	@property
	def full_name(self):
		return f"{self.fname} {self.lname}"

	@property
	def camping_friday(self):
		return self.camping[0]
	
	@property
	def camping_saturday(self):
		return self.camping[1]


	def __str__(self) -> str:
		"I have committed to {len(self.blocks_committed)} blocks: {','.join(self.blocks_committed)}."
		return f"This is {'C/' if self.member_type == CADET_MEMBER else ''}{self.grade} {self.full_name} (Member #{self.CAPID}) from {self.squadron}. I am {self.age} years old and have been to the balloon festival {self.experience_level} time(s) ebfore. I am a {'cadet' if self.member_type == CADET_MEMBER else 'senior member'}. My food preference is {FOOD_PREF_MAP[self.food_pref]}. My medical history is {len(self.med_hist)} characters long.{' I am ICUT certified.' if self.icut_cert else ''}{' I am a driver.' if self.driver else ''} I will be camping on {CAMPING_MAP[self.camping]}. My weighted experience is {self.weighted_exp}"


def handler(app: webpy.App, *args):
	from flask import request, redirect

	volunteer = Volunteer(
		int(request.form["CAPID"]),
		request.form["fname"],
		request.form["lname"],
		request.form["squadron"],
		request.form["grade"],
		int(request.form["age"]),
		int(request.form["member_type"]),
		request.form.get("blocks_committed"),
		int(request.form["food_pref"]),
		request.form["med_hist"],
		bool(request.form["icut_cert"]),
		bool(request.form["driver"]),
		(bool(request.form["camping_fri"]), bool(request.form["camping_sat"])),
		int(request.form["experience_level"])
	)

	with open(os.path.join(app.config['VOLUNTEER_DIR'], str(volunteer.CAPID)), "wb") as f:
		dill.dump(volunteer, f)

	return redirect("/CadetActionsPage")