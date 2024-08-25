import xlrd,xlwt
from utils.file_util import FileUtil
import pandas as pd
from xlwt import Workbook
from PIL import Image

class ExcelReader(object):

    def __init__(self, excel_name, sheet_name=None):
        excel_path = FileUtil.get_full_path(excel_name)
        self.data = xlrd.open_workbook(excel_path)
        self.__init_table_value(sheet_name)

    def get_rows_values(self, start_row=0, end_row=None):
        end_row = self.table.nrows - 1 if end_row is None else end_row
        rows_values = []
        for row_idx in range(start_row, end_row + 1):
            row_values = self.table.row_values(row_idx)
            rows_values.append(row_values)
        return rows_values

    def get_col_index(self, col_title):
        first_row_values = self.table.row_values(0)
        col_nums = len(first_row_values)
        for col_index in range(0, col_nums):
            if col_title == first_row_values[col_index]:
                return col_index
        return -1

    def __init_table_value(self, sheet_name):
        # 未指定sheet_name时，默认取第一个sheet
        if sheet_name is None:
            self.table = self.data.sheet_by_index(0)
        else:
            self.table = self.data.sheet_by_name(sheet_name)



class ExcelWrite(object):
    def __init__(self, excel_name, sheet_name='Sheet1'):
        self.workbook = Workbook()
        self.excel_name = excel_name 
        self.sheet = self.workbook.add_sheet(sheet_name)

    def write_excel(self,row ,col ,value):
        if isinstance(value, str):
            self.sheet.write(row, col, value)
        elif isinstance(value, Image.Image):
            drawing = self.workbook.add_drawing()
            drawing.picture.data = value.tobytes()
            drawing.set_position(row, col)
            self.sheet.insert_bitmap_image(drawing)
    
    def save_excel(self):
        self.workbook.save(self.excel_name)









class CsvReader(object):
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def get_row(self, row_index):
        return self.df.iloc[row_index]

    def get_col(self, col_index):  
        return self.df.iloc[:, col_index]

    def get_value(self, row_index, col_index):
        return self.df.iloc[row_index, col_index]
