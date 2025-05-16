# Asteroids Clone

A clone of the classic Asteroids game, built using Pygame and object-oriented programming concepts. Created as part of the Boot.Dev curriculum.

## Features

- Classic arcade gameplay: control a spaceship, shoot asteroids, and survive as long as you can.
- Object-oriented design for maintainable and extendable code.
- Score tracking and game-over logic.

## Getting Started

### Prerequisites

- Python 3.x
- [Pygame](https://www.pygame.org/) library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vmarin93/asteroids_clone.git
   cd asteroids_clone
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python3 main.py
   ```

## How to Play

- Use the keyboard to control your spaceship (w,a,s,d).
- Shoot asteroids and avoid collisions (SPACE for firing shots).
- Your score increases as you destroy asteroids.
- The game ends if your ship collides with an asteroid.

## Project Structure

- `main.py`: Entry point and game loop.
- `player.py`: Handles the player's spaceship.
- `asteroid.py`, `asteroidfield.py`: Asteroid behavior and management.
- `shot.py`: Shots fired by the player.
- `score.py`: Score tracking and display.
- `constants.py`: Game settings and constants.
---
