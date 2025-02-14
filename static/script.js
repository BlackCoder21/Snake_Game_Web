const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const gridSize = 20;
const canvasSize = 400;
const gridCount = canvasSize / gridSize;

let snake = [{x: 100, y: 100}];
let direction = {x: gridSize, y: 0};
let food = generateFood();
let gameOver = false;
let score = 0;
let speed = 100;

function generateFood() {
    return {
        x: Math.floor(Math.random() * gridCount) * gridSize,
        y: Math.floor(Math.random() * gridCount) * gridSize
    };
}

function updateDirection(e) {
    if (gameOver) return;
    if (e.key === "ArrowRight" && direction.x === 0) {
        direction = {x: gridSize, y: 0};
    } else if (e.key === "ArrowLeft" && direction.x === 0) {
        direction = {x: -gridSize, y: 0};
    } else if (e.key === "ArrowUp" && direction.y === 0) {
        direction = {x: 0, y: -gridSize};
    } else if (e.key === "ArrowDown" && direction.y === 0) {
        direction = {x: 0, y: gridSize};
    } else if (e.key === "r" || e.key === "R") {
        restartGame();
    }
}

function drawSnake() {
    snake.forEach((segment) => {
        ctx.fillStyle = "black";
        ctx.fillRect(segment.x, segment.y, gridSize, gridSize);
    });
}

function drawFood() {
    ctx.fillStyle = "green";
    ctx.fillRect(food.x, food.y, gridSize, gridSize);
}

function moveSnake() {
    const newHead = {x: snake[snake.length - 1].x + direction.x, y: snake[snake.length - 1].y + direction.y};

    // Check for wall collisions
    if (newHead.x < 0 || newHead.x >= canvasSize || newHead.y < 0 || newHead.y >= canvasSize) {
        gameOver = true;
        document.getElementById("gameOverMessage").style.display = "block";
        document.getElementById("score").textContent = score;
        return;
    }

    // Check for self-collision
    if (snake.some(segment => segment.x === newHead.x && segment.y === newHead.y)) {
        gameOver = true;
        document.getElementById("gameOverMessage").style.display = "block";
        document.getElementById("score").textContent = score;
        return;
    }

    snake.push(newHead);

    // Check if snake eats food
    if (newHead.x === food.x && newHead.y === food.y) {
        score += 1;
        food = generateFood();
        if (speed > 50) speed -= 5; // Increase game speed slightly as snake eats food
    } else {
        snake.shift(); // Remove tail segment
    }
}

function gameLoop() {
    if (gameOver) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    moveSnake();
    drawSnake();
    drawFood();

    setTimeout(gameLoop, speed); // Control game speed
}

function restartGame() {
    snake = [{x: 100, y: 100}];
    direction = {x: gridSize, y: 0};
    food = generateFood();
    gameOver = false;
    score = 0;
    speed = 100; // Reset speed
    document.getElementById("gameOverMessage").style.display = "none";
    gameLoop();
}

window.addEventListener("keydown", updateDirection);
gameLoop(); // Start the game loop
