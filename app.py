from flask import Flask, render_template, jsonify, request
from random import randint

app = Flask(__name__)

# Game state (could be stored in a more persistent way if needed)
game_state = {
    "snake": [{"x": 100, "y": 100}],
    "direction": {"x": 20, "y": 0},
    "food": {"x": 200, "y": 200},
    "game_over": False,
    "score": 0,
    "speed": 100,  # milliseconds between game updates (adjust for difficulty)
}

# Initialize the game state
def restart_game():
    game_state["snake"] = [{"x": 100, "y": 100}]
    game_state["direction"] = {"x": 20, "y": 0}
    game_state["food"] = generate_food()
    game_state["game_over"] = False
    game_state["score"] = 0
    game_state["speed"] = 100  # Reset to normal speed

# Generate new food at random location
def generate_food():
    return {
        "x": (randint(0, 19) * 20),
        "y": (randint(0, 19) * 20),
    }

# Main route to serve the game page
@app.route('/')
def index():
    return render_template('index.html')

# API to get current game state (snake, food, score, etc.)
@app.route('/game_state', methods=['GET'])
def get_game_state():
    return jsonify(game_state)

# API to update game direction (when arrow keys are pressed)
@app.route('/update_direction', methods=['POST'])
def update_direction():
    if game_state["game_over"]:
        return jsonify({"message": "Game Over! Restart to play again."}), 400

    direction = request.json.get("direction")
    if direction:
        if direction == "Right" and game_state["direction"]["x"] == 0:
            game_state["direction"] = {"x": 20, "y": 0}
        elif direction == "Left" and game_state["direction"]["x"] == 0:
            game_state["direction"] = {"x": -20, "y": 0}
        elif direction == "Up" and game_state["direction"]["y"] == 0:
            game_state["direction"] = {"x": 0, "y": -20}
        elif direction == "Down" and game_state["direction"]["y"] == 0:
            game_state["direction"] = {"x": 0, "y": 20}

    return jsonify({"message": "Direction updated successfully."})

# API to update the game state and check for collisions
@app.route('/move', methods=['GET'])
def move():
    if game_state["game_over"]:
        return jsonify({"message": "Game Over! Restart to play again."}), 400

    snake_head = game_state["snake"][-1]
    new_head = {"x": snake_head["x"] + game_state["direction"]["x"], "y": snake_head["y"] + game_state["direction"]["y"]}

    # Check collision with walls
    if new_head["x"] < 0 or new_head["x"] >= 400 or new_head["y"] < 0 or new_head["y"] >= 400:
        game_state["game_over"] = True
        return jsonify({"message": "Game Over! Snake hit the wall."})

    # Check collision with self (snake body)
    if new_head in game_state["snake"]:
        game_state["game_over"] = True
        return jsonify({"message": "Game Over! Snake collided with itself."})

    game_state["snake"].append(new_head)

    # Check if snake eats food
    if new_head == game_state["food"]:
        game_state["score"] += 1
        game_state["food"] = generate_food()
        # Increase speed slightly as the snake eats food (game difficulty)
        if game_state["speed"] > 50:
            game_state["speed"] -= 5
    else:
        game_state["snake"].pop(0)  # Remove tail

    return jsonify(game_state)

# API to restart the game
@app.route('/restart', methods=['POST'])
def restart():
    restart_game()
    return jsonify({"message": "Game restarted!"})

if __name__ == '__main__':
    app.run(debug=True)
