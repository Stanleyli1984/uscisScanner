__author__ = 'TJ Liu'

from openpyxl import Workbook


class ExcelWriter:
    def __init__(self, filename):
        self.filename = filename + ".xlsx"
        self.wb = Workbook(write_only=True)
        self.ws = self.wb.create_sheet()
        self.num = 1

    def write_to_file(self, info):
        for key, value in sorted(info.items()):
            self.ws.append((str(key), value))

    def close(self):
        self.wb.save(self.filename)
        print "Data has been saved to", self.filename
