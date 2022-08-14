import sys
import json

__name = "template"
__version = "0.0.0"
__description = """
This is the description for the plugin template.\r\n
Newline.
"""
__author = "Yunge Yu"
__homepage = "https://github.com/xcloudyunx/TapControlPlugins/tree/main/template"
__properties = {
	# reserved property names
	# page
	# id
	# name
	# image
	"property1":{
		"type":"choice",
		"required":True,
		"settings":["option1", "option2"]
	},
	"property2":{
		"type":"file",
		"required":False,
		"settings":"(*.png)|*.png"
		# "settings":"filetypename (*.extension1,*.extension2,...)|*.extension1;*.extension2;..."
	}
}
# user typing???
# recording macro????

def getName():
	return __name

def getVersion():
	return __version

def getDescription():
	return __description
	
def getAuthor():
	return __author
	
def getHomePage():
	return __homepage
	
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
	print(properties)
	print("yay everything runs")

if sys.argv[1] == "--name":
	print(getName())
elif sys.argv[1] == "--version":
	print(getVersion())
elif sys.argv[1] == "--description":
	print(getDescription())
elif sys.argv[1] == "--author":
	print(getAuthor())
elif sys.argv[1] == "--homepage":
	print(getHomePage())
elif sys.argv[1] == "--properties":
	print(getProperties())
elif len(sys.argv) > 2:
	run(sys.argv[1:])