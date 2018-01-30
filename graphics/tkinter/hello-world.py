#!/usr/bin/python

from os import listdir

print 'Hello, world!'

print listdir('/usr')

def printsomething(txt):
	print txt
	return "nothing"

printsomething("test")

# GUI example
# --------------------------------------------------
import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()