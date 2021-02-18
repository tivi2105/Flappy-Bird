import random
import time
import tkinter
from tkinter import *


def drawPipes(canvas):
	global root, x1, y1, x2, y2, pa1, pa2, pb1, pb2, moon, moonY, jump, score
	canvas.move(pa1, -10, 0)
	canvas.move(pa2, -10, 0)
	canvas.move(pb1, -10, 0)
	canvas.move(pb2, -10, 0)
	if(jump > 0):
		canvas.move(moon, 0, -10)
		moonY -= 10
		jump -= 2
	else:
		canvas.move(moon, 0, 20)
		moonY += 20
	x1 -= 10
	x2 -= 10
	if(x1 < 0):
		canvas.delete(pa1)
		canvas.delete(pa2)
		x1 = random.randint(70, 90)*10
		y1 = random.randint(10, 50)*10
		pa1 = canvas.create_rectangle(x1, 0, x1+20, y1, fill='white')
		pa2 = canvas.create_rectangle(x1, y1+100, x1+20, 600, fill='white')
		score += 1
	if(x2 < 0):
		canvas.delete(pb1)
		canvas.delete(pb2)
		x2 = x1+300
		y2 = random.randint(10, 50)*10
		pb1 = canvas.create_rectangle(x2, 0, x2+20, y2, fill='white')
		pb2 = canvas.create_rectangle(x2, y2+100, x2+20, 600, fill='white')
		score += 1
	#print(moonY)
	if(moonY >=0 and moonY <= 550 and notCollided(canvas)):
		canvas.after(50, drawPipes, canvas)
	else:
		canvas.destroy()
		w = tkinter.Label(root)
		s = 'score:'+str(score)
		w.configure(text=s)
		w.pack()

def move(root, canvas, x1, y1, x2, y2):
	x1 -= 10
	x2 -= 10
	if(x1 < 0):
		x1 = random.randint(70, 90)*10
		y1 = random.randint(10, 50)*10
	if(x2 < 0):
		x2 = x1+300
		y2 = random.randint(10, 50)*10

def changeJump(event):
	global jump
	jump += 10

def notCollided(canvas):
	global x1, y1, x2, y2, moonY
	#print(x1,y1,moonY)
	if(0 < x1 < 50 and (moonY < y1 or moonY+50 > y1+100) or (0 < x2 < 50 and (moonY <= y2 or moonY+50 >= y2+100))):
		return False
	return True

def StartGame():
	global root, x1, y1, x2, y2, pa1, pa2, pb1, pb2, moon, moonY, jump, score
	for ele in root.winfo_children():
		ele.destroy()
	x1 = random.randint(70, 90)*10
	y1 = random.randint(10, 50)*10
	x2 = x1+300
	y2 = random.randint(10, 50)*10
	moonY = 10
	jump = 0
	score = 0
	canvas = Canvas(root, width=800, height=600)
	canvas.pack()
	canvas.create_rectangle(0, 0, 800, 600, fill='black')
	moon = canvas.create_oval(10, moonY, 50, 50, fill='red')
	pa1 = canvas.create_rectangle(x1, 0, x1+20, y1, fill='white')
	pa2 = canvas.create_rectangle(x1, y1+100, x1+20, 600, fill='white')
	pb1 = canvas.create_rectangle(x2, 0, x2+20, y2, fill='white')
	pb2 = canvas.create_rectangle(x2, y2+100, x2+20, 600, fill='white')
	drawPipes(canvas)

def newGame(event):
	if(event.char == 'a'):
		StartGame()
		

x1 = random.randint(70, 90)*10
y1 = random.randint(10, 50)*10
x2 = x1+300
y2 = random.randint(10, 50)*10
moonY = 10
jump = 0
score = 0
root = tkinter.Tk()
root.geometry('800x600')
StartGame()
root.bind("<space>", changeJump)
root.bind("<Key>", newGame)
root.mainloop()