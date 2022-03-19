import random
import time 
from playsound import playsound


def doYes():
	print("Ben: Yes")
	playsound('yes.wav')
def doNo():
	print("Ben: No")
	playsound('no.wav')
def doHohoho():
	print("Ben: Hohoho")
	playsound('hohoho.wav')
def doEugh():
	print("Ben: Eugh")
	playsound('eugh.wav')
	


def main():
	print("Talkin' Ben")
	
	playsound('baen.wav')
	while True:
		print(" ")
		playerInput = input("You: ")
		print(" ")
		time.sleep(0.4)
		num = random.randint(1, 4)
		if num == 1:
			doYes()
		elif num == 2:
			doNo()
		elif num == 3:
			doHohoho()
		elif num == 4:
			doEugh()

main()	
		
	