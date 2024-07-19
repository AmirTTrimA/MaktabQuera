def play_shot(balls, pocketed_balls, current_player, ball_color):
    for i, ball in enumerate(balls):
        if ball['color'] == ball_color:
            pocketed_balls.append(ball)
            balls.pop(i)
            current_player = (current_player + 1) % 2
            return pocketed_balls, current_player, True
    return pocketed_balls, current_player, False

def parse_input(input_str):
    shots = input_str.split()
    balls = [
        {'color': "white", 'value': 0},
        *[{'color': "red", 'value': 1} for _ in range(15)],
        {'color': "yellow", 'value': 2},
        {'color': "green", 'value': 3},
        {'color': "brown", 'value': 4},
        {'color': "blue", 'value': 5},
        {'color': "pink", 'value': 6},
        {'color': "black", 'value': 7}
    ]
    pocketed_balls = []
    current_player = 0
    for shot in shots:
        if shot.isdigit():
            shot_index = int(shot)
            if shot_index < 0 or shot_index >= len(balls):
                return None, None, None
            pocketed_balls, current_player, valid = play_shot(balls, pocketed_balls, current_player, "red")
        else:
            ball_color = shot
            pocketed_balls, current_player, valid = play_shot(balls, pocketed_balls, current_player, ball_color)
        if not valid:
            return None, None, None
    return balls, pocketed_balls, current_player

def calculate_score(pocketed_balls):
    player1_score = sum(ball['value'] for i, ball in enumerate(pocketed_balls) if i % 2 == 0)
    player2_score = sum(ball['value'] for i, ball in enumerate(pocketed_balls) if i % 2 == 1)
    return player1_score, player2_score


input_str = "red red red black white red blue green red miss red yellow"
balls, pocketed_balls, current_player = parse_input(input_str)
if balls is None:
    print("Invalid input sequence")

while True:
    player1_score, player2_score = calculate_score(pocketed_balls)
    if player1_score >= 147 or player2_score >= 147:
        if player1_score > player2_score:
            print("Player 1 wins!")
        elif player2_score > player1_score:
            print("Player 2 wins!")
        else:
            print("Tie")

    print(f"Player {current_player + 1}'s turn")
    pocketed_balls, current_player, valid_shot = play_shot(balls, pocketed_balls, current_player, "red")
    if not valid_shot:
        pocketed_balls, current_player, valid_shot = play_shot(balls, pocketed_balls, current_player, "yellow")
        if not valid_shot:
            print("Invalid shot, turn passes to the other player.")


