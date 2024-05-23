#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from logo import art
print(art)

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100. ")
mode=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if mode=="easy":
  attempts=10
elif mode=="hard":
  attempts=5
print(f"You have {attempts} attempts remaining to guess the number.")

import random
number=random.randint(1,100)
print(number)

def guess():
  global attempts
  global number
  while attempts>0:
    guess=int(input("Make a guess: "))
    if guess==number:
      print(f"You got it! The answer was {number}.")
      return
      attempts=0
    elif guess>number:
      print("Too high.")
      attempts-=1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess<number:
      print("Too low.")
      attempts-=1
      print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts==0:
      print("You've run out of guess, you lose. ")

guess()
  
