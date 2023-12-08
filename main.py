from front import Front
from utils import Utils


# Set the path where your files are located
path = r"C:\Users\altai\Desktop\IZI 5\metrologia\stuff" + "\\"

# Manually select files
files = [
    "200k-30.xls",
    "200k-40.xls",
    "200k-50.xls",
    "200k-60.xls",
    "200k-70.xls",
    "20k-30.xls",
    "20k-40.xls",
    "20k-50.xls",
    "20k-60.xls",
    "20k-70.xls",
    "2k-30.xls",
    "2k-40.xls",
    "2k-50.xls",
    "2k-60.xls",
    "2k-70.xls"
]

# Or use this method to get all files in the path specified above
# files = Utils(path).get_files()

# You can also get pretty version of it as a string, which you can copy and paste in directly
# print(Utils(path).get_pretty_files())

"""
These settings are required to properly make a graph based on XLS data.
This script only supports 1 column of time and 2 columns of values.
In case you want to draw only one channel, set col_ch2 to the same value as col_ch1

* cell A1 translates to row: 0, col: 0
* cell B9 translates to row: 8, col: 1
* Range upper limit is never used so if you have A99 cell 
as the last one, you need to pass in 99 as the second parameter
"""
data_settings = {
    "row_range": range(8, 5008),
    "col_time": 1,
    "col_ch1": 2,
    "col_ch2": 3
}

if __name__ == "__main__":
    app = Front(path, files, data_settings)
    app.mainloop()
