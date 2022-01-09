import random
from replit import clear
from art import logo, vs
from game_data import data

# Add art.
print(logo)

# Create a function to generate a random account from the game data.
def random_account(): 
  return random.choice(data)

# Create a function to format account data into printable format.
def format_data(account): 
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

# Check if user is correct.
## Get follower count.
## If Statement
def compare(guess, follower_a, follower_b):
  if follower_a > follower_b: 
    return guess == "a"
  else: 
    return guess == "b"
   
# Make game repeatable. 
def game(): 
  score = 0
  game_continue = True
  account_a = random_account()
  account_b = random_account()

  while game_continue:
    account_a = account_b
    account_b = random_account()

    # Make B become the next A.
    while account_a == account_b: 
      account_b = random_account() 

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Aganist B: {format_data(account_b)}")

    # Ask user for a guess.
    # Check if user is correct.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    follower_a_count = account_a["follower_count"] 
    follower_b_count = account_b["follower_count"]
    is_correct = compare(guess, follower_a_count, follower_b_count)
    
    # Clear screen between rounds.
    clear()
    # Feedback.
    # Score Keeping.
    if is_correct: 
      score += 1
      print(f"You're right! Current score: {score}.") 
    else: 
      game_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

