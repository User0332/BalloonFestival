import dill
import sys
import os

if len(sys.argv) < 2:
	print("Must specify CAPID as first argument")
	exit(1)

CAPID = sys.argv[1]

with open(f"{os.path.dirname(sys.argv[0])}/../data/volunteers/{CAPID}", "rb") as f:
	print(dill.load(f))