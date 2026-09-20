# 🏓 pygamePing-Pong

A simple two-player **Ping Pong game built with Python and Pygame**.

This project was built to explore the fundamentals of 2D game development — including real-time input handling, object movement, collision detection, scoring, and the Pygame game loop.

## 🎮 Gameplay

Two players compete using paddles on opposite sides of the screen.

* **Player 1:** `W` / `S`
* **Player 2:** `↑` / `↓`
* The ball bounces off the top and bottom boundaries.
* Players score when the opponent misses the ball.
* The first player to reach **5 points** wins.

## ✨ Features

* Real-time two-player gameplay
* Keyboard-controlled paddles
* Ball movement and wall collisions
* Paddle collision detection
* Score tracking
* Win condition
* Randomized initial ball direction
* Simple, lightweight Pygame implementation

## 🛠️ Tech Stack

* **Python**
* **Pygame**

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AadhilPaul/pygamePing-Pong.git
cd pygamePing-Pong
```

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Run the game

```bash
python main.py
```

## 🕹️ Controls

| Player   | Move Up | Move Down |
| -------- | ------- | --------- |
| Player 1 | `W`     | `S`       |
| Player 2 | `↑`     | `↓`       |

Press `SPACE` to start the ball after a point is scored.

## 🧠 What I Learned

This project helped me understand some of the core concepts behind real-time game development:

* Working with the **Pygame game loop**
* Handling keyboard and window events
* Moving objects using velocity
* Detecting collisions using rectangles
* Managing game state such as scores and ball movement
* Keeping game objects within the screen boundaries
* Structuring game logic into reusable functions

## 📁 Project Structure

```text
pygamePing-Pong/
└── main.py
```

The project intentionally keeps the implementation small and focused, making the core game mechanics easy to follow.

## 🔮 Possible Improvements

Some features that could be added in future versions:

* [ ] Start menu
* [ ] Game-over screen
* [ ] Restart functionality
* [ ] Sound effects
* [ ] Increasing ball speed
* [ ] Single-player mode with AI
* [ ] Improved visual design
* [ ] Configurable winning score

## 📌 Project Status

**Completed — basic playable version**

This project is primarily a learning project focused on understanding the fundamentals of game programming with Python and Pygame.

## 👤 Author

**Aadhil Paul**

[GitHub](https://github.com/AadhilPaul)
