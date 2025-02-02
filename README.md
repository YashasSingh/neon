# Rock-Paper-Scissors Cellular Automaton on RGB Matrix

## Overview
This project implements a cellular automaton based on the game of Rock-Paper-Scissors (RPS) using an RGB LED matrix. The simulation evolves over time, with colors representing different states that interact according to predefined rules.

## Features
- Runs on a 64x32 RGB matrix display
- Uses Rock-Paper-Scissors rules for cell evolution
- Randomized initial conditions
- Dynamic color changes over time

## Hardware Requirements
- Adafruit RGB Matrix Panel (64x32)
- A compatible microcontroller (e.g., Raspberry Pi with CircuitPython support)
- Necessary wiring and power supply

## Software Requirements
- CircuitPython
- `board`, `displayio`, `framebufferio`, and `rgbmatrix` libraries

## Installation
1. Install CircuitPython on your microcontroller.
2. Install the necessary libraries from the Adafruit CircuitPython bundle.
3. Copy the script to your device and run it.

## How It Works
1. **Initialization**: A 64x32 display is set up using `rgbmatrix` and `framebufferio`.
2. **Randomization**: The grid is randomly initialized with three different states representing Rock, Paper, and Scissors.
3. **Update Rule**: Each cell interacts with its neighbors based on Rock-Paper-Scissors rules:
   - Rock (Red) beats Scissors (Blue)
   - Scissors (Blue) beats Paper (Green)
   - Paper (Green) beats Rock (Red)
4. **Display Update**: The display refreshes at regular intervals, showing evolving patterns.
5. **Color Variations**: Occasionally, colors are randomized to add variation.

## Usage
- Power on the device and observe the evolving patterns.
- The simulation runs indefinitely, cycling through different configurations.

## Customization
- Modify the `SCALE` variable to adjust resolution.
- Change the color palette by modifying `palette[]` values.
- Adjust the probability of color change by modifying `random.random() < 0.02`.

## License
This project is open-source and can be freely modified and distributed.

