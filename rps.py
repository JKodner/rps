import random
choices = ["rock", "paper", "scissors"]
user_choice = " "
com_choice = random.choice(choices)
def statement(x,y):
	if x != y:
	    print " "
	    print "-*-"
	    print "You put down: %s" % user_choice.upper()
	    print "The Computer put down: %s" % com_choice.upper()
	    print "%s beats %s." % (x.upper(), y.upper())
	    print "-*-"
	    print " "
	elif x == y:
	    print " "
	    print "-*-"
	    print "You put down: %s" % user_choice.upper()
	    print "The Computer put down: %s" % com_choice.upper()
	    print "%s ties with %s." % (x.upper(), y.upper())
	    print "You Tie!"
	    print "-*-"
	    print " "
print " "
while user_choice.lower() not in choices:
	user_choice = raw_input("Rock, Paper, or Scissors?")
if user_choice.lower() == "rock":
	if com_choice == "paper":
	    statement("paper", "rock")
	    print "You Lose!"
	elif com_choice == "scissors":
	    statement("rock", "scissors")
	    print "You Win!"
	elif com_choice.lower() == user_choice.lower():
	    statement("rock", "rock")
elif user_choice.lower() == "paper":
	if com_choice == "rock":
	    statement("paper", "rock")
	    print "You Win!"
	elif com_choice == "scissors":
	    statement("scissors", "paper")
	    print "You Lose!"
	elif com_choice.lower() == user_choice.lower():
	    statement("paper", "paper")
elif user_choice.lower() == "scissors":
	if com_choice == "rock":
	    statement("rock", "scissors")
	    print "You Lose!"
	elif com_choice == "paper":
	    statement("scissors", "paper")
	    print "You Win!"
	elif com_choice.lower() == user_choice.lower():
	    statement("scissors", "scissors")