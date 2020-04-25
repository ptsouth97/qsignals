#!/usr/bin/python3

import random


def main():
	''' main function for quizzing on QSignals for Ham Radio'''

	qsignals=[['QRG', 'exact frequency'],
			  ['QRL','busy'],
			  ['QRM','interference'],
  	  		  ['QRN','static'],
		  	  ['QRO','increase power'],
		  	  ['QRP','decrease power'],
		  	  ['QRQ','send faster'],
		  	  ['QRS','send slower'],
		  	  ['QRT','stop sending']]

	print('Welcome to the QSignal Quiz!')
	print('')

	total = 0
	correct = 0

	while True:
				
		random_choice = qsignals[random.randint(0, len(qsignals)-1)]
		meaning = random_choice[1]
		answer = random_choice[0]

		response = input('Which QSignal means ' + meaning + '? ').lstrip().upper()

		if response == answer:
			print('You got it!')
			correct += 1

		elif response == 'EXIT':
			break

		elif response != answer:
			print('Nope. The correct answer is ' + answer)

		total += 1
		print('')
		
	percent_correct = correct/total*100
	print('You got ' +str(percent_correct)+ '% correct')
	print('Goodbye!')

if __name__ == '__main__':
	main()


