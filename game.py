import random
import time

# Game Configurations: (Difficulty Name: (Max Range, Max Attempts))
DIFFICULTIES = {
    "1": ("Easy", 50, 10),
    "2": ("Medium", 100, 7),
    "3": ("Hard", 200, 5),
}


def display_welcome():
    """Prints the game header and introductory message."""
    print("=" * 50)
    print("      🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯      ")
    print("=" * 50)
    print("I'm thinking of a number within a range.")
    print("Can you guess it before you run out of attempts?\n")


def select_difficulty():
    """Prompts the player to choose a difficulty setting.

    Returns:
        tuple: (difficulty_name, max_range, max_attempts)
    """
    print("Select Difficulty Level:")
    for key, (name, max_num, attempts) in DIFFICULTIES.items():
        print(f"  [{key}] {name:<7} (Range: 1–{max_num}, Attempts: {attempts})")

    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        if choice in DIFFICULTIES:
            name, max_num, attempts = DIFFICULTIES[choice]
            print(f"\nAwesome! You chose {name} mode.")
            print(f"Guess a number between 1 and {max_num}. You have {attempts} attempts.\n")
            return name, max_num, attempts
        print("❌ Invalid selection. Please enter 1, 2, or 3.")


def get_valid_guess(max_num):
    """Ensures the player's input is an integer within the valid range.

    Returns:
        int: Validated guess integer
    """
    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            if 1 <= guess <= max_num:
                return guess
            print(f"⚠️  Please enter a number within the range 1 to {max_num}.")
        except ValueError:
            print("⚠️  Invalid input! Please enter a whole number.")


def play_round():
    """Executes a single round of the game."""
    _, max_num, max_attempts = select_difficulty()
    secret_number = random.randint(1, max_num)
    attempts_left = max_attempts
    attempts_taken = 0

    while attempts_left > 0:
        guess = get_valid_guess(max_num)
        attempts_taken += 1
        attempts_left -= 1

        if guess == secret_number:
            print("\n" + "🎉" * 20)
            print(f"  BOOM! You got it right in {attempts_taken} attempt(s)!")
            print(f"  The number was indeed {secret_number}.")
            print("🎉" * 20 + "\n")
            return True
        
        # Provide directional feedback
        if guess < secret_number:
            print("  📉 Too LOW!")
        else:
            print("  📈 Too HIGH!")

        # Show remaining attempts
        if attempts_left > 0:
            print(f"  Attempts remaining: {attempts_left}\n")
        else:
            print("\n" + "💀" * 20)
            print(f"  Game Over! You ran out of attempts.")
            print(f"  The secret number was: {secret_number}")
            print("💀" * 20 + "\n")

    return False


def main():
    """Main execution entry point."""
    display_welcome()
    
    score = 0
    rounds_played = 0

    while True:
        rounds_played += 1
        print(f"--- ROUND {rounds_played} ---")
        
        won = play_round()
        if won:
            score += 1

        # Ask to replay
        replay = input("Play again? (y/n): ").strip().lower()
        if replay not in ("y", "yes"):
            print("\n" + "=" * 50)
            print(f" Thanks for playing! Final Score: {score}/{rounds_played} rounds won.")
            print("=" * 50)
            break
        print("\nResetting the game...\n")
        time.sleep(1)


if __name__ == "__main__":
    main()