"""TODO"""
import xlrd
import xlutils
import pandas
from arcode import anycode, uprint, clean_str

class Xcell(object):
    """TODO"""
    def __init__(self):
        pass

    def read_cell(self, row_idx, col_idx, filepath, sheetnum=0):
        """TODO"""
        xbook = xlrd.open_workbook(filepath)
        xsheet = xbook.sheet_by_index(sheetnum)
        return xsheet.cell(row_idx, col_idx).value

    def write_cell(self, string, row_idx, col_idx, filepath, sheetnum=0):
        """TODO"""
        try:
            rbook = xlutils.open_workbook(filepath)
            wbook = copy(rbook)
            xsheet = wbook.get_sheet(sheetnum)
            xsheet.write(row_idx, col_idx, string)
            wbook.save(filepath)
            return True
        except:
            return False


# test area
if __name__ == '__main__':
    pass
else:
    pass
