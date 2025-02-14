# Snake Game with Flask

A classic Snake game implemented using **Flask**, **HTML5**, **CSS**, and **JavaScript**. The game runs on your web browser and provides a simple, interactive snake game where you control the snake to eat food, grow in length, and avoid collisions with walls or the snake's own body.

## Features

- **Responsive game interface** on desktop browsers.
- Real-time **game updates** through JavaScript and Flask API calls.
- Dynamic **speed increase** as the snake eats more food.
- **Game Over** screen with the option to restart.
- **Controls** using the arrow keys and an option to restart by pressing `R`.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Canvas API)
- **Game logic**: Flask API routes to control game state and directions, JavaScript for game loop and rendering.

## Installation

### Prerequisites

- Python 3.x
- Flask (installed via pip)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/BlackCoder21/Snake_Game_Web.git
    cd snake-game-flask
    ```

2. **Install required packages**:

    If you don't have Flask installed, run the following command in your terminal:

    ```bash
    pip install Flask
    ```

3. **Run the Flask Application**:

    In the terminal, run the following command to start the Flask server:

    ```bash
    python app.py
    ```

4. **Access the Game**:

    Open your web browser and navigate to:

    ```
    http://127.0.0.1:5000/
    ```

    The game will load, and you can start playing the Snake game.

## How to Play

- **Arrow Keys**: Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to control the movement of the snake.
- **Restart the Game**: If you lose, press `R` to restart the game.

## File Structure

```
Snake_Game_Web/
├── app.py              # Flask backend (API routes for the game logic)
├── static/
│   ├── style.css       # Game styles (CSS)
│   └── script.js       # Game logic (JavaScript)
└── templates/
    └── index.html      # Main game page (HTML)
```

- **app.py**: Contains the Flask application and game state logic, including routes to move the snake, update the game state, and handle user input.
- **static/style.css**: Styles the game page and gives the Snake game a visually appealing look.
- **static/script.js**: Handles the game logic on the frontend, including updating the game state, drawing the snake and food, and detecting collisions.
- **templates/index.html**: The main HTML file that renders the game page in the browser.

## Game Controls

- **Arrow Keys**: Control the snake's movement direction.
- **R**: Restart the game after a Game Over.
