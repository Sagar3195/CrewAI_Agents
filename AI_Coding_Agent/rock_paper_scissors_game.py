import random
import json

def play_round(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Tie"
    elif (
        (player1_choice == "Rock" and player2_choice == "Scissors") or
        (player1_choice == "Paper" and player2_choice == "Rock") or
        (player1_choice == "Scissors" and player2_choice == "Paper")
    ):
        return "Player 1"
    else:
        return "Player 2"

def simulate_game(num_rounds):
    choices = ["Rock", "Paper", "Scissors"]
    player1_score = 0
    player2_score = 0
    round_results = []

    for i in range(num_rounds):
        player1_choice = random.choice(choices)
        player2_choice = random.choice(choices)
        winner = play_round(player1_choice, player2_choice)

        if winner == "Player 1":
            player1_score += 1
        elif winner == "Player 2":
            player2_score += 1
        
        round_results.append({
            "round": i + 1,
            "player1_choice": player1_choice,
            "player2_choice": player2_choice,
            "winner": winner
        })
    
    overall_winner = "Tie" if player1_score == player2_score else \
                     "Player 1" if player1_score > player2_score else \
                     "Player 2"

    game_outcome = {
        "total_rounds": num_rounds,
        "player1_final_score": player1_score,
        "player2_final_score": player2_score,
        "overall_winner": overall_winner,
        "round_details": round_results
    }
    
    print(json.dumps(game_outcome, indent=4))

if __name__ == "__main__":
    # Simulate for 5 rounds
    simulate_game(5)
