import re
phone = "Home: (555) 265-2901"
result = re.search('\((\d{3})\)', phone)
area_code = result.group(1)
print("The area code is: " + area_code)
