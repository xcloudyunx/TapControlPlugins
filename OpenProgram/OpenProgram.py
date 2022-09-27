import sys
import json
import os

__name = "OpenProgram"
__version = "0.0.0"
__properties = {
	# reserved property names
	# page
	# id
	# name
	# image
	"Program":{
		"type":"file",
		"required":True,
		"settings":""
	}
}

def getName():
	return __name

def getVersion():
	return __version
	
def getProperties():
	return json.dumps(__properties)
	
def run(args):
	properties = {}
	if len(args)%2:
		raise Exception("the number of properties and values are different")
	for i in range(0, len(args), 2):
		prop = args[i]
		value = args[i+1]
		properties[prop] = value
	
	for prop in __properties:
		if __properties[prop]["required"] and prop not in properties:
			raise Exception(prop+" is a required property")
	
	# handle running
	os.system("\""+properties["Program"]+"\"")

if len(sys.argv) < 2:
	raise Exception("need to provide arguments")
elif sys.argv[1] == "--setup":
	print(getName())
	print(getVersion())
	print(getProperties())
elif len(sys.argv) > 2:
	run(sys.argv[1:])