# Accept queue automatically on League of Legends.
I was inspired by the lucassmonn code
[accept-queue-lol-telegram](https://github.com/lucassmonn/accept-queue-lol-telegram), and I modify it according to my needs.

## Installation

/!\You must have python3.6 to run this script/!\ - [python download](https://www.python.org/downloads/)


Install using pip - [How to install pip on Windows](https://stackoverflow.com/questions/43304612/how-to-install-pip-on-python-3-6#:~:text=Just%20head%20to%20Command%20Prompt,of%20path%20variable%20is%20updated.&text=0-,I%20just%20successfully%20installed%20a%20package%20for%20excel.,the%20desired%20package%2C%20then%20install.)
```bash
python3.6 -m pip install -r requirements.txt
```
You must modify the access paths, in particular in the file run.cmd and accept.py. They need to be absolute path.

accept.py
```python
line14: button = pyautogui.locateOnScreen('ABSOLUTE_PATH/queue_acceptor/en.png', confidence=0.7)
line15: buttonPt = pyautogui.locateOnScreen('ABSOLUTE_PATH/queue_acceptor/pt.png', confidence=0.7)
```
run.bat
```
cd PATH_TO_PYTHON3.6_FOLDER
python.exe PATH_TO_accept.py
```
## Usage

Just run run.cmd and queue up! :-)

## Demonstration

![alt text](2.gif)

