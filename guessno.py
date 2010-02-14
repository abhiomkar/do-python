#!/Library/Frameworks/Python.framework/Versions/2.6/bin/python
#Author: Abhinay Omkar
#Title: Guess Number Game

import random

class GuessNumber:
    def startGame(self):
	print 'Guess a number!'
	t=0
	for t in xrange(6):
		num = raw_input("\ntry ("+str(t+1)+")] ")
		try:
			inp = int(num)
		except ValueError:
			inp=0

		if(inp == random.randint(1,10)):
			print "\nWinner! You guessed the number in "+str(t+1)+" guesses! Well done!"
			return self.quitGame()
		else:
			print random.choice(['nah!', 'what?', 'try again plz', 'No', 'he he..', 'bad'])
	print 'You reached maximum number of guesses :('	
	return self.quitGame()
	
    def quitGame(self):
	if(str(raw_input("\nTry Again? (Y/n)")).lower() in ('y','')):
	# Game is Interesting! :)
		return True
	else:
	# Game is NOT Interesting! :(
		print "Thx for using our useless games! Bye! ;)"
		return False

if __name__ == '__main__':
	G = GuessNumber()
	GameIsInteresting = True
	while GameIsInteresting:
		GameIsInteresting = G.startGame()
