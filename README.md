# Windows Blue Screen (Fake BSoD) Simulator  
A Python-based application that simulates a realistic Windows **Blue Screen of Death (BSoD)**.  
Useful for pranks, demos, or creating controlled computer lock screens.

---

## 🚀 Features

- Fully fullscreen and always-on-top window  
- Realistic Windows 10/11 Blue Screen layout  
- Progress percentage animation  
- Auto-generated QR code (same as real Windows stopcode link)  
- Blocks:
  - **ALT + F4**
  - **Delete key**
- Secret exit hotkey: **Ctrl + Alt + Insert**
- Displays after a configurable delay  
- Multithreaded delay & UI handling  

---

## 📸 Preview

A simulated Blue Screen with:
- Sad face  
- Error text  
- Stop code  
- Progress percent counter  
- QR code linking to: `https://www.windows.com/stopcode`

---

## 🧩 Requirements

Install dependencies:


- pip install pillow qrcode keyboard
---
## 📄 Code Overview

Main technologies used:
- tkinter → Creates fullscreen UI
- Pillow (PIL) → Displays the QR code
- qrcode → Generates Windows-like QR
- keyboard → Blocks keys & adds exit hotkeys
- threading + time → Delay before showing BSoD

The script:
- Waits for X seconds
- Launches a fullscreen fake BSoD
- Slowly increases progress
- Locks the screen until the secret exit hotkey is pressed

---
## 🔧 Configuration
  - DELAY_SECONDS = 10         # Delay before showing BSoD
  - START_PERCENT = 1
  - MAX_PERCENT = 100
  - UPDATE_DELAY_MS = 4000     # Progress update speed

---

## 🛑 Emergency Exit
- Ctrl + Alt + Insert

---

## ⚠️ Disclaimer
- This project is strictly for educational and harmless prank purposes.
- Do NOT use it to mislead, scare, disrupt, or cause issues on devices you don't own or have permission to use.





