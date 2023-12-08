import xlrd
import re


class ExcelData:
    def __init__(self, path, files, data_settings):
        self.excel_files = files
        self.path = path
        self.settings = data_settings

    def get_file_names(self):
        return self.excel_files

    def get_file_name(self):
        return self.excel_files[0]

    def get_path(self):
        return self.path

    @staticmethod
    def __handle_string(s):
        s = s.replace(",", ".")
        dot_idx = s.find(".")
        if dot_idx != -1:
            p1, p2 = s.split(".", 1)
            p1 = re.sub("[^0-9]", '', p1)
            p2 = re.sub("[^0-9]", '', p2)
            s = p1 + "." + p2
        if not s:
            s = "0"
        return float(re.sub("[^0-9.]", '', s))

    def get_values(self, filename):
        xls = xlrd.open_workbook(self.path + filename).sheet_by_index(0)
        time = []
        ch1_vals = []
        ch2_vals = []
        for i in self.settings["row_range"]:
            t = xls.cell_value(rowx=i, colx=self.settings["col_time"])
            c1 = xls.cell_value(rowx=i, colx=self.settings["col_ch1"])
            c2 = xls.cell_value(rowx=i, colx=self.settings["col_ch2"])

            # in case of string, try to format it properly
            if isinstance(t, str):
                t = self.__handle_string(t)
            if isinstance(c1, str):
                c1 = self.__handle_string(c1)
            if isinstance(c2, str):
                c2 = self.__handle_string(c2)

            time.append(t)
            ch1_vals.append(c1)
            ch2_vals.append(c2)
        return {
            "time": time,
            "ch1_vals": ch1_vals,
            "ch2_vals": ch2_vals
        }
