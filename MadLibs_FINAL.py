"""
Author: Ryan Nevares
Date: 17 October 2017
Title: Mad Libs
Version 2.0

This is a little Mad Libs game that I made.  It is rewritten from my original one that I made as my first Python project.  This version not only supports more stories (TO BE ADDED LATER) and fewer bugs, but also has more features and lets just say it's a lot less like a "first python project" than the original.  :)
ENJOY!

Report any bugs to ryannevares@gmail.com
"""
from time import sleep
from sys import stdout
from textwrap import fill # This will make screen layout better later

# I want this program to 'slow type' its messages rather than just dumping them all on the screen at once.  Before doing anything else, define this function
def print_slow(string):
    for letter in fill(string): # Fill lets us wrap the text.  I chose to use the default value of 80 characters
        stdout.write(letter)
        stdout.flush()
        sleep(.03)
    print ""

# Print initial message to user when the program starts
intro = "Remember, everything in this game including places, characters, weapons, and everything else can be real or fictional"
print ""
print_slow("WELCOME TO MAD LIBS!")
print ""
sleep(.4)
print_slow("This game will ask for a series of inputs from you, then from your inputs assemble a hillarious story!")
print ""
sleep(.4)
print_slow("Remember, everything in this game including places, characters, weapons, and everything else can be real or fictional")
print ""
sleep (1)

# ask player if they want to go again
def again():
    playagain = raw_input("Play again? (y/n): ")
    if playagain == "y" or playagain == "Y":
        print_slow("Alright!  Let's go!")
        print ""
        sleep(1.5)
        plumbus()
    elif playagain == "n" or playagain == "N":
        print ""
        print_slow("Sorry to see you go.")
        sleep(.4)
        print "\n\n"
        print_slow("Exiting now.....")
        print "\n\n\n\n"
        exit()
    else:
        print "Please choose y or n: \n"
        sleep (1)
        return again()
# create a function for each storyline
def plumbus(): # Script based on Plumbus scene from Rick and Morty
    # get user inputs
    plumbus = raw_input("Enter a noun: ")
    home = raw_input("Enter a noun: ")
    dinglebop = raw_input("Enter another noun: ")
    smooth = raw_input("Enter a verb: ")
    schleem = raw_input("Enter a noun: ")
    push = raw_input("Enter a verb: ")
    grumbo = raw_input("Enter a noun: ")
    fleeb = raw_input("Enter another noun: ")
    rub = raw_input("Enter a verb ending in -d: ")
    schlami = raw_input("Enter an animal/creature: ")
    rub2 = raw_input("Enter a verb ending with -s: ")
    spit = raw_input("Enter a verb ending with -s: ")
    hizzard = raw_input("Enter a plural noun: ")
    blamf = raw_input("Enter a plural amimal or creature: ")
    chumble = raw_input("Enter a plural noun: ")
    plubis = raw_input("Enter a noun: ")
    adj1 = raw_input("Enter an adjective ending with -ly: ")
    adj2 = raw_input("Enter an adjective: ")
    adj3 = raw_input ("Enter another adjective: ")




    # Tell the story
    story = "Next on How They Do It: %s!  Everyone has a %s in their %s, but how do they make them?  Lets find out!  First they take the %s and they %s it with a bunch of %s.  The %s is then repurposed for later batches.  Next, they take the %s and %s it through the %s, where the %s is %s against it.  It's important that the %s is %s, because it has all of the %s juice.  Then, a %s shows up and %s it and then %s on it.  Then they cut the %s.  There are several %s in the way.  Finally, the %s rub against the %s as the %s and %s are %s shaved away, leaving you with a %s, %s, %s!" % (plumbus, plumbus, home, dinglebop, smooth,schleem, schleem, dinglebop, push, grumbo, fleeb, rub, fleeb, rub, fleeb, schlami, rub2, spit, fleeb, hizzard, blamf, chumble, plubis, grumbo, adj1, adj2, adj3, plumbus)
    sleep(2)
    print "\n\n"
    # slow print the story to the console
    print_slow(story)

# create a flag variable to determine if the program should keep Running
def main():
    while(True):
        print_slow("Alright, lets go!\n")
        sleep(1)
        print ""
        plumbus()
        sleep(2)
        print ""
        again()

main()
""" FUTURE SUGGESTIONS:  Make text wrapping work with ANY SIZE WINDOW.
Add more stories

"""
