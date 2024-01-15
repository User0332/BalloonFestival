import dill
import sys
import os

DATA_DIR = f"{os.path.dirname(sys.argv[0])}/../data/volunteers/"

num = 0

for filename in os.listdir(DATA_DIR):
	file = os.path.join(DATA_DIR, filename)

	if not os.path.isfile(file): continue

	with open(file, "rb") as f:
		volunteer = dill.load(f)

		print(f"{volunteer.full_name} ({volunteer.CAPID})")
		
	num+=1

print(f"{num} total volunteer(s)")