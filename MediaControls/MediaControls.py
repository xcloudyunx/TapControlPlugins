import sys
import json
import os

__name = "MediaControls"
__version = "0.0.0"
__properties = {
	# reserved property names
	# page
	# id
	# name
	# image
	"Control":{
		"type":"choice",
		"required":True,
		"settings":["Play/Pause", "Next Track", "Previous Track", "Volume Mute", "Volume Down", "Volume Up", "Mic Mute"]
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
	import win32api, win32gui
	WM_APPCOMMAND = 0x0319
	
	commands = {
		"Play/Pause":0xE0000,
		"Next Track":0xB0000,
		"Previous Track":0xC0000,
		"Volume Mute":0x80000,
		"Volume Down":0x90000,
		"Volume Up":0xA0000,
		"Mic Mute":0x180000
	}

	hwnd_active = win32gui.GetForegroundWindow()
	win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, commands[properties["Control"]])
	

if len(sys.argv) < 2:
	raise Exception("need to provide arguments")
elif sys.argv[1] == "--setup":
	print(getName())
	print(getVersion())
	print(getProperties())
elif len(sys.argv) > 2:
	run(sys.argv[1:])