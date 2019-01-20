import xlrd
from xlutils.copy import copy


class ExcelUntils:
    #初始化函数
    def __init__(self,excel_file=None):
        workebook=None
        #定义一个其他方法使用变量
        self.excel_file=excel_file
        if excel_file==None:
            #打开工作簿
            workebook=xlrd.open_workbook("../dataconfig/接口测试用例.xlsx")
        else:
            workebook=xlrd.open_workbook(excel_file)
        # 定义一个其他方法使用变量
        self.worke=workebook
        #获取对应的表
        self.table=workebook.sheets()[0]

    #能够获取当前测试用例
    def getCaseCount(self):
        return self.table.nrows

    #获取单元格内容
    def getExcelData(self,row,col):
        #print(col)
        return self.table.cell_value(row,col)

    #写入单元格内容
    def writeExcelData(self,row,col,value):
        workebook=None
        #打开工作簿
        if self.excel_file!=None:
            workebook=xlrd.open_workbook(self.excel_file)
        else:
            workebook=xlrd.open_workbook("../dataconfig/接口测试用例.xlsx")

        #复制原内容
            write_data=copy(workebook)
        #获取工作簿中一张表
            sheet_data=write_data.get_sheet(0)
        #找到要写入的单元格
            sheet_data.write(row,col,value)
        #保存内容
            if self.excel_file!=None:
                write_data.save(self.excel_file)
            else:
                write_data.save("../dataconfig/接口测试用例.xlsx")


# if __name__ == '__main__':
#     excelUntil=ExcelUntils()
#     print(excelUntil.getCaseCount())
#     print(excelUntil.getExcelData(1,2))
#     #excelUntil.writeExcelData(47,2,"小马拉大车")
#     #print(excelUntil.getExcelData(47,2))