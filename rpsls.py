import random
import time


speed = 0.2

# Function to print sentences with time.sleep


def print_sentences(sents):
    sents = sents.split('\n')
    for el in sents:
        print(el)
        time.sleep(speed)

# Function to record the users move


def users_move():
    rock = "rock\U0001F5FB"
    paper = "paper\U0001F4C3"
    scissors = "scissors\U00002702"
    lizard = "lizard\U0001F98E"
    spock = "spock\U0001F596"
    sent = f"{rock} / {paper} / {scissors} / {lizard} / {spock}: "
    while True:
        try:
            user_input = input(sent).lower()
            if user_input in ('rock', 'paper', 'scissors', 'lizard', 'spock'):
                break
            else:
                print("Invalid: rock-paper-scissors-lizard-spock")
        except ValueError:
            print("Invalid: rock-paper-scissors-lizard-spock")
    return user_input

# Funtion for validating user 1/2 input


def user_1_2():
    while True:
        try:
            user_input = int(input("Pick Game Mode: "))
            if user_input in (1, 2):
                break  # Exit the loop if the input is 1 or 2
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1 or 2).")
    return user_input

# Function to ask user choice of number


def game_no(x):
    y = "Invalid input. Please enter a valid number"
    while True:
        try:
            user_input = int(input(f"{x}"))
            if isinstance(user_input, int):
                break  # Exit the loop if the input is 1 or 2
            else:
                print(f"{y}")
        except ValueError:
            print(f"{y}")
    return user_input

# Super class player


class Player:

    moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def move(self):
        pass

# Class for Human player


class Human(Player):
    def move(self):
        user_play = users_move()
        return user_play

    def learn(self, my_move, their_move):
        pass

# Class for Player who cycles through moves


class Cycle(Player):
    def __init__(self):
        super().__init__()
        self.learned_move = None

    def move(self):
        if self.learned_move is None:
            # Return a random move for the first round
            return Player.moves[0]
        else:
            return Player.moves[Player.moves.index(self.learned_move)+1]

    def learn(self, my_move, their_move):
        self.learned_move = my_move

# Class for Player who plays random moves


class Random(Player):
    def move(self):
        return random.choice(Player.moves)

    def learn(self, my_move, their_move):
        pass

# Class for Player who repeats rock


class Repeat(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# Class for player who reflects on opponents move


class Reflect(Player):
    def __init__(self):
        super().__init__()
        self.learned_move = None

    def move(self):
        if self.learned_move is None:
            # Return a random move for the first round
            random_move = random.choice(Player.moves)
            return random_move
        else:
            # Use the learned move in subsequent rounds
            return self.learned_move

    def learn(self, my_move, their_move):
        # Store the opponent's move as the learned move
        self.learned_move = their_move

# Class for Game rounds and total games


class Game:
    def __init__(self, p1, p2, rounds=3):
        self.player1 = p1
        self.player2 = p2
        self.rounds = rounds
        self.curr_round = 1
        self.scores = {self.player1: 0, self.player2: 0}

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()

        x = self.player1
        y = self.player2
        z = self.scores

        if Game.beats(move1, move2):
            self.scores[x] += 1
            print(f'\033[93mRound: {self.curr_round}\033[m')
            time.sleep(speed)
            print(f'{x.__class__.__name__}- {move1}: {z[x]}')
            time.sleep(speed)
            print(f'{y.__class__.__name__}- {move2}: {z[y]}')
            time.sleep(speed)
            print(f'\033[1m{x.__class__.__name__} wins this round!\033[m')

        elif Game.beats(move2, move1):
            self.scores[y] += 1
            print(f'\033[93mRound: {self.curr_round}\033[m')
            time.sleep(speed)
            print(f'{x.__class__.__name__}- {move1}: {z[x]}')
            time.sleep(speed)
            print(f'{y.__class__.__name__}- {move2}: {z[y]}')
            time.sleep(speed)
            print(f'\033[1m{y.__class__.__name__} wins this round!\033[m')
        else:
            print(f'\033[93mRound: {self.curr_round}\033[m')
            time.sleep(speed)
            print(f'{x.__class__.__name__}- {move1}: {z[x]}')
            time.sleep(speed)
            print(f'{y.__class__.__name__}- {move2}: {z[y]}')
            time.sleep(speed)
            print('\033[1mIt\'s a tie!\033[m')

        self.curr_round += 1

        if self.curr_round > self.rounds:
            self.curr_round = 1  # Reset back to 1

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def play_game(self):

        self.scores[self.player1] = 0
        self.scores[self.player2] = 0

        time.sleep(speed)
        for _ in range(self.rounds):
            self.play_round()
        print('\n\033[93mRound Scores!\033[m')
        x = self.player1
        y = self.player2
        print(f'{x.__class__.__name__} score: {self.scores[x]}')
        print(f'{y.__class__.__name__} score: {self.scores[y]}')
        return self.scores[self.player1], self.scores[self.player2]

    def beats(move1, move2):
        # Define the winning moves
        winning_moves = {
            'rock': ['scissors', 'lizard'],
            'scissors': ['paper', 'lizard'],
            'paper': ['rock', 'spock'],
            'lizard': ['spock', 'paper'],
            'spock': ['scissors', 'rock']
        }
        return move2 in winning_moves.get(move1, [])

    def start_rps(self):

        time.sleep(speed)
        arg = "How many Total Games do you want to play?: "
        total = game_no(arg)
        i = 1
        pls1 = 0
        pls2 = 0

        while i <= total:

            sent = f'\nScore\nPlayer1 : {pls1} Player2 : {pls2}\n'
            print_sentences(f"\n\033[93m{sent}\033[m")

            print(f'\033[93mGame {i}!\033[m\n')
            pl1, pl2 = Game.play_game(self)

            if pl1 > pl2:
                pls1 += 1
            elif pl1 < pl2:
                pls2 += 1
            elif pl1 == pl2:
                pass
            i += 1

        time.sleep(speed)
        print(f"\n\033[93mGame Over!\033[m\n")
        print(f"\033[93mPlayer1 : {pls1} || Player2 : {pls2}\033[m")

        x = f"\033[1;97;42mPlayer1 Wins {pls1} out of {total} game(s) \033[m"
        y = f"\033[1;97;41mPlayer2 Wins {pls2} out of {total} game(s) \033[m"

        if pls1 > pls2:
            print(x)
        elif pls1 < pls2:
            print(y)
        elif pls1 == pls2:
            print("\033[1;90;100mThe Game is a Draw\033[m")

# Play game, choose mode and no of rounds


def play_rps_game():

    # Define your player instances
    human_player = Human()
    random_player = Random()
    repeat_player = Repeat()
    reflect_player = Reflect()
    cycle_player = Cycle()
    computer_opp = [random_player, repeat_player, reflect_player, cycle_player]
    co_op_1 = random.choice(range(0, 4))
    while True:
        co_op_2 = random.choice(range(0, 4))
        if co_op_2 != co_op_1:
            break

    time.sleep(speed)
    print('\n\033[93mStarting Game...\033[m\n')

    time.sleep(speed)
    print("\033[1;97;43m~~~~ Welcome to the RPS game ~~~~\033[m\n")

    # Ask if Game mode is Vs another Human or Computer
    mode1 = "Human vs Computer - Press 1"
    mode2 = "Computer vs Computer - Press 2"
    sent = f"What game mode do you want to play?\n{mode1}\n{mode2}"
    print_sentences(f"\n\033[93m{sent}\033[m")
    opponent_choice = user_1_2()

    # Ask Human for Best out of how many games
    time.sleep(speed)
    arg = "How many Rounds per game would you like to play: "
    best_of = game_no(arg)

    if opponent_choice == 1:
        game = Game(human_player, computer_opp[co_op_1], best_of)
    elif opponent_choice == 2:
        game = Game(computer_opp[co_op_1], computer_opp[co_op_2], best_of)

    game.start_rps()


play_rps_game()
