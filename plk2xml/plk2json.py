import json

def plk2json(plk, indent=None):
	return json.dumps(plk.data, indent=indent)