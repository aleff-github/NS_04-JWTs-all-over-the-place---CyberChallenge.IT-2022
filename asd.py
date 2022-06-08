import base64
from datetime import datetime
import re

output = open("output_decoded.txt", "r")
lines = output.readlines()

d1 = datetime(2022, 5, 31)
d2 = datetime(2022, 6, 2)

for line in lines:
	pattern = '"nbf":(\d+),"exp":(\d+)'
	match = re.search(pattern, line)
	
	gruppi = match.group().split(",\"exp\":")
	date2 = datetime.fromtimestamp(int(gruppi[1]))
	
	gruppi = gruppi[0].split("\"nbf\":")
	date1 = datetime.fromtimestamp(int(gruppi[1]))
	
	if date1 <= datetime(2022, 6, 1):
		if date2 >= datetime(2022, 6, 1):
			print(line)
			print(date1)
			print(date2)
