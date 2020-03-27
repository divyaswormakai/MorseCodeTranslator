from playsound import playsound
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from MorseCodeTranslator import ChangeToMorseCode
import time

dotPath = './Audio/short.mp3'
dashPath = './Audio/long.mp3'

def Convert():
	print("Converting")
	txt = str(textBox.get("1.0", tk.END)).strip()

	if len(txt)>0:
		print(txt)
		morseCode = ChangeToMorseCode(txt)
		f=open("MorseCode.txt","w")
		f.write(morseCode)
		f.close()
		speakBtn.configure(state=tk.NORMAL)

def Speak():
	print("Speaking in morse")
	f=open("MorseCode.txt","r")
	line = f.readline()
	while line:
		letters = line.split(' ')
		for letter in letters:
			for part in letter:
				if(part =='.'):
					print("dot")
					PlayDot()
				elif(part == '-'):
					print("dash")
					PlayDash()
			print("-------------")
			time.sleep(0.1)
		time.sleep(0.15)

		line = f.readline()

def PlayDot():
	playsound(dotPath)

def PlayDash():
	playsound(dashPath)

window = tk.Tk()
window.title("Morse Corse Translator")
window.minsize(400,100)

label = tk.Label(window,text = "Enter the text here")
label.place(x=10,y=10,width =100,height=100)

textBox = ScrolledText(window)
textBox.pack()
textBox.place(x=120,y=10,width =250,height=100)

convertBtn = tk.Button(window,text="Convert",command=Convert)
convertBtn.place(x=190,y=120,width=75,height=25)

speakBtn = tk.Button(window,text="Speak in morse", command=Speak,state=tk.DISABLED)
speakBtn.place(x=175,y=160,width=100,height=25)

window.mainloop()

