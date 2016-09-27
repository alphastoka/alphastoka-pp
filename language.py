#!venv/bin/python3.5
#
import re
def language(text):
	m = re.search(r'[ก-ฮ]', text, re.UNICODE)
	if m is None:
		return "EN"
	else:
		return "TH"