players = []

def add_player(player_name):
    players.append(player_name)
    print(f"Player {player_name} has joined the lobby")

def add_card():
    for _ in range(5):
        player_name = input("Enter player name (or 'done' to start the game): ")
        if player_name.lower() == 'done':
            break
        add_player(player_name)

    if len(players) < 2:
        print("You need at least 2 players to start the game.")
        return False

    cards_each = 12 - len(players)
    print(f"All players drew {cards_each} cards")
    return True

def main():
    add_card()

if __name__ == "__main__":
    main()
