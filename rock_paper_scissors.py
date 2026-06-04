import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    winning_rules = {
        'rock': 'scissors',   
        'paper': 'rock',       
        'scissors': 'paper'   
    }    
    if winning_rules[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'
def start_game():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("--------------------------------------------------")   
    user_score = 0
    computer_score = 0   
    while True:
        user_choice = input("\nEnter choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
        
        if user_choice == 'quit':
            print("\nThanks for playing!")
            break           
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please type rock, paper, or scissors.")
            continue            
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")
        result = determine_winner(user_choice, computer_choice)        
        if result == 'tie':
            print("It's a Tie!")
        elif result == 'user':
            print("You Win this round!")
            user_score += 1
        else:
            print("Computer Wins this round!")
            computer_score += 1
        print(f"Score - YOU: {user_score} | COMPUTER: {computer_score}")
        print("-" * 35)
    print("\n--- FINAL SCORE SUMMARY ---")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the match!")
    elif user_score < computer_score:
        print("Better luck next time! Computer won the match.")
    else:
        print("Overall Match is a Tie!")
if __name__ == "__main__":
    start_game()