# Simple Oscilloscope

This script draws a graph based on Excel (.xls) files, which are loaded using the `ExcelData` class constructor. Note that this script was created quickly and require improvements.

## Installation
Make sure to install required packages using the following commands:
```bash
git clone https://github.com/Muszchrom/PyOscilloscope.git
pip install xlrd  # for working with .xls files
pip install matplotlib  # for graphs 
```
In case tkinter is not installed:
```bash
pip install tkinter  # for user interface
```

## Configuration
1. Open `main.py` file and edit parameters to your needs, based on their descriptions.

## Running the Application
After installing dependencies and configuring main file, run the script:
```bash
py main.py
```

## Controls
* Use the keys `1`, `2`, `3`, `4` to control cursors. 
* Switch the `checkbox` to display Lissajous graphs. 
* Select different files from the `combobox`.
