# CapsLock to W

A simple Python script that remaps a double press of the Caps Lock key to type the letter `w`. This script is ideal for cases where the `w` key is malfunctioning, and Caps Lock serves as a convenient replacement.

## Features
- **Cross-platform compatibility**: Works on macOS, Linux, and Windows.
- **Lightweight and intuitive**: Detects double key presses with configurable timing.
- **Startup ready**: Can be configured to run at startup on all supported platforms.

## How It Works
- When the Caps Lock key is pressed twice in quick succession (default: 0.3 seconds), the script simulates typing the `w` character.
- The Caps Lock state (on/off) is unaffected.

## Requirements
- Python 3.x
- `pynput` library: Install with `pip install pynput`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/capslock-to-w.git
   cd capslock-to-w
