#!/usr/bin/env python3

import sys

dad_wager = sys.argv[1]
ben_wager = sys.argv[2]
result = sys.argv[3]


print('Dad\'s wager: ' + dad_wager)
print('Ben\'s wager: ' + ben_wager)
print('The winner was: ' + result)

pot = int(dad_wager) + int(ben_wager)
dad = 0
ben = 0

new_dad = -int(dad_wager)
new_ben = -int(ben_wager)

with open("scores_and_wagers.txt", "r") as file:
	dad = int(file.readline())
	ben = int(file.readline())


if result == 'Dad':
	new_dad += int(dad) + int(pot)
	new_ben += int(ben)
else:
	new_ben += int(ben) + int(pot)
	new_dad += int(dad)

prev_out = sys.stdout

open('scores_and_wagers.txt', 'w').close()
with open('scores_and_wagers.txt', 'w') as f:
	sys.stdout = f # Change the standard output to the file we created.
	print(new_dad)
	print(new_ben)
	sys.stdout = prev_out

print('Dad had: ' + str(dad))
print('Ben had: ' + str(ben))
print('Pot was: ' + str(pot))

print('~~~~~~~~~~~~~~~~~\n')
print('Dad now has: ' + str(new_dad))
print('Ben now has: ' + str(new_ben))

