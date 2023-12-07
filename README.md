# Simple Oscilloscope

This script draws a graph based on Excel (.xls) files, which are loaded using the `ExcelData` class constructor. Note that this script was created quickly and require A LOT OF improvements.

## Configuration

1. Update the list of files and the path in the `ExcelData` class.
2. Adjust the location of cells as needed.

## Running the Application

Make sure to install the required packages using the following commands:

```bash
pip install tkinter # should be installed by default
pip install xlrd  # for working with .xls files
pip install matplotlib
```
After installing the dependencies, run the script:
```bash
py file.py
```

and run `py file.py`
## Controls
* Use the keys `1`, `2`, `3`, `4` to control cursors. 
* Switch the `checkbox` to display Lissajous graphs. 
* Select different files from the `combobox`.
