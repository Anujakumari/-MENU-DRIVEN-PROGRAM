import os
os.system("cls")
os.system("color 6")

import pyttsx3
pyttsx3.speak( "Hello! Welcome to this Program " )

from pyfiglet import Figlet
f = Figlet( font = "puffy")
result = f.renderText( " *** CHAT WITH ME *** ")
print(result)

while True:
	print("WHAT CAN I DO FOR YOU: ", end = " ")
	x = input()
	if (("open" in x) or ("run" in x) or ("execute" in x)) and (("chrome" in x) or ("google" in x)):
		os.system("chrome")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("notepad" in x) or ("text" in x) or ("editor" in x)):
		os.system("notepad")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("Paint" in x) or ("mspaint" in x) or ("drawing" in x)):
		os.system("Paint")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("Word" in x) or ("msword" in x) or ("document" in x)):
		os.system("Word")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("Excel" in x) or ("sheet" in x) or ("MSexcel" in x)):
		os.system("Excel")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("wmplayer" in x) or ("media" in x) or ("player" in x) or ("songs" in x)):
		os.system("wmplayer")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("PowerPoint" in x) or ("mspowerpoint" in x) or ("POWERPOINT" in x) or ("ppt" in x)):
		os.system("PowerPoint")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("Control" in x) or ("Panel" in x)):
		os.system("Control Panel")
	elif (("bye" in x) or ("exit" in x) or ("stop" in x) or ("close" in x)):
		pyttsx3.speak("bye, Have a NICE Day!!")
		break
	else:
		pyttsx3.speak("SORRY, This Program is not supported.")