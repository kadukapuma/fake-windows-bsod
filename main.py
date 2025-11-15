import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import keyboard
import sys
import os
import time
import threading

# CONFIG 
DELAY_SECONDS = 10  # show after 10 seconds

# CLOSE HOTKEY FUNCTION 
def global_exit():
    os._exit(0)   

keyboard.add_hotkey("ctrl+alt+insert", global_exit)

# Block the Delete key globally
try:
    keyboard.block_key('delete')
except Exception:
    pass


#Configuration for BSoD display 
BG_COLOR = "#0078D4"  # Official Windows Blue Screen color
TEXT_COLOR = "white"
START_PERCENT = 1
MAX_PERCENT = 100
UPDATE_DELAY_MS = 4000  # Delay 


class BSoD_App:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        
        # Fullscreen Window 
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.configure(bg=BG_COLOR, cursor='none')

        # Block Alt+F4
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # disables window close
        self.root.bind_all('<Alt-F4>', lambda e: 'break')      # disables Alt+F4 event
        
        # Variables
        self.current_percent = START_PERCENT
        self.qr_photo_image = None  # To hold the QR code image

        # Fonts
        self.font_sad = ("Segoe UI", 120)
        self.font_main = ("Segoe UI", 24)
        self.font_progress = ("Segoe UI", 18)
        self.font_info = ("Segoe UI", 11)

        # Main Frame
        main_frame = tk.Frame(root, bg=BG_COLOR)
        main_frame.pack(fill="both", expand=True, padx=150, pady=80)

        # Sad Face 
        sad_label = tk.Label(
            main_frame,
            text=":(",
            font=self.font_sad,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        sad_label.pack(anchor="w")

        # Main Message 
        message_text = (
            "Your PC ran into a problem and needs to restart. We're\n"
            "just collecting some error info, and then we'll restart for\n"
            "you."
        )
        main_message_label = tk.Label(
            main_frame,
            text=message_text,
            font=self.font_main,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            justify="left"
        )
        main_message_label.pack(anchor="w", pady=(30, 0))

        # Progress Label
        self.progress_label = tk.Label(
            main_frame,
            text=f"{self.current_percent}% complete",
            font=self.font_progress,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        self.progress_label.pack(anchor="w", pady=(20, 0))
        
        # QR Code and Info Frame
        info_frame = tk.Frame(main_frame, bg=BG_COLOR)
        info_frame.pack(anchor="w", pady=(40, 0))

        # QR Code
        self.qr_label = tk.Label(info_frame, bg=BG_COLOR)
        self.qr_label.pack(side="left", anchor="nw")
        self.generate_and_display_qr()

        # Info Text
        text_info_frame = tk.Frame(info_frame, bg=BG_COLOR)
        text_info_frame.pack(side="left", anchor="nw", padx=20)
        
        info_text_1 = "For more information about this issue and possible fixes, visit\nhttps://www.windows.com/stopcode"
        info_label_1 = tk.Label(
            text_info_frame,
            text=info_text_1,
            font=self.font_info,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            justify="left"
        )
        info_label_1.pack(anchor="w")
        
        info_text_2 = "If you call a support person, give them this info:"
        info_label_2 = tk.Label(
            text_info_frame,
            text=info_text_2,
            font=self.font_info,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            justify="left"
        )
        info_label_2.pack(anchor="w", pady=(15, 0))

        info_text_3 = "Stop code: CRITICAL_PROCESS_DIED"
        info_label_3 = tk.Label(
            text_info_frame,
            text=info_text_3,
            font=self.font_info,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            justify="left"
        )
        info_label_3.pack(anchor="w")

        
        self.root.bind_all('<Delete>', lambda e: 'break')

       

        # the progress update loop
        self.update_progress()

    def generate_and_display_qr(self):
        qr_url = "https://www.windows.com/stopcode"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_photo_image = ImageTk.PhotoImage(img)
        self.qr_label.config(image=self.qr_photo_image)

    def update_progress(self):
        if self.current_percent < MAX_PERCENT:
            self.current_percent += 1
        self.progress_label.config(text=f"{self.current_percent}% complete")
        self.root.after(UPDATE_DELAY_MS, self.update_progress)

    def quit_app(self, event=None):
       
        try:
            keyboard.unblock_key('delete')
        except Exception:
            pass
        self.root.destroy()


def show_bsod():
    root = tk.Tk()
    app = BSoD_App(root)
    root.mainloop()



def delayed_start():
    time.sleep(DELAY_SECONDS)
    show_bsod()

threading.Thread(target=delayed_start, daemon=True).start()

# keep script alive
while True:
    time.sleep(1)
