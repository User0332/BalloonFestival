from dataclasses import dataclass
import datetime
import webpy
import dill

TimeSlot = None
FoodPreference: str

SENIOR_MEMBER = 0
CADET_MEMBER = 1

MemberType = int

NOT_A_CAP_MEMBER = 0

@dataclass
class Volunteer:
	CAPID: int
	fname: str
	lname: str
	squadron: str
	grade: str
	age: str
	member_type: MemberType
	blocks_committed: list[TimeSlot]
	food_pref: FoodPreference
	experience_level: int = None
	weighted_exp: int = None
	med_hist: str
	icut_cert: bool
	driver: bool
	camping: tuple[bool, bool]

	@property
	def full_name(self):
		return f"{self.fname} {self.lname}"

	@property
	def camping_friday(self):
		return self.camping[0]
	
	@property
	def camping_saturday(self):
		return self.camping[1]


def handler(app: webpy.App, *args):
	from flask import request
	
	name: str = None

