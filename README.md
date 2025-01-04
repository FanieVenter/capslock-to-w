

---


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
   ```

2. Install dependencies:
   ```bash
   pip install pynput
   ```

3. Run the script:
   ```bash
   python capslock_to_w.py
   ```

## Configure to Run at Startup

### macOS
1. **Save the Script**:
   Ensure your script is saved at a convenient location (e.g., `~/scripts/capslock_to_w.py`).

2. **Create a `.plist` File**:
   Create a new `.plist` file in `~/Library/LaunchAgents`:
   ```bash
   nano ~/Library/LaunchAgents/com.capslocktow.w.plist
   ```

3. **Add the Following Content**:
   Replace the script path accordingly:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
     <dict>
       <key>Label</key>
       <string>com.capslocktow.w</string>
       <key>ProgramArguments</key>
       <array>
         <string>/usr/local/bin/python3</string>
         <string>/Users/yourusername/scripts/capslock_to_w.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
     </dict>
   </plist>
   ```

4. **Load the `.plist` File**:
   To ensure the script runs at startup:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.capslocktow.w.plist
   ```

5. **Verify**:
   The script will now automatically run after a reboot.

### Linux
1. **Make the Script Executable**:
   Make sure your script is executable:
   ```bash
   chmod +x /path/to/capslock_to_w.py
   ```

2. **Create a `.desktop` File**:
   Create a new `.desktop` file in `~/.config/autostart/`:
   ```bash
   nano ~/.config/autostart/capslock_to_w.desktop
   ```

3. **Add the Following Content**:
   Replace the path to your script:
   ```ini
   [Desktop Entry]
   Type=Application
   Exec=python3 /path/to/capslock_to_w.py
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name=CapsLock to W
   ```

4. **Save and Close**:
   After a restart, the script will run at startup.

### Windows
1. **Locate `pythonw.exe`**:
   Python scripts should be run using `pythonw.exe` to avoid opening a terminal window. It's typically located at `C:\Python39\pythonw.exe` (adjust based on your installation).

2. **Create a Shortcut in the Startup Folder**:
   - Open the `Run` dialog (`Win + R`) and type `shell:startup`, then press Enter to open the Startup folder.
   - Right-click inside the folder and select `New` > `Shortcut`.
   - Enter the following as the location (adjust the path):
     ```
     "C:\Python39\pythonw.exe" "C:\path\to\capslock_to_w.py"
     ```

3. **Name the Shortcut**:
   Name the shortcut (e.g., "CapsLock to W").

4. **Test**:
   Restart your computer, and the script should launch automatically.

## Configuration
You can modify the following settings in `capslock_to_w.py`:
- **Double Press Interval**: Adjust the timing for detecting a double press (default: 0.3 seconds).

## Exit the Script
To stop the script, press the `Esc` key.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution
Contributions are welcome! If you encounter a bug or have a feature request, feel free to open an issue or submit a pull request.

## Acknowledgments
Thanks to the [pynput](https://pypi.org/project/pynput/) library for simplifying cross-platform keyboard input handling.
```

