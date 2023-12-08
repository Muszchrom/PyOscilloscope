import xlrd


class ExcelData:
    def __init__(self):
        self.excel_files = [
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
        self.path = r"C:\Users\altai\Desktop\IZI 5\metrologia\stuff" + "\\"

    def get_file_names(self):
        return self.excel_files

    def get_file_name(self):
        return self.excel_files[0]

    def get_path(self):
        return self.path

    def get_values(self, filename):
        xls = xlrd.open_workbook(self.path + filename).sheet_by_index(0)
        time = []
        ch1_vals = []
        ch2_vals = []
        for i in range(8, 5008):
            time.append(float(xls.cell_value(rowx=i, colx=1)[:-2]))
            ch1_vals.append(int(xls.cell_value(rowx=i, colx=2)))
            ch2_vals.append(int(xls.cell_value(rowx=i, colx=3)))
        return {
            "time": time,
            "ch1_vals": ch1_vals,
            "ch2_vals": ch2_vals
        }