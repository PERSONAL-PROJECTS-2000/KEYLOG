# Keystroke Logger Project
This is a simple, educational Python project designed to demonstrate global keyboard monitoring using the `pynput` library, wrapped in a simple web interface built with **Gradio**.

**Ethical Warning:** This project is for **educational, security auditing, or personal monitoring purposes only**. **DO NOT** deploy this code on any system you do not own or have explicit, legal permission to monitor. Unauthorized keystroke logging is illegal and unethical.

---

## Features
<ul>* **Global Monitoring:** Records keyboard inputs across all applications and windows on the local machine.</ul>
<ul>* **Web Interface:** Uses Gradio for a simple **START/STOP** interface.</ul>
<ul>* **Single String Output:** Stores all recorded inputs (including special keys like `[ENTER]` and `[SPACE]`) and displays the full log as a single text string upon stopping.</ul>

## Prerequisites
Before running the application, ensure you have the following installed on your local machine:-
1. **Python 3.7+** (Ensure Python is added to your system's PATH during installation).
2. **Git** (If you plan to clone the repository).

## Installation and Setup

### 1. Clone the Repository
Clone this project to your local machine:
```bash
git clone [YOUR_REPOSITORY_URL_HERE]
cd [YOUR_PROJECT_FOLDER_NAME]
```
### 2. Install Dependencies
You need the `pynput` library for system monitoring and `gradio` for the web interface.
Open your terminal or command prompt in the project directory and run:
```bash
pip install pynput gradio
```

## Running the Application
Execute the Python script to start the Gradio web server:
```bash
python KeyLog.py
```
* The terminal will display a local URL (e.g., `http://127.0.0.1:7860`).
* Open this URL in your web browser.

### Usage Instructions
1. Click the **START LOGGING** button in the web interface.
2. Switch to any application (browser, text editor, chat client) and begin typing.
3. Switch back to the Gradio interface.
4. Click the **STOP LOGGING** button.
5. The recorded keystrokes will appear in the **Status / Final Output** box as a single string.

## Code Structure
The core logic is contained within `KeyLog.py`.
| Component | Purpose | Details |
| --- | --- | --- |
| `KeyloggerState` Class | **State Management** | Holds the log string, tracks the `logging_active` state, and manages thread safety via a `threading.Lock`. |
| `on_press()` | **Pynput Callback** | Appends the key character to the global `log_string`. Handles special keys by replacing them with readable tokens (e.g., `[SPACE]`, `[ENTER]`). |
| `start_logging()` | **Gradio Function** | Resets the log, sets `logging_active = True`, and starts the `pynput` listener in a separate `threading.Thread` to prevent the web interface from freezing. |
| `stop_logging()` | **Gradio Function** | Sets `logging_active = False`, explicitly stops the `pynput` listener, and returns the final collected `log_string` to the Gradio output box. |

## Contributing
Feel free to open issues or submit pull requests for enhancements, such as:
* Adding timed output logging (e.g., `[2025-12-29 14:45:00]`).
* Implementing logging to a local file in addition to the screen output.

## License
This project is licensed under the MIT License- see the `LICENSE.md` file for details.
