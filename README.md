‌```markdown
# 🔒 Data-hider

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/UI-CustomTkinter-orange.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Bot API](https://img.shields.io/badge/Bot%20Platform-Bale-green.svg)](https://github.com/python-bale-bot/bale.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Data-hider** is an advanced, multi-platform security and data concealment ecosystem written in Python. It allows users to securely serialize, hide, and manage sensitive files locally using a modern GUI, while providing a powerful **remote administration and monitoring bot via the Bale Messenger API**. It even includes an emergency "Exigent Mode" to lock system interactions when needed.

---

## ✨ Key Features

### 🖥️ 1. Desktop Application (GUI)
* **Secure Serialization:** Reads raw binary streams of files and secures them into a dedicated `.dat` local repository using Python's `pickle` module.
* **Bulk Operation (Group Hide):** Concurrently hide entire directories of files automatically while preserving original file extensions in placeholders.
* **Smart Retrieval:** Extract individual files back to their original state or perform a **Random Load** filtering assets by partial string features.
* **🔒 Exigent Mode:** An emergency lock protocol that expands the UI to fullscreen black, runs a background thread, and completely locks the mouse pointer to `(0,0)` to prevent unauthorized physical access.

### 🤖 2. Remote Administration Bot (Bale Bot API)
* **Live System Monitoring:** Request a real-time `.png` screenshot of the host machine sent straight to your chat room.
* **Remote File Retrieval:** Load files dynamically inside the host PC or pull the secured files directly through the messenger as downloadable attachments.
* **Remote Shell Execution (`/cmd:`):** Execute raw shell commands on the host OS from anywhere via remote subprocess spawning.
* **Secure Access Control:** Hardcoded primary gateway authentication (`MRT_data` / `MRT_datas`) to restrict administration access to authorized admins only.

---

## 🧰 Architecture & Tech Stack

* **Core Engine:** `Python 3.8+`, `pickle` (Data binary serialization), `os`, `threading`, `subprocess`.
* **Graphics UI:** `CustomTkinter` & `Tkinter` (Modernized dark/light responsive styling).
* **System Automation:** `pyautogui` (Screen capture and mouse locking vectors), `keyboard` (Global system hotkeys interceptor).
* **Remote Framework:** `bale` library (Asynchronous event-driven wrapper for Bale bot platform).

---

## 🚀 Installation & Setup

### 1. Clone the Workspace
```bash
git clone [https://github.com/mrtprogrammer1389-ctrl/Data-hider.git](https://github.com/mrtprogrammer1389-ctrl/Data-hider.git)
cd Data-hider

```
### 2. Install Infrastructure Dependencies
Make sure you install all mandatory system wrappers:
```bash
pip install customtkinter pyautogui keyboard bale

```
> *Note: On Linux, keyboard and pyautogui packages may require root privileges or additional X11 server development headers (xlib).*
> 
## 💻 Operational Workflows
### Starting the Local Core Interface
Launch the primary Graphical Interface:
```bash
python Hider.py

```
 * **Default Security Challenge:** Enter the secure master passphrase MRT_data to grant workspace access.
 * **Emergency Override Hotkey:** While in *Exigent Mode*, press E + X simultaneously on your keyboard to instantly release the mouse lock and return to safety.
### Launching Remote Telegram/Bale Controller
Deploy the asynchronous monitoring agent script:
```bash
python balebot.py

```
Once initialized, open your bot chat interface, input your master verification passphrase (MRT_datas), and issue the following directives:
| Command | Action Description |
|---|---|
| /data_list | Generates a formatted summary table of all stored datasets |
| /data_count | Returns the absolute integer count of hidden modules |
| /screen_shot | Intercepts current active display and postsa media file back |
| /load:Name,Format | Fetches the binary object directly to your chat app client |
| /load_in_pc:Name,Format | Decodes the secure dataset directly onto the host storage surface |
| /cmd:your_command | Spawns a background OS process to run terminal instructions |
| /exit | /off | Kills the script interpreter stack remotely |
## 📂 Source Code Layout
```text
Data-hider/
│
├── data_base.py    # Database Manager: Handles binary pickle streams, hiding, and extraction logic.
├── Hider.py        # Desktop Interface: CustomTkinter GUI dashboard and Exigent mouse-lock routines.
├── balebot.py      # Telemetry Agent: Asynchronous event handling loop processing remote chat commands.
└── data base/       # Local Sandbox: Automated subdirectory where encrypted encrypted .dat records reside.

```
## 🤝 Contributing
 1. Fork the Repository
 2. Branch your features (git checkout -b feature/Optimization)
 3. Commit structural updates (git commit -m 'Optimized thread loops')
 4. Push to the remote engine branch (git push origin feature/Optimization)
 5. Open a Pull Request
## 📄 License
Distributed under the MIT License.
## 👤 Author
 * **Lead Engineer:** Mohammad Reza Taghdiri
 * **GitHub Profile:** @mrt-prog
 * **Email:** mrt.programmer1389@gmail.com
 * **Telegram:** @Mohammadhhawhd
*"Security is not a product, it's a structural process."* 🔐
```

```
